import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P114 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P114")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 내부 풀이 로직 (정답 생성용): Kruskal MST + 선택 간선 목록 출력
# ---------------------------------------------------------
class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

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

def solve_internal(n, edges):
    dsu = DSU(n)
    # 정렬: 비용 오름차순, 동률이면 (u, v)로 안정화
    edges_sorted = sorted(edges, key=lambda x: (x[2], min(x[0], x[1]), max(x[0], x[1])))

    total = 0
    chosen = []
    for u, v, w in edges_sorted:
        if dsu.union(u, v):
            total += w
            a, b = (u, v) if u < v else (v, u)
            chosen.append((a, b))
            if len(chosen) == n - 1:
                break

    if len(chosen) != n - 1:
        return "-1"

    chosen.sort()  # (u, v) 오름차순
    out_lines = [str(total)]
    out_lines.extend([f"{u} {v}" for u, v in chosen])
    return "\n".join(out_lines)

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
def edges_to_str(ed):
    return "\n".join(f"{u} {v} {w}" for (u, v, w) in ed)

# 샘플 3개 (출력 자동 계산)
sample1_n = 4
sample1_edges = [
    (1, 2, 3),
    (2, 3, 2),
    (3, 4, 4),
    (1, 4, 10),
    (1, 3, 6),
]
sample1_out = solve_internal(sample1_n, sample1_edges)

sample2_n = 5
sample2_edges = [
    (1, 2, 2),
    (2, 3, 2),
    (3, 4, 2),
    (4, 5, 2),
    (1, 5, 9),
    (2, 4, 5),
    (1, 3, 4),
]
sample2_out = solve_internal(sample2_n, sample2_edges)

sample3_n = 6
sample3_edges = [
    (1, 2, 1),
    (2, 3, 2),
    (4, 5, 1),
    (5, 6, 2),
    # 1~3 과 4~6 사이를 잇는 후보가 없음 → 연결 불가
]
sample3_out = solve_internal(sample3_n, sample3_edges)

