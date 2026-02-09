import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level02/P06 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level02", "P006")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "후위 표기식 계산"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
일반적인 수식은 `2 + 3 * 4`처럼 연산자가 피연산자 사이에 들어가는 **중위 표기식(Infix Notation)**을 사용합니다. <br />
하지만 컴퓨터가 수식을 계산할 때는 연산자가 피연산자 뒤에 오는 **후위 표기식(Postfix Notation)** 이 훨씬 처리하기 쉽습니다. <br />

후위 표기식의 계산 규칙은 다음과 같습니다:
1. 수식을 앞에서부터 읽으면서 숫자를 만나면 **스택(Stack)**에 넣습니다 (`push`).
2. 연산자(`+`, `-`, `*`, `/`)를 만나면 스택에서 두 개의 숫자를 꺼냅니다 (`pop`).
   * 먼저 꺼낸 수가 연산자의 오른쪽 피연산자, 나중에 꺼낸 수가 왼쪽 피연산자가 됩니다.
3. 두 수에 대해 해당 연산을 수행하고, 그 결과를 다시 스택에 넣습니다.
4. 수식이 끝나면 스택에 남은 마지막 숫자가 최종 결과입니다.

문자열 배열 형태의 후위 표기식이 주어졌을 때, 그 계산 결과를 구하는 프로그램을 작성하세요.
(나눗셈은 정수 나눗셈으로, 소수점 이하는 버립니다. 예를 들어 `3 / 2`는 `1`입니다.)

## input_description
* 첫 번째 줄에 연산(토큰)의 개수 $N$이 주어집니다. ($1 \le N \le 100$)
* 두 번째 줄에 후위 표기식이 공백으로 구분되어 주어집니다.
    * 피연산자는 정수이며, 연산자는 `+`, `-`, `*`, `/` 중 하나입니다.
    * 주어지는 식은 항상 유효한 후위 표기식임이 보장됩니다.
    * 0으로 나누는 경우는 없습니다.

## output_description
* 수식의 계산 결과를 정수로 출력합니다.

# samples
### input 1
{TICK}
5
2 3 + 5 *
{TICK}

### output 1
{TICK}
25
{TICK}


### input 2
{TICK}
5
4 13 5 / +
{TICK}

### output 2
{TICK}
6
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 식 입력
    expression = input().split()
    stack = []

    for token in expression:
        if token not in ["+", "-", "*", "/"]:
            # 숫자일 경우 push
            stack.append(int(token))
        else:
            # 연산자일 경우 pop 2번
            val2 = stack.pop()
            val1 = stack.pop()
            
            if token == '+':
                res = val1 + val2
            elif token == '-':
                res = val1 - val2
            elif token == '*':
                res = val1 * val2
            elif token == '/':
                # C/Java 스타일의 정수 나눗셈 (0을 향해 버림)
                # Python의 //는 내림(floor)이므로 음수 계산시 차이가 있음
                # 문제 의도에 맞게 int(val1 / val2) 사용
                res = int(val1 / val2)
                
            stack.append(res)
            
    # 최종 결과 출력
    print(stack[0])

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 내부 정답 로직 (테스트케이스 생성용)
def solve_internal(tokens):
    stack = []
    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+': res = val1 + val2
            elif token == '-': res = val1 - val2
            elif token == '*': res = val1 * val2
            elif token == '/': res = int(val1 / val2)
            stack.append(res)
    return str(stack[0])

# 유효한 RPN 생성기
def generate_rpn(num_count):
    # num_count개의 숫자를 사용하려면 num_count-1 개의 연산자가 필요
    # 생성 규칙:
    # 1. 스택에 숫자가 2개 이상 있어야 연산자를 넣을 수 있음 (안전을 위해)
    # 2. 숫자를 다 쓰면 남은 만큼 연산자를 채워 넣어야 함
    
    nums_to_add = num_count
    ops_to_add = num_count - 1
    
    tokens = []
    current_stack_size = 0
    
    while nums_to_add > 0 or ops_to_add > 0:
        # 선택지: 숫자(N) 또는 연산자(O)
        choices = []
        
        if nums_to_add > 0:
            choices.append("NUM")
        
        # 연산자는 스택에 최소 2개가 있어야 안전하게 연산 가능
        if ops_to_add > 0 and current_stack_size >= 2:
            choices.append("OP")
            
        # 강제 선택 조건
        # 마지막에 연산자가 부족하면 안되므로 적절히 섞어야 하지만
        # 위 조건만으로도 유효한 RPN이 생성됨 (단, 숫자가 너무 몰리면 스택이 깊어짐)
        
        choice = random.choice(choices)
        
        if choice == "NUM":
            # 숫자 추가 (단순화를 위해 1~9, 나눗셈 0 방지 및 크기 조절)
            num = random.randint(1, 10) 
            tokens.append(str(num))
            current_stack_size += 1
            nums_to_add -= 1
        else:
            # 연산자 추가
            op = random.choice(["+", "-", "*", "/"])
            tokens.append(op)
            current_stack_size -= 1 # 2개 꺼내서 1개 넣으므로 -1
            ops_to_add -= 1
            
    return tokens

# 테스트 케이스 20개 생성
for i in range(1, 21):
    while True:
        try:
            # 숫자의 개수 랜덤 (3 ~ 15) -> 전체 토큰은 약 2배
            n_nums = random.randint(3, 15)
            rpn_tokens = generate_rpn(n_nums)
            
            # 0으로 나누기 등의 런타임 에러 확인을 위해 미리 계산
            result = solve_internal(rpn_tokens)
            
            # 결과가 너무 크거나 작으면 다시 생성 (가독성 위함)
            if abs(int(result)) > 100000:
                continue
                
            input_str = f"{len(rpn_tokens)}\n" + " ".join(rpn_tokens)
            output_str = result
            
            save_file(os.path.join(test_dir, f"{i}.in"), input_str)
            save_file(os.path.join(test_dir, f"{i}.out"), output_str)
            break # 성공적으로 생성되면 루프 탈출
        except ZeroDivisionError:
            # 0으로 나누기 발생 시 재생성
            continue

print(f"✅ 'Level02/P006' 생성이 완료되었습니다.")