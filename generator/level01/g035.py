import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P35 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P035")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 한스의 공학용 계산기 엔진

## 문제 설명
독일에서 수학을 공부하는 **한스**는 자신만의 공학용 계산기를 만들고 있습니다. 한스는 사람이 흔히 사용하는 '중위 표기법(Infix notation, 예: $A+B$)' 수식을 컴퓨터가 연산자 우선순위를 고려하여 더 빠르고 정확하게 계산할 수 있는 **'후위 표기법(Postfix notation, 예: $AB+$)'** 으로 변환하는 엔진을 설계하려고 합니다.

후위 표기법은 연산자가 피연산자 뒤에 위치하는 방식으로, 괄호가 필요 없고 컴퓨터의 스택 자료구조를 활용해 계산하기에 매우 효율적인 방식입니다. 한스의 계산기 엔진은 다음과 같은 연산자 우선순위 규칙을 따릅니다:

1.  곱셈(`*`)과 나눗셈(`/`)은 덧셈(`+`)과 뺄셈(`-`)보다 우선순위가 높습니다.
2.  우선순위가 같은 연산자끼리는 먼저 나온 것을 먼저 처리합니다.
3.  피연산자(알파벳 대문자)는 수식에 나타난 순서대로 출력합니다.

한스를 도와 중위 표기법으로 작성된 수식을 후위 표기법으로 변환하는 프로그램을 작성하세요. (단, 이 문제에서는 괄호가 없는 간단한 수식만 다룹니다.)

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 중위 표기법으로 된 수식이 주어집니다.
* 수식은 알파벳 대문자($A-Z$)와 사칙연산 기호(`+`, `-`, `*`, `/`)로만 구성됩니다.
* 수식의 길이는 $1$ 이상 $100$ 이하입니다.

## 출력 형식 (Output Format)
* 변환된 후위 표기법 수식을 한 줄로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
A+B*C
{TICK}

**Output:**
{TICK}
ABC*+
{TICK}

* 곱셈(`*`)이 덧셈(`+`)보다 우선순위가 높으므로 `B*C`가 먼저 묶여 `BC*`가 되고, 이후 `A`와 더해져 `ABC*+`가 됩니다.

### 예시 2
**Input:**
{TICK}
A*B+C/D
{TICK}

**Output:**
{TICK}
AB*CD/+
{TICK}

* `A*B`가 먼저 처리되어 `AB*`가 됩니다.
* `C/D`가 처리되어 `CD/`가 됩니다.
* 마지막으로 두 결과를 더하여 `AB*CD/+`가 됩니다.

---
## 힌트
중위 표기법을 후위 표기법으로 바꿀 때는 **연산자를 담아두는 스택**이 필요합니다. 피연산자는 바로 출력하고, 연산자는 스택에 있는 자신보다 우선순위가 높거나 같은 것들을 모두 꺼내 출력한 뒤에 스택에 들어가야 합니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    expression = sys.stdin.read().strip()
    if not expression:
        return
        
    # 연산자별 우선순위 설정
    precedence = {{'*': 2, '/': 2, '+': 1, '-': 1}}
    stack = []
    result = []
    
    for char in expression:
        # 피연산자(알파벳)는 바로 결과에 추가
        if char.isalpha():
            result.append(char)
        else:
            # 스택에 있는 연산자가 현재 연산자보다 우선순위가 높거나 같다면 pop하여 결과에 추가
            while stack and precedence[stack[-1]] >= precedence[char]:
                result.append(stack.pop())
            # 현재 연산자를 스택에 push
            stack.append(char)
            
    # 스택에 남은 모든 연산자를 결과에 추가
    while stack:
        result.append(stack.pop())
        
    print("".join(result))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

def generate_test_cases():
    cases = []
    # 샘플 및 고정 케이스
    cases.append(("A+B*C", "ABC*+"))
    cases.append(("A*B+C/D", "AB*CD/+"))
    cases.append(("A+B+C", "AB+C+"))
    cases.append(("A*B*C", "AB*C*"))
    cases.append(("A-B+C*D/E", "AB-CD*E/+"))
    
    # 랜덤 케이스 생성
    ops = ['+', '-', '*', '/']
    letters = "ABCDEFGHIJKLMN"
    for i in range(len(cases) + 1, 21):
        length = random.randint(2, 5)
        expr_list = []
        for j in range(length):
            expr_list.append(letters[j])
            if j < length - 1:
                expr_list.append(random.choice(ops))
        
        inp = "".join(expr_list)
        
        # 정답 계산 시뮬레이션
        prec = {'*': 2, '/': 2, '+': 1, '-': 1}
        stk = []
        res = []
        for c in inp:
            if c.isalpha(): res.append(c)
            else:
                while stk and prec[stk[-1]] >= prec[c]:
                    res.append(stk.pop())
                stk.append(c)
        while stk: res.append(stk.pop())
        
        cases.append((inp, "".join(res)))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P035' 문제 생성이 완료되었습니다.")