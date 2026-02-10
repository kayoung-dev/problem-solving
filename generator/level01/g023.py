import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P23 폴더 생성) 
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P23")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 접시 닦기 아르바이트

## 문제 설명
주방 보조 민수는 설거지를 하여 접시를 찬장에 정리해야 합니다.

민수 앞에는 더러운 접시가 쌓인 '설거지 통'이 있고, 씻은 접시를 잠시 두는 '식기 건조대', 그리고 최종적으로 접시를 정리하는 '찬장'이 있습니다.

민수는 다음 순서로만 접시를 옮길 수 있습니다.
1. [설거지 통]에서 접시를 하나 꺼내 씻어서 [식기 건조대]에 쌓습니다. (Push)
2. [식기 건조대]의 맨 위에 있는 접시를 꺼내 [찬장]에 옮깁니다. (Pop)

**중요한 점은 '식기 건조대'가 좁고 깊은 모양이라, 가장 나중에 넣은(맨 위의) 접시만 꺼낼 수 있다는 것입니다.**

민수는 '설거지 통'에 있는 접시들을 하나씩 꺼내서 씻어야 합니다. 씻은 접시는 바로 찬장에 넣을 수도 있고, 건조대에 잠시 쌓아뒀다가 나중에 찬장에 넣을 수도 있습니다.

'설거지 통'에 쌓인 접시의 순서(입력)와, 주방장님이 원하는 '찬장'의 접시 정리 순서(목표)가 주어질 때, 이 순서를 만들 수 있는지 확인하고 그 과정을 출력하세요.
(단, 모든 접시는 고유한 알파벳 소문자로 구분됩니다.)

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 '세척 전 접시 순서'를 나타내는 문자열 S1이 주어집니다.
* 두 번째 줄에 '목표 완성 순서'를 나타내는 문자열 S2가 주어집니다.
* S1과 S2는 서로 구성하는 문자가 같고 순서만 다른(혹은 같은) 문자열이며, 길이는 1 이상 26 이하입니다. 각 문자는 중복되지 않습니다.

## 출력 형식 (Output Format)
* 목표 순서를 만들 수 있다면, 수행해야 하는 동작을 순서대로 출력합니다.
    * 세척(Push)은 `0`, 건조(Pop)는 `1`로 표기하며, 공백 없이 이어서 출력합니다.
* 만약 목표 순서를 만드는 것이 불가능하다면 `impossible`을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
abc
cba
{TICK}

**Output:**
{TICK}
000111
{TICK}
* `a` 세척(0), `b` 세척(0), `c` 세척(0) -> 건조대:[a, b, c]
* `c` 건조(1) -> 건조대:[a, b]
* `b` 건조(1) -> 건조대:[a]
* `a` 건조(1) -> 건조대:[]
* 결과: `000111`

### 예시 2
**Input:**
{TICK}
abcde
bdcae
{TICK}

**Output:**
{TICK}
0010011101
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    # 문자열 읽기
    try:
        source = sys.stdin.readline().strip()
        target = sys.stdin.readline().strip()
    except:
        return

    if not source or not target:
        return

    stack = []
    result = []
    
    source_idx = 0
    target_idx = 0
    n = len(source)
    
    # target 문자열을 하나씩 완성해 나감
    while target_idx < n:
        target_char = target[target_idx]
        
        # 1. 스택의 Top이 찾는 문자와 같다면 -> Pop (건조)
        if stack and stack[-1] == target_char:
            stack.pop()
            result.append('1')
            target_idx += 1
        
        # 2. 스택의 Top이 다르다면 -> 찾는 문자가 나올 때까지 Push (세척)
        elif source_idx < n:
            stack.append(source[source_idx])
            result.append('0')
            source_idx += 1
            
        # 3. 더 이상 Push할 것도 없고, 스택 Top도 다르다면 -> 불가능
        else:
            print("impossible")
            return
            
    print("".join(result))

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(source, target):
    stack = []
    result = []
    source_idx = 0
    target_idx = 0
    n = len(source)
    
    while target_idx < n:
        t_char = target[target_idx]
        
        if stack and stack[-1] == t_char:
            stack.pop()
            result.append('1')
            target_idx += 1
        elif source_idx < n:
            stack.append(source[source_idx])
            result.append('0')
            source_idx += 1
        else:
            return "impossible"
    return "".join(result)

# 수동 케이스
manual_cases = [
    ("abc", "abc", "010101"),
    ("abc", "cba", "000111"),
    ("abc", "cab", "impossible"),
    ("abcdef", "fedcba", "000000111111"), # 전체 역순
    ("algorithm", "algorithm", "01"*9),  # 전체 정순
    ("z", "z", "01"),
    ("xy", "yx", "0011"),
    ("xy", "xy", "0101")
]

test_cases = []
for src, tgt, ans in manual_cases:
    inp_str = f"{src}\n{tgt}"
    test_cases.append((inp_str, ans))

# 랜덤 케이스 생성
char_pool = "abcdefghijklmnopqrstuvwxyz"

while len(test_cases) < 20:
    length = random.randint(3, 15)
    
    # 중복 없는 문자열 생성
    chosen_chars = random.sample(char_pool, length)
    source_str = "".join(chosen_chars)
    
    # 타겟 생성: source를 셔플
    target_list = list(source_str)
    random.shuffle(target_list)
    target_str = "".join(target_list)
    
    # 정답 계산
    ans = solve_internal(source_str, target_str)
    
    inp_str = f"{source_str}\n{target_str}"
    
    # 중복 입력 방지
    if not any(tc[0] == inp_str for tc in test_cases):
        test_cases.append((inp_str, ans))

# 파일 저장
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P23' 문제 생성이 완료되었습니다.")