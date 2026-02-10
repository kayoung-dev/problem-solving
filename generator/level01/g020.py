import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P20 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P20")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 중복된 괄호 찾기

## 문제 설명
AI 프로그래머 **지니**는 사람이 작성한 수식 코드를 분석하여 불필요한 부분을 정리하는 최적화 작업을 수행하고 있습니다.
지니가 발견한 비효율적인 패턴 중 하나는 바로 **'중복된 괄호'** 입니다.

중복된 괄호란, 수식의 연산 순서에 아무런 영향을 주지 않으면서 불필요하게 감싸져 있는 괄호를 의미합니다.
예를 들어:
* `(a+b)` : 중복 없음. (필요한 괄호)
* `((a+b))` : 바깥쪽 괄호는 불필요함 $\\rightarrow$ **중복!**
* `(a+(b+c))` : 중복 없음.
* `((a))` : 바깥쪽 괄호 불필요 $\\rightarrow$ **중복!**

주어진 수식 문자열에 이러한 중복된 괄호 쌍이 존재하는지 판별하는 프로그램을 작성하세요.
(단, 입력되는 수식은 괄호의 짝이 올바르게 맞고 문법적으로 오류가 없는 수식이라고 가정합니다.)

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 공백 없는 수식 문자열 $S$가 주어집니다.
* 문자열의 길이는 $1$ 이상 $100$ 이하입니다.
* 문자열은 알파벳 소문자, 사칙연산 기호(`+`, `-`, `*`, `/`), 그리고 괄호(`(`, `)`)로만 구성됩니다.

## 출력 형식 (Output Format)
* 중복된 괄호가 존재하면 `YES`, 존재하지 않으면 `NO`를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
(a+b)+(c+d)
{TICK}

**Output:**
{TICK}
NO
{TICK}
* 모든 괄호가 연산의 우선순위를 위해 필요합니다.

### 예시 2
**Input:**
{TICK}
(a+(b))
{TICK}

**Output:**
{TICK}
NO
{TICK}
* `(b)`의 괄호는 `b`를 감싸고 있지만, 일반적으로 `(a)`나 `(b)`처럼 단항에 괄호를 치는 것도 수식의 일부로 인정합니다.
*  이 문제에서는 `((...))` 처럼 **이중으로 감싸진 경우**를 주로 찾습니다. 
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    expression = sys.stdin.readline().strip()
    stack = []
    
    for char in expression:
        if char == ')':
            top = stack.pop()
            
            # 괄호 안에 내용물이 없거나, 바로 여는 괄호가 나온 경우
            # 일반적인 수식에서는 연산자나 피연산자가 있어야 함
            # 여기서는 '((...))' 형태를 잡기 위해, 
            # 닫는 괄호를 만났을 때 스택 top이 바로 '('라면 
            # 이는 '()' (빈 괄호) 이거나 '((...))' (내용물이 이미 pop된 상태)를 의미함
            if top == '(':
                print("YES")
                return
            
            # '('를 만날 때까지 계속 pop (내용물 제거)
            while top != '(':
                top = stack.pop()
        else:
            stack.append(char)
            
    print("NO")

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(expression):
    stack = []
    for char in expression:
        if char == ')':
            if not stack: return "NO" # Should not happen based on problem constraints
            top = stack.pop()
            if top == '(':
                return "YES"
            while top != '(':
                if not stack: break
                top = stack.pop()
        else:
            stack.append(char)
    return "NO"

# 수동 케이스
manual_cases = [
    ("((a+b))", "YES"),
    ("(a+b)", "NO"),
    ("((a))", "YES"),
    ("(a)", "NO"), # (a) is usually considered valid grouping, not duplicate like ((a))
    ("(a+(b))", "NO"),
    ("((a+b)+c)", "NO"),
    ("(((a+b)))", "YES"),
    ("a+b", "NO"),
    ("(a+b)*((c+d))", "YES"),
    ("(a+b)*(c+d)", "NO")
]

test_cases = []
for inp, out in manual_cases:
    test_cases.append((inp, out))

# 랜덤 케이스 생성
# 재귀적으로 유효한 수식을 만들고 확률적으로 중복 괄호를 씌움
def generate_expression(depth):
    if depth > 3:
        return random.choice(['a', 'b', 'c', 'x', 'y'])
    
    # 1. 단항
    if random.random() < 0.4:
        expr = generate_expression(depth + 1)
        # 확률적으로 중복 괄호 추가
        if random.random() < 0.3:
            return f"(({expr}))" # 확실한 중복
        elif random.random() < 0.3:
            return f"({expr})"  # 정상 괄호
        else:
            return expr
            
    # 2. 이항 연산
    else:
        left = generate_expression(depth + 1)
        right = generate_expression(depth + 1)
        op = random.choice(['+', '-', '*', '/'])
        expr = f"{left}{op}{right}"
        
        r = random.random()
        if r < 0.2:
            return f"(({expr}))" # 중복
        elif r < 0.6:
            return f"({expr})"  # 정상
        else:
            return expr

while len(test_cases) < 20:
    expr = generate_expression(0)
    # 너무 길거나 짧으면 스킵
    if len(expr) > 50 or len(expr) < 3: continue
    
    ans = solve_internal(expr)
    if (expr, ans) not in test_cases:
        test_cases.append((expr, ans))

# 파일 저장 (형식: input_01.in / output_01.out)
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P20' 문제 생성이 완료되었습니다.")