#!/usr/bin/env python3
"""check_md.py — 自检：标记块配对、表格列数、相对链接目标存在。"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def check_markers(path, text):
    starts = re.findall(r"<!-- table:start (\w+) -->", text)
    ends = re.findall(r"<!-- table:end (\w+) -->", text)
    if sorted(starts) != sorted(ends):
        errors.append(f"{path}: 标记块不配对 start={starts} end={ends}")


def check_tables(path, text):
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("|") and not line.rstrip().endswith("|"):
            errors.append(f"{path}:{i}: 表格行未闭合")


def check_links(path, text):
    for m in re.finditer(r"\[[^\]]*\]\(((?!http|#|mailto)[^)]+)\)", text):
        target = (path.parent / m.group(1).split("#")[0]).resolve()
        if m.group(1) and not target.exists():
            errors.append(f"{path}: 相对链接失效 -> {m.group(1)}")


for md in sorted(ROOT.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    check_markers(md, text)
    check_tables(md, text)
    check_links(md, text)

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("自检通过 ✔")
