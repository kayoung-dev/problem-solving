import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P32 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P032")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
O1_LATEX = r"$O(1)$"

problem_md = f"""# 리암의 스마트 등산 가방

## 문제 설명
아일랜드의 열정적인 등산가 **리암**은 험준한 산을 오를 때 가방의 무게 배분을 매우 중요하게 생각합니다. 리암의 배낭은 입구가 하나뿐이라 장비를 넣고 뺄 때 가장 나중에 넣은 물건을 가장 먼저 꺼내야 하는 스택(Stack) 구조로 되어 있습니다. 컴퓨터 아키텍처를 전공하는 케이트는 리암을 위해 가방에 장비를 넣거나(`PUSH`) 뺄 때(`POP`)마다, 현재 가방 안에 들어있는 모든 장비 중 **가장 가벼운 장비의 무게**가 얼마인지(`MIN`) 실시간으로 확인하는 시스템을 설계하고자 합니다.

일반적인 스택에서는 최솟값을 찾기 위해 내부를 모두 뒤져봐야 하지만, 이 시스템은 가방에 장비가 아무리 많아도 단 한 번에 최솟값을 찾아내는 **{O1_LATEX}** 성능을 보장해야 합니다. 이는 실제 시스템에서 특정 자원의 상태를 빠르게 조회하기 위해 별도의 보조 저장 공간을 운영하는 최적화 원리와 같습니다. 장비를 관리하면서 어떤 순간에도 가장 위에 있는 장비 무게(`TOP`)와 전체 중 가장 가벼운 무게(`MIN`)를 즉시 알려주는 스마트 배낭 시스템을 구현해 보세요.



---
## 입력 형식 (Input Format)
* 첫 번째 줄부터 명령어가 한 줄에 하나씩 주어집니다.
* 명령어의 총 개수 $N$은 $1$ 이상 $200,000$ 이하입니다.
* `PUSH X`: 무게가 $X$ ($1 \le X \le 10^9$)인 장비를 추가합니다.
* `POP`: 가장 위에 있는 장비를 제거합니다. (배낭이 비어있으면 무시합니다.)
* `TOP`: 가장 위에 있는 장비의 무게를 출력합니다. (배낭이 비어있으면 **-1**을 출력합니다.)
* `MIN`: 현재 배낭에 들어있는 모든 장비 중 가장 가벼운 무게를 출력합니다. (배낭이 비어있으면 **-1**을 출력합니다.)

## 출력 형식 (Output Format)
* `TOP` 또는 `MIN` 명령이 주어질 때마다 해당 결과값을 한 줄씩 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
PUSH 10
PUSH 5
MIN
PUSH 8
MIN
POP
MIN
{TICK}

**Output:**
{TICK}
5
5
5
{TICK}

### 예시 2
**Input:**
{TICK}
PUSH 100
TOP
MIN
POP
MIN
{TICK}

**Output:**
{TICK}
100
100
-1
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    lines = sys.stdin.read().splitlines()
    
    stack = []      # 실제 데이터를 담는 메인 스택
    min_stack = []  # 각 시점의 최솟값을 관리하는 보조 스택
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        cmd = parts[0]
        
        if cmd == 'PUSH':
            val = int(parts[1])
            stack.append(val)
            # 보조 스택이 비어있거나, 현재 값이 최솟값보다 작거나 같으면 추가
            if not min_stack or val <= min_stack[-1]:
                min_stack.append(val)
        
        elif cmd == 'POP':
            if stack:
                popped = stack.pop()
                # 제거된 값이 현재 최솟값이었다면 보조 스택에서도 제거
                if popped == min_stack[-1]:
                    min_stack.pop()
        
        elif cmd == 'TOP':
            print(stack[-1] if stack else "-1")
        
        elif cmd == 'MIN':
            print(min_stack[-1] if min_stack else "-1")

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
    # 샘플 케이스
    cases.append(("PUSH 10\\nPUSH 5\\nMIN\\nPUSH 8\\nMIN\\nPOP\\nMIN", "5\\n5\\n5"))
    cases.append(("PUSH 100\\nTOP\\nMIN\\nPOP\\nMIN", "100\\n100\\n-1"))
    
    # 랜덤 케이스 생성
    for i in range(len(cases) + 1, 21):
        num_cmds = i * 1000
        cmds = []
        ans = []
        stk_sim = []
        min_stk_sim = []
        
        for _ in range(num_cmds):
            r = random.random()
            if r < 0.4: # PUSH
                val = random.randint(1, 10**6)
                cmds.append(f"PUSH {{val}}")
                stk_sim.append(val)
                if not min_stk_sim or val <= min_stk_sim[-1]:
                    min_stk_sim.append(val)
            elif r < 0.6: # POP
                cmds.append("POP")
                if stk_sim:
                    p = stk_sim.pop()
                    if p == min_stk_sim[-1]:
                        min_stk_sim.pop()
            elif r < 0.8: # MIN
                cmds.append("MIN")
                ans.append(str(min_stk_sim[-1]) if min_stk_sim else "-1")
            else: # TOP
                cmds.append("TOP")
                ans.append(str(stk_sim[-1]) if stk_sim else "-1")
        
        cases.append(("\\n".join(cmds), "\\n".join(ans)))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    real_inp = inp.replace("\\\\n", "\\n").replace("\\n", "\n")
    real_out = out.replace("\\\\n", "\\n").replace("\\n", "\n")
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(real_inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(real_out)

print(f"✅ 'Level01/P032' 문제 생성이 완료되었습니다.")