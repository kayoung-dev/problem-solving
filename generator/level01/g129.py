import os
import random
import itertools

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P129 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P129")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 최적의 작업 스케줄링

## 문제 설명
컴퓨터 시스템 엔지니어인 준영이는 서버에 들어온 $N$개의 작업을 처리해야 합니다. 서버는 한 번에 하나의 작업만 처리할 수 있으며, 각 작업이 완료될 때까지 걸리는 시간은 서로 다릅니다.

각 작업의 **대기 시간**은 해당 작업을 처리하기 위해 기다린 시간과 그 작업을 처리하는 데 걸린 시간을 합친 값입니다. 예를 들어, 처리 시간이 각각 $3$분, $1$분, $2$분인 세 작업을 `[3, 1, 2]` 순서대로 처리한다면:
- 첫 번째 작업: $3$분 만에 완료 (대기 시간 3분)
- 두 번째 작업: $3$분 기다린 후 $1$분 동안 처리하여 $4$분 만에 완료 (대기 시간 4분)
- 세 번째 작업: $4$분 기다린 후 $2$분 동안 처리하여 $6$분 만에 완료 (대기 시간 6분)
따라서 총 대기 시간의 합은 $3 + 4 + 6 = 13$분이 됩니다.

하지만 작업의 순서를 `[1, 2, 3]`으로 바꾼다면:
- 첫 번째 작업: $1$분 만에 완료 (대기 시간 1분)
- 두 번째 작업: $1$분 기다린 후 $2$분 동안 처리하여 $3$분 만에 완료 (대기 시간 3분)
- 세 번째 작업: $3$분 기다린 후 $3$분 동안 처리하여 $6$분 만에 완료 (대기 시간 6분)
총 대기 시간의 합은 $1 + 3 + 6 = 10$분이 되어 더 효율적입니다.

준영이는 가능한 모든 작업 순서를 따져보아 **총 대기 시간의 합이 최소**가 되는 값을 찾으려고 합니다. 작업의 개수 $N$과 각 작업의 처리 시간이 주어질 때, 최소 대기 시간 합계를 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 작업의 개수 $N$이 주어집니다 
- $1 \le N \le 8$
- 두 번째 줄에 각 작업의 처리 시간을 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 처리 시간은 $1$ 이상 $100$ 이하입니다.

## 출력 형식 (Output Format)
- 가능한 모든 작업 순서 중 총 대기 시간 합계의 최솟값을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
3 1 2
{TICK}
**Output:**
{TICK}
10
{TICK}
- 위 문제 설명에서와 같이 `[1, 2, 3]` 순서로 처리할 때 합계가 $10$으로 최소가 됩니다.

### 예시 2
**Input:**
{TICK}
4
5 2 8 1
{TICK}
**Output:**
{TICK}
27
{TICK}

- 4개의 작업을 나열하는 모든 순서는 $4! = 24$가지 입니다.
- 가장 효율적인 순서인 `[1, 2, 5, 8]`인 경우를 계산하면:
   - 1번 작업 완료: $1$분
   - 2번 작업 완료: $1 + 2 = 3$분
   - 3번 작업 완료: $1 + 2 + 5 = 8$분
   - 4번 작업 완료: $1 + 2 + 5 + 8 = 16$분
- 총합: $1 + 3 + 8 + 16 = 28$입니다. 

### 예시 3
**Input:**
{TICK}
2
10 50
{TICK}
**Output:**
{TICK}
70
{TICK}

- 가능한 순서는 `[10, 50]`과 `[50, 10]` 두 가지입니다.
- `[10, 50]`의 합: $10 + (10+50) = 70$
- `[50, 10]`의 합: $50 + (50+10) = 110$
- 최솟값은 70입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    times = list(map(int, input_data[1:]))
    
    min_total_wait = float('inf')
    
    # 모든 가능한 작업 순서(순열)를 생성하여 전수 조사 (O(N! * N))
    for p in permutations(times):
        current_total_wait = 0
        current_time = 0
        # 선택된 순서대로 대기 시간 계산
        for t in p:
            current_time += t
            current_total_wait += current_time
        
        # 최솟값 갱신
        if current_total_wait < min_total_wait:
            min_total_wait = current_total_wait
            
    print(min_total_wait)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(times):
    min_w = float('inf')
    for p in itertools.permutations(times):
        total = 0
        curr = 0
        for t in p:
            curr += t
            total += curr
        if total < min_w:
            min_w = total
    return str(min_w)

for i in range(1, 21):
    # N이 커지면 N!이 급격히 증가하므로 최대 8로 제한
    if i <= 5:
        n = random.randint(1, 4)
    else:
        n = random.randint(5, 8)
        
    times = [random.randint(1, 100) for _ in range(n)]
    
    input_str = f"{n}\n" + " ".join(map(str, times))
    ans = solve_internal(times)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P129' 문제 생성이 완료되었습니다.")