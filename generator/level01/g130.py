import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P130 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P130")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 스마트 에너지 저장 장치 최적 운영

## 문제 설명
스마트 그리드 엔지니어인 지수는 마을의 전력 효율을 높이기 위해 $N$개의 에너지 저장 장치(ESS)를 관리하고 있습니다. 각 장치는 저장할 수 있는 전력의 용량이 서로 다릅니다.

지수는 오늘 마을의 메인 전력망에 연결할 장치들을 선택하려고 합니다. 하지만 안전상의 이유로 연결된 장치들의 **전력 용량 합계가 송전 한계치인 $K$를 초과해서는 안 됩니다.** 지수의 목표는 $N$개의 장치 중 일부(또는 전체, 또는 0개)를 자유롭게 선택하여, **용량의 합계가 $K$ 이하이면서 최대한 $K$에 가까운(합계가 최대가 되는)** 조합을 찾는 것입니다. 각 장치는 한 번씩만 연결 여부를 결정할 수 있습니다. 

송전 한계치 $K$를 넘지 않으면서 선택된 장치들의 전력 용량 합계가 가질 수 있는 최댓값을 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 에너지 저장 장치의 개수 $N$과 송전 한계치 $K$가 공백으로 구분되어 주어집니다 
- $1 \le N \le 15$ 
- $1 \le K \le 1,000,000$
- 두 번째 줄에 각 장치의 전력 용량을 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 용량은 $1$ 이상 $100,000$ 이하입니다.

## 출력 형식 (Output Format)
- 한계치 $K$를 초과하지 않는 범위 내에서 장치 용량 합계의 최댓값을 출력합니다. 
- 어떤 장치도 연결할 수 없는 경우 $0$을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 50
20 25 30
{TICK}
**Output:**
{TICK}
50
{TICK}

- 가능한 조합들을 확인합니다
  - {20}, {25}, {30}, {20,25}=45, {20,30}=50, {25,30}=55 ...
- 합계가 $50$ 이하인 조합 중 가장 큰 값은 $20 + 30 = 50$입니다.

### 예시 2
**Input:**
{TICK}
4 100
15 30 45 60
{TICK}
**Output:**
{TICK}
90
{TICK}

- 총 $2^4 = 16$가지의 모든 선택 경우의 수를 따져봅니다.
- 합계가 $100$ 이하인 경우 중 가장 큰 값을 찾습니다.
   - $15 + 30 + 45 = 90$ (조건 만족)
   - $30 + 60 = 90$ (조건 만족)
   - $45 + 60 = 105$ (한계 초과)
   - $15 + 30 + 60 = 105$ (한계 초과)
- 가능한 최대 합계는 $90$입니다.

### 예시 3
**Input:**
{TICK}
2 10
15 20
{TICK}
**Output:**
{TICK}
0
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k_limit = int(input_data[1])
    capacities = list(map(int, input_data[2:]))
    
    max_sum = 0
    
    # 2^n 가지의 모든 부분집합을 비트마스킹으로 탐색
    for i in range(1 << n):
        current_sum = 0
        for j in range(n):
            # i의 j번째 비트가 1이면 j번째 장치를 선택한 것으로 간주
            if (i & (1 << j)):
                current_sum += capacities[j]
        
        # 합계가 한계치 이하이고 현재 최댓값보다 크면 갱신
        if current_sum <= k_limit:
            if current_sum > max_sum:
                max_sum = current_sum
                
    print(max_sum)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k, caps):
    ans = 0
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if (i & (1 << j)):
                s += caps[j]
        if s <= k and s > ans:
            ans = s
    return str(ans)

for i in range(1, 21):
    n = random.randint(1, 15)
    k = random.randint(100, 500000)
    caps = [random.randint(1, 100000) for _ in range(n)]
    
    input_str = f"{n} {k}\n" + " ".join(map(str, caps))
    ans = solve_internal(n, k, caps)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P130' 문제 생성이 완료되었습니다. ")