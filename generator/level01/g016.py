import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P16 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P016")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "무거운 상자 쌓기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
물류 창고에서 일하는 **지수**는 컨베이어 벨트를 통해 들어오는 상자들을 차곡차곡 쌓으려고 합니다.<br/>
이 창고의 상자들은 재질이 약해서 특이한 규칙을 가지고 있습니다.<br/>
1. 새로운 상자를 기존에 쌓인 상자 위에 올릴 때, 새로운 상자가 바로 아래 상자보다 더 무겁다면 아래 상자는 찌그러져 제거됩니다.<br/>
2. 상자가 제거되면, 새로운 상자는 그 아래에 있던 상자와 다시 비교합니다.<br/>
3. 새로운 상자보다 무겁거나 같은 상자를 만날 때까지 이 과정이 반복되며, 더 이상 찌그러질 상자가 없거나 자신보다 무거운 상자를 만나면 그 위에 안착합니다.<br/>
컨베이어 벨트를 통해 들어오는 상자들의 무게 순서가 주어질 때, 모든 상자가 지나간 후 최종적으로 쌓여 있는 상자들의 무게를 밑바닥부터 순서대로 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 상자들의 무게를 나타내는 정수들이 공백으로 구분되어 주어집니다.
- 상자의 개수 $n$은 $1 \\le n \\le 100,000$ 입니다. 
- 각 상자의 무게는 $1$ 이상 $1,000,000$ 이하의 자연수입니다.

## output_description
- 최종적으로 남은 상자들의 무게를 밑바닥부터 순서대로 공백으로 구분하여 출력합니다.

# samples

### input 1
{TICK}
5 3 4
{TICK}

### output 1
{TICK}
5 4
{TICK}


### input 2
{TICK}
10 8 6 12 5
{TICK}

### output 2
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

# 파일 저장 
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(out))

print(f"✅ 'Level01/P016' 문제 생성이 완료되었습니다.")