import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P80 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P80")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 어벤져스 시너지 링크의 최대치

## 문제 설명
어벤져스 멤버들이 일직선상의 전선에 배치되었습니다. 각 히어로는 위치 $x_i$와 개별 전투력 $y_i$를 가지고 있습니다. 토니 스타크는 두 히어로 $i$와 $j$ ($i < j$)가 합동 작전을 펼칠 때의 **'시너지 점수'** 를 다음과 같이 정의했습니다.

$$Synergy = y_i + y_j + (x_j - x_i)$$

단, 무전기 성능 한계로 인해 두 히어로 사이의 거리는 **$K$ 이하**여야만 시너지가 발생합니다.
- $x_j - x_i \le K$

모든 히어로의 위치 정보가 $x$축 오름차순으로 주어질 때, 가능한 시너지 점수의 **최댓값**을 구하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 히어로의 수 $N$과 최대 통신 거리 $K$가 주어집니다. 
- $2 \le N \le 100,000, 1 \le K \le 10^8$
- 두 번째 줄부터 $N$개의 줄에 걸쳐 각 히어로의 위치 $x_i$와 전투력 $y_i$가 주어집니다. 
- $-10^8 \le x_i, y_i \le 10^8$

## 출력 형식 (Output Format)
- 가능한 최대 시너지 점수를 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4 1
1 3
2 0
5 10
6 -10
{TICK}

**Output:**
{TICK}
4
{TICK}

| 단계 | 현재 히어로 ($x, y$) | 큐 상태 (값, 위치) | 작전 결과 및 설명 |
| :--- | :--- | :--- | :--- |
| **1** | (1, 3) | `[(2, 1)]` | 과거 데이터 없음. 자신의 값 $3-1=2$를 큐에 저장. |
| **2** | (2, 0) | `[(2, 1), (-2, 2)]` | 1번과의 거리 $1 \le K$. 시너지: $2 + (0+2) = \mathbf{4}$. |
| **3** | (5, 10) | `[(5, 5)]` | 1, 2번 모두 거리 초과로 제거. 자신의 값 $10-5=5$ 저장. |
| **4** | (6, -10) | `[(5, 5), (-16, 6)]` | 5번과의 거리 $1 \le K$. 시너지: $5 + (-10+6) = 1$. |

### 예시 2
**Input:**
{TICK}
6 3
1 10
2 15
3 5
4 30
6 10
7 40
{TICK}

**Output:**
{TICK}
73
{TICK}

| 단계 | 히어로 ($x, y$) | [정리] 거리 초과 제거 | [계산] 시너지 $(y_i-x_i) + (y_j+x_j)$ | [유지] 큐 상태 $(y-x, x)$ |
| :--- | :--- | :--- | :--- | :--- |
| **1** | (1, 10) | - | - | `[(9, 1)]` |
| **2** | (2, 15) | 없음 | $9 + (15+2) = 26$ | `[(13, 2)]` (13이 9 밀어냄) |
| **3** | (3, 5) | 없음 | $13 + (5+3) = 21$ | `[(13, 2), (2, 3)]` |
| **4** | (4, 30) | 없음 | $13 + (30+4) = 47$ | `[(26, 4)]` (26이 다 밀어냄) |
| **5** | (6, 10) | 없음 | $26 + (10+6) = 42$ | `[(26, 4), (4, 6)]` |
| **6** | (7, 40) | **위치 1, 2, 3 제거** | $26 + (40+7) = \mathbf{73}$ | `[(33, 7)]` |

### 예시 3 
**Input:**
{TICK}
6 3
1 5
2 10
4 30
5 5
8 20
9 60
{TICK}

**Output:**
{TICK}
81
{TICK}

| 단계 | 히어로 ($x, y$) | [정리] 거리 초과 제거 | [계산] 시너지 $(y_i-x_i) + (y_j+x_j)$ | [유지] 큐 상태 $(y-x, x)$ |
| :--- | :--- | :--- | :--- | :--- |
| **1** | (1, 5) | - | - | `[(4, 1)]` |
| **2** | (2, 10) | 없음 | $4 + (10+2) = 16$ | `[(8, 2)]` |
| **3** | (4, 30) | 없음 | $8 + (30+4) = 42$ | `[(26, 4)]` |
| **4** | (5, 5) | 없음 | $26 + (5+5) = 36$ | `[(26, 4), (0, 5)]` |
| **5** | (8, 20) | **위치 4 제거** | $0 + (20+8) = 28$ | `[(12, 8)]` (12가 0 밀어냄) |
| **6** | (9, 60) | 없음 | $12 + (60+9) = \mathbf{81}$ | `[(51, 9)]` |

---
## 힌트 (Note)
우리가 구해야 하는 식을 변형하면 다음과 같습니다:
$$Synergy = (y_i - x_i) + (y_j + x_j)$$

현재 $j$번째 히어로를 확인하고 있다면, $(y_j + x_j)$는 고정된 값입니다. 따라서 전체 시너지를 최대화하려면, 거리 제한($x_j - x_i \le K$) 내에 있는 과거의 $i$들 중 **$(y_i - x_i)$ 값이 가장 큰 히어로**를 찾아 더해주면 됩니다.


"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 1. N, K 읽기
    line = input().split()
    if not line: return
    n, k = int(line[0]), int(line[1])
    
    # dq: (y - x, x) 쌍을 저장하며 y-x 기준 내림차순 유지
    dq = deque()
    max_synergy = -float('inf')
    
    # 2. 히어로 정보 순차 처리
    for _ in range(n):
        xj, yj = map(int, input().split())
        
        # [A] 거리 제한을 벗어난 파트너 제거 (x_j - x_i > k)
        while dq and xj - dq[0][1] > k:
            dq.popleft()
            
        # [B] 최적의 파트너와 시너지 계산
        if dq:
            max_synergy = max(max_synergy, dq[0][0] + yj + xj)
            
        # [C] 자신의 잠재력(y-x)을 큐에 추가 (단조성 유지)
        current_potential = yj - xj
        while dq and current_potential >= dq[-1][0]:
            dq.pop()
        dq.append((current_potential, xj))
        
    # 3. 결과 출력
    print(max_synergy)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직 (20개)
# ---------------------------------------------------------
def solve_internal(n, k, pts):
    dq, ans = deque(), -float('inf')
    for x, y in pts:
        while dq and x - dq[0][1] > k: dq.popleft()
        if dq: ans = max(ans, dq[0][0] + y + x)
        v = y - x
        while dq and v >= dq[-1][0]: dq.pop()
        dq.append((v, x))
    return str(int(ans))

test_data = [
    (4, 1, [[1, 3], [2, 0], [5, 10], [6, -10]]),
    (6, 3, [[1, 10], [2, 15], [3, 5], [4, 30], [6, 10], [7, 40]])
]

for _ in range(18):
    tn = random.randint(100, 500)
    tk = random.randint(50, 100)
    tx = sorted(random.sample(range(-10000, 10000), tn))
    tpts = [[x, random.randint(-5000, 5000)] for x in tx]
    test_data.append((tn, tk, tpts))

for i, (n, k, pts) in enumerate(test_data, 1):
    input_str = f"{n} {k}\n" + "\n".join(f"{p[0]} {p[1]}" for p in pts)
    ans = solve_internal(n, k, pts)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P80' 문제 생성이 완료되었습니다.")