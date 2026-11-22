-- Research Radar: table for each reader's chosen topics.
-- Paste this into Supabase -> SQL Editor -> New query -> Run.

create table if not exists public.preferences (
  user_id    uuid primary key references auth.users (id) on delete cascade,
  topics     text[] not null default '{}',
  updated_at timestamptz not null default now()
);

-- Row-level security: every reader can see and change only their own row.
-- This is what makes it safe to publish the "anon" key in docs/data/site.json.
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
