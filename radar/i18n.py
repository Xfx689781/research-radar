"""Text used in the digest and in the summary prompt, in English and Chinese."""

STRINGS = {
    "en": {
        "title": "Research digest · {date}",
        "coverage": "Covers papers posted from about {start} to {end} (UTC).",
        "note": ("> Relevance = TF-IDF cosine similarity to your interest description, plus a "
                 "keyword bonus. It measures how close the wording is to what you care about, "
                 "not how good a paper is. AI summaries are written from the abstract only; "
                 "check the paper before relying on them."),
        "must_read": "Must-read this week",
        "no_must_read": "No paper reached the threshold this week.",
        "nothing": "Nothing notable this week.",
        "failed": "⚠️ Fetch failed: {error}",
        "relevance": "relevance",
        "et_al": " et al.",
        "one_liner": "In one sentence",
        "fallback": " (first sentence of the abstract; no AI summary)",
        "why": "Why it matters",
        "background": "Background needed",
        "difficulty": "difficulty",
        "keywords": "Matched keywords",
        "list_sep": ", ",
        "abstract": "Original abstract",
        "stats": "Fetch statistics",
        "stats_header": "| Topic | Fetched | New | Selected |",
        "colon": ": ",
    },
    "zh": {
        "title": "研究进展简报 · {date}",
        "coverage": "覆盖约 {start} 至 {end}（UTC）发布的论文。",
        "note": ("> 相关度 = 和你的兴趣描述的 TF-IDF 余弦相似度 + 关键词加权。它只衡量文字上像不像你"
                 "关心的东西，不代表论文质量。AI 摘要只依据论文摘要写成，读原文前请自己核对。"),
        "must_read": "本周必读",
        "no_must_read": "本周没有达到推荐门槛的论文。",
        "nothing": "本周无重点。",
        "failed": "⚠️ 抓取失败：{error}",
        "relevance": "相关度",
        "et_al": " 等",
        "one_liner": "一句话",
        "fallback": "（摘要首句，未生成 AI 摘要）",
        "why": "为什么值得看",
        "background": "需要的背景",
        "difficulty": "难度",
        "keywords": "命中关键词",
        "list_sep": "、",
        "abstract": "原始摘要",
        "stats": "抓取统计",
        "stats_header": "| 方向 | 抓到 | 新论文 | 入选 |",
        "colon": "：",
    },
}

DIFFICULTIES = {
    "en": ("introductory", "intermediate", "research-level"),
    "zh": ("入门", "中等", "研究级"),
}

SYSTEM_PROMPT = {
    "en": ("You help a mathematically trained reader triage new research papers. Write only "
           "from the given title and abstract. Do not invent results, numbers, methods or author "
           "details that are not in the abstract; if the abstract is too thin, say so. Be measured "
           "and do not overstate a paper's importance."),
    "zh": ("你是一位帮有数学背景的读者筛选新论文的研究助理。只根据给出的标题和摘要写，不要编造摘要里"
           "没有的结论、数字、方法或作者信息；摘要信息不足时如实说明。用中文写，专业术语保留英文原词。"
           "语气克制，不要夸大论文的意义。"),
}

USER_PROMPT = {
    "en": """Topic: {topic}
Title: {title}
Abstract: {abstract}

Reply with one JSON object and nothing else. Fields:
- "one_liner": one sentence on what the paper does
- "why": 2-3 sentences on why it is worth attention and what it may connect to (say so if unsure)
- "background": the background needed to follow the core idea (short list)
- "difficulty": one of "introductory", "intermediate", "research-level"
""",
    "zh": """方向：{topic}
标题：{title}
摘要：{abstract}

只输出一个 JSON 对象，不要输出其他文字。字段：
- "one_liner": 一句话说明这篇论文做了什么
- "why": 2 到 3 句，为什么值得关注、可能和哪些方向有联系（不确定就说不确定）
- "background": 读懂核心思想需要的背景（简短列举）
- "difficulty": "入门"、"中等"、"研究级" 三者之一
""",
}
