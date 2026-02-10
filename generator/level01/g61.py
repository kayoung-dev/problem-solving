import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P61 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P61")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 파티시에 레오의 소금 뿌리기 기계

## 문제 설명
파티시에 레오는 명품 소금빵을 만들기 위해 특수 제작된 소금 뿌리기 기계를 사용합니다. 이 기계는 한 번에 정확히 $S$ 그램의 소금만 뿌릴 수 있도록 설계되어 있습니다.

레오 앞에는 $N$개의 빵 반죽이 일렬로 늘어서 있으며, 각 반죽 $i$ ($1 \le i \le N$)마다 완성에 필요한 소금의 총량 $A_i$가 정해져 있습니다. 기계는 다음과 같은 규칙으로 작동합니다.

1. 대기열의 맨 앞에 있는 반죽을 꺼내 기계에 넣습니다.
2. 기계는 해당 반죽에 $S$ 그램의 소금을 뿌립니다. 
3. 소금을 뿌린 후, 반죽에 누적된 소금의 양이 필요한 총량 $A_i$ 이상이 되면 해당 반죽은 오븐으로 들어가며 대기열에서 제외됩니다.
4. 만약 소금이 더 필요하다면, 해당 반죽은 다시 대기열의 **맨 뒤**로 돌아가 차례를 기다립니다.

반죽들이 오븐에 들어가는(완성되는) 순서를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 반죽의 개수 $N$과 한 번에 뿌리는 소금의 양 $S$가 공백으로 구분되어 주어집니다. ($1 \le N \le 1,000$, $1 \le S \le 100$)
- 두 번째 줄에 각 반죽이 완성되기 위해 필요한 소금의 양 $A_1, A_2, \dots, A_N$이 공백으로 구분되어 주어집니다. ($1 \le A_i \le 1,000$)

## 출력 형식 (Output Format)
- 빵이 완성되어 오븐에 들어가는 순서대로 반죽의 번호(입력 순서대로 1번부터 시작)를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 10
25 10 15
{TICK}

**Output:**
{TICK}
2 3 1
{TICK}

- 1회전
  - 1번 반죽($25$g 필요): $10$g 뿌림. $15$g 남음. 뒤로 이동. <br/>(대기열: $[2, 3, 1]$)
  - 2번 반죽($10$g 필요): $10$g 뿌림. $0$g 남음. **완성(2번)!**  <br/>(대기열: $[3, 1]$)
  - 3번 반죽($15$g 필요): $10$g 뿌림. $5$g 남음. 뒤로 이동.  <br/>(대기열: $[1, 3]$)
- 2회전
  - 1번 반죽($15$g 필요): $10$g 뿌림. $5$g 남음. 뒤로 이동.  <br/>(대기열: $[3, 1]$)
  - 3번 반죽($5$g 필요): $10$g 뿌림. $0$g 남음. **완성(3번)!** <br/>(대기열: $[1]$)
- 3회전
  - 1번 반죽($5$g 필요): $10$g 뿌림. $0$g 남음. **완성(1번)!**

### 예시 2
**Input:**
{TICK}
5 5
10 5 15 2 8
{TICK}

**Output:**
{TICK}
2 4 1 5 3
{TICK}

- 2번($5$g)과 4번($2$g)은 첫 번째 차례에 바로 완성됩니다.
- 1번($10$g)은 두 번째 차례(두 번의 소금 투하)에 완성됩니다.
- 5번($8$g)은 두 번째 차례에 완성됩니다.
- 3번($15$g)은 세 번째 차례에 가장 마지막으로 완성됩니다.

### 예시 3
**Input:**
{TICK}
3 100
10 20 30
{TICK}

**Output:**
{TICK}
1 2 3
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = int(input_data[1])
    a = list(map(int, input_data[2:]))
    
    queue = deque()
    for i in range(n):
        queue.append([i + 1, a[i]]) # [번호, 남은 양]
        
    results = []
    while queue:
        idx, remain = queue.popleft()
        remain -= s
        
        if remain <= 0:
            results.append(str(idx))
        else:
            queue.append([idx, remain])
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, s, a):
    queue = deque()
    for i in range(n):
        queue.append([i + 1, a[i]])
    results = []
    while queue:
        idx, remain = queue.popleft()
        remain -= s
        if remain <= 0:
            results.append(str(idx))
        else:
            queue.append([idx, remain])
    return " ".join(results)

test_data = []

# 기본 예시 데이터
test_data.append((3, 10, [25, 10, 15]))
test_data.append((5, 5, [10, 5, 15, 2, 8]))
test_data.append((3, 100, [10, 20, 30]))

# 추가 랜덤 데이터 생성 (20개를 채우기 위함)
for _ in range(17):
    n = random.randint(5, 50)
    s = random.randint(5, 20)
    a = [random.randint(1, 100) for _ in range(n)]
    test_data.append((n, s, a))

# 파일 저장
for i, (n, s, a) in enumerate(test_data, 1):
    input_str = f"{n} {s}\n{' '.join(map(str, a))}"
    ans = solve_internal(n, s, a)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P61' 문제 생성이 완료되었습니다.")