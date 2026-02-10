import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P13 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P13")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 회전하는 우주 정거장

## 문제 설명
우주비행사 **리사**는 우주 정거장에 도킹하기 위해 접근 중입니다. 우주 정거장의 도킹 포트는 $S$라는 문자열로 표현되며, 여기에는 세 종류의 괄호 문양인 $(, ), [, ], {{, }}$ 가 새겨져 있습니다.

이 정거장은 일정한 속도로 회전하고 있어서, 리사는 문자열 $S$를 왼쪽으로 $x$만큼 회전시켰을 때 포트가 '올바른 규칙'을 만족하는지 확인해야 합니다. 문자열을 왼쪽으로 $x$칸 회전시킨다는 것은 첫 번째 문자를 제일 뒤로 보내는 과정을 $x$번 반복하는 것을 의미합니다.

예를 들어, $S = "[](){{}}"$ 일 때:
* $x=0$: $"[](){{}}"$ (올바름)
* $x=1$: $"](){{}}["$ (올바르지 않음)
* $x=2$: $"(){{}}[]"$ (올바름)

리사가 $S$를 $0$칸부터 $n-1$칸($n$은 $S$의 길이)까지 각각 회전시켜 보았을 때, 올바른 괄호 문자열이 되는 $x$의 개수가 총 몇 개인지 계산하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 대괄호, 중괄호, 소괄호로 이루어진 문자열 $S$가 주어집니다.
* $S$의 길이 $n$은 $1 \le n \le 1,000$ 입니다.

## 출력 형식 (Output Format)
* $x$번 회전시켰을 때 올바른 괄호 문자열이 되는 경우의 수를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
[](){{}}
{TICK}

**Output:**
{TICK}
3
{TICK}
* $x=0, x=2, x=4$ 일 때 각각 $"[](){{}}", "(){{}}[]", "{{}}[]()"$ 가 되어 올바른 괄호열이 됩니다. 나머지 회전 위치에서는 닫는 괄호가 먼저 나오는 등 규칙을 위반합니다.

### 예시 2
**Input:**
{TICK}
}}}}}}]
{TICK}

**Output:**
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

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

def solution(s):
    n = len(s)
    count = 0
    if n % 2 != 0: return 0
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
    else:
        print(solution(input_data))
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------

def check_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else: return False
    return len(stack) == 0

def solve(s):
    n = len(s)
    if n % 2 != 0: return 0
    res = 0
    for i in range(n):
        if check_valid(s[i:] + s[:i]):
            res += 1
    return res

manual_cases = [
    ("[](){}", 3),
    ("}}}]", 0),
    ("[)(]", 0),
    ("}}", 0),
    ("({[]})", 1),
    ("()()()", 3),
    ("((()))", 1),
    ("({[ ]})", 1) # 공백은 실제 입력엔 없지만 구조 확인용
]
# 수동 케이스 정제 (공백 제거)
manual_cases = [(c[0].replace(" ", ""), c[1]) for c in manual_cases]

test_cases = manual_cases[:]

# 랜덤 케이스 생성 (괄호 3종 혼합)
chars = "()[]{}"
while len(test_cases) < 20:
    length = random.randint(4, 20)
    if len(test_cases) % 2 == 0:
        # 홀수 길이는 무조건 0이므로 가끔 섞어줌
        length = length if length % 2 == 0 else length + 1
    
    inp = "".join(random.choice(chars) for _ in range(length))
    out = solve(inp)
    
    if (inp, out) not in test_cases:
        test_cases.append((inp, out))

for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(str(out))

print(f"✅ 'Level01/P13' 문제 생성이 완료되었습니다.")