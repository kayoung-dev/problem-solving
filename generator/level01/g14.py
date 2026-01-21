import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P14 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P14")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 외계 신호 압축 해제

## 문제 설명
우주 탐사선 **나로호**는 먼 외계 행성으로부터 의문의 신호를 수신했습니다. 분석 결과, 이 신호는 저장 공간을 아끼기 위해 특정 규칙으로 압축되어 있었습니다.

압축된 신호의 규칙은 $k[string]$ 형태입니다. 이는 대괄호($[]$) 안에 있는 $string$ 내용을 $k$번 반복한다는 의미입니다. 여기서 $k$는 $1$ 이상의 양의 정수입니다. 이 규칙은 중첩되어 나타날 수도 있습니다.

예를 들어:
* `3[a]2[bc]`는 `aaabcbc`로 복원됩니다.
* `3[a2[c]]`는 `accaccacc`로 복원됩니다.
* `2[abc]3[cd]ef`는 `abcabccdcdef`로 복원됩니다.

수신된 압축 신호 $S$가 주어질 때, 이를 원래의 문장으로 복원하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 압축된 신호 문자열 $S$가 주어집니다.
* 문자열 $S$의 길이는 $1$ 이상 $1,000$ 이하입니다.
* 숫자는 $k$를 의미하며, $1$ 이상 $300$ 이하의 정수입니다.
* 문자열은 알파벳 소문자로만 구성됩니다.
* 모든 입력은 항상 올바른 압축 형식을 따릅니다.

## 출력 형식 (Output Format)
* 압축을 해제한 원래의 문자열을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3[a]2[bc]
{TICK}

**Output:**
{TICK}
aaabcbc
{TICK}
* `a`를 3번 반복하여 `aaa`, `bc`를 2번 반복하여 `bcbc`를 만든 뒤 합칩니다.

### 예시 2
**Input:**
{TICK}
3[a2[c]]
{TICK}

**Output:**
{TICK}
accaccacc
{TICK}
* 안쪽의 `2[c]`가 `cc`가 되고, `a2[c]`는 `acc`가 됩니다. 이를 다시 3번 반복합니다.
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution(s):
    stack = []
    current_str = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char
            
    return current_str

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
    stack = []
    cur_s = ""
    cur_n = 0
    for c in s:
        if c.isdigit():
            cur_n = cur_n * 10 + int(c)
        elif c == '[':
            stack.append((cur_s, cur_n))
            cur_s, cur_n = "", 0
        elif c == ']':
            p_s, n = stack.pop()
            cur_s = p_s + n * cur_s
        else:
            cur_s += c
    return cur_s

manual_cases = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdef"),
    ("abc3[cd]xyz", "abccdcdcdxyz"),
    ("10[a]", "aaaaaaaaaa"),
    ("2[2[abbb]]", "abbbabbbabbbabbb"),
    ("z3[a]2[b]", "zaaabb"),
    ("2[ba]3[a]2[bc]", "bababaaabbcbc")
]

test_cases = manual_cases[:]

# 9~20번: 랜덤 및 중첩 케이스 생성
letters = "abcde"
while len(test_cases) < 20:
    # 중첩 구조 생성
    depth = random.randint(1, 3)
    case_str = ""
    
    def gen_nested(d):
        if d == 0:
            return "".join(random.choice(letters) for _ in range(random.randint(1, 2)))
        num = random.randint(2, 4)
        inner = gen_nested(d-1)
        prefix = "".join(random.choice(letters) for _ in range(random.randint(0, 1)))
        return f"{prefix}{num}[{inner}]"

    inp = gen_nested(depth)
    out = solve_internal(inp)
    
    if len(out) < 2000 and (inp, out) not in test_cases: # 너무 길어지지 않게 조절
        test_cases.append((inp, out))

# 파일 저장 (파일명 형식 수정)
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(str(out))

print(f"✅ 'Level01/P14' 문제 생성이 완료되었습니다.")