#!/usr/bin/env python3
"""fetch_arxiv.py — 从 arXiv 检索、打分、归类、去重，写入各赛道文档的标记表格。

用法：
    python scripts/fetch_arxiv.py                          # 默认回填 30 天
    python scripts/fetch_arxiv.py --days 365               # 回填一年
    python scripts/fetch_arxiv.py --since 2014-01-01 --until 2017-12-31   # 上溯到 attention 起源
    python scripts/fetch_arxiv.py --dry-run                # 只看会写什么
    python scripts/fetch_arxiv.py --category efficient-attention --days 30

设计：
- 分页抓取（每页 200 条，页间 sleep 3s 遵守 arXiv API 礼仪）
- 状态外置到 data/papers.json，去重靠历史库
- 每个赛道跑完立即落盘（状态 + 文档表格），中断后可安全续跑
- 文档表格 = 状态库中该赛道全量条目的投影（按日期倒序，table_limit 截断）
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ATOM = "{http://www.w3.org/2005/Atom}"
UA = "awesome-ai-architecture/1.0 (arxiv fetcher)"
PAGE = 200
MAX_PAGES = 20          # 单查询窗口最多翻 20 页（4000 条），避免宽关键词把窗口拖进超时
DEFAULT_TABLE_LIMIT = 1000


def load_taxonomy():
    with open(ROOT / "config" / "taxonomy.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)["categories"]


def load_state():
    p = ROOT / "data" / "papers.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"papers": {}}


def save_state(state):
    p = ROOT / "data" / "papers.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def arxiv_query(query, since, until, start=0):
    q = f"({query}) AND submittedDate:[{since}0000 TO {until}2359]"
    url = (
        "https://export.arxiv.org/api/query?search_query="
        + urllib.parse.quote(q)
        + f"&start={start}&max_results={PAGE}&sortBy=submittedDate&sortOrder=descending"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(10 * (attempt + 1))


def parse_entries(xml_bytes):
    root = ET.fromstring(xml_bytes)
    entries = []
    for e in root.findall(f"{ATOM}entry"):
        arxiv_id = e.find(f"{ATOM}id").text.rsplit("/abs/", 1)[-1]
        title = " ".join(e.find(f"{ATOM}title").text.split())
        abstract = " ".join(e.find(f"{ATOM}summary").text.split())
        published = e.find(f"{ATOM}published").text[:10]
        entries.append({"id": arxiv_id, "title": title, "abstract": abstract, "published": published})
    return entries


def score(entry, kw, title_only=False):
    text_title = entry["title"].lower()
    text_abs = "" if title_only else entry["abstract"].lower()
    s = 0
    for term in kw.get("strong", []):
        t = term.lower()
        if t in text_title:
            s += 6
        elif t in text_abs:
            s += 4
    for term in kw.get("medium", []):
        t = term.lower()
        if t in text_title:
            s += 3
        elif t in text_abs:
            s += 2
    for term in kw.get("weak", []):
        t = term.lower()
        if t in text_title or t in text_abs:
            s += 1
    return s


def rewrite_table(doc_path, rows):
    """把 (date, title, id, score) 列表按年份分组写入标记块，保持块外正文不动。"""
    text = doc_path.read_text(encoding="utf-8")
    start_marker = "<!-- table:start papers -->"
    end_marker = "<!-- table:end papers -->"
    block = [start_marker]
    by_year = {}
    for row in rows:
        by_year.setdefault(row[0][:4], []).append(row)
    for year in sorted(by_year, reverse=True):
        block.append(f"### {year}")
        block.append("| 日期 | 标题 | arXiv | 分数 |")
        block.append("| :-- | :-- | :-- | --: |")
        for date, title, aid, s in by_year[year]:
            block.append(f"| {date} | [{title}](https://arxiv.org/abs/{aid}) | {aid} | {s} |")
        block.append("")
    block.append(end_marker)
    new_block = "\n".join(block)
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.S)
    if not pattern.search(text):
        print(f"  [skip] {doc_path} 缺少标记块")
        return False
    doc_path.write_text(pattern.sub(lambda _: new_block, text), encoding="utf-8")
    return True


def rebuild_doc(cat, state):
    """文档表格 = 状态库中该赛道条目的投影。分数缺失时按标题重算。"""
    doc_path = ROOT / cat["doc"]
    if not doc_path.exists():
        return
    limit = cat.get("table_limit")  # 可选：限制展示行数；默认全量按年份分组展示
    rows = []
    for aid, p in state["papers"].items():
        if p.get("category") != cat["id"]:
            continue
        s = p.get("score")
        if s is None:
            s = score({"title": p["title"], "abstract": ""}, cat["keywords"], title_only=True)
        rows.append((p["published"], p["title"], aid, s))
    rows.sort(key=lambda r: r[0], reverse=True)
    rewrite_table(doc_path, rows[:limit] if limit else rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30, help="从今天往前回填 N 天")
    ap.add_argument("--since", help="起始日期 YYYY-MM-DD（覆盖 --days）")
    ap.add_argument("--until", help="截止日期 YYYY-MM-DD，默认今天")
    ap.add_argument("--category", help="只跑某条赛道")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    until = args.until or dt.date.today().isoformat()
    since = args.since or (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    since_s, until_s = since.replace("-", ""), until.replace("-", "")

    categories = load_taxonomy()
    if args.category:
        categories = [c for c in categories if c["id"] == args.category]
        if not categories:
            sys.exit(f"未知赛道: {args.category}")

    state = load_state()
    seen = state["papers"]
    total_new = 0
    print(f"时间窗: {since} → {until}")

    for cat in categories:
        found = {}
        for q in cat["arxiv_queries"]:
            start = 0
            while True:
                try:
                    entries = parse_entries(arxiv_query(q, since_s, until_s, start=start))
                except Exception as e:
                    print(f"  [warn] {cat['id']} 查询失败(start={start}): {e}")
                    break
                if not entries:
                    break
                for entry in entries:
                    if entry["id"] in seen or entry["id"] in found:
                        continue
                    s = score(entry, cat["keywords"])
                    if s >= cat.get("threshold", 6):
                        found[entry["id"]] = (entry, s)
                if len(entries) < PAGE or start + PAGE >= MAX_PAGES * PAGE:
                    break
                start += PAGE
                time.sleep(3)  # arXiv API 礼仪
            time.sleep(3)

        print(f"[{cat['id']}] 命中 {len(found)} 篇")
        if args.dry_run:
            for aid, (entry, s) in sorted(found.items(), key=lambda x: x[1][0]["published"], reverse=True):
                print(f"  {entry['published']} [{s}] {entry['title']} ({aid})")
            continue

        for aid, (entry, s) in found.items():
            seen[aid] = {
                "title": entry["title"],
                "category": cat["id"],
                "published": entry["published"],
                "score": s,
            }
        save_state(state)      # 每条赛道落盘一次，中断可续跑
        rebuild_doc(cat, state)
        total_new += len(found)

    print(f"完成，新增 {total_new} 篇。{'（dry-run，未写入）' if args.dry_run else ''}")


if __name__ == "__main__":
    main()
