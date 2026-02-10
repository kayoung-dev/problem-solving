import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P067 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P067")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = """# 풍선 터트리기 축제

## 문제 설명
마을 축제에서 가장 인기 있는 게임은 '릴레이 풍선 터트리기'입니다. 
$N$개의 풍선이 원형으로 놓여 있고, 각 풍선 안에는 **다음 이동할 거리($K$)** 가 적힌 쪽지가 들어있습니다.

게임은 다음과 같은 규칙으로 진행됩니다.

1. 풍선에는 1번부터 $N$번까지 번호가 매겨져 있습니다.
2. 제일 처음에는 무조건 **1번 풍선**을 터트립니다.
3. 풍선을 터트리면 쪽지에 적힌 숫자 $K$를 확인합니다.
4. 터진 풍선의 위치를 기준으로, 남은 풍선들 사이에서 시계 방향으로 **$K$번째** 위치에 있는 풍선을 찾아 터트립니다.
5. 모든 풍선이 터질 때까지 이 과정을 반복합니다.

$N$개 풍선 안에 들어있는 쪽지의 숫자가 주어질 때, 풍선이 **터지는 순서**를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 풍선의 개수 $N$이 주어집니다. ($1 \le N \le 1,000$)
- 두 번째 줄에 1번 풍선부터 $N$번 풍선까지 순서대로 쪽지에 적힌 숫자 $K_1, K_2, \dots, K_N$이 공백으로 구분되어 주어집니다. 
  ($1 \le K_i \le 1,000$)

## 출력 형식 (Output Format)
- 풍선이 터지는 순서대로 풍선의 번호를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
2 3 1 4 2
{TICK}

**Output:**
{TICK}
1 3 4 2 5
{TICK}

- **초기 상태** $[(1, 2), (2, 3), (3, 1), (4, 4), (5, 2)]$
- **1번 펑!** (쪽지: $2$) 
  - 남은 `[2, 3, 4, 5]` 중 $2$번째인 **3번**으로 이동.
- **3번 펑!** (쪽지: $1$) 
  - 남은 `[4, 5, 2]` 중 $1$번째인 **4번**으로 이동.
- **4번 펑!** (쪽지: $4$)
  - 남은 `[5, 2]` 중 $4$번째 이동.
  - $5$번 - $2$번 - $5$번 - $2$번. **2번** 도착.
- **2번 펑!** (쪽지: $3$) 
  - 남은 `[5]` 중 $3$번째 이동.
- **5번 펑!**

### 예시 2
**Input:**
{TICK}
4
1 1 1 1
{TICK}

**Output:**
{TICK}
1 2 3 4
{TICK}

- 이동 거리가 모두 $1$이므로 터진 풍선 바로 오른쪽에 있는 풍선이 차례대로 터지게 됩니다.

### 예시 3
**Input:**
{TICK}
3
5 5 5
{TICK}

**Output:**
{TICK}
1 2 3
{TICK}

- **1번 펑!** (쪽지: $5$) 
  - 남은 `[2, 3]` 중 $5$번째 이동.
  - $2$번 - $3$번 - $2$번 - $3$번 - $2$번. **2번** 도착.
- **2번 펑!** (쪽지: $5$) 
  - 남은 `[3]` 중 $5$번째 이동.
  - **3번** 도착.
- **3번 펑!** 종료.
"""

problem_md = problem_template.replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k_values = list(map(int, input_data[1:]))
    
    # (풍선 번호, 쪽지 숫자)를 덱에 저장
    dq = deque()
    for i in range(n):
        dq.append((i + 1, k_values[i]))
        
    results = []
    
    while dq:
        # 1. 현재 풍선을 터트림
        idx, jump = dq.popleft()
        results.append(str(idx))
        
        # 풍선이 더 이상 없으면 종료
        if not dq:
            break
            
        # 2. 다음 풍선을 찾기 위해 회전
        # popleft()로 인해 이미 한 칸이 시계 방향으로 당겨진 상태임
        # 따라서 (jump - 1)번 만큼 시계 방향(왼쪽)으로 회전시키면 
        # 다음 터질 풍선이 맨 앞으로 오게 됨
        dq.rotate(-(jump - 1))
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k_values):
    dq = deque()
    for i in range(n):
        dq.append((i + 1, k_values[i]))
    results = []
    while dq:
        idx, jump = dq.popleft()
        results.append(str(idx))
        if not dq: break
        dq.rotate(-(jump - 1))
    return " ".join(results)

test_data = []

# [예시 케이스]
test_data.append((5, [2, 3, 1, 4, 2])) # 예시 1
test_data.append((4, [1, 1, 1, 1]))    # 예시 2
test_data.append((3, [5, 5, 5]))       # 예시 3

# [랜덤 케이스] 17개
for _ in range(17):
    n = random.randint(5, 100)
    # 쪽지 숫자는 n보다 클 수도 있음 (원형 순환 강조)
    ks = [random.randint(1, 100) for _ in range(n)]
    test_data.append((n, ks))

# 파일 저장
for i, (n, ks) in enumerate(test_data, 1):
    input_str = f"{n}\n{' '.join(map(str, ks))}"
    ans = solve_internal(n, ks)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P067' 문제 생성이 완료되었습니다. ")