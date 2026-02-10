import os

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P46 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P046")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 우주 기지의 보안 코드

## 문제 설명
우주 기지 **'제네시스'** 의 메인 컴퓨터는 보안을 위해 매시간 괄호로 이루어진 특수 문자열 $s$를 생성합니다. 이 기지에 출입하기 위해서는 이 문자열을 왼쪽으로 $x$만큼 회전시켰을 때, 해당 문자열이 **'올바른 괄호 문자열'** 이 되도록 하는 모든 $x$의 개수를 구해야 합니다.

여기서 **'올바른 괄호 문자열'** 의 정의는 다음과 같습니다:
1. `()`, `[]`, `{}` 는 모두 올바른 괄호 문자열입니다.
2. 만약 $A$가 올바른 괄호 문자열이라면, $(A)$, $[A]$, $\{A\}$ 도 올바른 괄호 문자열입니다.
3. 만약 $A, B$가 올바른 괄호 문자열이라면, $AB$ 도 올바른 괄호 문자열입니다.

문자열 $s$를 왼쪽으로 $x$ ($0 \le x < |s|$) 칸만큼 회전시킨다는 것은, 앞의 $x$개의 문자를 순서대로 뒤로 보내는 것을 의미합니다. 보안 전문가인 당신은 기지 방어를 위해 올바른 괄호가 되는 회전 횟수의 총합을 계산하는 프로그램을 작성해야 합니다.

---
## 입력 형식 (Input Format)
* 대괄호 `[` , `]`, 중괄호 `{` , `}`, 소괄호 `(` , `)` 로만 이루어진 문자열 $s$가 주어집니다.
* 문자열 $s$의 길이는 $1$ 이상 $1,000$ 이하입니다.

## 출력 형식 (Output Format)
* $s$를 왼쪽으로 $x$칸만큼 회전시켰을 때, $s$가 올바른 괄호 문자열이 되게 하는 $x$의 개수를 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
[](){}
{TICK}

**Output:**
{TICK}
3
{TICK}

- $x=0$: `[](){}` (올바름)
- $x=2$: `(){}[]` (올바름)
- $x=4$: `{}[]()` (올바름)
따라서 총 3가지를 반환합니다.

### 예시 2
**Input:**
{TICK}
}}}]
{TICK}

**Output:**
{TICK}
0
{TICK}

* 어떤 방향으로 회전하더라도 닫는 괄호 `]`나 `}`가 먼저 나오므로 올바른 문자열을 만들 수 없습니다.

### 예시 3
**Input:**
{TICK}
{}[()]
{TICK}

**Output:**
{TICK}
2
{TICK}

- $x=0$: `{}[()]` (올바름)
- $x=2$: `[()]{}` (올바름)
그 외의 회전은 올바른 규칙에 어긋납니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_content = """import sys
from collections import deque

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return not stack

def solve():
    s = sys.stdin.read().strip()
    if not s: return
    
    n = len(s)
    count = 0
    q = deque(s)
    
    for _ in range(n):
        if is_valid(list(q)):
            count += 1
        q.append(q.popleft())
    print(count)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(s):
    def check(string):
        stk = []
        m = {')': '(', ']': '[', '}': '{'}
        for c in string:
            if c in m.values(): stk.append(c)
            elif stk and stk[-1] == m.get(c): stk.pop()
            else: return False
        return not stk
    cnt = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if check(rotated): cnt += 1
    return str(cnt)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_inputs = [
    "[](){}", "}]()[{", "}}}", "({[]})", "()()()", 
    "[(])", "[]", "}{", "{{}}", "((()))", 
    "()[]{}", "((())", "[[[]]]((()))", "}{}{}{}{", "([]){}[()]",
    "(((((((((())))))))))", "[[[[", "]]]]", "()[{}]()[{}]", "()()()()()()()()()()"
]

for i, s in enumerate(test_inputs, 1):
    ans = solve_internal(s)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(s)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P046' 생성이 완료되었습니다.")