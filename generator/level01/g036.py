import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P36 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P36")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3
# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 유키의 데이터 2진수 변환기

## 문제 설명
일본의 시스템 엔지니어 **유키**는 센서에서 들어오는 10진수 정수 데이터를 처리하여 네트워크로 전송하는 모듈을 개발하고 있습니다. 데이터를 효율적으로 전송하기 위해서는 10진수 숫자를 2진수 비트 열로 변환해야 합니다.

10진수를 2진수로 변환하는 가장 일반적인 방법은 숫자를 0이 될 때까지 2로 계속 나누어 그 나머지를 기록하는 것입니다. 하지만 이때 계산된 나머지들을 구한 순서대로 나열하면 안 되고, 가장 마지막에 구한 나머지부터 역순으로 읽어야 정확한 2진수 값이 됩니다. 

유키는 이 '역순 출력' 문제를 해결하기 위해 가장 나중에 들어간 데이터가 가장 먼저 나오는 **스택(Stack)** 자료구조를 사용하기로 했습니다. 10진수 숫자가 주어질 때, 스택을 활용하여 2진수로 변환된 비트 열을 출력하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 10진수 정수 $N$이 주어집니다.
* $N$의 범위는 $0 \\le N \\le 10^{{18}}$ 입니다.

## 출력 형식 (Output Format)
* 변환된 2진수 문자열을 한 줄로 출력합니다.
* 입력이 0인 경우 `0`을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
13
{TICK}

**Output:**
{TICK}
1101
{TICK}

* 13을 2로 나누면 몫은 6, 나머지는 **1** (스택: `[1]`)
* 6을 2로 나누면 몫은 3, 나머지는 **0** (스택: `[1, 0]`)
* 3을 2로 나누면 몫은 1, 나머지는 **1** (스택: `[1, 0, 1]`)
* 1을 2로 나누면 몫은 0, 나머지는 **1** (스택: `[1, 0, 1, 1]`)
* 스택에서 차례대로 꺼내면 **1101**이 됩니다.

### 예시 2
**Input:**
{TICK}
255
{TICK}

**Output:**
{TICK}
11111111
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    # 입력을 읽어 정수로 변환
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    n = int(input_data)
    
    # 0인 경우 예외 처리
    if n == 0:
        print("0")
        return
        
    stack = []
    
    # 2로 나누며 나머지를 스택에 저장
    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n //= 2
        
    # 스택에서 하나씩 꺼내어 문자열로 합침 (역순 출력)
    result = ""
    while stack:
        result += str(stack.pop())
        
    print(result)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

def generate_test_cases():
    cases = []
    # 기본 및 경계 케이스
    cases.append(("0", "0"))
    cases.append(("1", "1"))
    cases.append(("2", "10"))
    cases.append(("13", "1101"))
    cases.append(("255", "11111111"))
    cases.append(("1024", "10000000000"))
    
    # 랜덤 대규모 케이스 (64비트 정수 범위 시뮬레이션)
    for i in range(len(cases) + 1, 21):
        # 숫자의 크기를 점진적으로 늘림
        val = random.randint(2**(i*3), 2**(i*3 + 5))
        inp = str(val)
        ans = bin(val)[2:] # 파이썬 내장 함수로 정답 생성
        cases.append((inp, ans))
        
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P36' 문제 생성이 완료되었습니다.")