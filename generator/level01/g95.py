import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P95 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P95")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 가장 큰 주문 코드 만들기

## 문제 설명
물류 관리자 **도윤**은 여러 주문 코드를 한 줄의 문자열로 합쳐서, 화면에 표시되는 주문 코드가 **가장 크게** 보이도록 만들고 싶습니다.

정수 배열이 주어질 때, 배열의 모든 숫자를 문자열로 이어 붙여 만들 수 있는 결과 중 **가장 큰 값**을 출력하세요.

- 예: [3, 30, 34] → "34330" 이 최대

결과는 매우 큰 수가 될 수 있으므로 **정수로 변환하지 말고 문자열로 출력**하세요. 모든 숫자가 0이면 결과는 "0" 입니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 숫자 개수가 정수 N으로 주어진다. 
- 둘째 줄에 N개의 주문코드가 정수로 주어진다. (0 이상 10<sup>9</sup> 이하)

---

## 출력 형식 (Output Format)
- 만들 수 있는 가장 큰 값을 문자열로 출력한다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
3 30 34 5 9
{TICK}
**Output:**
{TICK}
9534330
{TICK}
- "9"를 가장 앞에 두는 것이 유리합니다.
- "34"와 "3"과 "30"은 이어 붙였을 때 더 큰 조합이 앞에 오도록 정렬합니다.

### 예시 2
**Input:**
{TICK}
3
0 0 0
{TICK}
**Output:**
{TICK}
0
{TICK}
- 모든 숫자가 0이면 "0"을 출력합니다.

### 예시 3
**Input:**
{TICK}
4
12 121 9 0
{TICK}
**Output:**
{TICK}
9121210
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
#    - 비교 기준: a+b vs b+a
# ---------------------------------------------------------
solution_py = """import sys
from functools import cmp_to_key

def cmp(a: str, b: str) -> int:
    # a가 앞에 오는 것이 더 큰 수를 만들면 -1 (내림차순 정렬)
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    nums = list(map(int, input().split()))[:n]

    strs = list(map(str, nums))
    strs.sort(key=cmp_to_key(cmp))

    # all zero 처리
    if strs and strs[0] == "0":
        print("0")
    else:
        print("".join(strs))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
from functools import cmp_to_key

def cmp_internal(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

def solve_internal(nums):
    strs = list(map(str, nums))
    strs.sort(key=cmp_to_key(cmp_internal))
    if strs and strs[0] == "0":
        return "0"
    return "".join(strs)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(95)
test_data = []

# 예시 3개 (문제 예시와 일치)
test_data.append([3, 30, 34, 5, 9])   # 9534330
test_data.append([0, 0, 0])           # 0
test_data.append([12, 121, 9, 0])     # 9121210

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 8)

    if mode == 1:
        nums = [random.randint(0, 1000) for _ in range(n)]
    elif mode == 2:
        nums = [random.randint(0, 10**9) for _ in range(n)]
    elif mode == 3:
        # 0 많이 포함
        nums = [random.choices([0, random.randint(1, 1000)], weights=[60, 40])[0] for _ in range(n)]
    elif mode == 4:
        # 비슷한 접두어 숫자 섞기 (예: 12, 121, 120 등)
        base = str(random.randint(1, 99))
        nums = []
        for _ in range(n):
            t = random.randint(0, 3)
            if t == 0:
                nums.append(int(base))
            elif t == 1:
                nums.append(int(base + str(random.randint(0, 9))))
            elif t == 2:
                nums.append(int(base + str(random.randint(0, 9)) + str(random.randint(0, 9))))
            else:
                nums.append(int(base + "0"))
    elif mode == 5:
        # 한 자리 숫자만
        nums = [random.randint(0, 9) for _ in range(n)]
    elif mode == 6:
        # 같은 숫자 반복
        v = random.randint(0, 10**6)
        nums = [v] * n
    elif mode == 7:
        # 큰 수 + 작은 수 섞기
        nums = [random.choice([random.randint(0, 50), random.randint(10**7, 10**9)]) for _ in range(n)]
    else:
        # 자리수 다양한 숫자
        nums = []
        for _ in range(n):
            length = random.randint(1, 10)
            first = random.randint(0, 9) if length == 1 else random.randint(1, 9)
            s = str(first) + "".join(str(random.randint(0, 9)) for _ in range(length - 1))
            nums.append(int(s))
    test_data.append(nums)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, nums in enumerate(test_data, 1):
    input_str = f"{len(nums)}\n" + " ".join(map(str, nums)) + "\n"
    ans = solve_internal(nums)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P95' 문제 생성이 완료되었습니다.")
