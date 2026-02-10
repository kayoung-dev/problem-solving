import os
import random
import heapq

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P110 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P110")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 게시글 피드 정렬

## 문제 설명
운영자 **유나**는 커뮤니티의 게시글 피드를 정리해야 합니다.

각 게시글에는 다음 정보가 있습니다.

- 게시글 ID \(id\)
- 작성 시각 \(t\) (정수)
- 좋아요 수 \(l\) (정수)
- 댓글 수 \(c\) (정수)

유나는 피드를 다음 규칙으로 정렬해 상위 \(K\)개의 게시글만 보여주려고 합니다.

1. 점수 \(S\)가 큰 게시글이 먼저 온다.
2. 점수 \(S\)가 같다면 작성 시각 \(t\)가 더 최근인 게시글이 먼저 온다. (큰 값 우선)
3. 위까지 같다면 게시글 ID가 작은 게시글이 먼저 온다.

점수 $S$는 다음과 같이 계산합니다.

$S = 2l + 3c$

정렬 규칙에 따라 상위 \(K\)개의 게시글 ID를 순서대로 출력하세요.

---

## 입력 형식
- 첫 줄에 게시글 개수 N과 출력할 상위 게시글 개수 K가 공백으로 주어집니다.
- 다음 N줄에 `id t l c`가 주어집니다.

---

## 출력 형식
- 정렬 규칙에 따른 상위 \(K\)개 게시글의 ID를 한 줄에 공백으로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6 3
10 100 5 0
11 101 4 1
12 99 4 1
13 110 2 2
14 105 1 3
15 105 1 3
{TICK}

**Output:**
{TICK}
14 15 11
{TICK}

- 각 게시글의 점수는 `S = 2 × 좋아요 + 3 × 댓글`로 계산한다.
  - ID 10: $S = 2\\cdot5 + 3\\cdot0 = 10$, 시각 $t=100$
  - ID 11: $S = 2\\cdot4 + 3\\cdot1 = 11$, 시각 $t=101$
  - ID 12: $S = 2\\cdot4 + 3\\cdot1 = 11$, 시각 $t=99$
  - ID 13: $S = 2\\cdot2 + 3\\cdot2 = 10$, 시각 $t=110$
  - ID 14: $S = 2\\cdot1 + 3\\cdot3 = 11$, 시각 $t=105$
  - ID 15: $S = 2\\cdot1 + 3\\cdot3 = 11$, 시각 $t=105$
- 점수 11인 게시글은 ID 11, 12, 14, 15이다.
- 이 중 작성 시각이 가장 최근인 게시글은 ID 14와 15(시각 105)이다.
- ID 14와 15는 점수와 시각이 같으므로 ID가 작은 14가 먼저 온다.
- 그 다음으로 시각이 더 최근인 ID 11이 선택되어 상위 3개가 된다.

---

### 예시 2
**Input:**
{TICK}
4 2
1 10 0 1
2 11 1 0
3 12 0 1
4 9 5 0
{TICK}

**Output:**
{TICK}
4 3
{TICK}

---

### 예시 3
**Input:**
{TICK}
3 3
7 1 0 0
6 2 0 0
5 3 0 0
{TICK}

**Output:**
{TICK}
5 6 7
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    posts = []
    for _ in range(n):
        pid, t, l, c = map(int, input().split())
        s = 2*l + 3*c
        posts.append((s, t, pid))

    # 정렬: s desc, t desc, id asc
    posts.sort(key=lambda x: (-x[0], -x[1], x[2]))

    top = posts[:k]
    print(" ".join(str(x[2]) for x in top))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(posts, k):
    arr = []
    for pid, t, l, c in posts:
        s = 2*l + 3*c
        arr.append((s, t, pid))
    arr.sort(key=lambda x: (-x[0], -x[1], x[2]))
    ans_ids = [str(x[2]) for x in arr[:k]]
    return " ".join(ans_ids) + "\n"

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(110)
test_data = []

# 예시 3개 (problem.md와 일치)
test_data.append((
    [(10, 100, 5, 0),
     (11, 101, 4, 1),
     (12, 99, 4, 1),
     (13, 110, 2, 2),
     (14, 105, 1, 3),
     (15, 105, 1, 3)],
    3
))

test_data.append((
    [(1, 10, 0, 1),
     (2, 11, 1, 0),
     (3, 12, 0, 1),
     (4, 9, 5, 0)],
    2
))

test_data.append((
    [(7, 1, 0, 0),
     (6, 2, 0, 0),
     (5, 3, 0, 0)],
    3
))

def gen_case():
    n = random.randint(1, 200)
    k = random.randint(1, n)
    used = set()
    posts = []
    for _ in range(n):
        while True:
            pid = random.randint(1, 999)
            if pid not in used:
                used.add(pid)
                break
        t = random.randint(0, 5000)
        l = random.randint(0, 200)
        c = random.randint(0, 200)
        posts.append((pid, t, l, c))
    return posts, k

for _ in range(17):
    test_data.append(gen_case())

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성 (✅ 실제 개행)
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (posts, k) in enumerate(test_data, 1):
    n = len(posts)
    input_lines = [f"{n} {k}"]
    for pid, t, l, c in posts:
        input_lines.append(f"{pid} {t} {l} {c}")
    input_str = "\n".join(input_lines) + "\n"

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    ans = solve_internal(posts, k)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P110' 문제 생성이 완료되었습니다.")
