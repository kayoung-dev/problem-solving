import os
import random
import heapq

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P111 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P111")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 내부 풀이 로직 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(grid, H):
    n = len(grid)
    N2 = n * n
    flat = [v for row in grid for v in row]
    visited = [False] * N2

    def cost(a, b):
        d = flat[a] - flat[b]
        if d < 0:
            d = -d
        d -= H
        return 0 if d <= 0 else d

    pq = []
    visited[0] = True
    visited_cnt = 1

    def push(frm, to):
        heapq.heappush(pq, (cost(frm, to), to))

    # 시작점 이웃 추가
    if n > 1:
        push(0, 1)
        push(0, n)

    total = 0
    while visited_cnt < N2:
        c, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total += c
        visited_cnt += 1

        r, col = divmod(node, n)
        if r > 0:
            nb = node - n
            if not visited[nb]:
                push(node, nb)
        if r < n - 1:
            nb = node + n
            if not visited[nb]:
                push(node, nb)
        if col > 0:
            nb = node - 1
            if not visited[nb]:
                push(node, nb)
        if col < n - 1:
            nb = node + 1
            if not visited[nb]:
                push(node, nb)

    return str(total)

def grid_to_str(g):
    return "\n".join(" ".join(map(str, row)) for row in g)

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
# 샘플 3개 (출력은 내부 로직으로 계산해 자동 일치)
sample1_n, sample1_h = 4, 2
sample1_grid = [
    [10, 11, 12, 13],
    [10, 11, 12, 13],
    [10, 11, 12, 13],
    [10, 11, 12, 13],
]
sample1_out = solve_internal(sample1_grid, sample1_h)

sample2_n, sample2_h = 4, 3
sample2_grid = [
    [1, 1, 1, 1],
    [1, 2, 2, 2],
    [1, 2, 9, 9],
    [1, 2, 9, 20],
]
sample2_out = solve_internal(sample2_grid, sample2_h)

sample3_n, sample3_h = 4, 1
sample3_grid = [
    [5, 8, 6, 7],
    [4, 9, 3, 10],
    [2, 11, 1, 12],
    [13, 14, 15, 16],
]
sample3_out = solve_internal(sample3_grid, sample3_h)

