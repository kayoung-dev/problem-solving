import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P079 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P079")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 어벤져스 양자 영역의 타임 트래블

## 문제 설명
타노스의 핑거 스냅으로 사라진 생명체들을 되살리기 위해, 어벤져스는 양자 영역을 통해 과거의 특정 시점들을 방문하여 인피니티 스톤의 에너지를 모아야 합니다. 

양자 영역에는 일직선상에 $N$개의 **'시간의 분기점'** 이 나열되어 있습니다. 각 분기점에는 해당 시점에 개입했을 때 얻을 수 있는 **'승리 기여도'** 점수가 부여되어 있습니다. 점수는 빌런을 물리쳐 얻는 양수(+)일 수도 있고, 역사의 개변으로 인해 발생하는 리스크인 음수(-)일 수도 있습니다.

토니 스타크는 슈트의 전력 한계로 인해 다음과 같은 이동 규칙을 설계했습니다.

- **점프 제한** 
    - 현재 $i$번째 분기점에 있다면, 다음으로 방문할 분기점 $j$는 반드시 현재 위치보다 뒤에 있어야 하며, 그 거리는 $K$를 초과할 수 없습니다. 
    - 즉, $1 \le j - i \le K$ 를 만족해야 합니다.
- **작전 개시** 
    - 어벤져스는 어느 분기점에서든 여정을 시작할 수 있으며, 어느 분기점에서든 마칠 수 있습니다. 
    - 단, 최소 하나 이상의 분기점은 반드시 방문해야 합니다.
- **최종 목표** 
    - 규칙을 지키며 방문한 모든 분기점의 승리 기여도 합을 **최대**로 만드세요.

시간 분기 $N$개와 점프 한계 $K$가 주어질 때, 어벤져스가 달성할 수 있는 최대 승리 기여도를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 분기점의 개수 $N$과 최대 점프 거리 $K$가 공백으로 구분되어 주어집니다. ($1 \le N \le 100,000, 1 \le K \le N$)
- 두 번째 줄에 각 분기점의 승리 기여도 점수 $s_1, s_2, \dots, s_N$이 공백으로 구분되어 주어집니다. 
- 각 점수는 $-10,000$ 이상 $10,000$ 이하의 정수입니다.

## 출력 형식 (Output Format)
- 어벤져스가 얻을 수 있는 **최대 승리 기여도 합**을 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 2
10 2 -10 5 20
{TICK}

**Output:**
{TICK}
37
{TICK}

- $K=2$이므로 현재 위치에서 다음 2칸 이내($i+1, i+2$)의 모든 곳으로 점프할 수 있습니다.
- 1번(10) → 2번(2) → 4번(5) → 5번(20) 순으로 방문하면 거리 차이가 모두 2 이하이며 총합은 37입니다.

### 예시 2
**Input:**
{TICK}
3 1
-1 -2 -3
{TICK}

**Output:**
{TICK}
-1
{TICK}

- 모든 시점의 리스크가 큽니다. 최소 하나는 방문해야 하므로 그나마 피해가 적은 -1점 시점만 방문하고 작전을 종료합니다.

### 예시 3 
**Input:**
{TICK}
7 3
10 10 -50 20 -100 -100 30
{TICK}

**Output:**
{TICK}
70
{TICK}

- $K=3$이므로 현재 위치에서 다음 3칸 이내($i+1, i+2, i+3$)의 모든 곳으로 점프할 수 있습니다.
- 1번(10)에서 시작해 2번(10)으로 이동합니다. (현재 합: 20)
- 2번(10)에서 3번(-50)을 건너뛰고($K=2$ 점프) 4번(20)으로 점프합니다. (현재 합: 40)
- 4번(20)에서 5번(-100)과 6번(-100)을 모두 건너뛰고($K=3$ 점프) 7번(30)으로 점프합니다. (최종 합: 70)
- 이보다 더 높은 점수를 얻을 수 있는 경로는 존재하지 않습니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    # 1. 데이터 읽기
    line = input().split()
    if not line: return
    n, k = int(line[0]), int(line[1])
    scores = list(map(int, input().split()))
    
    # dp[i]: i번째 시점을 마지막으로 방문했을 때의 최대 승리 기여도
    dp = [0] * n
    # 단조 감소 큐: 윈도우 내의 dp 최댓값을 O(1)에 찾기 위해 사용
    dq = deque()
    
    for i in range(n):
        # 윈도우 범위를 벗어난(거리가 K 초과) 인덱스 제거
        if dq and dq[0] < i - k:
            dq.popleft()
            
        # 이전 최적값 중 양수인 것만 가져와 현재 점수에 더함
        # 큐의 맨 앞에는 항상 현재 범위 내 최대 dp 인덱스가 있음
        prev_best = dp[dq[0]] if dq else 0
        dp[i] = scores[i] + max(0, prev_best)
        
        # 현재 dp[i]보다 작은 이전 값들은 필요 없으므로 제거 (단조성 유지)
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        dq.append(i)
        
    # 결과 출력: 모든 시점 중 도달 가능한 최대 점수
    print(max(dp))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k, scores):
    dp = [0] * n
    dq = deque()
    for i in range(n):
        if dq and dq[0] < i - k: dq.popleft()
        dp[i] = scores[i] + max(0, dp[dq[0]] if dq else 0)
        while dq and dp[i] >= dp[dq[-1]]: dq.pop()
        dq.append(i)
    return str(max(dp))

test_data = [
    (5, 2, [10, 2, -10, 5, 20]),
    (3, 1, [-1, -2, -3])
]

# 랜덤 데이터 생성
for _ in range(18):
    tn = random.randint(100, 500)
    tk = random.randint(5, 30)
    ts = [random.randint(-500, 500) for _ in range(tn)]
    test_data.append((tn, tk, ts))

for i, (n, k, scores) in enumerate(test_data, 1):
    input_str = f"{n} {k}\n" + " ".join(map(str, scores))
    ans = solve_internal(n, k, scores)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P079' 문제 생성이 완료되었습니다. ")