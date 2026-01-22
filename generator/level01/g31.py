import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P31 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P31")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
# LaTeX 수식 및 기호 정의
PC_LATEX = r"$PC(Program \,\, Counter)$"
RET_ADDR_LATEX = r"$PC + 1$"
ARROW_LATEX = r"$\rightarrow$"

problem_md = f"""# 시스템 에뮬레이터의 서브루틴 추적

## 문제 설명
컴퓨터 아키텍처를 전공하는 엔지니어 **레이나**는 새로운 명령어 집합 구조(ISA)를 위한 시스템 에뮬레이터를 개발하고 있습니다. 이 에뮬레이터는 프로그램의 제어 흐름을 관리하기 위해 {PC_LATEX}를 사용하며, 현재 실행 중인 명령어의 주소를 추적합니다.

에뮬레이터가 함수를 처리하는 방식은 다음과 같습니다:

1. 초기 {PC_LATEX} 값은 **0**에서 시작합니다.
2. `CALL addr`: 현재 명령어의 다음 주소({RET_ADDR_LATEX})를 시스템 스택에 저장(Push)하고, {PC_LATEX}를 $addr$로 즉시 변경합니다.
3. `RET`: 시스템 스택의 최상단에 저장된 주소를 꺼내(Pop) {PC_LATEX}에 대입합니다. 만약 스택이 비어 있어 복귀할 주소가 없다면 `STACK_ERROR`를 발생시키고 시뮬레이션을 중단합니다.

명령어 시퀀스가 주어질 때, 각 명령어를 수행한 직후의 {PC_LATEX} 값을 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄부터 명령어들이 한 줄에 하나씩 주어집니다.
* 명령어의 총 개수는 $1$개 이상 $100,000$개 이하입니다.
* `CALL addr`에서 $addr$는 $1$ 이상 $10^9$ 이하의 정수입니다.

## 출력 형식 (Output Format)
* 각 명령어를 수행한 직후의 {PC_LATEX} 값을 한 줄에 하나씩 출력합니다.
* `RET` 실행 시 스택이 비어 있다면 `STACK_ERROR`를 출력하고 프로그램을 즉시 종료합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
CALL 1024
CALL 2048
RET
RET
{TICK}

**Output:**
{TICK}
1024
2048
1025
1
{TICK}

* `CALL 1024`: 복귀 주소 **1**을 스택에 저장하고 {PC_LATEX}는 **1024**가 됩니다.
* `CALL 2048`: 복귀 주소 **1025**를 스택에 저장하고 {PC_LATEX}는 **2048**가 됩니다.
* `RET`: 스택에서 **1025**를 꺼내 {PC_LATEX}에 저장합니다.
* `RET`: 스택에서 **1**을 꺼내 {PC_LATEX}에 저장합니다.

### 예시 2
**Input:**
{TICK}
CALL 512
RET
RET
{TICK}

**Output:**
{TICK}
512
1
STACK_ERROR
{TICK}

* 두 번째 `RET` 연산 시 스택이 비어 있으므로 오류 메시지를 출력하고 종료합니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    lines = sys.stdin.read().splitlines()
    pc = 0
    stack = []
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        opcode = parts[0]
        
        if opcode == 'CALL':
            target_addr = int(parts[1])
            # 복귀 주소 (PC + 1) 저장
            stack.append(pc + 1)
            pc = target_addr
            print(pc)
        elif opcode == 'RET':
            if not stack:
                print("STACK_ERROR")
                break
            # 스택에서 주소 복구
            pc = stack.pop()
            print(pc)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def generate_test_cases():
    cases = []
    # 1-3: 기본 및 고정 케이스
    cases.append(("CALL 1024\\nCALL 2048\\nRET\\nRET", "1024\\n2048\\n1025\\n1"))
    cases.append(("CALL 512\\nRET\\nRET", "512\\n1\\nSTACK_ERROR"))
    cases.append(("RET", "STACK_ERROR"))
    
    # 4-20: 랜덤 대규모 케이스
    for i in range(4, 21):
        num_cmds = i * 500
        cmds = []
        ans = []
        pc_sim = 0
        stk_sim = []
        is_error = False
        
        for _ in range(num_cmds):
            if is_error: break
            
            # 스택 상태에 따라 CALL 또는 RET 생성
            if stk_sim and random.random() < 0.4:
                cmds.append("RET")
                pc_sim = stk_sim.pop()
                ans.append(str(pc_sim))
            else:
                if not stk_sim and random.random() < 0.05:
                    cmds.append("RET")
                    ans.append("STACK_ERROR")
                    is_error = True
                else:
                    addr = random.randint(1, 10**6)
                    cmds.append(f"CALL {{addr}}")
                    stk_sim.append(pc_sim + 1)
                    pc_sim = addr
                    ans.append(str(pc_sim))
                    
        cases.append(("\\n".join(cmds), "\\n".join(ans)))
    return cases

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    real_inp = inp.replace("\\\\n", "\\n").replace("\\n", "\n")
    real_out = out.replace("\\\\n", "\\n").replace("\\n", "\n")
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(real_inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(real_out)

print(f"✅ 'Level01/P31' 문제 생성이 완료되었습니다.")