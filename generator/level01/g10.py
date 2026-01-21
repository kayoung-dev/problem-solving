import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P10 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P10")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 에디터 (Editor)
## 문제 설명
한 줄로 된 간단한 텍스트 에디터를 구현하려고 합니다.
이 에디터에는 커서(cursor)가 존재하며, 커서는 문장의 맨 앞, 문장의 맨 뒤, 또는 문장 중간의 임의의 곳에 위치할 수 있습니다.

초기에 편집기에 입력되어 있는 문자열의 길이가 $N$이라고 할 때, 커서가 위치할 수 있는 곳은 $N+1$가지 경우가 있습니다.
초기 상태에서 커서는 문장의 맨 뒤에 위치합니다.

그 후 $M$개의 명령어가 입력됩니다. 명령어는 다음 4가지입니다.

* `L`: 커서를 왼쪽으로 한 칸 옮깁니다. (커서가 문장의 맨 앞이면 무시됨)
* `D`: 커서를 오른쪽으로 한 칸 옮깁니다. (커서가 문장의 맨 뒤면 무시됨)
* `B`: 커서 왼쪽에 있는 문자를 삭제합니다. (커서가 문장의 맨 앞이면 무시됨)
* `P x`: 문자 $x$를 커서 왼쪽에 추가합니다.

모든 명령어를 수행하고 난 뒤의 최종 문자열을 출력하세요.

### 예시
초기 문자열이 `abcd`이고, 초기 커서는 맨 뒤(`abcd|`)에 있습니다.

1. `P x`: $x$를 커서 왼쪽에 추가합니다. -> `abcdx|`
2. `L`: 커서를 왼쪽으로 이동합니다. -> `abcd|x`
3. `P y`: $y$를 커서 왼쪽에 추가합니다. -> `abcdy|x`

최종 결과: `abcdyx`

[핵심 힌트]
* 문자열의 길이 $N$은 최대 $100,000$, 명령어의 개수 $M$은 최대 $500,000$입니다.
* 일반적인 배열(List)에서 중간에 데이터를 삽입하거나 삭제하는 연산은 $O(N)$의 시간이 걸립니다.
* 이를 $M$번 반복하면 총 시간 복잡도는 $O(N \\times M)$이 되어 시간 초과가 발생합니다.
* 두 개의 스택(Stack)을 사용하여 커서를 기준으로 왼쪽 문자들과 오른쪽 문자들을 나누어 관리하면, 모든 명령을 $O(1)$에 처리할 수 있습니다.
---

## 입력 형식 (Input Format)
* 첫째 줄에 초기에 입력되어 있는 문자열이 주어집니다. (길이 $N$, $1 \\le N \\le 100,000$)
* 둘째 줄에 명령어의 개수 $M$이 주어집니다. ($1 \\le M \\le 500,000$)
* 셋째 줄부터 $M$개의 줄에 걸쳐 입력할 명령어가 순서대로 주어집니다.

## 출력 형식 (Output Format)
* 모든 명령어를 수행한 후의 문자열을 출력합니다.

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
* 처음에 `abc|` 상태에서 `L`을 5번 반복해도 커서는 맨 앞(`|abc`)에 머뭅니다.
* `P x` -> `x|abc`
* `L` -> 맨 앞이므로 무시됨 -> `x|abc`
* `B` -> 커서 왼쪽에 삭제할 문자가 없음 -> `x|abc`
* `P y` -> `yx|abc`
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def solve():
    # 빠른 입출력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline
    
    # 초기 문자열 읽기 (개행문자 제거)
    initial_str = input().strip()
    
    try:
        line = input().strip()
        if not line: return
        m = int(line)
    except ValueError:
        return

    # 두 개의 스택을 사용 (커서 기준 왼쪽 스택, 오른쪽 스택)
    # 예: "abc|de" 상태라면 left=['a','b','c'], right=['e','d'] (오른쪽은 거꾸로 쌓임)
    left_stack = list(initial_str)
    right_stack = []
    
    for _ in range(m):
        command = input().split()
        op = command[0]
        
        if op == 'L':
            # 커서를 왼쪽으로: 왼쪽 스택의 문자를 오른쪽 스택으로 이동
            if left_stack:
                right_stack.append(left_stack.pop())
                
        elif op == 'D':
            # 커서를 오른쪽으로: 오른쪽 스택의 문자를 왼쪽 스택으로 이동
            if right_stack:
                left_stack.append(right_stack.pop())
                
        elif op == 'B':
            # 커서 왼쪽 문자 삭제: 왼쪽 스택에서 pop
            if left_stack:
                left_stack.pop()
                
        elif op == 'P':
            # 커서 왼쪽에 문자 추가: 왼쪽 스택에 push
            char_to_add = command[1]
            left_stack.append(char_to_add)
            
    # 최종 결과 출력
    # right_stack은 스택 구조상 문자열 순서가 반대이므로 뒤집어서 출력
    print("".join(left_stack + right_stack[::-1]))

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

# 내부 정답 로직 (테스트케이스 생성 및 검증용)
def solve_internal(initial, commands):
    left = list(initial)
    right = []
    
    for cmd in commands:
        parts = cmd.split()
        op = parts[0]
        
        if op == 'L':
            if left: right.append(left.pop())
        elif op == 'D':
            if right: left.append(right.pop())
        elif op == 'B':
            if left: left.pop()
        elif op == 'P':
            left.append(parts[1])
            
    return "".join(left + right[::-1])

# 테스트 케이스 20개 생성
# 주의: N과 M이 크므로, 시간 효율을 고려하여 생성
for i in range(1, 21):
    # 난이도 설정
    if i <= 5:
        # 작은 케이스 (디버깅용)
        init_len = random.randint(1, 10)
        m = random.randint(1, 20)
    elif i <= 15:
        # 중간 케이스
        init_len = random.randint(100, 1000)
        m = random.randint(100, 1000)
    else:
        # 큰 케이스 (최대 10만/50만 근접)
        # 생성 시간 단축을 위해 실제 최대치보다는 약간 작게 설정하되 충분히 크게
        init_len = random.randint(10000, 30000)
        m = random.randint(10000, 30000)
        
    # 초기 문자열 생성 (알파벳 소문자)
    chars_pool = "abcdefghijklmnopqrstuvwxyz"
    init_str = "".join(random.choice(chars_pool) for _ in range(init_len))
    
    # 명령어 생성
    commands_list = []
    for _ in range(m):
        dice = random.random()
        # 명령어 확률 조정 (삽입/삭제/이동)
        if dice < 0.25:
            commands_list.append("L")
        elif dice < 0.5:
            commands_list.append("D")
        elif dice < 0.7:
            commands_list.append("B")
        else:
            char = random.choice(chars_pool)
            commands_list.append(f"P {char}")
            
    # 입력 파일 저장
    input_content = f"{init_str}\n{m}\n" + "\n".join(commands_list)
    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_content)
    
    # 출력 파일 저장 (파이썬 내부 로직으로 정답 생성)
    output_content = solve_internal(init_str, commands_list)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_content)

print(f"✅ 'Level01/P10' 문제 생성이 완료되었습니다.")