problem_md = f"""# 비상 연락선 최소 케이블 구축

## 문제 설명
산악 지역 안전 담당 **유진**은 $N$개의 관측 지점을 **비상 연락선**으로 연결하려 합니다.  
각 연락선 후보는 두 지점을 직접 잇는 계획이며, 후보마다 필요한 **케이블 길이(미터)** 가 정해져 있습니다.

- 한 후보 $(u, v, w)$는 “$u$ 지점과 $v$ 지점을 직접 잇는 연락선”을 뜻합니다.
- 이 연락선을 설치하려면 케이블이 **$w$ m**(미터) 필요합니다.
- 연락선은 **양방향**으로 통신이 가능합니다.

유진의 목표는 다음을 만족하면서 **필요한 케이블 총길이(미터)의 합을 최소**로 만드는 것입니다.

- 모든 지점이 서로 연락이 닿아야 합니다.  
  즉, 어떤 두 지점 $a$, $b$를 골라도 여러 연락선을 따라가면 $a$에서 $b$로 도달할 수 있어야 합니다.
- 사용할 수 있는 연락선은 입력으로 주어진 후보들 중에서만 고를 수 있습니다.

만약 후보만으로 전체를 하나로 만들 수 없다면, 계획을 세울 수 없으므로 `-1`을 출력합니다.  
가능하다면, 최소 총 케이블 길이와 함께 **선택한 연락선 목록**을 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 두 정수 $N$, $M$이 공백으로 주어집니다.
  - $N$: 지점의 개수 $(4 \\le N \\le 2000)$
  - $M$: 연락선 후보의 개수 $(0 \\le M \\le 20000)$
- 다음 $M$줄에 걸쳐 세 정수 $u$, $v$, $w$가 공백으로 주어집니다.
  - $u$, $v$는 서로 다른 지점 번호 $(1 \\le u,v \\le N)$
  - $w$는 해당 후보 연락선의 설치 비용 $(1 \\le w \\le 10^9)$
- 연락선은 **양방향**입니다.

---

## 출력 형식 (Output Format)
- 전체 연결이 불가능하면 `-1`을 출력합니다.
- 가능하면 아래 형식으로 출력합니다.
  1) 첫째 줄: 최소 총비용  
  2) 다음 줄들: 선택한 연락선 $N-1$개를 한 줄에 하나씩 `u v`로 출력  
     - 각 줄에서는 항상 $u < v$가 되도록 출력합니다.
     - 전체 목록은 $(u, v)$ 오름차순으로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
{sample1_n} {len(sample1_edges)}
{edges_to_str(sample1_edges)}
{TICK}
**Output:**
{TICK}
{sample1_out}
{TICK}

- 비용이 작은 후보부터 살펴보면,
  - $(2,3)$ 비용 $2$
  - $(1,2)$ 비용 $3$
  - $(3,4)$ 비용 $4$
  - 위 후보들을 선택하면 모든 지점이 하나로 이어집니다. 
  - 총 비용 $2+3+4=9$
- $(1,4)$는 비용이 크고, $(1,3)$은 이미 이어진 지점끼리라 추가로 선택할 필요가 없습니다.

### 예시 2
**Input:**
{TICK}
{sample2_n} {len(sample2_edges)}
{edges_to_str(sample2_edges)}
{TICK}
**Output:**
{TICK}
{sample2_out}
{TICK}

- 비용 $2$짜리 후보들이 연속으로 존재해 $(1,2),(2,3),(3,4),(4,5)$만 선택해도 전체가 하나로 이어집니다.
- 이때 총 비용은 $2+2+2+2=8$이므로, 더 비싼 후보를 섞는 것보다 유리합니다.

### 예시 3
**Input:**
{TICK}
{sample3_n} {len(sample3_edges)}
{edges_to_str(sample3_edges)}
{TICK}
**Output:**
{TICK}
{sample3_out}
{TICK}
- 1~3번 지점끼리는 서로 이어질 수 있고, 4~6번 지점끼리도 이어질 수 있지만,
  두 묶음을 연결하는 후보가 하나도 없습니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys

class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

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
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    edges.sort(key=lambda x: (x[2], min(x[0], x[1]), max(x[0], x[1])))

    dsu = DSU(N)
    total = 0
    chosen = []

    for u, v, w in edges:
        if dsu.union(u, v):
            total += w
            a, b = (u, v) if u < v else (v, u)
            chosen.append((a, b))
            if len(chosen) == N - 1:
                break

    if len(chosen) != N - 1:
        print(-1)
        return

    chosen.sort()
    print(total)
    for a, b in chosen:
        print(a, b)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 (입출력 20개) + 파일 저장
# ---------------------------------------------------------
random.seed(114)

def gen_connected_case(n, extra_edges, wmax):
    # 먼저 트리로 연결 보장
    edges = []
    parents = list(range(n + 1))
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        w = random.randint(1, wmax)
        edges.append((u, v, w))

    # 추가 간선
    s = set((min(u, v), max(u, v)) for u, v, _ in edges)
    attempts = 0
    while extra_edges > 0 and attempts < 10000:
        a = random.randint(1, n)
        b = random.randint(1, n)
        if a == b:
            attempts += 1
            continue
        x, y = (a, b) if a < b else (b, a)
        if (x, y) in s:
            attempts += 1
            continue
        s.add((x, y))
        w = random.randint(1, wmax)
        edges.append((a, b, w))
        extra_edges -= 1
    return edges

def gen_disconnected_case(n, wmax):
    # 두 컴포넌트로 분리 (연결 간선 없음)
    cut = n // 2
    edges = []
    # comp1: 1..cut
    for v in range(2, cut + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v, random.randint(1, wmax)))
    # comp2: cut+1..n
    for v in range(cut + 2, n + 1):
        u = random.randint(cut + 1, v - 1)
        edges.append((u, v, random.randint(1, wmax)))
    # 약간의 추가 간선(각 컴포넌트 내부)
    for _ in range(n // 2):
        a = random.randint(1, cut)
        b = random.randint(1, cut)
        if a != b:
            edges.append((a, b, random.randint(1, wmax)))
        a = random.randint(cut + 1, n)
        b = random.randint(cut + 1, n)
        if a != b:
            edges.append((a, b, random.randint(1, wmax)))
    return edges

test_data = []
for i in range(1, 21):
    # 출력에 간선 목록이 포함되므로 N은 과하게 키우지 않음(읽기/검증용)
    n = random.randint(6, 25)
    wmax = 50

    if i % 5 == 0:
        # 일부 케이스는 의도적으로 연결 불가
        edges = gen_disconnected_case(n, wmax)
        test_data.append((n, len(edges), edges))
    else:
        extra = random.randint(n, 3 * n)  # 후보 간선 수를 늘려 선택이 “정렬”에 의존하도록
        edges = gen_connected_case(n, extra, wmax)
        test_data.append((n, len(edges), edges))

# problem.md 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# solution.py 저장
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 테스트 저장
for i, (n, m, edges) in enumerate(test_data, 1):
    input_str = f"{n} {m}\n" + "\n".join(f"{u} {v} {w}" for (u, v, w) in edges) + "\n"
    ans = solve_internal(n, edges) + "\n"

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P114' 문제 생성이 완료되었습니다.")
