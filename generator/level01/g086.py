import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P086 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P086")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = """# 티켓 라인업 정리

## 문제 설명
축제 매니저 **지후**는 관람객들이 들고 온 티켓 번호를 정리하려고 합니다.  
티켓에는 정수 번호가 적혀 있으며, 같은 번호의 티켓이 여러 장 있을 수 있습니다.

지후는 티켓을 번호 기준으로 정리한 뒤, 각 번호가 **몇 장인지** 요약해서 출력하려고 합니다.

티켓 번호 목록이 주어질 때,

- 서로 다른 티켓 번호를 **오름차순**으로 정렬하고
- 각 번호의 **등장 횟수**를 함께 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 둘째 줄에 $N$개의 정수 $A_1, A_2, \\dots, A_N$이 공백으로 구분되어 주어집니다.  
  $(-10^9 \\le A_i \\le 10^9)$

## 출력 형식 (Output Format)
- 서로 다른 티켓 번호를 오름차순으로 정렬한 뒤, 각 번호와 등장 횟수를 한 줄에 하나씩 출력하세요.
- 각 줄은 `번호 개수` 형태입니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
8
10 12 10 15 12 10 7 15
{TICK}
**Output:**
{TICK}
7 1
10 3
12 2
15 2
{TICK}
- 티켓 번호를 오름차순으로 정리하면 7, 10, 12, 15 순서입니다.
- 각 번호가 나온 횟수를 세어 `번호 개수` 형태로 출력합니다.

### 예시 2
**Input:**
{TICK}
5
3 3 3 3 3
{TICK}
**Output:**
{TICK}
3 5
{TICK}
- 모든 티켓 번호가 같으므로 한 줄만 출력합니다.
- 번호 3은 총 5번 등장합니다.

### 예시 3
**Input:**
{TICK}
6
-1 2 -1 0 2 2
{TICK}
**Output:**
{TICK}
-1 2
0 1
2 3
{TICK}
""".format(TICK=TICK)

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

    arr.sort()

    out = []
    i = 0
    while i < n:
        v = arr[i]
        j = i
        while j < n and arr[j] == v:
            j += 1
        out.append(f"{v} {j - i}")
        i = j

    sys.stdout.write("\\n".join(out))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(arr):
    arr = sorted(arr)
    out = []
    i = 0
    n = len(arr)
    while i < n:
        v = arr[i]
        j = i
        while j < n and arr[j] == v:
            j += 1
        out.append(f"{v} {j - i}")
        i = j
    return "\n".join(out)

random.seed(86)

test_data = []

# 샘플 3개 (problem.md 예시와 일치)
test_data.append([10, 12, 10, 15, 12, 10, 7, 15])   # 예시 1
test_data.append([3, 3, 3, 3, 3])                    # 예시 2
test_data.append([-1, 2, -1, 0, 2, 2])               # 예시 3

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 7)

    if mode == 1:
        # 완전 랜덤 (중복 적당)
        arr = [random.randint(-50, 50) for _ in range(n)]

    elif mode == 2:
        # 큰 범위 랜덤
        arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    elif mode == 3:
        # 중복 매우 많음 (소수의 값만 반복)
        pool = [random.randint(-10, 10) for _ in range(random.randint(1, 5))]
        arr = [random.choice(pool) for _ in range(n)]

    elif mode == 4:
        # 모두 동일
        v = random.randint(-100, 100)
        arr = [v] * n

    elif mode == 5:
        # 이미 정렬된 상태
        arr = sorted([random.randint(-1000, 1000) for _ in range(n)])

    elif mode == 6:
        # 역정렬된 상태
        arr = sorted([random.randint(-1000, 1000) for _ in range(n)], reverse=True)

    else:
        # 0이 많이 포함된 케이스
        arr = [random.choices([0, random.randint(-20, 20)], weights=[70, 30])[0] for _ in range(n)]

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

print(f"✅ 'Level01/P086' 문제 생성이 완료되었습니다. ")