import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P87 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P87")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = """# 회의실 예약 충돌 제거

## 문제 설명
매니저 **다은**은 하루 동안의 회의실 예약 목록을 정리하고 있습니다.  
각 예약은 시작 시각과 종료 시각으로 주어지며, 다은은 **회의가 겹치지 않도록** 예약 일부를 취소하려고 합니다.

회의실은 동시에 하나의 회의만 진행할 수 있습니다.  
즉, 두 예약 구간이 겹치면 동시에 진행할 수 없습니다.

다은의 목표는 **최대한 많은 예약을 유지**하는 것입니다.  
취소해야 하는 예약 개수의 **최솟값**을 출력하세요.

- 예약 구간을 `[start, end)` 로 생각합니다.  
  즉, 한 회의가 끝나는 시각 `end`와 다른 회의가 시작하는 시각 `start`가 같으면 겹치지 않습니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 다음 $N$줄에 걸쳐 두 정수 $s$(시작시각), $e$(종료시각)가 공백으로 구분되어 주어집니다.
  - $0 \\le s < e \\le 10^9$

## 출력 형식 (Output Format)
- 겹치지 않게 만들기 위해 취소해야 하는 예약 개수의 최솟값을 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
1 3
2 4
3 5
4 6
{TICK}
**Output:**
{TICK}
2
{TICK}
- 종료 시간이 빠른 예약부터 선택하면 (1,3), (3,5)처럼 겹치지 않게 2개를 유지할 수 있습니다.
- 전체 4개 중 2개를 유지하므로 취소는 2개입니다.

### 예시 2
**Input:**
{TICK}
5
1 2
2 3
3 4
1 3
3 5
{TICK}
**Output:**
{TICK}
1
{TICK}
- (1,2), (2,3), (3,4), (4와 겹치지 않는 선택) 처럼 4개까지 유지 가능합니다.
- 전체 5개 중 4개를 유지하므로 취소는 1개입니다.

### 예시 3
**Input:**
{TICK}
1
10 20
{TICK}
**Output:**
{TICK}
0
{TICK}
""".format(TICK=TICK)

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

    intervals = []
    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append((e, s))  # (end, start)

    intervals.sort()  # end 오름차순, end 같으면 start 오름차순

    keep = 0
    last_end = -10**18
    for end, start in intervals:
        if start >= last_end:
            keep += 1
            last_end = end

    print(n - keep)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(intervals):
    intervals = sorted(((e, s) for s, e in intervals))
    keep = 0
    last_end = -10**18
    for end, start in intervals:
        if start >= last_end:
            keep += 1
            last_end = end
    return str(len(intervals) - keep)

random.seed(87)

test_data = []

# 샘플 3개 (problem.md 예시와 일치)
test_data.append([(1, 3), (2, 4), (3, 5), (4, 6)])  # ans 2
test_data.append([(1, 2), (2, 3), (3, 4), (1, 3), (3, 5)])  # ans 1
test_data.append([(10, 20)])  # ans 0

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 7)

    intervals = []

    if mode == 1:
        # 완전 랜덤
        for _ in range(n):
            s = random.randint(0, 10**6)
            e = s + random.randint(1, 1000)
            intervals.append((s, e))

    elif mode == 2:
        # 연속 체인 (겹침 거의 없음)
        t = random.randint(0, 1000)
        for _ in range(n):
            dur = random.randint(1, 20)
            intervals.append((t, t + dur))
            t += dur  # 바로 이어지게

    elif mode == 3:
        # 같은 시작 시간 몰기 (겹침 많음)
        base_s = random.randint(0, 1000)
        for _ in range(n):
            e = base_s + random.randint(1, 200)
            intervals.append((base_s, e))

    elif mode == 4:
        # 같은 종료 시간 몰기
        base_e = random.randint(200, 1000)
        for _ in range(n):
            s = random.randint(0, base_e - 1)
            intervals.append((s, base_e))

    elif mode == 5:
        # 짧은 회의 위주 (선택 많이 가능)
        for _ in range(n):
            s = random.randint(0, 5000)
            e = s + random.randint(1, 5)
            intervals.append((s, e))

    elif mode == 6:
        # 긴 회의 위주 (겹침 많음)
        for _ in range(n):
            s = random.randint(0, 5000)
            e = s + random.randint(50, 500)
            intervals.append((s, e))

    else:
        # 섞기: 체인 + 랜덤 + 겹침 구간
        t = random.randint(0, 1000)
        for _ in range(n // 3):
            dur = random.randint(1, 30)
            intervals.append((t, t + dur))
            t += dur
        for _ in range(n - len(intervals)):
            s = random.randint(0, 10**6)
            e = s + random.randint(1, 1000)
            intervals.append((s, e))

    test_data.append(intervals)

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, intervals in enumerate(test_data, 1):
    n = len(intervals)
    lines = [str(n)]
    for s, e in intervals:
        lines.append(f"{s} {e}")
    input_str = "\n".join(lines) + "\n"
    ans = solve_internal(intervals)

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P87' 문제 생성이 완료되었습니다.")
