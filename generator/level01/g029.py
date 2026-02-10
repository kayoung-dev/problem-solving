# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P29 폴더 생성)
# ---------------------------------------------------------
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P029")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "로라의 보석함"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
보석 수집가 **로라**는 매일 발견한 보석의 가치를 기록하여 보석함에 차곡차곡 쌓아둡니다.<br/>
나중에 넣은 보석이 항상 가장 위에 놓이게 됩니다.
가끔 보석의 가치를 잘못 기록하거나 상태가 나쁜 보석을 실수로 넣는 경우가 있습니다. 이때 숫자 **0**을 외치면 보석함의 가장 위에 있는(가장 최근에 넣은) 보석 하나를 즉시 꺼내어 버립니다.<br/>
보석을 넣거나 빼는 과정이 모두 끝났을 때, 보석함에 남아있는 보석들의 가치 총합을 구하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 기록한 정수들이 공백으로 구분되어 주어집니다.
- 입력되는 정수의 개수는 $1$개 이상 $10^5$개 이하입니다. 각 보석의 가치는 $1$ 이상 $1,000,000$ 이하의 정수이며, 잘못 넣었음을 의미하는 숫자는 $0$입니다.
- **0**이 입력될 때 보석함이 비어있는 경우는 발생하지 않음이 보장됩니다.

## output_description
- 최종적으로 보석함에 남아있는 모든 보석의 가치 총합을 정수로 출력합니다. 보석함이 비어있다면 $0$을 출력합니다.

# samples

### input 1
{TICK}
3 5 4 0 2 0
{TICK}

### output 1
{TICK}
8
{TICK}


### input 2
{TICK}
10 20 0 0 40
{TICK}

### output 2
{TICK}
40
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    stack = []
    for val in map(int, data):
        if val == 0:
            if stack:
                stack.pop()
        else:
            stack.append(val)
            
    print(sum(stack))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 및 파일 저장
# ---------------------------------------------------------
def generate_test_cases():
    cases = []
    # 고정 케이스
    cases.append(("3 5 4 0 2 0", "8"))
    cases.append(("10 20 0 0 40", "40"))
    cases.append(("1 2 3 4 5 0 0 0 0 0", "0"))
    cases.append(("100 200 300", "600"))
    
    # 랜덤 케이스 (20개까지)
    for i in range(len(cases) + 1, 21):
        length = i * 500
        nums = []
        stack_sim = []
        
        for _ in range(length):
            # 스택이 비어있지 않을 때만 30% 확률로 0 발생
            if stack_sim and random.random() < 0.3:
                nums.append(0)
                stack_sim.pop()
            else:
                val = random.randint(1, 1000)
                nums.append(val)
                stack_sim.append(val)
        
        cases.append((" ".join(map(str, nums)), str(sum(stack_sim))))
    return cases

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P029' 문제 생성이 완료되었습니다.")