import os
import random
from datetime import datetime, timedelta

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P101 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P101")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 출근 시간표 충돌 해결

## 문제 설명
신입사원 **민수**는 사내 출입 시스템에 기록된 출근 로그를 정리하는 업무를 맡았습니다.

출근 로그에는 여러 직원의 출근 기록이 뒤섞여 있으며,  
같은 직원의 기록이 여러 번 등장하기도 하고 입력 순서도 일정하지 않습니다.

각 출근 기록은 다음 정보를 가집니다.
- 사원 번호
- 출근 시각 (형식: HH:MM)

민수는 이 기록들을 정리하여 **실제 출근 순서표**를 만들려고 합니다.

출근 순서를 정리할 때는 다음과 같은 기준을 따릅니다.  
먼저 출근한 기록이 위에 오도록 정렬하되,  
출근 시각이 같은 경우에는 사원 번호가 작은 사람이 먼저 오도록 합니다.

정리된 출근 기록을 순서대로 출력하세요.

---

## 입력 형식
- 첫 줄에 출근 기록의 개수 N이 주어집니다.  
- 다음 N줄에는 각각 `사원번호 출근시각` 형식의 출근 기록이 주어집니다.

---

## 출력 형식
- 정렬된 출근 기록을 한 줄에 하나씩 출력합니다.  
- 출력 형식은 입력과 동일하게 `사원번호 출근시각`입니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
102 09:10
101 09:00
103 09:10
104 08:55
101 09:00
{TICK}

**Output:**
{TICK}
104 08:55
101 09:00
101 09:00
102 09:10
103 09:10
{TICK}
- 출근 시각이 빠른 기록부터 정렬합니다.
- 같은 시각에는 사원 번호가 작은 순서로 정렬됩니다.

### 예시 2
**Input:**
{TICK}
6
305 12:15
120 13:05
210 12:15
405 12:01
120 12:59
101 13:05
{TICK}

**Output:**
{TICK}
405 12:01
210 12:15
305 12:15
120 12:59
101 13:05
120 13:05
{TICK}
- 12시 이후 기록들도 동일하게 시각이 빠른 순서로 정렬합니다.
- 12:15처럼 시각이 같다면 사원 번호가 작은 210이 305보다 먼저 출력됩니다.
- 13:05처럼 시각이 같을 때도 사원 번호가 작은 101이 120보다 먼저 출력됩니다.

### 예시 3
**Input:**
{TICK}
1
301 08:30
{TICK}

**Output:**
{TICK}
301 08:30
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def time_to_min(t: str) -> int:
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    records = []

    for _ in range(n):
        emp, t = input().split()
        emp = int(emp)
        records.append((time_to_min(t), emp, t))

    records.sort()  # (time, emp)

    for _, emp, t in records:
        print(emp, t)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(rows):
    def to_min(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m
    arr = [(to_min(t), emp, t) for emp, t in rows]
    arr.sort()
    return "\n".join(f"{emp} {t}" for _, emp, t in arr)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(101)
test_data = []

# 예시 3개
test_data.append([
    (102, "09:10"),
    (101, "09:00"),
    (103, "09:10"),
    (104, "08:55"),
    (101, "09:00"),
])
test_data.append([
    (200, "09:00"),
    (100, "09:00"),
    (150, "09:00"),
])
test_data.append([
    (301, "08:30"),
])

def rand_time():
    h = random.randint(6, 11)
    m = random.choice([0, 5, 10, 15, 20, 30, 45, 55])
    return f"{h:02d}:{m:02d}"

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    rows = []
    for _ in range(n):
        emp = random.randint(1, 500)
        t = rand_time()
        rows.append((emp, t))
    test_data.append(rows)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, rows in enumerate(test_data, 1):
    input_lines = [str(len(rows))]
    for emp, t in rows:
        input_lines.append(f"{emp} {t}")
    input_str = "\n".join(input_lines) + "\n"
    ans = solve_internal(rows)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P101' 문제 생성이 완료되었습니다. ")
