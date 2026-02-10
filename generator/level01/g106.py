import os
import random
from collections import defaultdict

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P106 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P106")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 로그 검색 우선순위

## 문제 설명
서버 관리자 **은지**는 서비스 장애를 분석하기 위해 로그를 검색하는 일을 자주 합니다.

로그는 `로그ID`, `발생시각`, `중요도`, `메시지(단어들)`로 이루어져 있습니다.  
은지는 검색 속도를 높이기 위해, 메시지에 포함된 단어들을 이용해 **역색인(inverted file)** 을 구성해 두었습니다.

사용자가 여러 개의 검색어를 입력하면, 은지는 역색인을 이용해 검색 결과 로그를 모은 뒤
다음 기준으로 정렬해 상위 K개만 확인하려고 합니다.

각 로그에 대해 아래 값을 계산합니다.

- `hit`: 검색어 중 **서로 다른 단어**가 해당 로그 메시지에 포함된 개수
- `freq`: 해당 로그에서 검색어가 등장한 **총 횟수**
- `severity`: 중요도 (정수, 값이 클수록 더 중요)
- `time`: 발생 시각 (YYYYMMDDHHMM 정수, 값이 클수록 더 최근)

정렬 우선순위는 다음과 같습니다.

1. `hit`가 큰 로그가 먼저
2. `hit`가 같다면 `severity`가 큰 로그가 먼저
3. 위까지 같다면 `freq`가 큰 로그가 먼저
4. 위까지 같다면 `time`이 더 최근인 로그가 먼저
5. 위까지 같다면 로그ID가 작은 로그가 먼저

검색어가 하나도 포함되지 않은 로그는 결과에서 제외합니다.

정렬된 결과에서 상위 K개의 로그ID를 공백으로 출력하세요.

---

## 입력 형식
- 첫 줄에 로그 개수 N이 주어집니다.
- 다음 N줄에 `로그ID 발생시각 중요도 단어개수 단어1 단어2 ...` 가 주어집니다.
- 다음 줄에 검색어 개수 Q가 주어집니다.
- 다음 줄에 Q개의 검색어가 공백으로 주어집니다.
- 마지막 줄에 정수 K가 주어집니다.

---

## 출력 형식
- 조건에 맞게 정렬된 결과에서 상위 K개의 로그ID를 공백으로 출력합니다.
- 출력할 로그가 없다면 빈 줄을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
1 202601021010 3 5 api error timeout api db
2 202601021005 5 3 error auth fail
3 202601021020 4 4 api cache miss error
4 202512311200 5 2 deploy success
2
api error
3
{TICK}

**Output:**
{TICK}
3 1 2
{TICK}
- 검색어는 `api`, `error` 입니다.
- 각 로그의 hit와 freq는 다음과 같습니다.
  - 로그 1: 메시지에 api(2회), error(1회) 포함 <br/>hit=2, freq=3, severity=3, time=202601021010
  - 로그 2: 메시지에 error(1회)만 포함 <br/>hit=1, freq=1, severity=5, time=202601021005
  - 로그 3: 메시지에 api(1회), error(1회) 포함 <br/>hit=2, freq=2, severity=4, time=202601021020
  - 로그 4: 검색어가 없음 → 결과에서 제외
- 정렬 과정:
  - hit가 큰 로그(로그 1,3)가 먼저 옵니다. (둘 다 hit=2)
  - hit가 같으면 severity가 큰 로그가 먼저이므로, severity=4인 로그 3이 severity=3인 로그 1보다 앞입니다.
  - hit가 1인 로그 2는 그 다음에 옵니다.
- 따라서 상위 3개 결과는 `3 1 2` 입니다.

### 예시 2
**Input:**
{TICK}
5
10 202601010900 2 4 db slow query db
11 202601010905 2 3 db fail error
12 202601010910 5 4 api db fail timeout
13 202601010915 3 2 fail fail
14 202601010920 4 3 api error fail
3
db fail api
4
{TICK}

**Output:**
{TICK}
12 14 11 13
{TICK}
- 검색어는 `db`, `fail`, `api` 입니다.
- 로그별 hit를 보면:
  - 로그 12: db, fail, api 모두 포함 <br/>hit=3 (가장 우선)
  - 로그 14: api, fail 포함 <br/>hit=2
  - 로그 11: db, fail 포함 <br/>hit=2
  - 로그 13: fail만 포함 <br/>hit=1
  - 로그 10: db만 포함 <br/>hit=1 (하지만 K=4라서 최종 출력에서 밀림)
- hit가 같은 그룹에서는 severity가 큰 로그가 먼저입니다.
  - (hit=2 그룹) 로그 14(sev=4) > 로그 11(sev=2)
  - (hit=1 그룹) 로그 13(sev=3) > 로그 10(sev=2)
- 따라서 상위 4개 결과는 `12 14 11 13` 입니다.


### 예시 3
**Input:**
{TICK}
2
7 202601011000 5 2 cache hit
8 202601011005 4 2 api ok
1
error
5
{TICK}

**Output:**
{TICK}

