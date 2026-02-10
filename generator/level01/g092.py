import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P092 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P092")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 짝수 우선 정렬 보고서

## 문제 설명
회계 담당자 **서연**은 숫자 목록으로 된 정산 데이터를 정리하려고 합니다.

서연은 다음 규칙으로 숫자들을 정렬한 결과를 출력하려고 합니다.

1. **짝수**를 **홀수**보다 먼저 배치한다.
2. 짝수끼리는 **내림차순**으로 정렬한다.
3. 홀수끼리는 **오름차순**으로 정렬한다.

정수 배열이 주어질 때, 위 규칙대로 정렬한 결과를 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 N이 주어집니다. (1 ≤ N ≤ 200)
- 둘째 줄에 N개의 정수 A1, A2, ..., AN 이 공백으로 구분되어 주어집니다.
  - 각 정수는 -10<sup>9</sup> 이상 10<sup>9</sup> 이하입니다.

## 출력 형식 (Output Format)
- 규칙대로 정렬된 N개의 정수를 공백으로 구분해 한 줄에 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
7
5 2 9 4 8 1 6
{TICK}
**Output:**
{TICK}
8 6 4 2 1 5 9
{TICK}
- 짝수는 8, 6, 4, 2 순으로 내림차순 정렬됩니다.
- 홀수는 1, 5, 9 순으로 오름차순 정렬됩니다.

### 예시 2
**Input:**
{TICK}
5
7 3 5 1 9
{TICK}
**Output:**
{TICK}
1 3 5 7 9
{TICK}
- 짝수가 없으므로 홀수만 오름차순으로 정렬한 결과를 출력합니다.

### 예시 3
**Input:**
{TICK}
6
0 -2 -3 -4 1 2
{TICK}
**Output:**
{TICK}
2 0 -2 -4 -3 1
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))[:n]

    arr.sort(key=lambda x: (x % 2, -x if x % 2 == 0 else x))
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(arr):
    arr = sorted(arr, key=lambda x: (x % 2, -x if x % 2 == 0 else x))
    return " ".join(map(str, arr))

random.seed(92)

test_data = []

# 샘플 3개 (problem.md 예시와 일치)
test_data.append([5, 2, 9, 4, 8, 1, 6])          # 예시 1
test_data.append([7, 3, 5, 1, 9])                # 예시 2
test_data.append([0, -2, -3, -4, 1, 2])          # 예시 3

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 8)

    if mode == 1:
        # 완전 랜덤
        arr = [random.randint(-50, 50) for _ in range(n)]

    elif mode == 2:
        # 큰 범위
        arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    elif mode == 3:
        # 짝수만
        arr = [random.randint(-1000, 1000) * 2 for _ in range(n)]

    elif mode == 4:
        # 홀수만
        arr = [random.randint(-1000, 1000) * 2 + 1 for _ in range(n)]

    elif mode == 5:
        # 0 많이 포함
        arr = [random.choices([0, random.randint(-20, 20)], weights=[70, 30])[0] for _ in range(n)]

    elif mode == 6:
        # 중복 많음
        pool = [random.randint(-10, 10) for _ in range(random.randint(1, 6))]
        arr = [random.choice(pool) for _ in range(n)]

    elif mode == 7:
        # 이미 정렬된 형태(규칙대로)
        base = [random.randint(-50, 50) for _ in range(n)]
        arr = sorted(base, key=lambda x: (x % 2, -x if x % 2 == 0 else x))

    else:
        # 역정렬(규칙 반대 느낌)
        base = [random.randint(-50, 50) for _ in range(n)]
        arr = sorted(base, key=lambda x: (x % 2, -x if x % 2 == 0 else x), reverse=True)

    test_data.append(arr)

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, arr in enumerate(test_data, 1):
    n = len(arr)
    input_str = f"{n}\n" + " ".join(map(str, arr)) + "\n"
    ans = solve_internal(arr)

    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P092' 문제 생성이 완료되었습니다. ")
