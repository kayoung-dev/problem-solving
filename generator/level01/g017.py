import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P17 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P17")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 마법의 타자기

## 문제 설명
소설가 **지훈**이는 글을 쓸 때마다 이상한 오타가 발생하는 '마법의 타자기'를 가지고 있습니다. 이 타자기는 문자를 입력하는 도중에 커서(Cursor)가 제멋대로 움직이거나 글자가 지워지곤 합니다.

지훈이가 입력한 키로그(Keylog) 문자열 $S$가 주어졌을 때, 타자기가 모든 명령을 수행한 후 남게 되는 최종 완성된 글을 구하는 프로그램을 작성하세요.

입력된 문자열 $S$에는 알파벳, 숫자뿐만 아니라 다음과 같은 특수 명령어가 포함되어 있습니다.

* `<` : 커서를 왼쪽으로 한 칸 이동합니다. (커서가 맨 앞이면 무시됩니다.)
* `>` : 커서를 오른쪽으로 한 칸 이동합니다. (커서가 맨 뒤면 무시됩니다.)
* `-` : 커서 바로 왼쪽에 있는 문자를 삭제합니다. (커서가 맨 앞이면 무시됩니다.)
* 그 외 문자 : 커서 위치에 해당 문자를 입력합니다.

초기 커서는 문장의 맨 뒤가 아니라, 빈 화면의 **맨 앞**에서 시작한다고 가정하지만, 입력이 들어오는 족족 문자가 써지므로 사실상 입력 도중의 커서 위치를 추적해야 합니다.
또한 문자열 입력시, 커서의 앞쪽에 문자가 입력됩니다. 



---

## 입력 형식 (Input Format)
* 첫 번째 줄에 지훈이가 입력한 키로그 문자열 $S$가 주어집니다.
* 문자열 $S$의 길이는 $1$ 이상 $1,000,000$ 이하입니다.
* 문자열은 알파벳 대소문자, 숫자, 그리고 특수 기호 `<, >, -` 로 구성됩니다.

## 출력 형식 (Output Format)
* 모든 입력을 처리한 후의 최종 문자열을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
abc<d<e>>f-g
{TICK}

**Output:**
{TICK}
aebg
{TICK}

* `abc` 입력: `abc|` (커서는 c 뒤)
* `<`: `ab|c` (커서 왼쪽 이동)
* `d` 입력: `abd|c`
* `<`: `ab|dc`
* `e` 입력: `abe|dc`
* `>>`: `abedc|` (오른쪽 끝으로 이동)
* `f` 입력: `abedcf|`
* `-`: `abedc|` (f 삭제)
* `g` 입력: `abedcg|`

### 예시 2
**Input:**
{TICK}
<<a<b
{TICK}

**Output:**
{TICK}
ba
{TICK}

* `<<`: 맨 앞이므로 무시됨.
* `a` 입력: `a|`
* `<`: `|a`
* `b` 입력: `b|a`
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
# 이 문제는 'Two Stacks' 알고리즘을 사용하여 커서 이동을 O(1)로 처리해야 시간 초과가 나지 않습니다.
# insert(0, ...)이나 pop(0)을 쓰면 O(N)이 되어 시간 초과 가능성이 큽니다.

solution_code = """import sys

def solution():
    keylog = sys.stdin.read().strip()
    
    left_stack = []
    right_stack = []
    
    for char in keylog:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
    
    # 왼쪽 스택은 그대로, 오른쪽 스택은 거꾸로 출력해야 함
    print("".join(left_stack) + "".join(reversed(right_stack)))

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(keylog):
    left = []
    right = []
    for char in keylog:
        if char == '<':
            if left:
                right.append(left.pop())
        elif char == '>':
            if right:
                left.append(right.pop())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)
    return "".join(left) + "".join(reversed(right))

# 수동 케이스
manual_cases = [
    ("abc<d<e>>f-g", "abedcg"),
    ("<<a<b", "ba"),
    ("Python-Stack", "PythoStack"),
    ("He<ll>o", "Hello"),
    ("<<<>>>", ""),
    ("-a-b-c", "abc"), # 맨 앞 삭제 무시 후 입력
    ("abc---", ""),
    ("a<b<c<d", "dcba"), # 역순 입력 효과
    ("0123456789<<<<<-----", "01234")
]

test_cases = []
for inp, out in manual_cases:
    test_cases.append((inp, out))

# 랜덤 케이스 생성
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
commands = ["<", ">", "-"]

while len(test_cases) < 20:
    length = random.randint(20, 300)
    # 일반 문자와 명령어를 7:3 비율로 섞음
    inp_list = []
    for _ in range(length):
        if random.random() < 0.3:
            inp_list.append(random.choice(commands))
        else:
            inp_list.append(random.choice(chars))
    
    inp_str = "".join(inp_list)
    out_str = solve_internal(inp_str)
    
    if (inp_str, out_str) not in test_cases:
        test_cases.append((inp_str, out_str))

# 파일 저장 (파일명 형식: input_01.in / output_01.out)
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P17' 문제 생성이 완료되었습니다.")