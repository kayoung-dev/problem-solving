import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P41)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P041")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 맛집의 줄 서기 알바

## 문제 설명
주인공 **민수**는 요즘 SNS에서 가장 핫한 '데브 버거(Dev Burger)'에서 대기 줄 관리 아르바이트를 시작했습니다. 
이 가게는 **먼저 온 손님이 먼저 들어가는(FIFO)** 원칙을 철저히 지킵니다.

민수는 큐(Queue) 자료구조의 원리를 이용하여 다음 5가지 기능을 수행하는 프로그램을 작성해야 합니다.

1.  **enqueue X**: 손님 이름 `X`가 줄의 맨 뒤에 합류합니다. (Enqueue)
2.  **dequeue**: 가장 앞에 있는 손님이 식당으로 입장합니다. 입장한 손님의 이름을 출력하고 줄에서 제거합니다. 만약 줄이 비어있다면 `-1`을 출력합니다. (Dequeue)
3.  **size**: 현재 줄을 서서 기다리고 있는 손님이 총 몇 명인지 출력합니다.
4.  **empty**: 줄이 비어있으면 `1`, 비어있지 않으면 `0`을 출력합니다.
5.  **front**: 현재 줄의 가장 앞에 있는 손님의 이름을 확인만 합니다. 만약 줄이 비어있다면 `-1`을 출력합니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 처리해야 할 명령의 수 $N$이 주어집니다. ($1 \\le N \\le 10,000$)
* 두 번째 줄부터 $N$개의 줄에 걸쳐 명령이 하나씩 주어집니다.
* 이름 $X$는 영문 소문자이며, 길이는 10자를 넘지 않습니다.

## 출력 형식 (Output Format)
* 출력 명령(`dequeue`, `size`, `empty`, `front`)이 주어질 때마다 결과를 한 줄씩 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
8
enqueue minsu
enqueue chulsu
front
dequeue
size
empty
dequeue
dequeue
{TICK}

**Output:**
{TICK}
minsu
minsu
1
0
chulsu
-1
{TICK}

### 예시 2
**Input:**
{TICK}
7
enqueue alice
empty
dequeue
enqueue bob
size
dequeue
empty
{TICK}

**Output:**
{TICK}
0
alice
1
bob
1
{TICK}

* **enqueue alice**: `alice`가 줄을 섭니다. $\\rightarrow$ `[alice]`
* **empty**: 줄이 안 비었으므로 `0`을 출력합니다.
* **dequeue**: `alice`가 입장합니다. $\\rightarrow$ `alice` 출력 (남은 줄: `[]`)
* **enqueue bob**: `bob`이 줄을 섭니다. $\\rightarrow$ `[bob]`
* **size**: 1명이 줄 서 있으므로 `1`을 출력합니다.
* **dequeue**: `bob`이 입장합니다. $\\rightarrow$ `bob` 출력 (남은 줄: `[]`)
* **empty**: 줄이 비었으므로 `1`을 출력합니다.
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys
from collections import deque

def solution():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    queue = deque()
    results = []

    for i in range(1, n + 1):
        command = input_data[i].split()
        cmd_type = command[0]
        
        if cmd_type == "enqueue":
            queue.append(command[1])
        elif cmd_type == "dequeue":
            if queue:
                results.append(queue.popleft())
            else:
                results.append("-1")
        elif cmd_type == "size":
            results.append(str(len(queue)))
        elif cmd_type == "empty":
            results.append("1" if not queue else "0")
        elif cmd_type == "front":
            if queue:
                results.append(queue[0])
            else:
                results.append("-1")
                
    if results:
        sys.stdout.write("\\n".join(results) + "\\n")

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(commands):
    from collections import deque
    q = deque()
    res = []
    for c in commands:
        parts = c.split()
        cmd = parts[0]
        if cmd == "enqueue":
            q.append(parts[1])
        elif cmd == "dequeue":
            res.append(q.popleft() if q else "-1")
        elif cmd == "size":
            res.append(str(len(q)))
        elif cmd == "empty":
            res.append("1" if not q else "0")
        elif cmd == "front":
            res.append(q[0] if q else "-1")
    return "\\n".join(res)

names = ["minsu", "chulsu", "alice", "bob", "cathy", "dan", "eric", "flora"]

for i in range(1, 11):
    if i == 1:
        cmd_list = ["enqueue minsu", "enqueue chulsu", "front", "dequeue", "size", "empty", "dequeue", "dequeue"]
    elif i == 2:
        cmd_list = ["enqueue alice", "empty", "dequeue", "enqueue bob", "size", "dequeue", "empty"]
    else:
        n = random.randint(20, 40)
        cmd_list = []
        for _ in range(n):
            op = random.choice(["enqueue", "dequeue", "size", "empty", "front"])
            if op == "enqueue":
                cmd_list.append(f"enqueue {random.choice(names)}")
            else:
                cmd_list.append(op)
    
    ans = solve_internal(cmd_list)
    inp = f"{len(cmd_list)}\\n" + "\\n".join(cmd_list)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P041' 문제 생성이 완료되었습니다.")