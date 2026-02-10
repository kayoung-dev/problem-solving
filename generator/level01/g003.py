import os
import random
import collections

# ---------------------------------------------------------
# 1. 경로 설정 (Level/P03 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P003")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "단순한 줄 서기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Queue"]
---

## description
유명한 맛집에 손님들이 줄을 서고 있습니다. 식당은 한 번에 한 명씩만 입장할 수 있습니다.<br />

우리는 손님들에게 '대기 번호(숫자)'를 나눠줍니다.
1. 손님이 도착하면 줄의 맨 뒤에 섭니다. (in)
2. 자리가 나면 줄의 맨 앞에 있는 손님이 들어갑니다. (out)

이 과정은 먼저 온 사람이 먼저 나가는 '선입선출(FIFO)' 구조인 '큐(Queue)' 방식으로 동작합니다.
명령어에 따라 대기열을 관리하고, 식당에 들어가는 손님의 번호를 출력하세요.



## input_description
- 첫 번째 줄에 명령어의 개수 $N$이 주어집니다. ($1 \le N \le 100$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 명령어가 주어집니다.
    - `in [번호]`: 해당 번호를 가진 손님이 줄을 섭니다. ($1 \le 번호 \le 1000$)
    - `out`: 맨 앞의 손님이 식당에 들어갑니다.

## output_description
- `in`: 출력하지 않습니다. (내부적으로 줄만 섭니다)
- `out`: 
    - 식당에 들어가는 손님의 '대기 번호'를 출력합니다.
    - 만약 줄 선 사람이 아무도 없다면 `-1`을 출력합니다.

# samples

### input 1
{TICK}
5
in 101
in 202
out
in 303
out
{TICK}

### output 1
{TICK}
101
202
{TICK}

### input 2
{TICK}
3
out
in 77
out
{TICK}

### output 2
{TICK}
-1
77
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except ValueError:
        return

    # 큐 생성
    queue = deque()

    for _ in range(n):
        command_line = input().split()
        if not command_line: break
        
        cmd = command_line[0]

        if cmd == "in":
            number = int(command_line[1])
            queue.append(number) # 줄 서기
            
        elif cmd == "out":
            if queue:
                # 맨 앞사람 입장 (출력)
                print(queue.popleft())
            else:
                # 줄 선 사람이 없음
                print("-1")

if __name__ == "__main__":
    main()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 테스트 케이스 생성 로직
def solve_internal(commands):
    queue = collections.deque()
    results = []
    
    for line in commands:
        parts = line.split()
        cmd = parts[0]
        
        if cmd == "in":
            num = parts[1]
            queue.append(num)
            
        elif cmd == "out":
            if queue:
                val = queue.popleft()
                results.append(str(val))
            else:
                results.append("-1")
                
    return "\n".join(results)

# 임의의 테스트 케이스 20개 생성
cmd_types = ["in", "out"]

for i in range(1, 21):
    n = random.randint(5, 20)
    commands = []
    
    for _ in range(n):
        # in 비중 60%
        c_type = random.choices(cmd_types, weights=[60, 40], k=1)[0]
        
        if c_type == "in":
            num = random.randint(1, 100)
            commands.append(f"in {num}")
        else:
            commands.append("out")
            
    input_str = f"{n}\n" + "\n".join(commands)
    output_str = solve_internal(commands)
    
    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)
print(f"✅ 'Level01/P003' 생성이 완료되었습니다.")