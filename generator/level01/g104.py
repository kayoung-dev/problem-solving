import os
import random
from collections import defaultdict

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P104 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P104")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 강의 노트 검색 결과 정리

## 문제 설명
조교 **지수**는 여러 강의 노트(문서)를 빠르게 검색하기 위해 단어별로 문서 목록을 모아 둔 **역색인(inverted file)** 을 사용합니다.

각 기록은 `문서ID 단어` 형태로 주어지며, 같은 문서에서 같은 단어가 여러 번 등장할 수 있습니다.
사용자가 여러 개의 검색어를 입력하면, 지수는 역색인을 이용해 검색 결과 문서를 모은 뒤 우선순위에 따라 정렬해 상위 K개만 보여주려고 합니다.

지수는 각 문서에 대해 다음 값을 계산합니다.

- `hit`: 검색어 중 **서로 다른 단어**가 이 문서에 등장한 개수
- `freq`: 이 문서에서 검색어가 등장한 **총 횟수**
- `date`: 문서의 작성일(YYYYMMDD 정수)

문서는 다음 우선순위로 정렬합니다.

1. `hit`가 큰 문서가 먼저
2. `hit`가 같다면 `freq`가 큰 문서가 먼저
3. 위까지 같다면 `date`가 더 최근인 문서가 먼저
4. 위까지 같다면 문서ID가 작은 문서가 먼저

정렬된 결과에서 상위 K개의 문서ID를 공백으로 출력하세요.  
검색어가 하나도 등장하지 않는 문서는 결과에서 제외합니다.

---

## 입력 형식
- 첫 줄에 문서 개수 N이 주어집니다.
- 다음 N줄에 `문서ID 작성일`이 주어집니다. (작성일은 YYYYMMDD 정수)
- 다음 줄에 기록의 개수 M이 주어집니다.
- 다음 M줄에 `문서ID 단어` 형식의 기록이 주어집니다.
- 다음 줄에 검색어 개수 Q가 주어집니다.
- 다음 줄에 Q개의 검색어가 공백으로 주어집니다.
- 마지막 줄에 출력할 상위 문서 결과 정수 K가 주어집니다.

---

## 출력 형식
- 조건에 맞게 정렬된 결과에서 상위 K개의 문서ID를 공백으로 출력합니다.
- 출력할 문서가 없다면 빈 줄을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
1 20260101
2 20260103
3 20251231
4 20260102
10
1 network
1 network
1 db
2 network
2 db
2 auth
3 db
3 db
4 auth
4 auth
2
network db
3
{TICK}

**Output:**
{TICK}
1 2 3
{TICK}
- 문서 1
  - hit=2(network, db), freq=3, date=20260101
- 문서 2
  - hit=2(network, db), freq=2, date=20260103  
  - hit이 같으면 freq가 큰 문서가 먼저이므로 문서 1이 먼저입니다.
- 문서 3
  - hit=1(db), freq=2  
따라서 1 → 2 → 3 순서이며, K=3이므로 그대로 출력합니다.

### 예시 2
**Input:**
{TICK}
5
1 20240101
2 20240101
3 20240102
4 20240102
5 20240102
10
1 alpha
1 beta
2 alpha
2 beta
3 alpha
3 beta
3 beta
4 alpha
4 beta
5 alpha
2
alpha beta
5
{TICK}

**Output:**
{TICK}
3 4 1 2 5
{TICK}
- 문서 3
  - hit=2(alpha, beta), freq=3, date=20240102 
  - freq가 가장 커서 가장 먼저 출력
- 문서 4
  - hit=2, freq=2, date=20240102
  - 문서 1, 2보다 날짜가 더 최근
- 문서 1
  - hit=2, freq=2, date=20240101 
  - 문서 2와 모든 조건이 같아 문서ID가 작은 1이 먼저
- 문서 2
  - hit=2, freq=2, date=20240101
- 문서 5
  - hit=1(alpha만 등장)
  - hit가 가장 작아 마지막

