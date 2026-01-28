import os
import random
from bisect import bisect_left

TICK = "`" * 3

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P109 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P109")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# ---------------------------------------------------------
# 2. 내부 풀이 로직 (테스트 정답 생성용)
# ---------------------------------------------------------
def solve_internal(arr1, arr2):
    b = sorted(set(arr2))
    INF = 10**15

    # dp[last_value] = 최소 수정 횟수
    dp = {-(10**18): 0}

    for a in arr1:
        ndp = {}

        for prev, cost in dp.items():
            # 1) 그대로 사용
            if a > prev:
                ndp[a] = min(ndp.get(a, INF), cost)

            # 2) 수정해서 후보 점수로 교체 (단, 원래 기록보다 낮출 수 없음)
            #    또한 "앞 단계보다 커야" 하므로 prev보다도 커야 함
            need = max(a, prev + 1)
            k = bisect_left(b, need)
            if k < len(b):
                x = b[k]
                ndp[x] = min(ndp.get(x, INF), cost + 1)

        if not ndp:
            return "-1"

        # 지배 상태 제거:
        # 마지막 값이 더 큰데 수정 횟수도 더 크거나 같으면 의미 없음
        items = sorted(ndp.items())  # (last_value, cost)
        pruned = {}
        best = INF
        for v, c in items:
            if c < best:
                pruned[v] = c
                best = c
        dp = pruned

    return str(min(dp.values()))


# ---------------------------------------------------------
# 3. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 점수 로그 복구

## 문제 설명
한 자동 채점 시스템은 시험을 여러 단계로 채점합니다.  
정상적인 기록이라면, 단계가 진행될수록 점수는 **앞 단계보다 항상 더 큰 값**이 됩니다.

하지만 기록 오류로 인해, 일부 단계의 점수가 잘못 저장되었습니다.  
시스템은 오류를 수정하기 위해 **정상 후보 점수 목록**을 가지고 있습니다.

- 현재 기록된 점수 로그: $A = [a_1, a_2, \\dots, a_N]$
- 후보 점수 목록: $B = [b_1, b_2, \\dots, b_M]$

한 번의 수정 작업에서는 어떤 단계 $i$를 골라, 점수 $a_i$를 후보 점수 중 하나로 바꿀 수 있습니다.

$a_i \\leftarrow b_j$

단, 기록 보존 규칙 때문에 **수정 후 점수는 원래 기록보다 낮아질 수 없습니다.**  
즉, 수정한다면 반드시 다음을 만족해야 합니다.

$b_j \\ge a_i$

목표는 점수 로그가 모든 단계에서 다음 조건을 만족하도록 만드는 것입니다.

$a_1 < a_2 < \\cdots < a_N$

점수 로그를 이 조건에 맞게 만들기 위한 **최소 수정 횟수**를 구하세요.  
만약 어떤 방법으로도 만들 수 없다면 **-1**을 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 점수 로그 개수가 정수 $N$으로 주어집니다. 
- $1 \le N \le 2000$
- 둘째 줄에 $N$개의 정수 $a_1, a_2, \dots, a_N$이 공백으로 주어집니다. ($a_i$는 $i$번째 단계의 현재 점수)
- 셋째 줄에 후보 점수 개수가 정수 $M$으로 주어집니다.
- $1 \le M \le 2000$
- 넷째 줄에 $M$개의 정수 $b_1, b_2, \dots, b_M$이 공백으로 주어집니다. ($b_j$는 후보 점수)
- $1 \le a_i, b_j \le 10^9$
---

## 출력 형식 (Output Format)
- 최소 수정 횟수를 출력합니다.
- 이미 모든 단계에서 점수가 계속 증가한다면, 수정이 필요없으므로 0을 출력합니다.
- 불가능하면 -1을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
3 3 5 4
3
4 6 7
{TICK}

**Output:**
{TICK}
2
{TICK}

- 현재 로그: $[3, 3, 5, 4]$  
  목표는 **앞 단계보다 항상 더 큰 점수**가 되도록 만드는 것입니다.
- 2번째 단계에서 $3$은 바로 앞의 $3$보다 크지 않으므로 규칙이 깨집니다.
  - 후보 점수 중에서 **원래 점수보다 낮아지지 않으면서**($\\ge 3$) 앞 단계보다 큰 값이 필요합니다.
  - 후보에서 $4$를 선택해 2번째 점수를 $4$로 바꾸면 $[3, 4, 5, 4]$가 됩니다. (수정 1회)
- 이제 마지막 단계에서 $4$는 앞의 $5$보다 크지 않으므로 다시 규칙이 깨집니다.
  - 후보에서 $6$을 선택해 마지막 점수를 $6$으로 바꾸면 $[3, 4, 5, 6]$이 됩니다. (수정 2회)
- 모든 단계가 계속 커지므로 최소 수정 횟수는 **2**입니다.

---

### 예시 2
**Input:**
{TICK}
7
1 2 2 2 2 4 10
4
3 5 6 7
{TICK}

**Output:**
{TICK}
4
{TICK}

- 현재 로그에서 3~5번째 값이 모두 2라서, 앞 단계보다 계속 커지게 만들려면 **연속으로 여러 번 수정**이 필요합니다.
- 3번째를 3으로 바꾸면: $[1, 2, 3, 2, 2, 4, 10]$ (1회)
- 4번째는 3보다 커야 하므로 5로 바꾸면: $[1, 2, 3, 5, 2, 4, 10]$ (2회)
- 5번째는 5보다 커야 하므로 6으로 바꾸면: $[1, 2, 3, 5, 6, 4, 10]$ (3회)
- 6번째는 6보다 커야 하므로 7로 바꾸면: $[1, 2, 3, 5, 6, 7, 10]$ (4회)
- 이제 모든 단계에서 점수가 계속 커지므로 최소 수정 횟수는 **4**입니다.

