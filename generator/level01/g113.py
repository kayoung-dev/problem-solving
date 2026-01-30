import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P113 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P113")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 내부 풀이 로직 (정답 생성용) 
# ---------------------------------------------------------
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve_internal(points, existing_edges):
    n = len(points)
    dsu = DSU(n)

    # 기존 연결은 먼저 합친다(추가 비용 0)
    for a, b in existing_edges:
        dsu.union(a, b)

    # 모든 후보 연결(완전 그래프)
    edges = []
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            w = abs(xi - xj) + abs(yi - yj)
            edges.append((w, i, j))

    edges.sort()
    total = 0
    for w, i, j in edges:
        if dsu.union(i, j):
            total += w
    return str(total)

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
def points_to_str(pts):
    return "\n".join(f"{x} {y}" for x, y in pts)

def edges_to_str(ed):
    return "\n".join(f"{a+1} {b+1}" for a, b in ed)

# 샘플 3개 (출력은 내부 로직으로 자동 계산)
sample1_points = [(0, 0), (2, 0), (2, 2), (0, 2)]
sample1_existing = [(0, 1)]  # 1-2 already connected
sample1_out = solve_internal(sample1_points, sample1_existing)

sample2_points = [(1, 1), (4, 1), (7, 1), (4, 4), (7, 4)]
sample2_existing = [(1, 3), (2, 4)]  # 2-4, 3-5 connected
sample2_out = solve_internal(sample2_points, sample2_existing)

sample3_points = [(0, 0), (3, 1), (6, 0), (3, 4), (6, 5), (0, 5)]
sample3_existing = []
sample3_out = solve_internal(sample3_points, sample3_existing)

