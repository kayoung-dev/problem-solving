import os
import random
import heapq

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P88 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P88")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = """# 마감 임박 과제 선택

## 문제 설명
학생 **태오**는 오늘부터 여러 과제를 처리하려고 합니다.  
각 과제는

- 제출 마감일 `d` (며칠 뒤까지 제출해야 하는지)
- 받을 수 있는 점수 `p`

로 주어집니다.

태오는 하루에 과제를 **최대 1개만** 제출할 수 있습니다.  
또한 과제는 마감일 `d` **이내**(1일부터 d일까지) 어느 날에든 제출할 수 있습니다.

태오가 얻을 수 있는 **총 점수의 최댓값**을 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 다음 $N$줄에 두 정수 $d, p$가 공백으로 구분되어 주어집니다.
  - $1 \\le d \\le 200$
  - $1 \\le p \\le 10^6$

## 출력 형식 (Output Format)
- 얻을 수 있는 총 점수의 최댓값을 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
1 10
2 20
2 5
3 30
{TICK}
**Output:**
{TICK}
60
{TICK}
- 1일차: (1,10) 제출
- 2일차: (2,20) 제출
- 3일차: (3,30) 제출
- 받을 수 있는 점수의 최대값은 10 + 20 + 30 = 60 입니다.

### 예시 2
**Input:**
{TICK}
5
1 50
1 10
2 20
2 100
3 30
{TICK}
**Output:**
{TICK}
180
{TICK}
- 마감일이 빠른 과제부터 고려하면서, 선택한 과제 중 점수가 작은 것을 필요하면 제외합니다.
- 최대로 얻을 수 있는 합은 50 + 100 + 30 = 180 입니다.

### 예시 3
**Input:**
{TICK}
1
5 999
{TICK}
**Output:**
{TICK}
999
{TICK}
""".format(TICK=TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
import heapq

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    tasks = []
    for _ in range(n):
        d, p = map(int, input().split())
        tasks.append((d, p))

    tasks.sort()  # deadline 오름차순

    heap = []  # 선택한 과제들의 점수(최소 힙)
    for d, p in tasks:
        heapq.heappush(heap, p)
        # d일까지는 최대 d개만 제출 가능
        if len(heap) > d:
            heapq.heappop(heap)

    print(sum(heap))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(tasks):
    tasks = sorted(tasks)  # (d, p)
    heap = []
    for d, p in tasks:
        heapq.heappush(heap, p)
        if len(heap) > d:
            heapq.heappop(heap)
    return str(sum(heap))

random.seed(88)

test_data = []

# 샘플 3개 (problem.md 예시와 일치)
test_data.append([(1, 10), (2, 20), (2, 5), (3, 30)])  # ans 60
test_data.append([(1, 50), (1, 10), (2, 20), (2, 100), (3, 30)])  # ans 180
test_data.append([(5, 999)])  # ans 999

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 7)

    tasks = []

    if mode == 1:
        # 완전 랜덤
        for _ in range(n):
            d = random.randint(1, 200)
            p = random.randint(1, 10**4)
            tasks.append((d, p))

    elif mode == 2:
        # 마감일이 작은 과제 많음
        for _ in range(n):
            d = random.choices([1, 2, 3, 5, 10, 200], weights=[40, 25, 15, 10, 5, 5])[0]
            p = random.randint(1, 10**4)
            tasks.append((d, p))

    elif mode == 3:
        # 점수가 큰 과제 몇 개 섞기
        for _ in range(n):
            d = random.randint(1, 200)
            p = random.choice([random.randint(1, 1000), random.randint(5000, 10**6)])
            tasks.append((d, p))

    elif mode == 4:
        # 마감일이 모두 같음 (선택이 점수 상위로 결정됨)
        d0 = random.randint(1, 200)
        for _ in range(n):
            p = random.randint(1, 10**6)
            tasks.append((d0, p))

    elif mode == 5:
        # 마감일이 1~n 범위로 촘촘 (선택 과정 확인용)
        for _ in range(n):
            d = random.randint(1, min(200, n))
            p = random.randint(1, 10**5)
            tasks.append((d, p))

    elif mode == 6:
        # 작은 점수 위주 + 가끔 큰 점수
        for _ in range(n):
            d = random.randint(1, 200)
            p = random.choices(
                [random.randint(1, 200), random.randint(10000, 10**6)],
                weights=[85, 15]
            )[0]
            tasks.append((d, p))

    else:
        # 랜덤 + 중복 deadline 다수
        deadlines = [random.randint(1, 20) for _ in range(random.randint(1, 6))]
        for _ in range(n):
            d = random.choice(deadlines)
            p = random.randint(1, 10**6)
            tasks.append((d, p))

    test_data.append(tasks)

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, tasks in enumerate(test_data, 1):
    n = len(tasks)
    lines = [str(n)]
    for d, p in tasks:
        lines.append(f"{d} {p}")
    input_str = "\n".join(lines) + "\n"
    ans = solve_internal(tasks)

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P88' 문제 생성이 완료되었습니다.")
