import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P27 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P27")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 고대 유적의 비밀 수식 해독

## 문제 설명
고고학자 **지후**는 고대 유적의 벽면에서 특이한 계산식을 발견했습니다. 이 계산식은 우리가 흔히 사용하는 중위 표기법($3 + 4$)이 아닌, 연산자가 피연산자 뒤에 붙는 **후위 표기법**(Postfix Notation, 예: $3 \\, 4 \\, +$)으로 작성되어 있습니다.

유적의 보물 상자를 열기 위해서는 이 수식을 정확히 계산해야 합니다. 수식은 정수와 세 가지 사칙연산자($+$, $-$, $*$)로 구성됩니다. 스택을 활용하여 이 고대 수식의 결과값을 계산하는 프로그램을 작성하세요.

**계산 규칙:**
1. 숫자를 만나면 스택에 쌓습니다.
2. 연산자($+$, $-$, $*$)를 만나면 스택에서 숫자 두 개를 꺼냅니다.
3. **먼저 꺼낸 숫자가 오른쪽, 나중에 꺼낸 숫자가 왼쪽**에 오도록 하여 연산합니다. (예: 스택에서 $a$, $b$ 순으로 꺼냈다면 $b - a$ 계산)
4. 연산 결과값을 다시 스택에 넣습니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 후위 표기법으로 작성된 수식이 공백으로 구분되어 주어집니다.
* 수식의 길이는 $3$ 이상 $100$ 이하이며, 계산 결과와 중간 과정의 값은 항상 $-10^9$ 이상 $10^9$ 이하의 정수임이 보장됩니다.

## 출력 형식 (Output Format)
* 수식의 최종 계산 결과를 정수로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 4 + 2 *
{TICK}

**Output:**
{TICK}
14
{TICK}

* `3`과 `4`를 스택에 넣고 `+`를 만나면 $3+4=7$을 계산합니다. 그 후 `2`를 넣고 `*`를 만나면 $7*2=14$가 됩니다.

### 예시 2
**Input:**
{TICK}
10 2 5 * -
{TICK}

**Output:**
{TICK}
0
{TICK}

* `10`, `2`, `5`를 순서대로 스택에 넣습니다. `*`를 만나면 $2*5=10$을 계산하여 스택에 넣습니다. 마지막에 `-`를 만나면 $10-10=0$이 됩니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    stack = []
    
    for token in tokens:
        if token in ('+', '-', '*'):
            # 연산자를 만나면 스택에서 두 개 추출
            op2 = stack.pop()
            op1 = stack.pop()
            
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
        else:
            # 숫자인 경우 정수로 변환하여 스택에 추가
            stack.append(int(token))
            
    print(stack[0])

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 및 파일 저장
# ---------------------------------------------------------
def generate_test_cases():
    cases = []
    # 고정 케이스
    cases.append(("3 4 + 2 *", "14"))
    cases.append(("10 2 5 * -", "0"))
    cases.append(("5 10 15 + *", "125"))
    cases.append(("100 50 - 20 -", "30"))
    
    # 랜덤 케이스 생성을 위한 간단한 로직 (피연산자 3~5개 수준)
    for _ in range(16):
        num_count = random.randint(3, 6)
        nums = [random.randint(1, 20) for _ in range(num_count)]
        
        # 유효한 후위 표기법 생성 (단순화된 형태)
        temp_stack = [nums[0]]
        expr = [str(nums[0])]
        idx = 1
        
        while idx < num_count or len(temp_stack) > 1:
            if idx < num_count and (len(temp_stack) < 2 or random.random() > 0.5):
                expr.append(str(nums[idx]))
                temp_stack.append(nums[idx])
                idx += 1
            else:
                op = random.choice(['+', '-', '*'])
                b = temp_stack.pop()
                a = temp_stack.pop()
                if op == '+': res = a + b
                elif op == '-': res = a - b
                else: res = a * b
                temp_stack.append(res)
                expr.append(op)
        
        cases.append((" ".join(expr), str(temp_stack[0])))
    return cases

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P27' 문제 생성이 완료되었습니다.")