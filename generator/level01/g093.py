import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P093 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P093")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 요청 순서에 따른 점수 조회

## 문제 설명
시험 담당자 TA **민재**는 학생들의 점수 목록을 관리하고 있습니다.

민재는 점수 배열과 여러 개의 조회 요청을 받습니다.  
각 조회 요청마다 **항상 같은 순서의 작업**을 수행합니다.

조회 요청 처리 순서는 다음과 같습니다.
하나의 요청 `(i, j, k)`에 대해 다음 과정을 차례대로 수행합니다.

1. 점수 배열에서 **i번째부터 j번째까지**의 점수만 선택합니다.  
   (점수의 번호는 **1번부터 시작**합니다.)
2. 선택한 점수들을 **오름차순으로 정렬**합니다.
3. 정렬된 결과에서 **k번째에 위치한 점수**를 확인합니다.

각 요청에 대해 **확인한 점수**를 순서대로 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 점수의 개수가 정수 N으로 주어집니다. (1 ≤ N ≤ 200)
- 둘째 줄에 N개의 정수 점수 배열이 주어집니다.  
  - 각 점수는 -10<sup>9</sup> 이상 10<sup>9</sup> 이하입니다.
- 셋째 줄에 조회 요청의 개수가 정수 Q가 주어집니다. (1 ≤ Q ≤ 200)
- 다음 Q줄에 걸쳐 세 정수 (i, j, k)가 주어집니다.
  - 1 ≤ i ≤ j ≤ N
  - 1 ≤ k ≤ (j - i + 1)

## 출력 형식 (Output Format)
- 각 요청에 대한 결과를 **한 줄에 하나씩** 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
10 40 20 30 50
2
2 5 3
1 3 2
{TICK}
**Output:**
{TICK}
40
20
{TICK}
- 첫 번째 요청: [40, 20, 30, 50] 
  - 정렬 후 [20, 30, 40, 50] → 3번째 값은 40
- 두 번째 요청: [10, 40, 20] 
  - 정렬 후 [10, 20, 40] → 2번째 값은 20

### 예시 2
**Input:**
{TICK}
4
7 3 9 1
1
1 4 1
{TICK}
**Output:**
{TICK}
1
{TICK}
- 전체 배열을 정렬하면 [1, 3, 7, 9] 이며 1 번째 값은 1입니다.

### 예시 3
**Input:**
{TICK}
3
5 5 5
1
2 3 2
{TICK}
**Output:**
{TICK}
5
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline

    n = int(input().strip())
    arr = list(map(int, input().split()))

    q = int(input().strip())
    for _ in range(q):
        i, j, k = map(int, input().split())
        part = arr[i-1:j]
        part.sort()
        print(part[k-1])

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(arr, queries):
    res = []
    for i, j, k in queries:
        part = sorted(arr[i-1:j])
        res.append(str(part[k-1]))
    return "\n".join(res)

# ---------------------------------------------------------
# 5. 테스트케이스 생성
# ---------------------------------------------------------
random.seed(93)
test_data = []

# 예시 3개
test_data.append(
    ([10, 40, 20, 30, 50], [(2, 5, 3), (1, 3, 2)])
)
test_data.append(
    ([7, 3, 9, 1], [(1, 4, 1)])
)
test_data.append(
    ([5, 5, 5], [(2, 3, 2)])
)

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    arr = [random.randint(-1000, 1000) for _ in range(n)]

    q = random.randint(1, 200)
    queries = []
    for _ in range(q):
        i = random.randint(1, n)
        j = random.randint(i, n)
        k = random.randint(1, j - i + 1)
        queries.append((i, j, k))

    test_data.append((arr, queries))

# ---------------------------------------------------------
# 6. 파일 저장
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (arr, queries) in enumerate(test_data, 1):
    lines = []
    lines.append(str(len(arr)))
    lines.append(" ".join(map(str, arr)))
    lines.append(str(len(queries)))
    for i, j, k in queries:
        lines.append(f"{i} {j} {k}")

    input_str = "\n".join(lines) + "\n"
    output_str = solve_internal(arr, queries)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

print(f"✅ 'Level01/P093' 문제 생성이 완료되었습니다. ")