---

### 예시 3
**Input:**
{TICK}
3
5 4 3
4
4 4 4 5
{TICK}

**Output:**
{TICK}
-1
{TICK}

---

## 힌트(Note)
후보 점수 목록을 정렬해 두면, 어떤 값 이상인 후보 점수 중에서 **가장 작은 값**을 빠르게 고를 수 있습니다.  
각 단계에서 “그대로 둘지 / 후보 점수로 바꿀지”를 비교하며, 전체 수정 횟수가 최소가 되도록 선택해 보세요.
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)


# ---------------------------------------------------------
# 4. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    arr1 = list(map(int, input().split()))
    m = int(input().strip())
    arr2 = list(map(int, input().split()))

    b = sorted(set(arr2))
    INF = 10**15

    dp = {-(10**18): 0}

    for a in arr1:
        ndp = {}

        for prev, cost in dp.items():
            # 1) 그대로 사용
            if a > prev:
                old = ndp.get(a, INF)
                if cost < old:
                    ndp[a] = cost

            # 2) 수정해서 후보 점수로 교체 (수정 후 점수는 낮아지면 안 됨)
            need = max(a, prev + 1)
            k = bisect_left(b, need)
            if k < len(b):
                x = b[k]
                old = ndp.get(x, INF)
                if cost + 1 < old:
                    ndp[x] = cost + 1

        if not ndp:
            print(-1)
            return

        # 지배 상태 제거
        items = sorted(ndp.items())
        pruned = {}
        best = INF
        for v, c in items:
            if c < best:
                pruned[v] = c
                best = c
        dp = pruned

    print(min(dp.values()))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)


# ---------------------------------------------------------
# 5. 테스트 케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(109)

def write_case(idx, a, b):
    input_str = (
        f"{len(a)}\n"
        f"{' '.join(map(str, a))}\n"
        f"{len(b)}\n"
        f"{' '.join(map(str, b))}\n"
    )
    ans = solve_internal(a, b)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")


def make_solvable_case(n, m, vmax=50):
    # 1) 증가하는 "정상 로그"를 먼저 만든 뒤
    # 2) 일부 값을 낮춰(오류) arr1을 만든다 (수정은 올리는 방식으로 복구 가능)
    base = []
    cur = random.randint(1, max(2, vmax // 5))
    for _ in range(n):
        cur += random.randint(1, max(1, vmax // 10))
        base.append(cur)

    arr1 = base[:]
    for i in range(n):
        if random.random() < 0.35:
            # 오류: 낮아짐 (단, 1 이상)
            arr1[i] = max(1, arr1[i] - random.randint(1, max(1, vmax // 4)))

    # 후보는 base 주변 + 추가 값들
    candidates = set()
    for _ in range(m):
        pick = random.choice(base)
        candidates.add(max(1, pick + random.randint(-vmax // 6, vmax // 3)))
    # 그래도 충분히 큰 값이 있게
    candidates.add(base[-1] + random.randint(1, vmax))
    arr2 = list(candidates)

    return arr1, arr2


def make_hard_or_impossible_case(n, m, vmax=30):
    # 후보가 너무 작거나 제한적이어서 불가능이 자주 나오게
    arr1 = [random.randint(1, vmax) for _ in range(n)]
    # 후보는 작은 범위에 몰기
    arr2 = [random.randint(1, max(2, vmax // 3)) for _ in range(m)]
    return arr1, arr2


test_cases = []

# 1) 예시1
test_cases.append(([3, 3, 5, 4], [4, 6, 7]))
# 2) 예시2
test_cases.append(([1, 2, 4, 8, 9], [3, 5, 6, 10]))
# 3) 예시3
test_cases.append(([5, 4, 3], [4, 4, 4, 5]))

# 4) 이미 증가 + 후보 무관
test_cases.append(([2, 5, 9, 12], [1, 3, 7]))

# 5) 전부 같은 값 (대개 후보로 올려야 함)
test_cases.append(([4, 4, 4, 4], [4, 5, 6, 7, 8]))

# 6) 후보가 너무 작아 불가능
test_cases.append(([10, 10, 10], [1, 2, 3]))

# 7) 작은 solvable
test_cases.append(make_solvable_case(6, 10, vmax=40))

# 8~13) solvable 랜덤
for _ in range(6):
    n = random.randint(8, 30)
    m = random.randint(10, 40)
    test_cases.append(make_solvable_case(n, m, vmax=80))

# 14~16) 불가능/어려운 랜덤
for _ in range(3):
    n = random.randint(10, 40)
    m = random.randint(5, 20)
    test_cases.append(make_hard_or_impossible_case(n, m, vmax=40))

# 17~19) 중간 성능 (너무 무겁지 않게)
for n in [120, 200, 350]:
    m = n
    test_cases.append(make_solvable_case(n, m, vmax=300))

# 20) 큰 값 범위 랜덤 (혼합)
a = [random.randint(1, 10**9) for _ in range(180)]
b = [random.randint(1, 10**9) for _ in range(220)]
test_cases.append((a, b))

# 저장 (20개 보장)
test_cases = test_cases[:20]
for i, (a, b) in enumerate(test_cases, 1):
    write_case(i, a, b)

print("✅ 'Level01/P109' 문제 생성이 완료되었습니다.")