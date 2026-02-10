import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P090 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P090")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = """# 보조 배터리로 드론 작업 최대화

## 문제 설명
도시 정비팀 **다은**은 여러 수리 작업을 드론에게 배정하려고 합니다.

- 작업은 `필요 출력`을 가지며, 배열 `tasks[i]`로 주어집니다.
- 드론은 `기본 출력`을 가지며, 배열 `workers[j]`로 주어집니다.
- 드론은 작업 하나만 맡을 수 있고, 작업도 드론 하나에만 배정됩니다.
- 드론이 작업을 수행하려면 `workers[j] >= tasks[i]` 를 만족해야 합니다.

다은은 드론 출력이 부족할 때 사용할 수 있는 **보조 배터리**를 `pills`개 가지고 있습니다.

- 보조 배터리를 받은 드론은 출력이 `strength`만큼 증가합니다.
- 보조 배터리는 드론 한 대당 최대 1개만 사용할 수 있습니다.

완료할 수 있는 작업의 **최대 개수**를 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 `n m pills strength`가 공백으로 구분되어 주어집니다.
  - `n`은 작업 개수, `m`은 드론 개수입니다.
- 둘째 줄에 `n`개의 정수 `tasks`가 공백으로 구분되어 주어집니다.
- 셋째 줄에 `m`개의 정수 `workers`가 공백으로 구분되어 주어집니다.

---

## 출력 형식 (Output Format)
- 완료할 수 있는 작업의 최대 개수를 출력하세요.

---

## 제한 사항
- `1 <= n, m <= 50000`
- `0 <= pills <= m`
- `0 <= tasks[i], workers[j], strength <= 10^9`

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 3 1 1
3 2 1
0 3 3
{TICK}
**Output:**
{TICK}
3
{TICK}
- 출력 0인 드론은 보조 배터리를 사용하면 출력이 1이 되어 작업(필요 출력 1)을 수행할 수 있습니다.
- 나머지 드론(출력 3, 3)이 작업(2, 3)을 수행하여 총 3개를 완료합니다.

### 예시 2
**Input:**
{TICK}
2 3 1 5
5 4
0 0 0
{TICK}
**Output:**
{TICK}
1
{TICK}
- 보조 배터리를 사용한 드론 한 대만 출력 5가 되어 작업(필요 출력 5) 하나만 수행할 수 있습니다.

