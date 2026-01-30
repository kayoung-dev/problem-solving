import os
import random
import heapq

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P112 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P112")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 내부 풀이 로직 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(grid, H):
    R = len(grid)
    C = len(grid[0])
    N = R * C
    flat = [v for row in grid for v in row]
    visited = [False] * N

    def edge_cost(a, b):
        d = flat[a] - flat[b]
        if d < 0:
            d = -d
        return 0 if d <= H else 1

    pq = []

    def push(frm, to):
        heapq.heappush(pq, (edge_cost(frm, to), to))

    visited[0] = True
    visited_cnt = 1

    # 시작점 이웃
    if C > 1:
        push(0, 1)
    if R > 1:
        push(0, C)

    total = 0
    while visited_cnt < N:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total += cost
        visited_cnt += 1

        r, c = divmod(node, C)
        if r > 0:
            nb = node - C
            if not visited[nb]:
                push(node, nb)
        if r < R - 1:
            nb = node + C
            if not visited[nb]:
                push(node, nb)
        if c > 0:
            nb = node - 1
            if not visited[nb]:
                push(node, nb)
        if c < C - 1:
            nb = node + 1
            if not visited[nb]:
                push(node, nb)

    return str(total)

def grid_to_str(g):
    return "\n".join(" ".join(map(str, row)) for row in g)

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
# 샘플 3개 고정 + 출력 자동 계산
sample1_R, sample1_C, sample1_H = 4, 5, 2
sample1_grid = [
    [20, 20, 21, 21, 22],
    [20, 21, 21, 22, 22],
    [19, 20, 21, 22, 23],
    [19, 20, 20, 21, 22],
]
sample1_out = solve_internal(sample1_grid, sample1_H)

sample2_R, sample2_C, sample2_H = 4, 4, 3
sample2_grid = [
    [18, 18, 18, 40],
    [18, 19, 19, 41],
    [18, 19, 20, 42],
    [18, 18, 20, 43],
]
sample2_out = solve_internal(sample2_grid, sample2_H)

sample3_R, sample3_C, sample3_H = 5, 4, 1
sample3_grid = [
    [10, 12, 11, 13],
    [10, 12, 11, 13],
    [10, 25, 26, 13],
    [10, 25, 26, 13],
    [10, 12, 11, 13],
]
sample3_out = solve_internal(sample3_grid, sample3_H)

