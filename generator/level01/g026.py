import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P26 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P026")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "우주선 통제실의 괄호 보안 시스템"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
우주 통제실의 보안 요원 **케이트**는 외계 행성에서 전송된 암호화된 보안 코드를 분석하고 있습니다.<br/>
이 코드는 여러 종류의 괄호들로 구성되어 있으며, 코드가 유효하기 위해서는 모든 괄호가 올바른 순서로 닫혀야 합니다.
보안 코드가 유효하기 위한 조건은 다음과 같습니다.
1. 모든 열린 괄호는 반드시 같은 종류의 닫힌 괄호와 짝을 이뤄야 합니다.
2. 나중에 열린 괄호가 먼저 닫혀야 하는 LIFO(Last In, First Out) 원칙을 준수해야 합니다.
3. 모든 괄호 검사가 끝난 후, 남는 괄호가 없어야 합니다.
사용되는 괄호의 종류는 소괄호 $( )$, 중괄호 ${{}}$, 대괄호 $[ ]$ 총 3종류입니다. 주어진 보안 코드가 유효한지 판별하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 보안 코드 문자열이 주어집니다.
- 문자열의 길이는 $1$ 이상 $10^5$ 이하이며, `(`, `)`, `[`, `]`, `{{`, `}}`로만 구성됩니다.

## output_description
- 보안 코드가 유효하면 `PASS`를, 유효하지 않으면 `FAIL`을 출력합니다.

# samples

### input 1
{TICK}
([]) {{}}
{TICK}

### output 1
{TICK}
PASS
{TICK}


### input 2
{TICK}
([)]
{TICK}

### output 2
{TICK}
FAIL
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    # 문자열만 바로 읽어옴
    code = sys.stdin.read().strip()
    if not code:
        return
    
    stack = []
    bracket_map = {{')': '(', ']': '[', '}}': '{{'}}
    
    for char in code:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                print("FAIL")
                return
            stack.pop()
            
    if not stack:
        print("PASS")
    else:
        print("FAIL")

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def generate_valid_brackets(n):
    stack = []
    res = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    open_chars = ['(', '[', '{']
    while len(res) + len(stack) < n:
        char = random.choice(open_chars)
        stack.append(char)
        res.append(char)
    while stack:
        res.append(pairs[stack.pop()])
    return "".join(res)

def generate_test_cases():
    cases = []
    # 고정 케이스 (튜플로 묶어서 append)
    cases.append(("([]){}", "PASS"))
    cases.append(("([)]", "FAIL"))
    cases.append((")(", "FAIL"))
    cases.append(("{{[()(())]}}", "PASS"))
    
    # 랜덤 대규모 케이스 (총 20개를 채움)
    for i in range(len(cases) + 1, 21):
        length = i * 50 # 문자열 길이 조절
        if i % 2 == 0:
            s = generate_valid_brackets(length)
            cases.append((s, "PASS"))
        else:
            s = list(generate_valid_brackets(length))
            # 임의의 한 문자를 바꿔서 FAIL 유도
            idx = random.randint(0, len(s)-1)
            s[idx] = random.choice(['(', ')', '[', ']', '{', '}'])
            res_str = "".join(s)
            
            # 우연히 PASS가 될 수 있으므로 실제 검증
            ans = "PASS"
            stk = []
            m = {')': '(', ']': '[', '}': '{'}
            for c in res_str:
                if c in m.values(): stk.append(c)
                elif c in m:
                    if not stk or stk[-1] != m[c]: ans = "FAIL"; break
                    stk.pop()
                else: ans = "FAIL"; break
            if stk: ans = "FAIL"
            cases.append((res_str, ans))
    return cases

# ---------------------------------------------------------
# 5. 파일 저장
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    in_file = os.path.join(test_dir, f"{i}.in")
    out_file = os.path.join(test_dir, f"{i}.out")
    
    with open(in_file, "w", encoding="utf-8") as f:
        f.write(inp)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P026' 문제 생성이 완료되었습니다.")