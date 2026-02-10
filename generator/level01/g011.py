import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P11 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P011")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "고대 유적의 비밀 문"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
고고학자 **지수**는 깊은 정글 속에서 거대한 석문을 발견했습니다.<br/>
이 문을 열기 위해서는 문 위에 새겨진 괄호 문양들이 '올바른 규칙'을 따르고 있는지 확인해야 합니다.<br/>
석문에는 오직 소괄호 $($ 와 $)$ 로 구성된 문자열 $S$가 새겨져 있습니다. 지수는 다음의 규칙을 만족할 때만 문이 열린다는 사실을 알아냈습니다.
1. $($ 문자로 시작했다면, 반드시 그에 대응하는 $)$ 문자로 닫혀야 합니다.
2. 모든 괄호는 자신이 열린 순서의 역순으로 닫혀야 하며, 짝이 맞지 않는 괄호가 있어서는 안 됩니다.
3. 빈 문자열은 올바른 규칙을 따른 것으로 간주합니다.
지수를 도와 주어진 문자열 $S$가 올바른 괄호열인지 판별하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 괄호로 구성된 문자열 $S$가 주어집니다.
- 문자열의 길이 $n$의 범위는 $0 \\le n \\le 100,000$ 입니다.
- 문자열은 $($ 와 $)$ 로만 구성됩니다.

## output_description
- 주어진 문자열이 올바른 괄호열이면 `True`를, 그렇지 않으면 `False`를 출력합니다.

# samples

### input 1
{TICK}
(())()
{TICK}

### output 1
{TICK}
True
{TICK}


### input 2
{TICK}
(()(
{TICK}

### output 2
{TICK}
False
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    # 출력할 때도 str()로 변환하여 출력하는 것이 안전함
    print(solution(input_data))
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------

# 내부 로직 검증용 함수
def solve(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False # Bool 반환
            stack.pop()
    return len(stack) == 0 # Bool 반환

# 랜덤 괄호 문자열 생성 함수
def generate_random_case(length, ensure_valid=False):
    if ensure_valid:
        s = ""
        depth = 0
        target_length = length if length % 2 == 0 else length + 1
        while len(s) < target_length:
            if depth > 0 and random.random() > 0.5:
                s += ")"
                depth -= 1
            elif len(s) + depth < target_length:
                s += "("
                depth += 1
            else:
                s += ")"
                depth -= 1
        s += ")" * depth
        return s
    else:
        return "".join(random.choice(['(', ')']) for _ in range(length))

# 1~8번: 수동 엣지 케이스 (값은 Bool 혹은 String 혼용 가능성 있음)
manual_cases = [
    ("(((())))", True),
    ("(())()", True),
    ("(()(", False),
    ("())(", False),
    ("", True),
    ("((", False),
    ("))", False),
    ("()()()()", True)
]

test_cases = manual_cases[:]

# 9~20번: 랜덤 생성
while len(test_cases) < 20:
    length = random.randint(10, 50)
    is_valid_attempt = (len(test_cases) % 2 == 0)
    
    inp = generate_random_case(length, ensure_valid=is_valid_attempt)
    out = solve(inp) # 여기서는 Bool(True/False)이 반환됨
    
    if (inp, out) not in test_cases:
        test_cases.append((inp, out))

# 파일 쓰기
for i, (inp, out) in enumerate(test_cases, 1):
    # .in 파일 저장
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    
    # .out 파일 저장
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(out))

print(f"✅ 'Level01/P011' 문제 생성이 완료되었습니다.")