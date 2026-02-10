import os
import random
import sys
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P42)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P042")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 카드 섞기의 달인

## 문제 설명
마술사 **최현우**는 관객들에게 신기한 카드 마술을 보여주려고 합니다.
그는 $1$부터 $N$까지의 번호가 적힌 카드 $N$장을 가지고 있습니다.

카드는 $1$번이 가장 위에, $N$번이 가장 아래에 위치하도록 순서대로 쌓여 있습니다.
이제 최현우 마술사는 카드가 **딱 한 장 남을 때까지** 다음 동작을 반복합니다.

1.  가장 위에 있는 카드를 바닥에 버립니다. (제거)
2.  그다음, 가장 위에 있는 카드를 집어서 카드 뭉치의 가장 아래로 옮깁니다. (이동)

$N$이 주어졌을 때, 마지막에 남게 되는 카드의 번호를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫째 줄에 정수 $N$이 주어집니다. ($1 \\le N \\le 500,000$)

## 출력 형식 (Output Format)
* 마지막에 남게 되는 카드의 번호를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
{TICK}

**Output:**
{TICK}
4
{TICK}

* **1단계**: `1` 버림, `2` 뒤로 $\\rightarrow$ `[3, 4, 5, 6, 2]`
* **2단계**: `3` 버림, `4` 뒤로 $\\rightarrow$ `[5, 6, 2, 4]`
* **3단계**: `5` 버림, `6` 뒤로 $\\rightarrow$ `[2, 4, 6]`
* **4단계**: `2` 버림, `4` 뒤로 $\\rightarrow$ `[6, 4]`
* **5단계**: `6` 버림, `4` 뒤로 $\\rightarrow$ `[4]`
* **종료**: 카드가 한 장 남았으므로 마지막 남은 수 **4**를 출력합니다.

### 예시 2
**Input:**
{TICK}
7
{TICK}

**Output:**
{TICK}
6
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys
from collections import deque

def solution():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)

    if n == 1:
        print(1)
        return

    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:
        queue.popleft()            # 1. 맨 위 버리기
        queue.append(queue.popleft()) # 2. 다음 카드를 맨 뒤로
        
    print(queue[0])

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(n):
    if n == 1: return "1"
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    return str(q[0])

test_inputs = []

# 1~5: 기초 및 예제 케이스
test_inputs.append(6)  # 예시 1
test_inputs.append(7)  # 예시 2
test_inputs.append(1)  # 최소값
test_inputs.append(2)  # 최소 짝수
test_inputs.append(4)  # 2의 거듭제곱

# 6~10: 작은 범위의 랜덤 (10~100)
for _ in range(5):
    test_inputs.append(random.randint(10, 100))

# 11~15: 중간 범위의 랜덤 (1,000~10,000)
for _ in range(5):
    test_inputs.append(random.randint(1000, 10000))

# 16~20: 대량 데이터 처리 (100,000~500,000)
for _ in range(4):
    test_inputs.append(random.randint(100000, 499999))
test_inputs.append(500000) # 최대값 경계 케이스

# 파일 저장
for i, n in enumerate(test_inputs, 1):
    ans = solve_internal(n)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(str(n))
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P042' 문제 생성이 완료되었습니다.")