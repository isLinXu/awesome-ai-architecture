#!/usr/bin/env python3
"""update_metadata.py — 刷新 README 统计数字与更新日期（只动 STATS 标记块）。"""
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def replace_stat(text, key, value):
    pattern = re.compile(r"(<!--STATS:" + re.escape(key) + r"-->).*?(<!--/STATS:" + re.escape(key) + r"-->)")
    return pattern.sub(lambda m: m.group(1) + str(value) + m.group(2), text)


def main():
    state_path = ROOT / "data" / "papers.json"
    papers = json.loads(state_path.read_text(encoding="utf-8"))["papers"] if state_path.exists() else {}

    # 经典条目（各文档必读表）+ 自动收录条目合计
    classic = 0
    for doc in (ROOT / "docs").glob("*.md"):
        text = doc.read_text(encoding="utf-8")
        m = re.search(r"^## 奠基与必读$(.*?)^## ", text, re.S | re.M)
        if m:
            classic += len(re.findall(r"arxiv\.org/abs/", m.group(1)))
        classic += len(re.findall(r"transformer-circuits\.pub", text[: text.find("<!-- table:start")] if "<!-- table:start" in text else text))
    # 去重：自动收录的不与经典重复统计这里不做精确去重，取两者之和的下限口径
    total = classic + len(papers)

    week_ago = (dt.date.today() - dt.timedelta(days=7)).isoformat()
    new7 = sum(1 for p in papers.values() if p.get("published", "") >= week_ago)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = replace_stat(readme, "papers", total)
    readme = replace_stat(readme, "papers_new", f"+{new7}" if new7 else "—")
    readme = replace_stat(readme, "updated", dt.date.today().isoformat())
    # 各赛道收录数（从状态库统计）
    cat_counts = {}
    for p in papers.values():
        c = p.get("category")
        if c:
            cat_counts[c] = cat_counts.get(c, 0) + 1
    for cat_id, n in cat_counts.items():
        readme = replace_stat(readme, f"cat_{cat_id}", n)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"README 已更新：总条目 {total}，近 7 天新增 {new7}，赛道分布 {cat_counts}")


if __name__ == "__main__":
    main()
