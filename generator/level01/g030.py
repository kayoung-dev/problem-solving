import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P30 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P030")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "데이터 센터의 가중치 패킷 버퍼"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack", "Queue"]
---

## description
컴퓨터 아키텍처를 전공하는 **케이트**는 고성능 네트워크 스위치의 패킷 스케줄러를 설계하고 있습니다.<br/>
이 시스템은 도착한 순서대로 패킷을 처리하는 FIFO(First-In, First-Out) 방식을 따르지만, 하드웨어 구조상 두 개의 스택 자료구조만을 사용하여 이를 구현해야 합니다.<br/>
각 패킷은 고유한 가중치(Weight)를 가집니다. 관리자는 패킷이 처리될 때마다 **처리된 패킷의 가중치**와 **현재 버퍼에 남아있는 모든 패킷의 가중치 합**을 실시간으로 보고받길 원합니다.<br/>
다음 명령어를 처리하는 프로그램을 작성하세요.
1. `IN X`: 가중치가 $X$인 패킷이 버퍼에 들어옵니다.
2. `OUT`: 버퍼에서 가장 오래된 패킷을 꺼내고, (꺼낸 패킷의 가중치) (남은 패킷들의 가중치 총합)을 공백으로 구분하여 출력합니다. 버퍼가 비어있다면 `-1`을 출력합니다.

## input_description
- 첫 번째 줄부터 명령어가 한 줄에 하나씩 주어집니다.
- 명령어의 총 개수는 $1$개 이상 $200,000$개 이하입니다. 가중치 $X$는 $1$ 이상 $10^6$ 이하의 정수입니다.

## output_description
- `OUT` 명령이 주어질 때마다 결과를 출력합니다. 패킷이 있을 경우 `(가중치) (남은 총합)` 형태로, 없을 경우 `-1`을 출력합니다.

# samples

### input 1
{TICK}
IN 10
IN 20
OUT
IN 5
OUT
OUT
{TICK}

### output 1
{TICK}
10 20
20 5
5 0
{TICK}


### input 2
{TICK}
IN 100
OUT
OUT
{TICK}

### output 2
{TICK}
100 0
-1
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    lines = sys.stdin.read().splitlines()
    in_stack = []
    out_stack = []
    total_weight = 0
    
    for line in lines:
        parts = line.split()
        if not parts: continue
        
        if parts[0] == 'IN':
            w = int(parts[1])
            in_stack.append(w)
            total_weight += w
        elif parts[0] == 'OUT':
            if not out_stack:
                while in_stack:
                    out_stack.append(in_stack.pop())
            
            if not out_stack:
                print("-1")
            else:
                popped = out_stack.pop()
                total_weight -= popped
                print(f"{{popped}} {{total_weight}}")

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 및 파일 저장
# ---------------------------------------------------------
def generate_test_cases():
    cases = []
    # 고정 케이스
    cases.append(("IN 10\\nIN 20\\nOUT\\nIN 5\\nOUT\\nOUT", "10 20\\n20 5\\n5 0"))
    cases.append(("IN 100\\nOUT\\nOUT", "100 0\\n-1"))
    
    for i in range(len(cases) + 1, 21):
        num_cmds = i * 1000
        cmds = []
        ans = []
        q = [] # 정답 검증용 실제 큐
        total = 0
        
        for _ in range(num_cmds):
            if random.random() < 0.6 or not q:
                v = random.randint(1, 1000)
                cmds.append(f"IN {v}")
                q.append(v)
                total += v
            else:
                cmds.append("OUT")
                if not q:
                    ans.append("-1")
                else:
                    p = q.pop(0)
                    total -= p
                    ans.append(f"{p} {total}")
                    
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
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(real_inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(real_out)

print(f"✅ 'Level01/P030' 문제 생성이 완료되었습니다.")