problem_md = f"""# 온도 차단막 설치 최소화

## 문제 설명
시설 관리자 **소연**은 여러 구역으로 나뉜 실험 온실을 점검하려고 합니다.  
온실은 $R \\times C$ 격자 형태이며, 각 칸에는 그 구역의 **온도**가 적혀 있습니다.

소연은 한 번에 **상, 하, 좌, 우**로 인접한 한 칸만 이동할 수 있습니다.  
인접한 두 구역의 온도가 너무 다르면 순간적인 온도 변화로 장비에 문제가 생길 수 있어,
그 경계에 **차단막(단열 커버)** 을 설치하려 합니다.

인접한 두 칸의 온도를 $T_a$, $T_b$라고 할 때 온도 차는 $|T_a - T_b|$ 입니다.

- 허용 가능한 온도 차는 $H$ 입니다.
- $|T_a - T_b| \\le H$ 이면 차단막 없이 통과할 수 있습니다.
- $|T_a - T_b| > H$ 이면 그 경계에는 차단막을 설치해야 하며, **설치 개수는 1개**로 셉니다.
- 한 번 설치한 차단막은 계속 남아서, 그 경계는 이후에도 안전하게 통과할 수 있습니다.

소연이 **모든 칸을 서로 오갈 수 있도록** 만들기 위해 필요한 차단막 **최소 설치 개수**를 구하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $R$, $C$, $H$가 공백으로 주어집니다.
- 다음 $R$줄에 걸쳐 각 줄마다 $C$개의 정수로 온도가 주어집니다.

---

## 출력 형식 (Output Format)
- 모든 칸이 서로 이동 가능해지도록 만들기 위한 차단막 **최소 설치 개수**를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
{sample1_R} {sample1_C} {sample1_H}
{grid_to_str(sample1_grid)}
{TICK}
**Output:**
{TICK}
{sample1_out}
{TICK}

- 대부분의 인접 칸이 $|T_a - T_b| \\le 2$ 를 만족해 차단막이 거의 필요 없습니다.
- 꼭 필요한 경계만 골라 설치했을 때의 최소 개수가 출력값입니다.

### 예시 2
**Input:**
{TICK}
{sample2_R} {sample2_C} {sample2_H}
{grid_to_str(sample2_grid)}
{TICK}
**Output:**
{TICK}
{sample2_out}
{TICK}

- 오른쪽 열은 온도가 $40$ 이상이라, 왼쪽 영역($18\\sim20$)과 온도 차가 크게 벌어집니다.
- 결국 오른쪽 영역으로 넘어가는 경계는 최소 한 번 이상 차단막 설치가 필요하며,
  전체가 이어지도록 설치 개수를 최소화한 결과가 출력값입니다.

### 예시 3
**Input:**
{TICK}
{sample3_R} {sample3_C} {sample3_H}
{grid_to_str(sample3_grid)}
{TICK}
**Output:**
{TICK}
{sample3_out}
{TICK}

---

## 힌트 (Note)

- 각 칸을 “구역”, 인접한 상·하·좌·우 관계를 “연결 후보”라고 생각할 수 있습니다.
- 인접한 두 구역의 온도를 $T_a, T_b$라 할 때,
  
  $|T_a - T_b| \le H$
  이면 설치 없이 통과할 수 있고, 그렇지 않으면 그 경계에 **차단막 1개**가 필요합니다.
  즉, 모든 인접 경계의 비용은 **0 또는 1**입니다.

- 목표는 모든 구역이 서로 오갈 수 있도록 만들되, **차단막 설치 개수의 합을 최소화**하는 것입니다.  
  “이미 같은 덩어리로 이어진 구역들끼리” 다시 연결하는 선택은 의미가 없습니다.

- Minimum Spanning Tree 구현 팁:
  - 어떤 구역에서 시작해도 됩니다.
  - 현재까지 이어진 구역 집합과, 아직 이어지지 않은 구역을 잇는 경계들 중에서 **비용이 더 작은 경계(0이 우선, 그다음 1)** 를 반복해서 선택하면 유리합니다.
  - 새 구역이 이어지면, 그 구역의 인접 경계들을 후보로 추가하는 방식으로 확장할 수 있습니다.

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys
import heapq

def solve():
    input = sys.stdin.readline
    R, C, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    N = R * C
    flat = [v for row in grid for v in row]
    visited = [False] * N
    pq = []

    def edge_cost(a, b):
        d = flat[a] - flat[b]
        if d < 0:
            d = -d
        return 0 if d <= H else 1

    def push(frm, to):
        heapq.heappush(pq, (edge_cost(frm, to), to))

    visited[0] = True
    visited_cnt = 1

    if C > 1:
        push(0, 1)
    if R > 1:
        push(0, C)

    total = 0
    while visited_cnt < N:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = True
        total += cost
        visited_cnt += 1

        r, c = divmod(node, C)
        if r > 0:
            nb = node - C
            if not visited[nb]:
                push(node, nb)
        if r < R - 1:
            nb = node + C
            if not visited[nb]:
                push(node, nb)
        if c > 0:
            nb = node - 1
            if not visited[nb]:
                push(node, nb)
        if c < C - 1:
            nb = node + 1
            if not visited[nb]:
                push(node, nb)

    print(total)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (입출력 20개)
# ---------------------------------------------------------
random.seed(112)

def gen_case(case_idx):
    # 출력(설치 개수)이 과도하게 커지지 않도록: 패턴을 단순하게 섞어서 생성
    R = random.randint(4, 8)
    C = random.randint(4, 8)

    mode = case_idx % 4

    if mode == 0:
        # 거의 균일한 온도: 답 0이 자주 나오게
        H = random.randint(2, 6)
        base = random.randint(15, 25)
        grid = [[base + random.randint(0, 2) for _ in range(C)] for _ in range(R)]
        return R, C, H, grid

    if mode == 1:
        # 완만한 변화: 대부분 0, 가끔 1
        H = random.randint(1, 4)
        base = random.randint(10, 20)
        grid = []
        for r in range(R):
            row = []
            for c in range(C):
                row.append(base + r + c + random.randint(0, 1))
            grid.append(row)
        return R, C, H, grid

    if mode == 2:
        # 두 덩어리 온도대: 경계 몇 군데만 설치 필요하도록
        H = random.randint(2, 5)
        cool = random.randint(10, 18)
        hot = random.randint(30, 42)
        cut_r = R // 2
        cut_c = C // 2
        grid = []
        for r in range(R):
            row = []
            for c in range(C):
                if r < cut_r and c < cut_c:
                    row.append(cool + random.randint(0, 2))
                elif r >= cut_r and c >= cut_c:
                    row.append(hot + random.randint(0, 2))
                else:
                    # 완충 영역: 중간 온도로 깔아서 설치 개수가 폭증하지 않게
                    row.append((cool + hot) // 2 + random.randint(-1, 1))
            grid.append(row)
        return R, C, H, grid

    # mode == 3: 랜덤 (범위 제한)
    H = random.randint(1, 6)
    grid = [[random.randint(5, 45) for _ in range(C)] for _ in range(R)]
    return R, C, H, grid

test_data = []
for i in range(1, 21):
    R, C, H, grid = gen_case(i)
    test_data.append((R, C, H, grid))

# problem.md 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# solution.py 저장
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 테스트 저장
for i, (R, C, H, grid) in enumerate(test_data, 1):
    input_str = f"{R} {C} {H}\n" + "\n".join(" ".join(map(str, row)) for row in grid) + "\n"
    ans = solve_internal(grid, H) + "\n"

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P112' 문제 생성이 완료되었습니다.")
