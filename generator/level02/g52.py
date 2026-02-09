import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P52 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P52")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 공항 보안 검색용 무빙워크

## 문제 설명
공항의 보안 검색대에는 일정한 간격으로 칸이 나누어진 무빙워크가 있습니다. 승객들은 자신의 짐을 바구니에 담아 이 무빙워크에 올려두어야 합니다. 하지만 무빙워크는 너무 많은 짐이 올라가면 멈춰버리기 때문에, 한 번에 견딜 수 있는 최대 하중이 정해져 있습니다.

무빙워크와 짐의 이동 규칙은 다음과 같습니다.

1. 무빙워크는 총 L개의 칸으로 이루어져 있습니다. 짐은 1초에 한 칸씩 앞으로 전진하며, 무빙워크를 완전히 통과하는 데는 L초가 걸립니다.
2. 무빙워크 전체에 올라가 있는 짐들의 무게 합은 최대 W를 넘을 수 없습니다.
3. 짐들은 정해진 순서대로만 무빙워크에 올릴 수 있습니다.
4. 매초마다 무빙워크는 한 칸씩 전진합니다. 이때 맨 끝 칸에 도달했던 짐은 밖으로 나가게 됩니다.
5. 새로운 짐을 올릴 때, 현재 무빙워크 위에 있는 짐들의 무게 합에 새 짐의 무게를 더해도 W 이하이고 자리가 있다면 즉시 짐을 올립니다. 무게 제한을 넘는다면 해당 짐은 앞의 짐들이 빠져나갈 때까지 입구에서 대기합니다.

모든 짐이 무빙워크를 통과하여 밖으로 나오기까지 걸리는 최소 시간을 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 무빙워크의 칸 수 L, 최대 하중 W, 짐의 개수 N이 공백으로 구분되어 주어집니다. (1 <= L, W, N <= 10,000)
- 두 번째 줄에 각 짐의 무게가 순서대로 주어집니다. 모든 짐의 무게는 W보다 작거나 같습니다.

## 출력 형식 (Output Format)
- 모든 짐이 무빙워크를 빠져나오기까지 걸리는 최소 시간을 정수로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
2 10 2
7 4
{TICK}

**Output:**
{TICK}
5
{TICK}

- 1초: 7번 짐이 들어옴 [7, 0]
- 2초: 7번 짐이 한 칸 전진 [0, 7]. 4번 짐은 무게 제한(7+4=11) 때문에 못 들어오고 대기.
- 3초: 7번 짐이 나감. 동시에 4번 짐이 들어옴 [4, 0]
- 4초: 4번 짐이 한 칸 전진 [0, 4]
- 5초: 4번 짐이 나감. 완료!

### 예시 2
**Input:**
{TICK}
100 100 1
10
{TICK}

**Output:**
{TICK}
101
{TICK}

- 1초: 무게가 10인 첫 번째 짐이 무빙워크의 첫 번째 칸에 올라갑니다.
- 101초: 진입한 짐이 100칸의 무빙워크를 모두 거쳐 완전히 밖으로 빠져나옵니다.
- 총 시간은 (진입하는 데 걸리는 시간 1초) + (이동하여 통과하는 시간 100초) = 101초입니다.

### 예시 3
**Input:**
{TICK}
5 50 3
10 10 10
{TICK}

**Output:**
{TICK}
8
{TICK}

- 1초: 첫 번째 짐 진입 [10, 0, 0 ,0 ,0] (현재 무게 합: 10)
- 2초: 두 번째 짐 진입 [10, 10, 0, 0, 0] (현재 무게 합: 20)
- 3초: 세 번째 짐 진입 [10, 10, 10, 0, 0] (현재 무게 합: 30)
- 4초: 짐 이동 [0, 10, 10, 10, 0]
- 5초: 짐 이동 [0, 0, 10, 10, 10]
- 6초: 짐 이동 [0, 0, 0, 10, 10] (첫 번째짐 빠져나옴)
- 7초: 짐 이동 [0, 0, 0, 0, 10] (두 번째짐 빠져나옴)
- 8초: 마지막 짐이 무빙워크를 완전히 통과하여 빠져나옴. [0, 0, 0, 0, 0]
- 무게 제한(50)에 걸리지 않아 매초 짐을 하나씩 올릴 수 있었으므로, 총 시간은 (무빙워크 길이 5) + (짐 개수 3) = 8초
"""

problem_md = problem_template.replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_content = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    l = int(input_data[0])
    w = int(input_data[1])
    n = int(input_data[2])
    packages = deque(map(int, input_data[3:]))
    
    # 무빙워크의 각 칸을 0으로 초기화
    moving_walk = deque([0] * l)
    current_weight = 0
    time = 0
    
    while moving_walk:
        time += 1
        # 맨 끝 칸에서 밖으로 나가는 짐 처리
        out = moving_walk.popleft()
        current_weight -= out
        
        if packages:
            # 새로운 짐이 들어올 수 있는지 하중 체크
            if current_weight + packages[0] <= w:
                p = packages.popleft()
                moving_walk.append(p)
                current_weight += p
            else:
                # 못 들어오면 빈 공간(0)을 채워 넣음
                moving_walk.append(0)
                
    print(time)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(l, w, n, weights):
    from collections import deque
    pkgs = deque(weights)
    walk = deque([0] * l)
    cur_w = 0
    time = 0
    while walk:
        time += 1
        cur_w -= walk.popleft()
        if pkgs:
            if cur_w + pkgs[0] <= w:
                p = pkgs.popleft()
                walk.append(p)
                cur_w += p
            else:
                walk.append(0)
    return str(time)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (2, 10, 2, [7, 4]),
    (100, 100, 1, [10]),
    (10, 100, 10, [10]*10),
    (5, 50, 3, [20, 30, 10]),
    (3, 15, 4, [10, 5, 10, 5])
]

for _ in range(15):
    tl = random.randint(5, 50)
    tw = random.randint(20, 100)
    tn = random.randint(5, 20)
    tweights = [random.randint(1, tw // 2) for _ in range(tn)]
    test_cases.append((tl, tw, tn, tweights))

for i, (l, w, n, weights) in enumerate(test_cases, 1):
    input_str = f"{l} {w} {n}\n" + " ".join(map(str, weights))
    ans = solve_internal(l, w, n, weights)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P52' 문제 생성이 완료되었습니다.")