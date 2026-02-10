import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P18 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P18")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 편집증 작가의 원고

## 문제 설명
베스트셀러 작가 **제인**은 원고를 쓸 때 문장을 끊임없이 수정하는 편집증적인 습관이 있습니다. 그녀는 이미 작성된 문장의 중간으로 커서(Cursor)를 이동시켜 글자를 지우거나 새로운 글자를 끼워 넣곤 합니다.

제인이 초기에 작성한 문장이 주어지고, 그 후 $M$개의 명령어가 입력됩니다. 명령어는 다음과 같습니다.

* `L`: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
* `D`: 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤면 무시됨)
* `B`: 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
* `P $`: `$`(문자)를 커서 왼쪽에 추가함

초기 문장이 주어지고, 커서는 문장의 **맨 뒤**에 위치한 상태로 시작합니다. 모든 명령어를 수행한 후 제인의 원고에 남은 최종 문자열을 출력하는 프로그램을 작성하세요.

(참고: 문자열의 길이가 길고 명령어가 많으므로, 시간 복잡도를 고려하여 $O(N)$ 또는 그에 준하는 효율적인 알고리즘을 사용해야 합니다.)

---

## 입력 형식 (Input Format)
* 첫째 줄에 초기에 작성된 문자열이 주어집니다. (길이는 $100,000$을 넘지 않음, 소문자만 포함)
* 둘째 줄에 입력할 명령어의 개수 $M$이 주어집니다. ($1 \\le M \\le 500,000$)
* 셋째 줄부터 $M$개의 줄에 걸쳐 명령어가 주어집니다.

## 출력 형식 (Output Format)
* 모든 명령어를 수행한 후의 최종 문자열을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
abcd
3
P x
L
P y
{TICK}

**Output:**
{TICK}
abcdyx
{TICK}
* 초기: `abcd|` (커서는 맨 뒤)
* `P x`: `abcdx|`
* `L`: `abcd|x`
* `P y`: `abcdy|x`
* 최종 결과: `abcdyx`

### 예시 2
**Input:**
{TICK}
abc
9
L
L
L
L
L
P x
L
B
P y
{TICK}

**Output:**
{TICK}
yxabc
{TICK}
* 커서를 왼쪽으로 계속 옮겨 맨 앞(`|abc`)으로 이동합니다.
* `P x` -> `x|abc`
* `L` -> `|xabc`
* `B` -> 무시됨 (맨 앞이라 삭제 불가)
* `P y` -> `y|xabc`
* 최종 결과: `yxabc`
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    # 빠른 입출력을 위해 sys.stdin 사용
    input = sys.stdin.readline
    
    initial_str = input().strip()
    try:
        m_line = input().strip()
        if not m_line:
            m = 0
        else:
            m = int(m_line)
    except ValueError:
        m = 0
        
    left_stack = list(initial_str)
    right_stack = []
    
    for _ in range(m):
        command = input().split()
        cmd_type = command[0]
        
        if cmd_type == 'L':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif cmd_type == 'D':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif cmd_type == 'B':
            if left_stack:
                left_stack.pop()
        elif cmd_type == 'P':
            left_stack.append(command[1])
            
    # 오른쪽 스택은 역순으로 출력해야 함
    print("".join(left_stack) + "".join(reversed(right_stack)))

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(initial, commands):
    left = list(initial)
    right = []
    for cmd in commands:
        parts = cmd.split()
        c = parts[0]
        if c == 'L':
            if left: right.append(left.pop())
        elif c == 'D':
            if right: left.append(right.pop())
        elif c == 'B':
            if left: left.pop()
        elif c == 'P':
            left.append(parts[1])
    return "".join(left) + "".join(reversed(right))

# 수동 케이스
manual_cases = [
    ("abcd", ["P x", "L", "P y"], "abcdyx"),
    ("abc", ["L", "L", "L", "L", "L", "P x", "L", "B", "P y"], "yxabc"),
    ("editor", ["L", "L", "D", "B", "P z"], "editzr"), # editor -> edit|or -> edi|tor -> edit|or -> edi|or -> ediz|or
    ("", ["P a", "P b", "L", "B"], "a"),
    ("korea", ["D", "D", "L", "B", "B", "P K"], "koKa"),
    ("aaa", ["B", "B", "B", "B"], ""),
    ("xy", ["L", "P z", "L", "P w", "D", "P k"], "wzxyk"),
    ("test", ["P 1", "P 2", "L", "L", "B"], "test1")
]

test_cases = []
for init_s, cmds, out_s in manual_cases:
    # 입력 형식 조립: 초기문자열 \n 개수 \n 명령어들...
    inp_str = f"{init_s}\n{len(cmds)}\n" + "\n".join(cmds)
    test_cases.append((inp_str, out_s))

# 랜덤 케이스 생성
# 명령어 종류
cmd_pool = ['L', 'D', 'B', 'P']
char_pool = "abcdefghijklmnopqrstuvwxyz"

while len(test_cases) < 20:
    init_len = random.randint(10, 500)
    init_s = "".join(random.choice(char_pool) for _ in range(init_len))
    
    m = random.randint(10, 500)
    cmds = []
    
    for _ in range(m):
        c = random.choice(cmd_pool)
        if c == 'P':
            char_to_add = random.choice(char_pool)
            cmds.append(f"P {char_to_add}")
        else:
            cmds.append(c)
            
    out_s = solve_internal(init_s, cmds)
    
    inp_str = f"{init_s}\n{len(cmds)}\n" + "\n".join(cmds)
    
    # 중복 방지 (input string 기준)
    if not any(tc[0] == inp_str for tc in test_cases):
        test_cases.append((inp_str, out_s))

# 파일 저장 (형식: input_01.in / output_01.out)
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P18' 문제 생성이 완료되었습니다.")