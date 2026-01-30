import os
import random
from typing import List, Tuple

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P117 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P117")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 서연의 좌석 그룹 통합

## 문제 설명
공연 스태프 **서연**은 관객 좌석을 관리하고 있습니다.  
관객들은 여러 팀(동아리, 회사, 가족 등) 단위로 왔고, 현장에서 계속해서 “같은 그룹이다”라는 정보가 추가로 들어옵니다.

서연은 다음 두 종류의 요청을 빠르게 처리해야 합니다.

- `U a b` : 좌석 $a$와 좌석 $b$는 **같은 그룹**이라고 확인되었다. (두 그룹을 합친다)
- `Q a b` : 좌석 $a$와 좌석 $b$가 **현재 같은 그룹인지** 확인한다.

모든 요청을 처리하면서, `Q` 요청에 대해서는 그때그때 결과를 출력해야 합니다.

---
## 입력 형식 (Input Format)
- 첫째 줄에 좌석 수 $N$과 요청 수 $Q$가 공백으로 주어집니다.
- $1 \\le N \\le 200000$
- 다음 $Q$줄에 요청이 한 줄에 하나씩 주어집니다.
  - `U a b` 또는 `Q a b` 형태
  - $1 \\le a, b \\le N$
  - $1 \\le Q \\le 300000$

## 출력 형식 (Output Format)
- 각 `Q a b` 요청에 대해,
  - 같은 그룹이면 `YES`
  - 아니면 `NO`
  를 한 줄에 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 6
Q 1 2
U 1 2
Q 1 2
U 2 3
Q 1 3
Q 4 5
{TICK}
**Output:**
{TICK}
NO
YES
YES
NO
{TICK}

- 처음엔 모든 좌석이 서로 다른 그룹이므로 `1`과 `2`는 `NO`입니다.
- `U 1 2` 후에는 `1`과 `2`가 같은 그룹이 됩니다.
- `U 2 3`을 하면 `1-2-3`이 하나의 그룹으로 합쳐집니다.

### 예시 2
**Input:**
{TICK}
4 5
U 1 2
U 3 4
Q 1 4
U 2 3
Q 1 4
{TICK}
**Output:**
{TICK}
NO
YES
{TICK}

### 예시 3
**Input:**
{TICK}
3 3
Q 1 1
Q 1 2
U 2 3
{TICK}
**Output:**
{TICK}
YES
NO
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, size, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    parent = list(range(N + 1))
    size = [1] * (N + 1)

    out = []
    for _ in range(Q):
        t, a, b = input().split()
        a = int(a); b = int(b)
        if t == 'U':
            union(parent, size, a, b)
        else:  # 'Q'
            out.append("YES" if find(parent, a) == find(parent, b) else "NO")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))

if __name__ == "__main__":
    main()
"""

def solve_internal(n: int, queries: List[Tuple[str, int, int]]) -> str:
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    out = []
    for t, a, b in queries:
        if t == "U":
            union(a, b)
        else:
            out.append("YES" if find(a) == find(b) else "NO")
    return ("\n".join(out) + ("\n" if out else ""))

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
rng = random.Random(117_2026)

test_data: List[Tuple[int, List[Tuple[str, int, int]]]] = []

# 예시 1~3 고정
test_data.append((5, [("Q",1,2), ("U",1,2), ("Q",1,2), ("U",2,3), ("Q",1,3), ("Q",4,5)]))
test_data.append((4, [("U",1,2), ("U",3,4), ("Q",1,4), ("U",2,3), ("Q",1,4)]))
test_data.append((3, [("Q",1,1), ("Q",1,2), ("U",2,3)]))

def gen_case(n: int, q: int, rng: random.Random) -> List[Tuple[str, int, int]]:
    # U와 Q 비율 섞기, 자기 자신 질의도 가끔 포함
    queries = []
    for i in range(q):
        if rng.random() < 0.55:
            t = "U"
        else:
            t = "Q"
        a = rng.randint(1, n)
        b = rng.randint(1, n)
        if rng.random() < 0.1:
            b = a
        queries.append((t, a, b))
    return queries

# 나머지 17개 생성 (크기 점증 + 다양한 비율)
while len(test_data) < 20:
    idx = len(test_data) + 1
    if idx <= 8:
        n = rng.randint(5, 40)
        q = rng.randint(10, 80)
    elif idx <= 14:
        n = rng.randint(100, 2000)
        q = rng.randint(500, 5000)
    else:
        n = rng.randint(5000, 20000)
        q = rng.randint(20000, 60000)

    queries = gen_case(n, q, rng)
    test_data.append((n, queries))

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, (n, queries) in enumerate(test_data, 1):
    input_lines = [f"{n} {len(queries)}\n"]
    for t, a, b in queries:
        input_lines.append(f"{t} {a} {b}\n")
    input_str = "".join(input_lines)

    ans = solve_internal(n, queries)

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P117' 문제 생성이 완료되었습니다.")
