import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P094 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P094")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 역순 정렬 결과 조회

## 문제 설명
편집자 **하은**은 문서 번호 목록을 관리하고 있습니다.

문서 번호 배열과 하나의 요청 `(i, j, k)`가 주어질 때, 다음 작업을 수행하세요.

1. 배열의 i번째부터 j번째까지의 값을 선택한다. (1번부터 시작)
2. 선택한 값들을 **내림차순으로 정렬**한다.
3. 정렬된 결과에서 **k번째 값**을 출력한다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 문서 번호의 개수가 정수 N으로 주어진다.
- 둘째 줄에 문서 번호 배열이 N개의 정수로 주어진다.
- 셋째 줄에 정수 i, j, k가 주어진다.

---

## 출력 형식 (Output Format)
- 조건을 만족하는 값을 출력한다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
10 40 20 30 50
2 5 2
{TICK}
**Output:**
{TICK}
40
{TICK}
- 요청 (i, j, k) = (2 5 2)
  - [40, 20, 30, 50] → 내림차순 정렬 → [50, 40, 30, 20]

### 예시 2
**Input:**
{TICK}
6
5 1 9 3 7 2
1 6 3
{TICK}
**Output:**
{TICK}
5
{TICK}
- (1 6 3)은 전체 배열
- 내림차순으로 정렬하면 [9, 7, 5, 3, 2, 1]
- 3번째는 5

### 예시 3
**Input:**
{TICK}
3
4 4 4
1 3 1
{TICK}
**Output:**
{TICK}
4
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
    i, j, k = map(int, input().split())

    part = arr[i-1:j]
    part.sort(reverse=True)
    print(part[k-1])

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(arr, query):
    i, j, k = query
    part = sorted(arr[i-1:j], reverse=True)
    return str(part[k-1])

# ---------------------------------------------------------
# 5. 테스트케이스 생성
# ---------------------------------------------------------
random.seed(94)
test_data = []

# 예시 3개
test_data.append(([10, 40, 20, 30, 50], (2, 5, 2)))
test_data.append(([5, 1, 9, 3, 7, 2], (1, 6, 3)))
test_data.append(([4, 4, 4], (1, 3, 1)))

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    arr = [random.randint(-1000, 1000) for _ in range(n)]

    i = random.randint(1, n)
    j = random.randint(i, n)
    k = random.randint(1, j - i + 1)

    test_data.append((arr, (i, j, k)))

# ---------------------------------------------------------
# 6. 파일 저장
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (arr, query) in enumerate(test_data, 1):
    i, j, k = query
    input_str = (
        f"{len(arr)}\n"
        + " ".join(map(str, arr)) + "\n"
        + f"{i} {j} {k}\n"
    )
    ans = solve_internal(arr, query)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P094' 문제 생성이 완료되었습니다. ")
