import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P19 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P019")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "괄호의 값"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
수학자 **오일러**는 고대 유적에서 발견된 기묘한 문자열을 연구하고 있습니다.<br/>
이 문자열은 오직 `(`, `)`, `[`, `]` 네 개의 기호로만 이루어져 있으며, 다음과 같은 규칙에 따라 점수가 매겨진다는 것을 밝혀냈습니다.
1. `()` 형태의 괄호열 값은 $2$입니다.
2. `[]` 형태의 괄호열 값은 $3$입니다.
3. `(X)` 의 값은 $2 \\times$ (X의 값) 입니다. (단, $X$는 올바른 괄호열)
4. `[X]` 의 값은 $3 \\times$ (X의 값) 입니다. (단, $X$는 올바른 괄호열)
5. `XY` 의 값은 (X의 값) $+$ (Y의 값) 입니다. (단, $X$, $Y$는 올바른 괄호열)
6. 올바르지 않은 괄호열이라면 값은 $0$입니다.
예를 들어 `(()[[]])`의 값은 $2 \\times (2 + 3 \\times 3) = 22$가 됩니다. 문자열 $S$가 주어졌을 때, 그 값을 계산하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 괄호로 이루어진 문자열 $S$가 주어집니다.
- 문자열의 길이는 $1$ 이상 $30$ 이하입니다. (결과값이 $2^{{30}}$을 넘지 않도록 제한)

## output_description
- 주어진 괄호열의 값을 정수로 출력합니다. 올바르지 않은 괄호열이라면 $0$을 출력합니다.

# samples

### input 1
{TICK}
(()[[]])
{TICK}

### output 1
{TICK}
22
{TICK}


### input 2
{TICK}
[][]((])
{TICK}

### output 2
{TICK}
0
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    s = sys.stdin.readline().strip()
    stack = []
    temp = 1
    result = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            temp *= 2
        elif s[i] == '[':
            stack.append(s[i])
            temp *= 3
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                print(0)
                return
            if s[i-1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        elif s[i] == ']':
            if not stack or stack[-1] == '(':
                print(0)
                return
            if s[i-1] == '[':
                result += temp
            stack.pop()
            temp //= 3
            
    if stack:
        print(0)
    else:
        print(result)

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(s):
    stack = []
    temp = 1
    result = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            temp *= 2
        elif s[i] == '[':
            stack.append(s[i])
            temp *= 3
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                return 0
            if s[i-1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        elif s[i] == ']':
            if not stack or stack[-1] == '(':
                return 0
            if s[i-1] == '[':
                result += temp
            stack.pop()
            temp //= 3
            
    if stack:
        return 0
    else:
        return result

# 수동 케이스
manual_cases = [
    ("(()[[]])", 22),
    ("[][]((])", 0),
    ("()", 2),
    ("[]", 3),
    ("(())", 4),
    ("[[]]", 9),
    ("([])", 6),
    ("[()]", 6),
    ("(([]))", 12),
    ("([][])", 12)
]

test_cases = []
for inp, out in manual_cases:
    test_cases.append((inp, str(out)))

# 랜덤 케이스 생성 (Valid & Invalid 섞음)
def generate_valid(depth=0):
    if depth > 4: # 너무 깊어지지 않게
        return ""
    
    r = random.random()
    if r < 0.3:
        return ""
    elif r < 0.5:
        return "(" + generate_valid(depth+1) + ")" + generate_valid(depth)
    elif r < 0.7:
        return "[" + generate_valid(depth+1) + "]" + generate_valid(depth)
    elif r < 0.85:
        return "()" + generate_valid(depth)
    else:
        return "[]" + generate_valid(depth)

# 10개 추가 생성
while len(test_cases) < 20:
    if len(test_cases) % 3 == 0:
        # Invalid Case 생성 (괄호 짝 안 맞음)
        length = random.randint(4, 15)
        inp = "".join(random.choice("()[]") for _ in range(length))
        # 우연히 맞을 수도 있으므로 계산
        out = solve_internal(inp)
        # 0이 아닌 경우(우연히 Valid)도 있을 수 있으니 결과대로 저장
    else:
        # Valid Case 생성 시도
        inp = generate_valid()
        if not inp or len(inp) > 30: continue
        out = solve_internal(inp)
    
    # 중복 제거
    if (inp, str(out)) not in test_cases:
        test_cases.append((inp, str(out)))

# 파일 저장 
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P019' 문제 생성이 완료되었습니다.")