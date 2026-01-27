import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P64 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P64")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = """# 가뭄 든 마을의 물탱크

## 문제 설명
가뭄이 심하게 든 마을에 유일한 생명수인 거대한 물탱크가 있습니다. 이 물탱크는 최대 **$C$ 리터**의 물만 담을 수 있는 용량 제한이 있습니다.

마을 사람들은 물탱크를 다음과 같이 관리합니다.

1. **아침 (유입):** 매일 아침, 비가 오거나 급수 트럭이 와서 $A_i$ 리터의 물을 탱크에 붓습니다.
   - 이때, 물을 부은 후 탱크의 수위가 최대 용량 $C$를 초과하면, 넘치는 물은 모두 버려집니다.
2. **저녁 (소비):** 마을 사람들은 생활용수로 매일 같은 양의 **$K$ 리터**의 물을 사용합니다.
   - 만약 탱크에 남은 물이 $K$ 리터보다 적다면, 있는 물을 모두 다 쓰고 탱크는 텅 비게 됩니다(0 리터).

$N$일 동안 매일 아침 유입되는 물의 양이 주어질 때, **아깝게 버려진(넘친) 물의 총량**을 구하는 프로그램을 작성하세요. 단, 처음 물탱크는 비어있습니다.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 시뮬레이션 기간 $N$, 물탱크의 최대 용량 $C$, 일일 소비량 $K$가 공백으로 구분되어 주어집니다. 
  ($1 \le N \le 1,000$, $1 \le C, K \le 100$)
- 두 번째 줄에 $N$일 동안 매일 아침 유입되는 물의 양 $A_1, A_2, \dots, A_N$이 공백으로 구분되어 주어집니다. 
  ($0 \le A_i \le 200$)

## 출력 형식 (Output Format)
- $N$일 동안 발생한 **넘쳐서 버려진 물**의 총합을 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 10 5
5 10 5
{TICK}

**Output:**
{TICK}
0
{TICK}

- **1일차:** 0에서 시작. 
  - 아침 +5 유입 (현재 5). 
  - 물탱크 용량(10) 이하이므로 넘침 없음. 
  - 저녁 -5 사용 (남은 물 0).
- **2일차:** 0에서 시작. 
  - 아침 +10 유입 (현재 10). 
  - 물탱크 용량(10) 이하이므로 넘침 없음. 
  - 저녁 -5 사용 (남은 물 5).
- **3일차:** 5에서 시작.
  - 아침 +5 유입 (현재 10). 
  - 물탱크 용량(10) 이하이므로 넘침 없음. 
  - 저녁 -5 사용 (남은 물 5).
- 총 물넘침: 0

### 예시 2
**Input:**
{TICK}
3 10 2
12 5 5
{TICK}

**Output:**
{TICK}
8
{TICK}

- **1일차:** 0에서 시작. 
  - 아침 +12 유입 (현재 12). 
  - 물탱크 용량(10) 초과! **2리터 버려짐**. (현재 10). 
  - 저녁 -2 사용(남은 물 8).
- **2일차:** 8에서 시작. 
  - 아침 +5 유입 (현재 13). 
  - 물탱크 용량(10) 초과! **3리터 버려짐**. (현재 10). 
  - 저녁 -2 사용(남은 물 8).
- **3일차:** 8에서 시작. 
  - 아침 +5 유입 (현재 13). 
  - 물탱크 용량(10) 초과! **3리터 버려짐**. (현재 10). 
  - 저녁 -2 사용(남은 물 8).
- 총 물넘침: 2 + 3 + 3 = 8

### 예시 3
**Input:**
{TICK}
5 20 10
5 5 5 5 5
{TICK}

**Output:**
{TICK}
0
{TICK}
"""

problem_md = problem_template.replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    capacity = int(input_data[1])
    usage = int(input_data[2])
    
    inflows = list(map(int, input_data[3:]))
    
    current_water = 0
    total_overflow = 0
    
    for water_in in inflows:
        # 1. 아침 유입
        current_water += water_in
        
        # 2. 오버플로우 체크
        if current_water > capacity:
            overflow = current_water - capacity
            total_overflow += overflow
            current_water = capacity # 물은 가득 찬 상태로 유지
            
        # 3. 저녁 소비
        if current_water >= usage:
            current_water -= usage
        else:
            current_water = 0 # 물이 부족하면 있는 만큼만 다 씀
            
    print(total_overflow)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, c, k, inflows):
    current_water = 0
    total_overflow = 0
    
    for water_in in inflows:
        # 유입
        current_water += water_in
        
        # 오버플로우
        if current_water > c:
            total_overflow += (current_water - c)
            current_water = c
            
        # 소비
        if current_water >= k:
            current_water -= k
        else:
            current_water = 0
            
    return str(total_overflow)

test_data = []
# 예시 데이터
test_data.append((3, 10, 5, [5, 10, 5]))
test_data.append((3, 10, 2, [12, 5, 5]))
test_data.append((5, 20, 10, [5, 5, 5, 5, 5]))

# 랜덤 데이터 생성
for _ in range(17):
    n = random.randint(5, 100)
    c = random.randint(10, 100)
    k = random.randint(1, 50)
    inflows = [random.randint(0, 150) for _ in range(n)]
    test_data.append((n, c, k, inflows))

for i, (n, c, k, inflows) in enumerate(test_data, 1):
    input_str = f"{n} {c} {k}\n{' '.join(map(str, inflows))}"
    ans = solve_internal(n, c, k, inflows)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P64' 문제 생성이 완료되었습니다.")