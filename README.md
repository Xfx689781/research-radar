# research-radar

一个私人的每周论文雷达：每周日自动抓取 arXiv 上我关心的 8 个方向的新论文，按我的兴趣打分排序，可选用 Claude 写中文摘要，生成一份 Markdown 简报提交回仓库。

方向：ML 理论 · 概率 · 微分几何 · 数学物理 · 复分析 · AI4Math · 具身智能 · 理论物理

```
arXiv API ──► 抓取（按分类 + 关键词）──► 去重（已推荐过的跳过）
          ──► 打分（TF-IDF + 关键词）──► 每个方向选 top_k，交叉列出的论文只出现一次
          ──► （可选）Claude 写中文摘要 ──► digests/YYYY-MM-DD.md
```

## 目录

```
radar/
  arxiv_client.py   arXiv API 查询与 Atom 解析（只用标准库）
  rank.py           打分与跨方向去重
  summarize.py      可选的 AI 摘要（没有 API key 时自动退回摘要首句）
  digest.py         生成 Markdown
  state.py          记住推荐过的论文（state/seen.json）
  config.py         读取 config.yaml
  __main__.py       命令行入口
config.yaml         方向、关键词、兴趣描述 —— 主要在这里调
tests/              单元测试 + 一份虚构的测试数据（不是真论文）
.github/workflows/weekly.yml   每周自动运行
```

## 本地运行

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pytest -q                                                   # 测试（不联网）
python -m radar run --offline tests/fixtures/sample_feed.xml --dry-run   # 用测试数据跑一遍
python -m radar run --no-summary                            # 真的去抓 arXiv，不用 AI 摘要
export ANTHROPIC_API_KEY=...  && python -m radar run        # 带 AI 摘要
```

结果在 `digests/latest.md`。抓 8 个方向大约要几分钟，因为 arXiv 要求每次请求间隔约 3 秒。

## 放到 GitHub（私有仓库）

```bash
git init && git add . && git commit -m "research-radar v0.1"
gh repo create research-radar --private --source . --push
```

然后：

1. **Settings → Secrets and variables → Actions → New repository secret**，名字 `ANTHROPIC_API_KEY`。不想用 AI 摘要就不加，程序会自动跳过。**不要把 key 写进任何文件。**
2. **Actions** 页面里手动点一次 `weekly-digest → Run workflow`，确认能跑通。
3. 之后每周日早上自动运行，新简报会被提交到 `digests/`。

## 打分是怎么算的

对每个方向，把 `interest` 按逗号拆成若干"小方面"（facet），比如 `geometric flows`、`Lie groups`；每篇论文的分数是

$$
\text{score}(p) = \max_{f \in \text{facets}} \cos\big(\text{tfidf}(p), \text{tfidf}(f)\big) \;+\; \min(0.24,\ 0.08 \times \#\text{命中关键词})
$$

为什么取最大值而不是和整段兴趣描述比？因为整段描述很长，一篇只讲其中一个方面的论文和它的余弦相似度会被稀释得很小。分数只衡量**文字上像不像**，不衡量质量。

去重：一篇论文如果同时出现在多个方向（比如 math.PR 和 stat.ML 交叉列出），会被放进它得分最高的那个方向。

时间窗口：每次往回看 `days + overlap_days` 天，因为 arXiv 公布有延迟；`state/seen.json` 保证同一篇不会推荐两次。

## 怎么调

- 推荐的东西不对胃口：先改 `interest`，写得越具体越好；再加 `seed_ids`（你喜欢的论文的 arXiv 编号）。
- 某个方向太多噪音：加 `keywords`，只抓含这些词的论文。
- 太多"本周无重点"：调低 `min_score`；推荐太杂：调高。第一次真实运行后看一下"抓取统计"和各篇的相关度，再决定阈值。

## 已知局限

- TF-IDF 只认字面：`Ricci flow` 和 `geometric evolution equation` 在它眼里不相关。
- 只看 arXiv，不看新闻、博客、期刊。
- AI 摘要只根据摘要写，可能说错或说过头。读原文前自己核对。

## 下一步（我自己来做）

- [ ] **评估排序**：连续几周给推荐打"有用 / 没用"标签，算 precision@k，有了指标再改算法。
- [ ] **换成语义向量**：用 sentence-transformers 之类的 embedding 模型代替 TF-IDF，和现在的版本比一比 precision@k。
- [ ] **反馈学习**：把标"有用"的论文自动加进 `seed_ids`，或者训练一个简单的 logistic regression 分类器。
- [ ] **加信号**：用 Semantic Scholar API 拿引用数、作者信息。
- [ ] **加来源**：Quanta Magazine、几位研究者的博客、Lean Zulip 的 AI4Math 动态。
- [ ] **推送**：发邮件或者手机通知。
- [ ] **摘要审查**：检查 AI 摘要里有没有原始摘要中不存在的数字或结论。

## 致谢

Thank you to arXiv for use of its open access interoperability. 本项目通过 [arXiv API](https://info.arxiv.org/help/api/) 获取论文元数据，请遵守其使用条款，保持请求间隔。
