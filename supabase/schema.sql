-- Research Radar: each reader's chosen topics and email setting.
-- Paste this into Supabase -> SQL Editor -> New query -> Run.
-- Safe to run again: it only adds what is missing.

create table if not exists public.preferences (
  user_id    uuid primary key references auth.users (id) on delete cascade,
  topics     text[] not null default '{}',
  updated_at timestamptz not null default now()
);

-- Added in v0.6 for the daily email.
alter table public.preferences add column if not exists email text;
alter table public.preferences add column if not exists email_daily boolean not null default false;

-- Added in v0.8: a secret per reader for the one-click unsubscribe link in emails.
alter table public.preferences add column if not exists unsubscribe_token uuid not null default gen_random_uuid();

-- Unsubscribe without signing in: the website calls this with the token from the
-- email link. It can only switch the daily email off, and only for that one token.
create or replace function public.unsubscribe(token uuid) returns boolean
language sql security definer set search_path = public as $$
  update public.preferences set email_daily = false, updated_at = now()
  where unsubscribe_token = token and email_daily
  returning true;
$$;
revoke all on function public.unsubscribe(uuid) from public;
grant execute on function public.unsubscribe(uuid) to anon, authenticated;

-- Table access. Newer Supabase projects do not open tables created in SQL to the
-- Data API, so grant it explicitly: signed-in readers may read and write (rows are
-- still limited to their own by the policies below); the daily email job, using the
-- secret key (service_role), may read. Visitors who are not signed in get nothing.
grant usage on schema public to authenticated, service_role;
grant select, insert, update on table public.preferences to authenticated;
grant select on table public.preferences to service_role;

-- Row-level security: every reader can see and change only their own row.
-- This is what makes it safe to publish the publishable/anon key in docs/data/site.json.
-- The daily email job reads all subscribers with the secret (service) key, which
-- bypasses these rules and is stored only as a GitHub Actions secret.
alter table public.preferences enable row level security;

drop policy if exists "read own preferences" on public.preferences;
create policy "read own preferences" on public.preferences
  for select using (auth.uid() = user_id);

drop policy if exists "insert own preferences" on public.preferences;
create policy "insert own preferences" on public.preferences
  for insert with check (auth.uid() = user_id);

drop policy if exists "update own preferences" on public.preferences;
create policy "update own preferences" on public.preferences
  for update using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- Make the Data API pick up the changes right away.
notify pgrst, 'reload schema';
