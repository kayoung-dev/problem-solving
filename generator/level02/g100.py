import os
import random
import string
from datetime import datetime, timedelta

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P100 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P100")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 릴리즈 노트 정리하기

## 문제 설명
팀 리더 **지훈**은 새로운 버전을 배포하기 전에 Git 커밋 로그를 정리하여 릴리즈 노트를 작성하려고 합니다.

커밋 로그에는 실제 기능 개발과 관련 없는 기록도 함께 섞여 있기 때문에,  
지훈은 모든 커밋을 그대로 사용하지 않고 **릴리즈 노트에 적합한 커밋만 골라 정리**합니다.

각 커밋은 커밋 해시, 커밋 시간, 그리고 한 줄의 커밋 메시지로 이루어져 있으며,  
메시지는 보통 `type(scope): 내용` 또는 `type: 내용` 형태로 작성됩니다.  
이때 `type`은 커밋의 성격을 나타내며, `scope`는 변경이 적용된 영역을 의미합니다.

지훈은 릴리즈 노트에 필요한 커밋만 골라 아래 규칙으로 정렬해 출력합니다.
- 메시지가 `Merge`로 시작하는 커밋은 제외합니다.
- 메시지가 `docs:`로 시작하는 커밋은 제외합니다.
- `type` 우선순위: `fix` → `feat` → `refactor` → `test` → `chore`
- 같은 `type`이면 `scope`이 있는 커밋이 먼저 오고, 그 안에서 사전순으로 정렬합니다.
- 같은 `type`과 `scope`이면 커밋 시간을 **최신이 먼저** 오도록 정렬합니다.
- 그래도 같으면 해시를 사전순으로 정렬합니다.

정리된 결과는 커밋 메시지를 기반으로 한 간결한 형태로 출력하며,  
변경 범위가 없는 경우에는 범위를 생략하여 표시합니다.

주어진 Git 커밋 로그를 분석하여,  
지훈이 릴리즈 노트에 정리하게 될 커밋 목록을 순서대로 출력하세요.

---
## 입력 형식 (Input Format)
- 첫 줄에는 커밋의 개수 N이 주어집니다.  
- 이후 N줄에 걸쳐 각 줄마다 하나의 커밋 로그가 주어지며,  
- 각 로그는 `커밋해시 날짜 시간 메시지`의 순서로 구성됩니다.  
- 메시지는 공백을 포함할 수 있으며, 줄 끝까지가 하나의 메시지로 간주됩니다.

---

## 출력 형식 (Output Format)
- 릴리즈 노트에 포함되는 커밋만을 조건에 맞게 정렬하여,  
각 커밋을 한 줄씩 출력합니다.  
- 출력 형식은 `type(scope): 내용` 또는 `type: 내용`입니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
7
a1b2c3d4 2026-01-05 09:10 feat(api): add search endpoint
ff00aa11 2026-01-05 10:00 fix(api): handle null request
1234abcd 2026-01-05 08:30 docs: update README
beefcafe 2026-01-04 22:00 refactor(core): split service layer
0badf00d 2026-01-05 10:00 fix: patch build error
abcd0001 2026-01-03 12:00 Merge branch 'dev'
9999eeee 2026-01-05 09:50 chore(ci): update pipeline
{TICK}
**Output:**
{TICK}
fix(api): handle null request
fix: patch build error
feat(api): add search endpoint
refactor(core): split service layer
chore(ci): update pipeline
{TICK}
- `docs:`와 `Merge ...` 커밋은 제외됩니다.
- `fix`가 가장 먼저 나오고, 같은 `fix`에서는 scope가 있는 것이 먼저 정렬됩니다.

### 예시 2
**Input:**
{TICK}
5
aa11bb22 2026-01-01 10:00 feat: init project
cc33dd44 2026-01-01 10:01 feat(ui): add button
ee55ff66 2026-01-01 09:59 fix(ui): hotfix
11223344 2026-01-01 10:02 fix: adjust config
deadbeef 2026-01-01 10:03 test(ui): add tests
{TICK}
**Output:**
{TICK}
fix(ui): hotfix
fix: adjust config
feat(ui): add button
feat: init project
test(ui): add tests
{TICK}
- 같은 type이면 scope 사전순, scope가 없는 항목은 같은 type에서 뒤로 갑니다.
- 같은 type+scope라면 시간이 최신인 커밋이 먼저 옵니다.

### 예시 3
**Input:**
{TICK}
2
abcd1234 2026-01-01 00:00 chore: setup
bead5678 2026-01-01 00:01 docs: note
{TICK}
**Output:**
{TICK}
chore: setup
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
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

