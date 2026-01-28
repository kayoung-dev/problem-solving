import sys
import re
from datetime import datetime

TYPE_ORDER = {
    "fix": 0,
    "feat": 1,
    "refactor": 2,
    "test": 3,
    "chore": 4,
}
# docs는 출력 대상이 아님

MSG_RE = re.compile(r"^(feat|fix|refactor|test|chore|docs)(\(([^)]+)\))?:\s*(.+)$")

def parse_msg(msg: str):
    # Merge / docs 제외는 밖에서 처리
    m = MSG_RE.match(msg)
    if not m:
        return None
    typ = m.group(1)
    scope = m.group(3)  # 없으면 None
    subject = m.group(4)
    return typ, scope, subject

def fmt(typ, scope, subject):
    if scope is None:
        return f"{typ}: {subject}"
    return f"{typ}({scope}): {subject}"

def key_of(item):
    # item: (hash, dt, typ, scope, subject)
    h, dt, typ, scope, subject = item
    scope_key = (1, "") if scope is None else (0, scope)  # scope 없는건 뒤
    return (TYPE_ORDER[typ], scope_key, -int(dt.timestamp()), h)

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    items = []
    for _ in range(n):
        line = input().rstrip("\n")
        if not line:
            continue
        # hash YYYY-MM-DD HH:MM message...
        parts = line.split()
        h = parts[0]
        dt = datetime.strptime(parts[1] + " " + parts[2], "%Y-%m-%d %H:%M")
        msg = " ".join(parts[3:])

        if msg.startswith("Merge "):
            continue
        if msg.startswith("docs:"):
            continue

        parsed = parse_msg(msg)
        if not parsed:
            continue
        typ, scope, subject = parsed
        if typ == "docs":
            continue

        items.append((h, dt, typ, scope, subject))

    items.sort(key=key_of)
    for h, dt, typ, scope, subject in items:
        print(fmt(typ, scope, subject))

if __name__ == "__main__":
    solve()