### 예시 3
**Input:**
{TICK}
3 5 3 10
10 15 30
0 10 10 10 10
{TICK}
**Output:**
{TICK}
2
{TICK}
""".format(TICK=TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
#    - 정렬 + 이분탐색 + 덱(deque) 기반 검증
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def can(k, tasks, workers, pills, strength):
    if k == 0:
        return True

    # 쉬운 작업 k개, 강한 드론 k명만 고려
    t = tasks[:k]                  # 오름차순
    w = workers[len(workers)-k:]   # 오름차순 (강한 k명)

    dq = deque()  # 후보 드론 출력들을 오름차순으로 유지
    j = k - 1     # w의 끝(가장 강한)부터 내려오며 추가
    p = pills

    # 어려운 작업부터 처리
    for i in range(k - 1, -1, -1):
        need = t[i]

        # 보조 배터리를 쓰면 가능한 드론(need <= w[j] + strength)을 후보에 추가
        while j >= 0 and w[j] + strength >= need:
            # w는 오름차순, j는 감소 => 큰 값 -> 작은 값 순으로 들어옴
            # appendleft 하면 dq는 오름차순 유지 (left=작은, right=큰)
            dq.appendleft(w[j])
            j -= 1

        if not dq:
            return False

        # 배터리 없이 가능한 드론이 있으면(가장 큰 값이 need 이상) 우선 사용
        if dq[-1] >= need:
            dq.pop()
        else:
            # 배터리 사용: 가장 작은 후보에게 배터리를 주는 게 낭비가 적음
            if p == 0:
                return False
            dq.popleft()
            p -= 1

    return True

def solve():
    input = sys.stdin.readline
    first = input().split()
    if not first:
        return
    n, m, pills, strength = map(int, first)
    tasks = list(map(int, input().split()))[:n]
    workers = list(map(int, input().split()))[:m]

    tasks.sort()
    workers.sort()

    lo, hi = 0, min(n, m)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid, tasks, workers, pills, strength):
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이(테스트케이스 정답 생성용)
# ---------------------------------------------------------
def can_internal(k, tasks, workers, pills, strength):
    if k == 0:
        return True
    t = tasks[:k]
    w = workers[len(workers)-k:]
    dq = deque()
    j = k - 1
    p = pills
    for i in range(k - 1, -1, -1):
        need = t[i]
        while j >= 0 and w[j] + strength >= need:
            dq.appendleft(w[j])
            j -= 1
        if not dq:
            return False
        if dq[-1] >= need:
            dq.pop()
        else:
            if p == 0:
                return False
            dq.popleft()
            p -= 1
    return True

def solve_internal(n, m, pills, strength, tasks, workers):
    tasks = sorted(tasks)
    workers = sorted(workers)
    lo, hi = 0, min(n, m)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_internal(mid, tasks, workers, pills, strength):
            lo = mid
        else:
            hi = mid - 1
    return str(lo)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(90)

test_data = []

# 샘플 3개 (문제 예시와 동일)
test_data.append((3, 3, 1, 1, [3, 2, 1], [0, 3, 3]))                 # ans 3
test_data.append((2, 3, 1, 5, [5, 4], [0, 0, 0]))                    # ans 1
test_data.append((3, 5, 3, 10, [10, 15, 30], [0, 10, 10, 10, 10]))   # ans 2

def gen_case(mode):
    n = random.randint(1, 300)
    m = random.randint(1, 300)
    pills = random.randint(0, m)
    strength = random.randint(0, 50)

    if mode == 1:
        # 일반 랜덤(중간 범위)
        tasks = [random.randint(0, 100) for _ in range(n)]
        workers = [random.randint(0, 100) for _ in range(m)]

    elif mode == 2:
        # workers가 약함 + strength로만 커버
        tasks = [random.randint(30, 120) for _ in range(n)]
        workers = [random.randint(0, 50) for _ in range(m)]
        strength = random.randint(30, 80)

    elif mode == 3:
        # pills 거의 없음
        pills = random.randint(0, min(3, m))
        tasks = [random.randint(0, 200) for _ in range(n)]
        workers = [random.randint(0, 200) for _ in range(m)]
        strength = random.randint(0, 50)

    elif mode == 4:
        # strength = 0 (배터리 효과 없음)
        strength = 0
        tasks = [random.randint(0, 200) for _ in range(n)]
        workers = [random.randint(0, 200) for _ in range(m)]

    elif mode == 5:
        # tasks가 0이 많음
        tasks = [random.choices([0, random.randint(1, 200)], weights=[70, 30])[0] for _ in range(n)]
        workers = [random.randint(0, 50) for _ in range(m)]
        strength = random.randint(0, 30)

    elif mode == 6:
        # workers가 0 많음
        tasks = [random.randint(0, 80) for _ in range(n)]
        workers = [random.choices([0, random.randint(1, 80)], weights=[70, 30])[0] for _ in range(m)]
        strength = random.randint(0, 80)

    else:
        # 큰 값 섞기
        tasks = [random.choice([random.randint(0, 100), random.randint(10**6, 10**7)]) for _ in range(n)]
        workers = [random.choice([random.randint(0, 100), random.randint(10**6, 10**7)]) for _ in range(m)]
        strength = random.randint(0, 10**6)

    return n, m, pills, strength, tasks, workers

for _ in range(17):
    mode = random.randint(1, 7)
    test_data.append(gen_case(mode))

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, (n, m, pills, strength, tasks, workers) in enumerate(test_data, 1):
    input_str = (
        f"{n} {m} {pills} {strength}\n"
        + " ".join(map(str, tasks)) + "\n"
        + " ".join(map(str, workers)) + "\n"
    )
    ans = solve_internal(n, m, pills, strength, tasks, workers)

    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P090' 문제 생성이 완료되었습니다. ")
