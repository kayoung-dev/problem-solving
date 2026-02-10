import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P063 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P063")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 태양광 청소 로봇 써니

## 문제 설명
최첨단 태양광 청소 로봇 '써니'는 $N$개의 쓰레기 더미를 순서대로 치우려 합니다. 각 쓰레기 더미는 크기가 달라서 치우는 데 필요한 배터리 소모량이 다릅니다.

써니는 배터리 효율을 위해 다음과 같은 **충전 순환 시스템**으로 작동합니다.

1. 대기열의 맨 앞에 있는 쓰레기 더미를 확인합니다.
2. **청소 가능:** 현재 배터리 잔량이 쓰레기를 치우는 데 충분하다면($\\ge$), 즉시 청소합니다.
   - 청소 후에는 소모량만큼 배터리가 줄어들고, 쓰레기는 대기열에서 사라집니다.
3. **청소 불가:** 배터리가 부족하다면, 무리해서 청소하지 않고 해당 쓰레기를 **대기열의 맨 뒤**로 보냅니다.
   - 이때, 해당 쓰레기 더미가 다음 순서로 이동하는 동안 '써니'는 햇빛을 받으며 배터리가 $R$만큼 충전됩니다.
4. 모든 쓰레기를 치울 때까지 이 과정을 반복합니다.

쓰레기가 처리되는 순서를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 쓰레기 더미의 개수 $N$, 초기 배터리 $M$, 이동 시 충전량 $R$이 공백으로 구분되어 주어집니다. 
  ($1 \le N \le 100$, $1 \le M, R \le 100$)
- 두 번째 줄에 각 쓰레기 더미를 치우는 데 필요한 배터리 소모량 $C_1, C_2, \dots, C_N$이 공백으로 구분되어 주어집니다. 
  ($1 \le C_i \le 500$)
- 쓰레기 더미의 번호는 입력된 순서대로 1번부터 $N$번까지입니다.

## 출력 형식 (Output Format)
- 쓰레기가 청소되는 순서대로 번호를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 10 5
20 10 30
{TICK}

**Output:**
{TICK}
2 1 3
{TICK}

- 초기 상태
  - 배터리 $10$, 대기열: $[1번: 20, 2번: 10, 3번: 30)]$
- **1번(20) 시도:** 
  - 배터리 $10 < 20$ (부족). 뒤로 이동 및 충전($+5$). 
  - 배터리잔여량 $15$. 대기열: $[2번: 10, 3번: 30, 1번: 20]$
- **2번(10) 시도:** 
  - 배터리 $15 \\ge 10$ (가능). **청소(2번) 완료** 
  - 배터리잔여량 $15-10 = 5$. 대기열: $[3번: 30, 1번: 20)]$
- **3번(30) 시도:** 
  - 배터리 $5 < 30$ (부족). 뒤로 이동 및 충전($+5$). 
  - 배터리잔여량 $5+5 = 10$. 대기열: $[1번: 20, 3번: 30)]$
- **1번(20) 시도:** 
  - 배터리 $10 < 20$ (부족). 뒤로 이동 및 충전($+5$). 
  - 배터리잔여량 $10+5 = 15$. 대기열: $[3번: 30, 1번: 20]$
- **3번(30) 시도:** 
  - 배터리 $15 < 30$ (부족). 뒤로 이동 및 충전($+5$). 
  - 배터리잔여량 $15+5 = 20$. 대기열: $[1번:20, 3번: 30)]$
- **1번(20) 시도:** 
  - 배터리 $20 \\ge 20$ (가능). **청소(1번)** 완료. 
  - 배터리잔여량 $20-20 = 0$. 대기열: $[3번: 30]$
- 이후 배터리를 계속 충전하여 3번 처리.

### 예시 2
**Input:**
{TICK}
4 30 10
10 20 50 40
{TICK}

**Output:**
{TICK}
1 2 4 3
{TICK}

- 초기 배터리 30.
- 1번(10) 청소 $\\rightarrow$ 남은 배터리 20.
- 2번(20) 청소 $\\rightarrow$ 남은 배터리 0.
- 3번(50) 불가 $\\rightarrow$ 뒤로, 충전(+10) $\\rightarrow$ 배터리 10.
- 4번(40) 불가 $\\rightarrow$ 뒤로, 충전(+10) $\\rightarrow$ 배터리 20.
- ...반복하며 충전 후 처리.

### 예시 3
**Input:**
{TICK}
2 5 100
100 200
{TICK}

**Output:**
{TICK}
1 2
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    current_battery = int(input_data[1])
    charge_rate = int(input_data[2])
    
    # (쓰레기 번호, 필요 배터리)
    queue = deque()
    costs = list(map(int, input_data[3:]))
    for i in range(n):
        queue.append((i + 1, costs[i]))
        
    results = []
    
    while queue:
        idx, cost = queue.popleft()
        
        if current_battery >= cost:
            # 청소 가능
            current_battery -= cost
            results.append(str(idx))
        else:
            # 청소 불가: 뒤로 보내고 충전
            current_battery += charge_rate
            queue.append((idx, cost))
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, m, r, costs):
    from collections import deque
    queue = deque()
    for i in range(n):
        queue.append((i + 1, costs[i]))
    
    current_battery = m
    results = []
    
    while queue:
        idx, cost = queue.popleft()
        if current_battery >= cost:
            current_battery -= cost
            results.append(str(idx))
        else:
            current_battery += r
            queue.append((idx, cost))
            
    return " ".join(results)

test_data = []
# 예시 데이터
test_data.append((3, 10, 5, [20, 10, 30]))
test_data.append((4, 30, 10, [10, 20, 50, 40]))
test_data.append((2, 5, 100, [100, 200]))

# 랜덤 데이터 생성
for _ in range(17):
    n = random.randint(5, 20)
    m = random.randint(0, 50)
    r = random.randint(1, 20)
    costs = [random.randint(10, 100) for _ in range(n)]
    test_data.append((n, m, r, costs))

for i, (n, m, r, costs) in enumerate(test_data, 1):
    input_str = f"{n} {m} {r}\n{' '.join(map(str, costs))}"
    ans = solve_internal(n, m, r, costs)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P063' 문제 생성이 완료되었습니다. ")