### 예시 3
**Input:**
{TICK}
3
1 20240101
2 20240102
3 20240103
3
1 hello
2 world
3 hello
2
db network
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
    doc_date = {}
    for _ in range(n):
        doc_id, ymd = map(int, input().split())
        doc_date[doc_id] = ymd

    m = int(input().strip())
    # word -> list of doc_id occurrences (duplicates allowed)
    inv = defaultdict(list)
    # doc -> word -> count (for hit & freq calc)
    doc_word_cnt = defaultdict(lambda: defaultdict(int))

    for _ in range(m):
        doc_id_s, word = input().split()
        doc_id = int(doc_id_s)
        inv[word].append(doc_id)
        doc_word_cnt[doc_id][word] += 1

    q = int(input().strip())
    query = input().split()[:q]
    k = int(input().strip())

    hit = defaultdict(int)
    freq = defaultdict(int)

    for doc_id, wm in doc_word_cnt.items():
        h = 0
        f = 0
        for w in query:
            c = wm.get(w, 0)
            if c > 0:
                h += 1
                f += c
        if h > 0:
            hit[doc_id] = h
            freq[doc_id] = f

    if not hit:
        print()
        return

    docs = list(hit.keys())
    docs.sort(key=lambda d: (-hit[d], -freq[d], -doc_date[d], d))
    docs = docs[:k]
    print(" ".join(map(str, docs)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(doc_date, records, query, k):
    doc_word_cnt = defaultdict(lambda: defaultdict(int))
    for doc_id, word in records:
        doc_word_cnt[doc_id][word] += 1

    hit = {}
    freq = {}
    for doc_id, wm in doc_word_cnt.items():
        h = 0
        f = 0
        for w in query:
            c = wm.get(w, 0)
            if c > 0:
                h += 1
                f += c
        if h > 0:
            hit[doc_id] = h
            freq[doc_id] = f

    if not hit:
        return ""

    docs = list(hit.keys())
    docs.sort(key=lambda d: (-hit[d], -freq[d], -doc_date[d], d))
    return " ".join(map(str, docs[:k]))

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(104)
test_cases = []

# 예시 3개 (problem.md와 일치)
doc_date1 = {1: 20260101, 2: 20260103, 3: 20251231, 4: 20260102}
records1 = [
    (1, "network"), (1, "network"), (1, "db"),
    (2, "network"), (2, "db"), (2, "auth"),
    (3, "db"), (3, "db"),
    (4, "auth"), (4, "auth"),
]
query1 = ["network", "db"]
k1 = 3
test_cases.append((doc_date1, records1, query1, k1))

doc_date2 = {10: 20250101, 11: 20250102, 12: 20250103, 13: 20240101, 14: 20250103}
records2 = [
    (10, "api"), (10, "api"),
    (11, "auth"), (11, "api"),
    (12, "auth"), (12, "auth"), (12, "api"),
    (13, "log"),
    (14, "api"),
]
query2 = ["api", "auth"]
k2 = 4
test_cases.append((doc_date2, records2, query2, k2))

doc_date3 = {1: 20240101, 2: 20240102, 3: 20240103}
records3 = [(1, "hello"), (2, "world"), (3, "hello")]
query3 = ["db", "network"]
k3 = 5
test_cases.append((doc_date3, records3, query3, k3))

WORD_POOL = ["api", "db", "auth", "cache", "search", "index", "network", "log", "build", "deploy", "user", "order"]

def rand_ymd():
    y = random.randint(2023, 2026)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return y * 10000 + m * 100 + d

# 랜덤 17개
for _ in range(17):
    n = random.randint(2, 80)
    doc_ids = random.sample(range(1, 500), n)
    doc_date = {doc_id: rand_ymd() for doc_id in doc_ids}

    m = random.randint(1, 600)
    records = []
    for _ in range(m):
        doc_id = random.choice(doc_ids)
        word = random.choice(WORD_POOL)
        records.append((doc_id, word))

    q = random.randint(1, 5)
    query = random.sample(WORD_POOL, q)
    k = random.randint(1, 10)

    test_cases.append((doc_date, records, query, k))

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (doc_date, records, query, k) in enumerate(test_cases, 1):
    docs_sorted = sorted(doc_date.items(), key=lambda x: x[0])

    input_lines = [str(len(docs_sorted))]
    for doc_id, ymd in docs_sorted:
        input_lines.append(f"{doc_id} {ymd}")

    input_lines.append(str(len(records)))
    for doc_id, word in records:
        input_lines.append(f"{doc_id} {word}")

    input_lines.append(str(len(query)))
    input_lines.append(" ".join(query))
    input_lines.append(str(k))

    input_str = "\n".join(input_lines) + "\n"
    ans = solve_internal(doc_date, records, query, k)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P104' 문제 생성이 완료되었습니다. ")
