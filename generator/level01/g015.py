import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P15 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P015")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "뒤죽박죽 창고 정리"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
물류 센터장 **철수**는 창고 정리 로봇을 도입했습니다.<br/>
이 로봇은 우리가 흔히 쓰는 $A+B$와 같은 중위 표기식(Infix)을 이해하지 못하고, 연산자가 피연산자 뒤에 오는 후위 표기식(Postfix)으로 명령을 내려야만 작동합니다.<br/>
예를 들어 $A+B*C$는 로봇에게 $ABC*+$로 전달하고, $A*(B+C)$는 $ABC+*$가 됩니다.<br/>
철수를 도와 일반적인 수식을 로봇이 이해할 수 있는 후위 표기식으로 변환하는 프로그램을 작성하세요. 연산자는 $+$, $-$, $*$, $/$ 네 가지만 존재하며, 우선순위는 다음과 같습니다.
1. 괄호 $(, )$ : 가장 높은 우선순위 (괄호 안의 식을 먼저 처리)
2. $*$, $/$ : 중간 우선순위
3. $+$, $-$ : 가장 낮은 우선순위

## input_description
- 첫 번째 줄에 중위 표기식 문자열 $S$가 주어집니다.
- 문자열 $S$의 길이는 $1$ 이상 $1,000$ 이하입니다. 피연산자는 알파벳 대문자($A$~$Z$)로만 주어집니다.
- 수식은 항상 올바른 형태로 주어집니다.

## output_description
- 변환된 후위 표기식을 출력합니다.

# samples

### input 1
{TICK}
A+B*C
{TICK}

### output 1
{TICK}
ABC*+
{TICK}


### input 2
{TICK}
A*(B+C)
{TICK}

### output 2
{TICK}
ABC+*
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def get_priority(op):
    if op == '(' or op == ')': return 0
    if op == '+' or op == '-': return 1
    if op == '*' or op == '/': return 2
    return -1

def solution(s):
    stack = []
    result = ""
    
    for char in s:
        if char.isalpha():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and get_priority(stack[-1]) >= get_priority(char):
                result += stack.pop()
            stack.append(char)
            
    while stack:
        result += stack.pop()
        
    return result

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    print(solution(input_data))
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(s):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    res = []
    for char in s:
        if 'A' <= char <= 'Z':
            res.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            while stack and prec.get(stack[-1], 0) >= prec[char]:
                res.append(stack.pop())
            stack.append(char)
    while stack:
        res.append(stack.pop())
    return "".join(res)

manual_cases = [
    ("A+B*C", "ABC*+"),
    ("A*(B+C)", "ABC+*"),
    ("A+B+C", "AB+C+"),
    ("(A+B)*(C+D)", "AB+CD+*"),
    ("A+B*C-D/E", "ABC*+DE/-"),
    ("A+B*(C-D)/E", "ABCD-*E/+"),
    ("A/B/C", "AB/C/"),
    ("((A+B)*C)-D", "AB+C*D-")
]

test_cases = manual_cases[:]

# 9~20번: 무작위 수식 생성 (간단한 형태)
ops = ['+', '-', '*', '/']
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while len(test_cases) < 20:
    # 랜덤 식 생성 시 올바른 중위 표기식을 보장하기 위해 
    # 간단한 (A op B) op C 형태로 구성
    l1, l2, l3 = random.sample(letters, 3)
    o1, o2 = random.choices(ops, k=2)
    
    mode = random.randint(0, 2)
    if mode == 0:
        inp = f"{l1}{o1}{l2}{o2}{l3}"
    elif mode == 1:
        inp = f"({l1}{o1}{l2}){o2}{l3}"
    else:
        inp = f"{l1}{o1}({l2}{o2}{l3})"
        
    out = solve_internal(inp)
    if (inp, out) not in test_cases:
        test_cases.append((inp, out))

for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(out))

print(f"✅ 'Level01/P015' 문제 생성이 완료되었습니다.")