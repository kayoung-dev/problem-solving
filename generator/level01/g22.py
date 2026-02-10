import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P22 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P22")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 덜렁이 점장의 장부

## 문제 설명
카페 점장 **진수**는 매일 밤 그날의 매출 기록을 장부에 정리합니다. 하지만 진수는 성격이 조금 덜렁대는 탓에 숫자를 잘못 적는 실수를 자주 합니다.

그래서 진수는 장부를 적을 때 한 가지 규칙을 정했습니다.
* 매출액(숫자)을 순서대로 부르며 장부에 적습니다.
* 만약 실수를 했다면 `Z`라고 외칩니다.
* `Z`가 나오면, **바로 직전에 적었던 숫자를 장부에서 지웁니다.** (취소 기능)

진수가 부른 숫자와 `Z`가 공백으로 구분되어 담긴 문자열 `s`가 주어질 때, 모든 기록을 마친 후 장부에 남은 숫자들의 **총합**을 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 숫자와 `Z`가 공백으로 구분된 문자열 $S$가 주어집니다.
* $S$의 길이는 $1$ 이상 $10,000$ 이하입니다.
* 숫자는 정수이며, 음수일 수도 있습니다.
* 문자열의 시작이 `Z`인 경우는 주어지지 않습니다.
* `Z`가 나올 때 지울 숫자가 없는 경우도 주어지지 않습니다.

## 출력 형식 (Output Format)
* 최종적으로 장부에 남은 숫자들의 합을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
10 20 30 Z 40
{TICK}

**Output:**
{TICK}
70
{TICK}
* `10`, `20`을 적고 `30`을 적었으나 바로 `Z`가 나와 `30`은 취소됩니다.
* 남은 숫자는 `10, 20, 40` 이므로 합은 `70`입니다.

### 예시 2
**Input:**
{TICK}
1 2 Z Z 3
{TICK}

**Output:**
{TICK}
3
{TICK}
* `1`, `2`가 모두 `Z`에 의해 지워지고 `3`만 남습니다.
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    # 입력을 공백 기준으로 분리하여 리스트로 만듦
    tokens = sys.stdin.readline().strip().split()
    stack = []
    
    for token in tokens:
        if token == 'Z':
            # Z가 나오면 스택에서 가장 최근 숫자를 제거
            if stack:
                stack.pop()
        else:
            # 숫자가 나오면 스택에 추가 (정수로 변환)
            stack.append(int(token))
            
    # 스택에 남은 숫자들의 합 출력
    print(sum(stack))

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(s):
    tokens = s.split()
    stack = []
    for token in tokens:
        if token == 'Z':
            if stack:
                stack.pop()
        else:
            stack.append(int(token))
    return sum(stack)

# 수동 케이스
manual_cases = [
    ("10 20 30 Z 40", 70),
    ("10 Z 20 Z 1", 1),
    ("1 2 Z Z 3", 3),
    ("-10 20 Z 10", 0), # 음수 테스트 (-10 + 10)
    ("5 Z 10 Z 15 Z", 0), # 모두 지워짐
    ("1 2 3 4 5", 15), # Z 없음
    ("100 200 Z 300 Z Z 50", 50)
]

test_cases = []
for inp, out in manual_cases:
    test_cases.append((inp, str(out)))

# 랜덤 케이스 생성
# 주의: Z는 스택이 비어있지 않을 때만 나와야 올바른 테스트케이스가 됨 (문제 조건상)
for _ in range(13):
    tokens = []
    current_stack_size = 0
    
    # 10~50개의 명령 생성
    num_ops = random.randint(10, 50)
    
    for _ in range(num_ops):
        # 스택이 비어있으면 무조건 숫자 추가
        if current_stack_size == 0:
            val = random.randint(-100, 100)
            tokens.append(str(val))
            current_stack_size += 1
        else:
            # 스택이 있으면 30% 확률로 Z, 70% 확률로 숫자
            if random.random() < 0.3:
                tokens.append("Z")
                current_stack_size -= 1
            else:
                val = random.randint(-100, 100)
                tokens.append(str(val))
                current_stack_size += 1
                
    inp_str = " ".join(tokens)
    ans = solve_internal(inp_str)
    test_cases.append((inp_str, str(ans)))

# 파일 저장 (형식: input_01.in / output_01.out)
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P22' 문제 생성이 완료되었습니다.")