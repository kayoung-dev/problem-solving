import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P83 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P83")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# K번째 큰 쿠키 찾기

## 문제 설명
제과사 **소연**은 서로 다른 크기의 쿠키들을 상자에 담아 선물하려고 합니다.  
소연은 “가장 큰 쿠키부터 세었을 때 $K$번째에 해당하는 쿠키”를 골라야 합니다.

길이가 $N$인 정수 배열 $A$가 주어질 때, 배열을 내림차순으로 정렬했을 때의 **$K$번째 큰 값**을 출력하세요.

- 예를 들어, $A=[3,1,5,2]$이고 $K=2$라면 내림차순 정렬은 $[5,3,2,1]$이므로 정답은 $3$입니다.
- 배열에는 **같은 값이 여러 번** 나올 수 있으며, 이 경우에도 **순서대로 세어야** 합니다.  
  예: $[5,5,3]$에서 $K=2$이면 정답은 $5$입니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N, K$가 공백으로 구분되어 주어집니다.  
  $(1 \\le K \\le N \\le 200)$
- 둘째 줄에 $N$개의 정수 $A_1, A_2, \\dots, A_N$이 공백으로 구분되어 주어집니다.  
  $(-10^9 \\le A_i \\le 10^9)$

## 출력 형식 (Output Format)
- 배열에서 **$K$번째 큰 값**을 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4 2
3 1 5 2
{TICK}
**Output:**
{TICK}
3
{TICK}
- 내림차순으로 정렬하면 $[5,3,2,1]$ 입니다.
- 큰 값부터 세어 $2$번째 값은 $3$입니다.

### 예시 2
**Input:**
{TICK}
5 4
5 5 3 2 2
{TICK}
**Output:**
{TICK}
2
{TICK}
- 내림차순 정렬은 $[5,5,3,2,2]$ 입니다.
- $4$번째 값은 $2$입니다. (중복도 그대로 순서대로 셉니다)

### 예시 3
**Input:**
{TICK}
1 1
-7
{TICK}
**Output:**
{TICK}
-7
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    first = input().split()
    if not first:
        return
    n = int(first[0])
    k = int(first[1])
    arr = list(map(int, input().split()))
    arr = arr[:n]

    arr.sort(reverse=True)
    sys.stdout.write(str(arr[k - 1]))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(n, k, arr):
    arr_sorted = sorted(arr, reverse=True)
    return str(arr_sorted[k - 1])

random.seed(83)

test_data = []

# 샘플 3개를 1~3번 케이스로 고정 (problem.md 예시와 일치)
sample1 = (4, 2, [3, 1, 5, 2])
sample2 = (5, 4, [5, 5, 3, 2, 2])
sample3 = (1, 1, [-7])
test_data.extend([sample1, sample2, sample3])

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    k = random.randint(1, n)
    mode = random.randint(1, 7)

    if mode == 1:
        # 완전 랜덤 (중복 가능)
        arr = [random.randint(-50, 50) for _ in range(n)]

    elif mode == 2:
        # 큰 범위 랜덤
        arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    elif mode == 3:
        # 중복이 매우 많음
        pool = [random.randint(-10, 10) for _ in range(random.randint(1, 5))]
        arr = [random.choice(pool) for _ in range(n)]

    elif mode == 4:
        # 이미 정렬된(내림차순) 상태
        arr = sorted([random.randint(-1000, 1000) for _ in range(n)], reverse=True)

    elif mode == 5:
        # 이미 정렬된(오름차순) 상태
        arr = sorted([random.randint(-1000, 1000) for _ in range(n)])

    elif mode == 6:
        # 거의 정렬된 상태(약간만 섞기)
        arr = sorted([random.randint(-1000, 1000) for _ in range(n)], reverse=True)
        swaps = random.randint(0, min(30, n))
        for _ in range(swaps):
            i = random.randrange(n)
            j = random.randrange(n)
            arr[i], arr[j] = arr[j], arr[i]

    else:
        # 극단값 섞기
        arr = []
        for _ in range(n):
            arr.append(random.choice([-(10**9), 10**9, random.randint(-100, 100)]))

    test_data.append((n, k, arr))

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
for i, (n, k, arr) in enumerate(test_data, 1):
    input_str = f"{n} {k}\n" + " ".join(map(str, arr)) + "\n"
    ans = solve_internal(n, k, arr)

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P83' 문제 생성이 완료되었습니다.")
