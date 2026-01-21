import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P16 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P16")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 무거운 상자 쌓기

## 문제 설명
물류 창고에서 일하는 **지수**는 컨베이어 벨트를 통해 들어오는 상자들을 차곡차곡 쌓으려고 합니다. 하지만 이 창고의 상자들은 재질이 약해서 특이한 규칙을 가지고 있습니다.

1. 새로운 상자를 기존에 쌓인 상자 위에 올릴 때, 만약 새로운 상자가 바로 아래에 있는 상자보다 더 무겁다면 아래에 있는 상자는 찌그러져서 제거됩니다.
2. 상자가 찌그러져 제거되면, 새로운 상자는 그 아래에 있던 상자와 다시 비교하게 됩니다.
3. 새로운 상자보다 무겁거나 같은 상자를 만날 때까지 이 과정이 반복되며, 더 이상 찌그러질 상자가 없거나 자신보다 무거운 상자를 만나면 그 위에 안착합니다.



컨베이어 벨트를 통해 들어오는 상자들의 무게 순서가 주어질 때, 모든 상자가 지나간 후 최종적으로 쌓여 있는 상자들의 무게를 밑바닥부터 순서대로 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 상자들의 무게를 나타내는 정수들이 공백으로 구분되어 주어집니다.
* 상자의 개수 $n$은 $1 \le n \le 100,000$ 입니다.
* 각 상자의 무게는 $1$ 이상 $1,000,000$ 이하의 자연수입니다.

## 출력 형식 (Output Format)
* 최종적으로 남은 상자들의 무게를 밑바닥부터 순서대로 공백으로 구분하여 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 3 4
{TICK}

**Output:**
{TICK}
5 4
{TICK}
* 처음에 5가 놓이고, 그 위에 3이 쌓입니다.
* 다음에 오는 4는 3보다 무겁기 때문에 3을 찌그러뜨리고 제거합니다.
* 4는 그 아래에 있는 5보다는 가볍기 때문에 5 위에 안전하게 쌓여 최종적으로 [5, 4]가 남습니다.

### 예시 2
**Input:**
{TICK}
10 8 6 12 5
{TICK}

**Output:**
{TICK}
12 5
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        weights = list(map(int, line))
    except EOFError:
        return

    stack = []
    for w in weights:
        # 새로운 상자(w)가 스택 맨 위 상자보다 무거우면 찌그러뜨림
        while stack and stack[-1] < w:
            stack.pop()
        stack.append(w)
    
    print(*(stack))

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(weights):
    stack = []
    for w in weights:
        while stack and stack[-1] < w:
            stack.pop()
        stack.append(w)
    return " ".join(map(str, stack))

# 수동 케이스
manual_cases = [
    ([5, 3, 4], "5 4"),
    ([10, 8, 6, 12, 5], "12 5"),
    ([1, 2, 3, 4, 5], "5"),
    ([5, 4, 3, 2, 1], "5 4 3 2 1"),
    ([10, 10, 10], "10 10 10"),
    ([20, 10, 15, 5, 8], "20 15 8"),
    ([100], "100"),
    ([50, 60, 40, 30, 70, 10], "70 10")
]

test_cases = []
for inp, out in manual_cases:
    test_cases.append((" ".join(map(str, inp)), out))

# 랜덤 케이스 생성
while len(test_cases) < 20:
    length = random.randint(10, 50)
    nums = [random.randint(1, 100) for _ in range(length)]
    inp_str = " ".join(map(str, nums))
    out_str = solve_internal(nums)
    if (inp_str, out_str) not in test_cases:
        test_cases.append((inp_str, out_str))

# 파일 저장 (형식: input_01.in / output_01.out)
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(str(out))

print(f"✅ 'Level01/P16' 문제 생성이 완료되었습니다.")