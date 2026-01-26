import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P82 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P82")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 성적표 정렬 출력

## 문제 설명
조교 **민수**는 학생 성적표를 정리하고 있습니다.  
각 학생은 **학번** $id$와 **점수** $s$를 가집니다.

민수는 아래 규칙으로 성적표를 정렬해 출력하려고 합니다.

1. 점수 $s$가 **낮은 순** (오름차순)
2. 점수가 같다면 학번 $id$가 **작은 순** (오름차순)

학생 정보가 주어졌을 때, 정렬된 결과를 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 다음 $N$줄에 걸쳐 학생의 학번과 점수가 공백으로 구분되어 주어집니다.
  - 학번: $1 \\le id \\le 10^9$
  - 점수: $0 \\le s \\le 100$

## 출력 형식 (Output Format)
- 정렬된 순서대로 학생 정보를 $N$줄에 출력하세요.
- 각 줄은 `id s` 형태로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
1002 70
1001 70
2001 50
3000 90
1500 50
{TICK}
**Output:**
{TICK}
1500 50
2001 50
1001 70
1002 70
3000 90
{TICK}
- 점수 $50$인 학생이 먼저 나옵니다.
- 점수가 같으면 학번이 작은 순서로 정렬되므로 $1500$이 $2001$보다 먼저 출력됩니다.
- 점수 $70$도 같은 방식으로 $1001$이 $1002$보다 먼저 출력됩니다.

### 예시 2
**Input:**
{TICK}
4
10 0
7 100
8 100
9 0
{TICK}
**Output:**
{TICK}
9 0
10 0
7 100
8 100
{TICK}
- 점수 $0$이 먼저, 그 다음 점수 $100$이 나옵니다.
- 점수 $0$에서 학번 오름차순이므로 $9$가 $10$보다 먼저 출력됩니다.

### 예시 3
**Input:**
{TICK}
1
12345 88
{TICK}
**Output:**
{TICK}
12345 88
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    students = []
    for _ in range(n):
        line = input().split()
        if not line:
            continue
        sid = int(line[0])
        score = int(line[1])
        students.append((score, sid))

    # 점수 오름차순, 점수 같으면 학번 오름차순
    students.sort()

    out_lines = []
    for score, sid in students:
        out_lines.append(f"{sid} {score}")
    sys.stdout.write("\\n".join(out_lines))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(pairs):
    # pairs: list[(id, score)]
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))  # (score, id)
    return "\n".join(f"{sid} {score}" for sid, score in sorted_pairs)

random.seed(82)

test_data = []

# 샘플 3개를 1~3번 케이스로 고정 (problem.md 예시와 일치)
sample1 = [(1002, 70), (1001, 70), (2001, 50), (3000, 90), (1500, 50)]
sample2 = [(10, 0), (7, 100), (8, 100), (9, 0)]
sample3 = [(12345, 88)]
test_data.extend([sample1, sample2, sample3])

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 6)

    # 학번은 중복 없게 만드는 편이 자연스러워서 set으로 관리
    used = set()
    pairs = []

    def new_id():
        # 큰 범위에서 중복 방지
        while True:
            sid = random.randint(1, 10**7)
            if sid not in used:
                used.add(sid)
                return sid

    if mode == 1:
        # 완전 랜덤
        for _ in range(n):
            pairs.append((new_id(), random.randint(0, 100)))

    elif mode == 2:
        # 동점(같은 점수) 많이 만들기
        common_scores = [random.randint(0, 100) for _ in range(random.randint(1, 5))]
        for _ in range(n):
            pairs.append((new_id(), random.choice(common_scores)))

    elif mode == 3:
        # 점수 거의 정렬된 상태(약간만 섞기)
        scores = sorted([random.randint(0, 100) for _ in range(n)])
        # 약간 셔플
        swaps = random.randint(0, min(30, n))
        for _ in range(swaps):
            i = random.randrange(n)
            j = random.randrange(n)
            scores[i], scores[j] = scores[j], scores[i]
        for s in scores:
            pairs.append((new_id(), s))

    elif mode == 4:
        # 점수 모두 같고 학번만 다양 (2차 정렬 확인용)
        s = random.randint(0, 100)
        for _ in range(n):
            pairs.append((new_id(), s))

    elif mode == 5:
        # 극단 점수(0/100) 위주
        for _ in range(n):
            s = random.choice([0, 0, 0, 100, 100, random.randint(1, 99)])
            pairs.append((new_id(), s))

    else:
        # 학번 범위를 좁혀도 중복 없이 생성 + 점수 넓게
        # (학번이 비슷비슷한 케이스)
        base = random.randint(1, 5000)
        for k in range(n):
            sid = base + k  # 중복 없음
            score = random.randint(0, 100)
            pairs.append((sid, score))

    test_data.append(pairs)

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
# problem.md 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# solution.py 저장
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 테스트 입출력 파일 저장 (20개)
for i, pairs in enumerate(test_data, 1):
    n = len(pairs)
    lines = [str(n)]
    for sid, score in pairs:
        lines.append(f"{sid} {score}")
    input_str = "\n".join(lines) + "\n"

    ans = solve_internal(pairs)

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P82' 문제 생성이 완료되었습니다.")