problem_md = f"""# 충전 거점 연결 계획

## 문제 설명
드론 운영자 **태호**는 드론이 끊기지 않고 이동할 수 있도록, 여러 곳에 흩어진 충전 거점들을 하나의 네트워크로 묶으려 합니다.

충전 거점은 총 $N$개이며, 각 거점의 위치는 좌표 $(x_i, y_i)$로 주어집니다.  
두 거점 $i$, $j$를 직접 연결하는 데 필요한 추가 작업 비용은 다음과 같습니다.

$\\text{{cost}}(i, j) = |x_i - x_j| + |y_i - y_j|$

이미 일부 거점 쌍은 **기존 연결**이 설치되어 있어, 그 거점들은 추가 비용 없이 서로 왕래할 수 있습니다.  
태호의 목표는 **모든 거점이 서로 이동 가능하도록** 만들기 위해 필요한 **추가 비용의 최솟값**을 구하는 것입니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 두 정수 $N$, $M$이 공백으로 주어집니다.  
  - $N$: 거점의 개수
  - $M$: 이미 연결된 거점 쌍의 개수
- 다음 $N$줄에 거점의 좌표 $x_i$, $y_i$가 공백으로 주어집니다.
- 다음 $M$줄에 이미 연결된 두 거점의 번호 $a$, $b$가 공백으로 주어집니다. (거점 번호는 $1$부터 시작)

---

## 출력 형식 (Output Format)
- 모든 거점이 서로 이동 가능해지도록 만들기 위한 **추가 비용의 최솟값**을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4 1
{points_to_str(sample1_points)}
{edges_to_str(sample1_existing)}
{TICK}
**Output:**
{TICK}
{sample1_out}
{TICK}

- 좌표는 다음과 같습니다.
  - 1번: $(0,0)$
  - 2번: $(2,0)$
  - 3번: $(2,2)$
  - 4번: $(0,2)$
- 이미 연결된 쌍이 1개 있습니다.
  - (1–2)번은 이미 연결 (추가 비용 $0$)

- 따라서 시작 상태에서 연결 묶음은 다음처럼 3개입니다.
  - 묶음 A: {1,2}
  - 묶음 B: {3}
  - 묶음 C: {4}

- 이제 서로 다른 묶음을 잇는 연결 중에서 비용이 작은 것부터 선택합니다.
  - 2–3 비용: |2-2| + |0-2| = 2
  - 1–4 비용: |0-0| + |0-2| = 2
  - 둘 다 비용이 2로 가장 작습니다.

- 예를 들어 2–3을 먼저 선택하면 묶음 A와 B가 합쳐지고,
  그 다음 1–4를 선택하면 남은 묶음 C까지 합쳐져 전체가 하나로 연결됩니다.

- 최소 추가 비용 합은
  2 + 2 = 4
  입니다.

### 예시 2
**Input:**
{TICK}
5 2
{points_to_str(sample2_points)}
{edges_to_str(sample2_existing)}
{TICK}
**Output:**
{TICK}
{sample2_out}
{TICK}

- 좌표는 다음과 같습니다.
  - 1번: $(1,1)$
  - 2번: $(4,1)$
  - 3번: $(7,1)$
  - 4번: $(4,4)$
  - 5번: $(7,4)$
- 이미 연결된 쌍이 2개 있습니다.
  - $2$–$4$번은 이미 연결 (추가 비용 $0$)
  - $3$–$5$번은 는 이미 연결 (추가 비용 $0$)

- 따라서 시작 상태에서 연결 묶음은 다음처럼 3개입니다.
  - 묶음 A: (2번, 4번)
  - 묶음 B: (3번, 5번)
  - 묶음 C: (1번)

- 이제 서로 다른 묶음끼리만 이어야 의미가 있습니다.  
  우선 A와 B를 잇는 가장 싼 연결을 찾으면,
  - $2$–$3$번 비용: $|4-7| + |1-1| = 3$
  - $4$–$5$번 비용: $|4-7| + |4-4| = 3$
  둘 다 비용이 $3$으로 최솟값입니다. 예를 들어 $2$–$3$을 선택하면 A와 B가 하나로 합쳐집니다.

- 남은 묶음 C(1번)를 합쳐야 합니다. 가장 저렴한 연결은
  - $1$–$2$번 비용: $|1-4| + |1-1| = 3$
  - 다른 후보 보다 작음

- 따라서 최소 추가 비용 합은
  \[
  3 + 3 = 6
  \]
  이 되어 출력이 `6`입니다.

### 예시 3
**Input:**
{TICK}
6 0
{points_to_str(sample3_points)}
{TICK}
**Output:**
{TICK}
{sample3_out}
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    dsu = DSU(N)
    for _ in range(M):
        a, b = map(int, input().split())
        dsu.union(a - 1, b - 1)

    edges = []
    for i in range(N):
        xi, yi = pts[i]
        for j in range(i + 1, N):
            xj, yj = pts[j]
            w = abs(xi - xj) + abs(yi - yj)
            edges.append((w, i, j))

    edges.sort()
    total = 0
    for w, i, j in edges:
        if dsu.union(i, j):
            total += w

    print(total)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 (입출력 20개) + 파일 저장
# ---------------------------------------------------------
random.seed(113)

def gen_points(n, coord_max):
    # 너무 중복 좌표가 나오지 않게 약간 관리
    seen = set()
    pts = []
    while len(pts) < n:
        x = random.randint(0, coord_max)
        y = random.randint(0, coord_max)
        if (x, y) in seen:
            continue
        seen.add((x, y))
        pts.append((x, y))
    return pts

def gen_existing_edges(n, m):
    # 이미 연결된 간선은 랜덤으로 생성 (중복/자기자신 방지)
    s = set()
    edges = []
    tries = 0
    while len(edges) < m and tries < 5000:
        a = random.randrange(n)
        b = random.randrange(n)
        if a == b:
            tries += 1
            continue
        if a > b:
            a, b = b, a
        if (a, b) in s:
            tries += 1
            continue
        s.add((a, b))
        edges.append((a, b))
    return edges

test_data = []
for i in range(1, 21):
    # Level01이지만 MST 감각을 위해 N을 너무 작지만은 않게
    # (완전그래프 생성이므로 N은 적당히 제한)
    if i <= 6:
        n = random.randint(6, 10)
        coord_max = 12
    elif i <= 14:
        n = random.randint(10, 16)
        coord_max = 25
    else:
        n = random.randint(16, 22)
        coord_max = 40

    # 기존 연결 M: 0~n//2 정도
    m = random.randint(0, n // 2)
    pts = gen_points(n, coord_max)
    existing = gen_existing_edges(n, m)
    test_data.append((n, m, pts, existing))

# problem.md 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# solution.py 저장
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 테스트 저장
for i, (n, m, pts, existing) in enumerate(test_data, 1):
    input_lines = []
    input_lines.append(f"{n} {m}")
    input_lines.extend([f"{x} {y}" for (x, y) in pts])
    input_lines.extend([f"{a+1} {b+1}" for (a, b) in existing])
    input_str = "\n".join(input_lines) + "\n"

    ans = solve_internal(pts, existing) + "\n"

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P113' 문제 생성이 완료되었습니다.")
