import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P084 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P084")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 택배 상자 높이 정렬

## 문제 설명
택배 기사 **준호**는 창고 선반에 상자를 정리하려고 합니다.  
상자마다 **높이**가 다르며, 준호는 상자를 **낮은 것부터 높은 것까지** 정렬해 순서대로 놓으려고 합니다.

길이가 $N$인 정수 배열 $H$가 주어질 때, $H$를 **오름차순**으로 정렬한 결과를 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 둘째 줄에 $N$개의 정수 $H_1, H_2, \\dots, H_N$이 공백으로 구분되어 주어집니다.  
  $(1 \\le H_i \\le 10^9)$

## 출력 형식 (Output Format)
- 상자 높이를 오름차순으로 정렬한 뒤, $N$개의 정수를 공백으로 구분해 한 줄에 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
5 2 9 1 5 6
{TICK}
**Output:**
{TICK}
1 2 5 5 6 9
{TICK}
- 가장 낮은 높이부터 정렬하면 $1,2,5,5,6,9$ 순서가 됩니다.
- 같은 높이($5$)는 여러 번 등장해도 그대로 모두 출력합니다.

### 예시 2
**Input:**
{TICK}
4
10 3 7 3
{TICK}
**Output:**
{TICK}
3 3 7 10
{TICK}
- $3$이 두 개 있으므로 정렬 결과의 앞부분에 $3,3$이 연속으로 출력됩니다.

### 예시 3
**Input:**
{TICK}
1
42
{TICK}
**Output:**
{TICK}
42
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
    arr = list(map(int, input().split()))
    arr = arr[:n]

    arr.sort()
    sys.stdout.write(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(arr):
    return " ".join(map(str, sorted(arr)))

random.seed(84)

test_data = []

# 샘플 3개를 1~3번 케이스로 고정 (problem.md 예시와 일치)
samples = [
    [5, 2, 9, 1, 5, 6],
    [10, 3, 7, 3],
    [42],
]
test_data.extend(samples)

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 7)

    if mode == 1:
        # 완전 랜덤
        arr = [random.randint(1, 100) for _ in range(n)]

    elif mode == 2:
        # 큰 범위 랜덤
        arr = [random.randint(1, 10**9) for _ in range(n)]

    elif mode == 3:
        # 중복이 매우 많음
        pool = [random.randint(1, 20) for _ in range(random.randint(1, 5))]
        arr = [random.choice(pool) for _ in range(n)]

    elif mode == 4:
        # 이미 정렬된 오름차순
        arr = sorted([random.randint(1, 1000) for _ in range(n)])

    elif mode == 5:
        # 이미 정렬된 내림차순
        arr = sorted([random.randint(1, 1000) for _ in range(n)], reverse=True)

    elif mode == 6:
        # 거의 정렬된(약간만 섞기)
        arr = sorted([random.randint(1, 1000) for _ in range(n)])
        swaps = random.randint(0, min(30, n))
        for _ in range(swaps):
            i = random.randrange(n)
            j = random.randrange(n)
            arr[i], arr[j] = arr[j], arr[i]

    else:
        # 극단값 섞기
        arr = [random.choice([1, 10**9, random.randint(2, 1000)]) for _ in range(n)]

    test_data.append(arr)

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
for i, arr in enumerate(test_data, 1):
    n = len(arr)
    input_str = f"{n}\n" + " ".join(map(str, arr)) + "\n"
    ans = solve_internal(arr)

    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P084' 문제 생성이 완료되었습니다. ")
