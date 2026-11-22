"""Text used in the digest, the website and the summary prompt, in English and Chinese."""

STRINGS = {
    "en": {
        "title": "Research digest · {date}",
        "coverage": "New papers posted from about {start} to {end} (UTC).",
        "note": ("> Papers are picked by how closely their wording matches each topic's description "
                 "(the \"relevance\" score), not by quality. Summaries are written by AI from the "
                 "abstract only; open the paper before relying on them."),
        "must_read": "Highlights",
        "no_must_read": "No paper reached the threshold this time.",
        "nothing": "Nothing notable this time.",
        "failed": "⚠️ Fetch failed: {error}",
        "relevance": "relevance",
        "et_al": " et al.",
        "one_liner": "In one sentence",
        "plain": "In plain words",
        "fallback": " (first sentence of the abstract; AI summaries are off)",
        "why": "Why it matters",
        "background": "Background needed",
        "difficulty": "level",
        "keywords": "Matched keywords",
        "list_sep": ", ",
        "abstract": "Original abstract",
        "stats": "Fetch statistics",
        "stats_header": "| Topic | Fetched | New | Selected |",
        "colon": ": ",
        # website
        "site_title": "Research Radar",
        "site_intro": ("New research from many fields, picked and summarized for curious readers. "
                       "Updated every day from arXiv, bioRxiv and medRxiv."),
        "latest": "Latest digest",
        "archive": "All digests",
        "topics": "Topics covered",
        "papers": "papers",
    },
    "zh": {
        "title": "研究进展简报 · {date}",
        "coverage": "约 {start} 至 {end}（UTC）发布的新论文。",
        "note": ("> 论文按照和各方向描述的文字相似度（“相关度”）挑选，不代表论文质量。摘要由 AI 根据论文摘要写成，"
                 "引用或深入阅读前请打开原文核对。"),
        "must_read": "重点推荐",
        "no_must_read": "这次没有达到推荐门槛的论文。",
        "nothing": "这次无重点。",
        "failed": "⚠️ 抓取失败：{error}",
        "relevance": "相关度",
        "et_al": " 等",
        "one_liner": "一句话",
        "plain": "通俗地说",
        "fallback": "（摘要首句，AI 摘要未开启）",
        "why": "为什么值得看",
        "background": "需要的背景",
        "difficulty": "难度",
        "keywords": "命中关键词",
        "list_sep": "、",
        "abstract": "原始摘要",
        "stats": "抓取统计",
        "stats_header": "| 方向 | 抓到 | 新论文 | 入选 |",
        "colon": "：",
        "site_title": "Research Radar",
        "site_intro": "每天从 arXiv、bioRxiv、medRxiv 挑选各领域的新论文，并为感兴趣的读者写成通俗摘要。",
        "latest": "最新简报",
        "archive": "全部简报",
        "topics": "覆盖方向",
        "papers": "篇",
    },
}

DIFFICULTIES = {
    "en": ("introductory", "intermediate", "research-level"),
    "zh": ("入门", "中等", "研究级"),
}

SYSTEM_PROMPT = {
    "en": ("You write short briefs on new research papers for curious, educated readers who may "
           "come from a different field. Explain jargon in everyday words when you must use it. "
           "Write only from the given title and abstract: do not invent results, numbers, methods "
           "or author details, and if the abstract is too thin, say so. Be measured; do not "
           "overstate a paper's importance or call it a breakthrough unless the abstract shows why."),
    "zh": ("你为好奇、受过良好教育、但可能来自其他领域的读者写新论文的简短介绍。必须用到术语时，用日常语言解释。"
           "只根据给出的标题和摘要写，不要编造结论、数字、方法或作者信息；摘要信息不足时如实说明。"
           "用中文写，专业术语第一次出现时附英文原词。语气克制，不要夸大论文的意义，除非摘要说明了理由，"
           "不要称其为“突破”。"),
}

USER_PROMPT = {
    "en": """Field: {topic}
Title: {title}
Abstract: {abstract}

Reply with one JSON object and nothing else. Fields:
- "one_liner": one sentence on what the paper does, for a specialist
- "plain": 2-3 sentences for a reader from another field: what problem it tackles, what the authors did or found, in everyday words
- "why": 1-2 sentences on why it is worth attention and what it may connect to (say so if unsure)
- "background": what a reader needs to know to follow the core idea (short list)
- "difficulty": one of "introductory", "intermediate", "research-level"
""",
    "zh": """领域：{topic}
标题：{title}
摘要：{abstract}

只输出一个 JSON 对象，不要输出其他文字。字段：
- "one_liner": 一句话说明这篇论文做了什么（给同行看）
- "plain": 2 到 3 句，给其他领域的读者：它要解决什么问题，作者做了什么、发现了什么，用日常语言说
- "why": 1 到 2 句，为什么值得关注、可能和哪些方向有联系（不确定就说不确定）
- "background": 读懂核心思想需要知道什么（简短列举）
- "difficulty": "入门"、"中等"、"研究级" 三者之一
""",
}