MSG_RE = re.compile(r"^(feat|fix|refactor|test|chore|docs)(\\(([^)]+)\\))?:\\s*(.+)$")

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
        line = input().rstrip("\\n")
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
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
import re
TYPE_ORDER = {"fix": 0, "feat": 1, "refactor": 2, "test": 3, "chore": 4}
MSG_RE = re.compile(r"^(feat|fix|refactor|test|chore|docs)(\(([^)]+)\))?:\s*(.+)$")

def parse_msg_internal(msg: str):
    m = MSG_RE.match(msg)
    if not m:
        return None
    return m.group(1), m.group(3), m.group(4)

def fmt_internal(typ, scope, subject):
    if scope is None:
        return f"{typ}: {subject}"
    return f"{typ}({scope}): {subject}"

def key_internal(item):
    h, dt, typ, scope, subject = item
    scope_key = (1, "") if scope is None else (0, scope)
    return (TYPE_ORDER[typ], scope_key, -int(dt.timestamp()), h)

def solve_internal(lines):
    items = []
    for (h, dt_str, msg) in lines:
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        if msg.startswith("Merge "):
            continue
        if msg.startswith("docs:"):
            continue
        parsed = parse_msg_internal(msg)
        if not parsed:
            continue
        typ, scope, subject = parsed
        if typ == "docs":
            continue
        items.append((h, dt, typ, scope, subject))
    items.sort(key=key_internal)
    return "\n".join(fmt_internal(typ, scope, subject) for _, __, typ, scope, subject in items)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(100)
test_data = []

# 예시 3개
test_data.append([
    ("a1b2c3d4", "2026-01-05 09:10", "feat(api): add search endpoint"),
    ("ff00aa11", "2026-01-05 10:00", "fix(api): handle null request"),
    ("1234abcd", "2026-01-05 08:30", "docs: update README"),
    ("beefcafe", "2026-01-04 22:00", "refactor(core): split service layer"),
    ("0badf00d", "2026-01-05 10:00", "fix: patch build error"),
    ("abcd0001", "2026-01-03 12:00", "Merge branch 'dev'"),
    ("9999eeee", "2026-01-05 09:50", "chore(ci): update pipeline"),
])
test_data.append([
    ("aa11bb22", "2026-01-01 10:00", "feat: init project"),
    ("cc33dd44", "2026-01-01 10:01", "feat(ui): add button"),
    ("ee55ff66", "2026-01-01 09:59", "fix(ui): hotfix"),
    ("11223344", "2026-01-01 10:02", "fix: adjust config"),
    ("deadbeef", "2026-01-01 10:03", "test(ui): add tests"),
])
test_data.append([
    ("abcd1234", "2026-01-01 00:00", "chore: setup"),
    ("bead5678", "2026-01-01 00:01", "docs: note"),
])

SCOPES = [None, "api", "core", "ui", "db", "auth", "ci"]
TYPES = ["feat", "fix", "refactor", "test", "chore", "docs"]
SUBJECTS = [
    "add endpoint", "handle null", "optimize query", "update config",
    "improve logging", "add unit tests", "cleanup code", "bump version",
    "rename variable", "fix typo", "update pipeline", "reduce latency"
]

def rand_hash():
    return "".join(random.choice("0123456789abcdef") for _ in range(8))

def rand_dt(base: datetime):
    # base 기준 +- 3일, 분 단위
    delta_min = random.randint(-3 * 24 * 60, 3 * 24 * 60)
    dt = base + timedelta(minutes=delta_min)
    return dt.strftime("%Y-%m-%d %H:%M")

def make_msg():
    # merge 커밋도 섞어서 생성
    if random.randint(1, 20) == 1:
        return "Merge branch 'feature-x'"
    typ = random.choice(TYPES)
    scope = random.choice(SCOPES)
    subject = random.choice(SUBJECTS)

    if typ == "docs":
        # docs: 형태로만 나오게
        return f"docs: {subject}"

    if scope is None:
        return f"{typ}: {subject}"
    return f"{typ}({scope}): {subject}"

base_time = datetime(2026, 1, 15, 12, 0)

for _ in range(17):
    n = random.randint(1, 200)
    lines = []
    for _ in range(n):
        h = rand_hash()
        dt = rand_dt(base_time)
        msg = make_msg()
        lines.append((h, dt, msg))
    test_data.append(lines)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, lines in enumerate(test_data, 1):
    out_lines = [str(len(lines))]
    for h, dt, msg in lines:
        # 입력 형식: hash YYYY-MM-DD HH:MM message...
        out_lines.append(f"{h} {dt} {msg}")
    input_str = "\n".join(out_lines) + "\n"
    ans = solve_internal(lines)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + ("\n" if ans else ""))

print("✅ 'Level01/P100' 문제 생성이 완료되었습니다.")
