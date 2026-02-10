import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P99 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P99")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 숫자 카드 정렬 규칙

## 문제 설명
카드 정리 담당자 **서현**은 숫자 카드들을 규칙에 맞게 정렬하려고 합니다.

각 카드는 정수 하나가 적혀 있습니다. 서현은 다음 규칙으로 카드를 정렬합니다.

1. 각 숫자의 **자릿수 합**이 작은 카드가 먼저 온다.
2. 자릿수 합이 같다면 **숫자가 작은 카드**가 먼저 온다.

정렬된 결과를 공백으로 구분해 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 카드의 개수 정수 N이 주어집니다.  
- 둘째 줄에 각 카드의 숫자가 정수로 공백으로 구분되어 주어집니다.  
- 각 정수는 -10<sup>9</sup> 이상 10<sup>9</sup> 이하입니다.

---

## 출력 형식 (Output Format)
- 규칙에 따라 정렬된 N개의 정수를 공백으로 구분해 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
19 7 100 28 55 40
{TICK}
**Output:**
{TICK}
100 40 7 19 28 55
{TICK}
- 자릿수 합
  - 100→1
  - 40→4 
  - 7→7
  - 19→10
  - 28→10
  - 55→10
- 합이 같으면 숫자가 작은 것이 먼저 옵니다.

### 예시 2
**Input:**
{TICK}
5
-12 -3 0 21 111
{TICK}
**Output:**
{TICK}
0 -3 -12 21 111
{TICK}
- 음수는 부호를 제외한 숫자 부분의 자릿수 합을 사용합니다.
- 자릿수 합이 같을 때는 실제 숫자 크기 기준으로 정렬합니다.

### 예시 3
**Input:**
{TICK}
4
5 50 500 5000
{TICK}
**Output:**
{TICK}
5 50 500 5000
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def digit_sum(x: int) -> int:
    x = abs(x)
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))[:n]

    arr.sort(key=lambda v: (digit_sum(v), v))
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def digit_sum_internal(x: int) -> int:
    x = abs(x)
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def solve_internal(arr):
    arr2 = sorted(arr, key=lambda v: (digit_sum_internal(v), v))
    return " ".join(map(str, arr2))

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(99)
test_data = []

# 예시 3개 (problem.md와 일치)
test_data.append([19, 7, 100, 28, 55, 40])
test_data.append([-12, -3, 0, 21, 111])
test_data.append([5, 50, 500, 5000])

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 8)

    if mode == 1:
        arr = [random.randint(-1000, 1000) for _ in range(n)]
    elif mode == 2:
        arr = [random.randint(-10**9, 10**9) for _ in range(n)]
    elif mode == 3:
        # 양수만
        arr = [random.randint(0, 10**6) for _ in range(n)]
    elif mode == 4:
        # 음수만
        arr = [-random.randint(0, 10**6) for _ in range(n)]
    elif mode == 5:
        # 0 많이 포함
        arr = [random.choices([0, random.randint(-200, 200)], weights=[60, 40])[0] for _ in range(n)]
    elif mode == 6:
        # 자릿수 합 동률 많이 나오게 (예: 19, 28, 37, 46, 55...)
        arr = []
        target = random.randint(1, 20)
        for _ in range(n):
            # target을 만들도록 임의 구성
            a = random.randint(0, target)
            b = target - a
            val = a * 10 + b  # 0~99
            if random.randint(0, 1) == 1:
                val = -val
            arr.append(val)
    elif mode == 7:
        # 중복 많음
        pool = [random.randint(-50, 50) for _ in range(random.randint(1, 6))]
        arr = [random.choice(pool) for _ in range(n)]
    else:
        # 이미 정렬된 상태/역정렬 섞기
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        arr.sort(key=lambda v: (digit_sum_internal(v), v))
        if random.randint(0, 1) == 1:
            arr.reverse()

    test_data.append(arr)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, arr in enumerate(test_data, 1):
    input_str = f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"
    ans = solve_internal(arr)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P99' 문제 생성이 완료되었습니다.")
