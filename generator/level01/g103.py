import os
import random
from collections import defaultdict

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P103 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P103")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 문서 검색 결과 정렬

## 문제 설명
검색 엔지니어 **현우**는 간단한 문서 검색 기능을 만들고 있습니다.

현우는 각 단어가 어떤 문서에 등장했는지를 미리 정리한 **역색인(inverted file)** 을 가지고 있습니다.  
역색인에는 단어별로 문서 목록이 저장되어 있으며, 한 단어가 여러 문서에 등장할 수 있습니다.

사용자가 여러 개의 검색어를 입력하면, 현우는 역색인을 이용해 검색 결과 문서를 모아 정리하려고 합니다.  
이때 결과 문서를 정리하는 기준은 다음과 같습니다.

- 어떤 문서가 검색어와 **일치하는 단어 개수**가 많을수록 더 먼저 보여야 합니다.
- 일치하는 단어 개수가 같다면, 문서의 **작성일(YYYYMMDD)** 이 더 최근인 문서가 먼저 보여야 합니다.
- 위 기준까지 같다면, 문서 ID가 작은 문서가 먼저 보여야 합니다.

각 단어에 대한 문서 목록은 중복이 없다고 가정합니다.

주어진 역색인과 문서 작성일, 그리고 검색어 목록이 주어질 때  
정렬된 검색 결과 문서 ID를 출력하세요.

---

## 입력 형식
- 첫 줄에 문서 개수 N이 주어집니다.
- 다음 N줄에 문서 정보 `문서ID 작성일` 이 주어집니다. (작성일은 YYYYMMDD 정수)
- 다음 줄에 역색인 정보의 개수 W가 주어집니다.
- 다음 W줄에 단어별 역색인 정보가 주어집니다.
  - 형식: `단어 K 문서ID1 문서ID2 ... 문서IDK`
- 마지막 줄에 검색어 개수 Q가 주어집니다.
- 마지막 줄에 Q개의 검색어가 공백으로 주어집니다.

---

## 출력 형식
- 조건에 맞게 정렬된 문서 ID를 공백으로 출력합니다.
- 검색어와 하나도 일치하지 않는 문서는 출력하지 않습니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
1 20260101
2 20251231
3 20260103
4 20240101
5 20260102
3
apple 3 1 2 3
banana 2 3 5
carrot 2 2 5
2
apple banana
{TICK}

**Output:**
{TICK}
3 5 1 2
{TICK}
- 문서 3은 apple과 banana 모두 포함(2개) → 가장 먼저
- 문서 5는 banana 포함(1개)이며 날짜가 20260102로 가장 최근
- 문서 1과 2는 apple만 포함(1개), 날짜 비교 후 1이 더 최근이라 먼저

### 예시 2
**Input:**
{TICK}
4
10 20250101
11 20250103
12 20250102
13 20240101
2
network 3 10 11 12
db 2 11 13
2
network db
{TICK}

**Output:**
{TICK}
11 12 10 13
{TICK}
- 문서 11은 두 검색어 모두 포함
- 나머지는 포함 단어 수가 같으면 작성일이 최근인 문서가 먼저

### 예시 3
**Input:**
{TICK}
3
1 20240101
2 20240102
3 20240103
1
alpha 1 2
2
beta gamma
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

    w = int(input().strip())
    inv = defaultdict(list)
    for _ in range(w):
        parts = input().split()
        word = parts[0]
        k = int(parts[1])
        ids = list(map(int, parts[2:2+k]))
        inv[word] = ids

    q = int(input().strip())
    query_words = input().split()
    query_words = query_words[:q]

    match_count = defaultdict(int)
    for word in query_words:
        for doc_id in inv.get(word, []):
            match_count[doc_id] += 1

    # 결과가 없다면 빈 줄 출력
    if not match_count:
        print()
        return

    # 정렬: (일치 단어 수 desc, 작성일 desc, 문서ID asc)
    docs = list(match_count.keys())
    docs.sort(key=lambda d: (-match_count[d], -doc_date[d], d))

    print(" ".join(map(str, docs)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(doc_date, inv, query_words):
    match = defaultdict(int)
    for w in query_words:
        for doc_id in inv.get(w, []):
            match[doc_id] += 1
    if not match:
        return ""
    docs = list(match.keys())
    docs.sort(key=lambda d: (-match[d], -doc_date[d], d))
    return " ".join(map(str, docs))

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(103)
test_cases = []

# 예시 3개 (problem.md와 일치)
doc_date1 = {1: 20260101, 2: 20251231, 3: 20260103, 4: 20240101, 5: 20260102}
inv1 = {
    "apple": [1, 2, 3],
    "banana": [3, 5],
    "carrot": [2, 5],
}
q1 = ["apple", "banana"]
test_cases.append((doc_date1, inv1, q1))

doc_date2 = {10: 20250101, 11: 20250103, 12: 20250102, 13: 20240101}
inv2 = {
    "network": [10, 11, 12],
    "db": [11, 13],
}
q2 = ["network", "db"]
test_cases.append((doc_date2, inv2, q2))

doc_date3 = {1: 20240101, 2: 20240102, 3: 20240103}
inv3 = {"alpha": [2]}
q3 = ["beta", "gamma"]
test_cases.append((doc_date3, inv3, q3))

# 랜덤 17개
WORD_POOL = ["api", "db", "auth", "cache", "search", "index", "network", "log", "build", "deploy", "user", "order"]

def rand_ymd():
    # 2023~2026 범위의 YYYYMMDD
    y = random.randint(2023, 2026)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return y * 10000 + m * 100 + d

for _ in range(17):
    n = random.randint(1, 80)
    doc_ids = random.sample(range(1, 500), n)
    doc_date = {doc_id: rand_ymd() for doc_id in doc_ids}

    w = random.randint(1, min(30, len(WORD_POOL)))
    words = random.sample(WORD_POOL, w)

    inv = {}
    for word in words:
        k = random.randint(0, min(15, n))
        if k == 0:
            inv[word] = []
        else:
            inv[word] = random.sample(doc_ids, k)

    q = random.randint(1, 6)
    query_words = random.sample(WORD_POOL, q)

    test_cases.append((doc_date, inv, query_words))

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (doc_date, inv, query_words) in enumerate(test_cases, 1):
    # 입력 구성
    docs_sorted = sorted(doc_date.items(), key=lambda x: x[0])
    input_lines = [str(len(docs_sorted))]
    for doc_id, ymd in docs_sorted:
        input_lines.append(f"{doc_id} {ymd}")

    inv_items = list(inv.items())
    input_lines.append(str(len(inv_items)))
    for word, ids in inv_items:
        input_lines.append(f"{word} {len(ids)} " + (" ".join(map(str, ids)) if ids else ""))

    input_lines.append(str(len(query_words)))
    input_lines.append(" ".join(query_words))

    input_str = "\n".join(input_lines).rstrip() + "\n"
    ans = solve_internal(doc_date, inv, query_words)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P103' 문제 생성이 완료되었습니다.")