{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    n = int(input().strip())

    # log_id -> (time, severity, word_counts)
    time_map = {}
    sev_map = {}
    word_cnt = defaultdict(lambda: defaultdict(int))
    inv = defaultdict(set)  # word -> set(log_id) (for fast candidate union)

    for _ in range(n):
        parts = input().split()
        log_id = int(parts[0])
        t = int(parts[1])
        sev = int(parts[2])
        c = int(parts[3])
        words = parts[4:4+c]

        time_map[log_id] = t
        sev_map[log_id] = sev
        for w in words:
            word_cnt[log_id][w] += 1
            inv[w].add(log_id)

    q = int(input().strip())
    query = input().split()[:q]
    k = int(input().strip())

    # 후보 로그 모으기 (역색인 활용)
    candidates = set()
    for w in query:
        candidates |= inv.get(w, set())

    if not candidates:
        print()
        return

    hit = {}
    freq = {}

    for log_id in candidates:
        h = 0
        f = 0
        wm = word_cnt[log_id]
        for w in query:
            c = wm.get(w, 0)
            if c > 0:
                h += 1
                f += c
        if h > 0:
            hit[log_id] = h
            freq[log_id] = f

    if not hit:
        print()
        return

    logs = list(hit.keys())
    logs.sort(key=lambda x: (-hit[x], -sev_map[x], -freq[x], -time_map[x], x))
    logs = logs[:k]
    print(" ".join(map(str, logs)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(logs, query, k):
    # logs: list of (id, time, sev, words(list))
    time_map = {}
    sev_map = {}
    word_cnt = defaultdict(lambda: defaultdict(int))
    inv = defaultdict(set)

    for log_id, t, sev, words in logs:
        time_map[log_id] = t
        sev_map[log_id] = sev
        for w in words:
            word_cnt[log_id][w] += 1
            inv[w].add(log_id)

    candidates = set()
    for w in query:
        candidates |= inv.get(w, set())

    if not candidates:
        return ""

    hit = {}
    freq = {}
    for log_id in candidates:
        h = 0
        f = 0
        wm = word_cnt[log_id]
        for w in query:
            c = wm.get(w, 0)
            if c > 0:
                h += 1
                f += c
        if h > 0:
            hit[log_id] = h
            freq[log_id] = f

    if not hit:
        return ""

    ids = list(hit.keys())
    ids.sort(key=lambda x: (-hit[x], -sev_map[x], -freq[x], -time_map[x], x))
    return " ".join(map(str, ids[:k]))

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(106)
test_cases = []

# 예시 3개 (problem.md와 일치)
logs1 = [
    (1, 202601021010, 3, ["api", "error", "timeout", "api", "db"]),
    (2, 202601021005, 5, ["error", "auth", "fail"]),
    (3, 202601021020, 4, ["api", "cache", "miss", "error"]),
    (4, 202512311200, 5, ["deploy", "success"]),
]
query1 = ["api", "error"]
k1 = 3
test_cases.append((logs1, query1, k1))

logs2 = [
    (10, 202601010900, 2, ["db", "slow", "query", "db"]),
    (11, 202601010905, 2, ["db", "fail", "error"]),
    (12, 202601010910, 1, ["auth", "fail"]),
]
query2 = ["db", "fail"]
k2 = 2
test_cases.append((logs2, query2, k2))

logs3 = [
    (7, 202601011000, 5, ["cache", "hit"]),
    (8, 202601011005, 4, ["api", "ok"]),
]
query3 = ["error"]
k3 = 5
test_cases.append((logs3, query3, k3))

WORD_POOL = [
    "api", "db", "auth", "cache", "search", "index", "network", "log",
    "build", "deploy", "user", "order", "payment", "timeout", "error",
    "fail", "retry", "limit", "slow", "query", "miss", "hit", "success"
]

def rand_time():
    y = random.randint(2024, 2026)
    mo = random.randint(1, 12)
    d = random.randint(1, 28)
    h = random.randint(0, 23)
    mi = random.randint(0, 59)
    return y * 100000000 + mo * 1000000 + d * 10000 + h * 100 + mi

for _ in range(17):
    n = random.randint(1, 120)
    logs = []
    used_ids = set()
    for _ in range(n):
        while True:
            log_id = random.randint(1, 500)
            if log_id not in used_ids:
                used_ids.add(log_id)
                break
        t = rand_time()
        sev = random.randint(1, 5)
        c = random.randint(1, 12)
        words = [random.choice(WORD_POOL) for _ in range(c)]
        logs.append((log_id, t, sev, words))

    q = random.randint(1, 5)
    query = random.sample(WORD_POOL, q)
    k = random.randint(1, 10)

    test_cases.append((logs, query, k))

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (logs, query, k) in enumerate(test_cases, 1):
    input_lines = [str(len(logs))]
    for log_id, t, sev, words in logs:
        input_lines.append(f"{log_id} {t} {sev} {len(words)} " + " ".join(words))
    input_lines.append(str(len(query)))
    input_lines.append(" ".join(query))
    input_lines.append(str(k))

    input_str = "\n".join(input_lines) + "\n"
    ans = solve_internal(logs, query, k)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P106' 문제 생성이 완료되었습니다. ")
