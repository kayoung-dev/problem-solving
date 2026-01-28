import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P102 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P102")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 회의실 배정 최적화

## 문제 설명
팀장 **서연**은 하루 동안 진행되는 여러 회의 요청을 정리하고 있습니다.

각 회의는 시작 시각과 종료 시각을 가지며,  
하나의 회의실에서는 **동시에 하나의 회의만 진행**할 수 있습니다.

서연은 가능한 한 **많은 회의를 진행**하고 싶어 합니다.  
이를 위해 회의 요청들을 적절한 순서로 정리하여 회의실에 배정하려고 합니다.

회의가 끝나는 즉시 다음 회의를 시작할 수 있다고 가정합니다.

주어진 회의 요청 목록을 바탕으로,  
하나의 회의실에서 진행할 수 있는 **최대 회의 개수**를 구하세요.

---

## 입력 형식
- 첫 줄에 회의의 개수 N이 주어집니다.
- 다음 N줄에는 각각 하나의 회의에 대한 정보가 주어집니다.
- 각 줄은 `시작시각 종료시각` 형식이며, 시각은 분 단위의 정수입니다.

---

## 출력 형식
- 하나의 회의실에서 진행할 수 있는 최대 회의 개수를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
1 4
3 5
0 6
5 7
8 9
{TICK}

**Output:**
{TICK}
3
{TICK}
- (1,4) → (5,7) → (8,9) 순서로 회의를 배정할 수 있습니다.

### 예시 2
**Input:**
{TICK}
6
10 12
0 6
5 7
3 8
8 10
12 14
{TICK}

**Output:**
{TICK}
4
{TICK}
- 종료 시각이 빠른 회의부터 선택하면 더 많은 회의를 배정할 수 있습니다.

### 예시 3
**Input:**
{TICK}
1
2 3
{TICK}

**Output:**
{TICK}
1
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    meetings = []

    for _ in range(n):
        s, e = map(int, input().split())
        meetings.append((e, s))  # 종료 시각 기준 정렬

    meetings.sort()

    count = 0
    current_end = -1

    for e, s in meetings:
        if s >= current_end:
            count += 1
            current_end = e

    print(count)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(meetings):
    arr = [(e, s) for s, e in meetings]
    arr.sort()
    cnt = 0
    cur = -1
    for e, s in arr:
        if s >= cur:
            cnt += 1
            cur = e
    return str(cnt)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(102)
test_data = []

# 예시 3개
test_data.append([(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)])
test_data.append([(10, 12), (0, 6), (5, 7), (3, 8), (8, 10), (12, 14)])
test_data.append([(2, 3)])

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    meetings = []
    for _ in range(n):
        s = random.randint(0, 1000)
        e = random.randint(s + 1, s + random.randint(1, 50))
        meetings.append((s, e))
    test_data.append(meetings)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, meetings in enumerate(test_data, 1):
    input_lines = [str(len(meetings))]
    for s, e in meetings:
        input_lines.append(f"{s} {e}")
    input_str = "\n".join(input_lines) + "\n"
    ans = solve_internal(meetings)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P102' 문제 생성이 완료되었습니다.")