problem_md = f"""# 바닥 완충재 최소 설치

## 문제 설명
현장 관리자 **아린**은 $N \\times N$ 구역의 바닥을 점검하고 있습니다.  
각 칸에는 그 위치의 바닥 높이가 적혀 있으며, 아린은 한 번에 **상, 하, 좌, 우**로 인접한 한 칸으로만 이동할 수 있습니다.

인접한 두 칸의 높이가 $a$, $b$일 때 높이 차는 $|a-b|$ 입니다.  
아린은 높이 차가 너무 크면 넘어질 수 있어, 필요한 곳에 **완충재**를 설치하려 합니다.

- 허용 가능한 높이 차는 $H$ 입니다.
- $|a-b| \\le H$ 이면 **추가 작업 없이** 이동할 수 있습니다.
- $|a-b| > H$ 이면 그 경계에 완충재를 설치할 수 있고, 필요한 비용은  
  $MAX(0,\\ |a-b| - H)$
  입니다. (즉, 허용치 $H$를 넘는 **초과분만** 비용이 듭니다.)
- 한 번 설치한 완충재는 계속 남아, 그 경계는 이후에도 같은 방식으로 이동할 수 있습니다.

아린이 **모든 칸을 서로 오갈 수 있도록** 만들기 위해 필요한 완충재 설치 비용의 최솟값을 구하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$, $H$가 공백으로 주어집니다. $(4 \\le N \\le 30)$
- 다음 $N$줄에 걸쳐 각 줄마다 $N$개의 정수로 높이가 주어집니다. $(1 \\le \\text{{높이}} \\le 10{{,}}000)$

---

## 출력 형식 (Output Format)
- 모든 칸이 서로 안전하게 이동 가능해지도록 만들기 위한 최소 비용을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
{sample1_n} {sample1_h}
{grid_to_str(sample1_grid)}
{TICK}
**Output:**
{TICK}
{sample1_out}
{TICK}

- 모든 인접 칸의 높이 차가 $1$ 이하입니다.
- $H=2$ 이므로 항상 $|a-b| \\le H$를 만족해 비용이 $0$입니다.

### 예시 2
**Input:**
{TICK}
{sample2_n} {sample2_h}
{grid_to_str(sample2_grid)}
{TICK}
**Output:**
{TICK}
{sample2_out}
{TICK}

- 예를 들어 높이 $2$와 $9$는 차이가 $7$이고, $H=3$이므로 초과분 $7-3=4$만 비용이 듭니다.
- 전체를 연결할 때는, 이런 “초과분 비용”이 작은 경계들을 우선으로 선택하는 쪽이 유리합니다.

### 예시 3
**Input:**
{TICK}
{sample3_n} {sample3_h}
{grid_to_str(sample3_grid)}
{TICK}
**Output:**
{TICK}
{sample3_out}
{TICK}

## 힌트 (Note)

- 각 칸을 “정점”, 상/하/좌/우 인접 관계를 “연결 후보”로 생각해 볼 수 있습니다.
- 두 칸 $(a, b)$ 사이를 오갈 수 있게 만들 때 드는 비용은  
  $max(0,\ |a-b| - H)$
  로 계산됩니다. (허용치 $H$를 넘는 **초과분만** 비용)

- 목표는 “모든 칸이 서로 오갈 수 있도록” 연결 후보들을 일부 골라서 **총 비용 합을 최소**로 만드는 것입니다.  
  즉, 많은 연결 후보 중에서 **꼭 필요한 것만 선택**해야 합니다.

- “비용이 작은 연결부터” 선택해도 손해를 보지 않는 방향으로 진행하는 것이 유리합니다. (M) 
  단, 이미 같은 구역으로 이어진 칸들 사이를 또 연결하는 것은 의미가 없습니다.

- Minimum Spanning Tree 구현 팁:
  - 칸 번호를 $0 \sim N^2-1$로 바꿔 관리하면 편합니다.
  - $(r,c) \\rightarrow r\\cdot N + c$
  - 현재까지 이어진 구역과 “아직 안 이어진 칸”을 잇는 후보들 중에서 **가장 싼 비용**을 반복해서 선택하는 식으로 진행할 수 있습니다.
  - 방문/선택 여부를 기록하면서, 새 칸이 연결될 때 그 칸의 인접 후보들을 다시 후보 목록에 추가해 보세요.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys
import heapq

def solve():
    input = sys.stdin.readline
    N, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 인접 경계 비용: max(0, |a-b| - H)
    N2 = N * N
    flat = [v for row in grid for v in row]
    visited = [False] * N2
    pq = []

    def edge_cost(a, b):
        d = flat[a] - flat[b]
        if d < 0:
            d = -d
        d -= H
        return 0 if d <= 0 else d

    def push(frm, to):
        heapq.heappush(pq, (edge_cost(frm, to), to))

    visited[0] = True
    visited_cnt = 1

    if N > 1:
        push(0, 1)
        push(0, N)

    total = 0
    while visited_cnt < N2:
        c, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total += c
        visited_cnt += 1

        r, col = divmod(node, N)
        if r > 0:
            nb = node - N
            if not visited[nb]:
                push(node, nb)
        if r < N - 1:
            nb = node + N
            if not visited[nb]:
                push(node, nb)
        if col > 0:
            nb = node - 1
            if not visited[nb]:
                push(node, nb)
        if col < N - 1:
            nb = node + 1
            if not visited[nb]:
                push(node, nb)

    print(total)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(111)

def gen_case(case_idx):
    # Level01용: 크기 작게, 패턴 단순하게 (핵심 로직 연습용)
    n = random.randint(4, 8)

    mode = case_idx % 4

    if mode == 0:
        # 거의 평평: 답이 0이 자주 나오게
        H = random.randint(3, 7)
        base = random.randint(10, 30)
        grid = [[base + random.randint(0, 2) for _ in range(n)] for _ in range(n)]
        return n, H, grid

    if mode == 1:
        # 완만한 경사: 초과분이 조금씩만 나오게
        H = random.randint(1, 4)
        base = random.randint(1, 20)
        grid = []
        for r in range(n):
            row = []
            for c in range(n):
                row.append(base + r + c + random.randint(0, 1))
            grid.append(row)
        return n, H, grid

    if mode == 2:
        # 두 구역: 한두 군데만 비용이 크게 나오게(연결 선택 연습)
        H = random.randint(2, 6)
        low = random.randint(1, 20)
        high = random.randint(25, 60)
        cut = n // 2
        grid = []
        for r in range(n):
            row = []
            for c in range(n):
                if r < cut and c < cut:
                    row.append(low + random.randint(0, 2))
                elif r >= cut and c >= cut:
                    row.append(high + random.randint(0, 2))
                else:
                    row.append((low + high) // 2 + random.randint(-1, 1))
            grid.append(row)
        return n, H, grid

    # mode == 3: 완전 랜덤(그래도 범위는 너무 크지 않게)
    H = random.randint(1, 6)
    grid = [[random.randint(1, 80) for _ in range(n)] for _ in range(n)]
    return n, H, grid

test_data = []
for i in range(1, 21):
    n, H, grid = gen_case(i)
    test_data.append((n, H, grid))

# problem.md 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# solution.py 저장
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 테스트 저장
for i, (n, H, grid) in enumerate(test_data, 1):
    input_str = f"{n} {H}\n" + "\n".join(" ".join(map(str, row)) for row in grid) + "\n"
    ans = solve_internal(grid, H) + "\n"

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P111' 문제 생성이 완료되었습니다.")
