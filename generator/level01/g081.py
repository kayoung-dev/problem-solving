import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P081 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P081")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 세 가지 물감 정리

## 문제 설명
화가 **하린**은 작업실에서 물감 튜브를 정리하려고 합니다.  
튜브는 세 가지 색 중 하나로 표시되어 있습니다.

- $0$ : 빨강
- $1$ : 파랑
- $2$ : 노랑

하린은 모든 튜브를 **오름차순(0, 1, 2)** 으로 정렬한 결과를 출력하려고 합니다.

길이가 $N$인 배열 $A$가 주어질 때, 정렬된 배열을 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 둘째 줄에 $N$개의 정수 $A_1, A_2, \\dots, A_N$이 공백으로 구분되어 주어집니다.  
  각 원소는 $0$, $1$, $2$ 중 하나입니다.

## 출력 형식 (Output Format)
- 배열을 오름차순으로 정렬한 뒤, $N$개의 정수를 공백으로 구분해 한 줄에 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
2 0 2 1 1 0
{TICK}
**Output:**
{TICK}
0 0 1 1 2 2
{TICK}
- $0$이 2개, $1$이 2개, $2$가 2개이므로 정렬 결과는 $0,0,1,1,2,2$ 입니다.
- 출력은 정렬된 배열을 공백으로 구분해 한 줄로 출력합니다.

### 예시 2
**Input:**
{TICK}
5
2 2 1 0 2
{TICK}
**Output:**
{TICK}
0 1 2 2 2
{TICK}
- 가장 작은 값은 $0$이므로 맨 앞에 옵니다.
- 그 다음 $1$, 마지막으로 $2$들이 이어집니다.

### 예시 3
**Input:**
{TICK}
1
1
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
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))
    # 혹시 n과 길이가 다를 수 있으니 안전하게 처리 (코테 환경에서 가끔 발생)
    arr = arr[:n]

    cnt0 = cnt1 = cnt2 = 0
    for x in arr:
        if x == 0:
            cnt0 += 1
        elif x == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    out = ([0] * cnt0) + ([1] * cnt1) + ([2] * cnt2)
    sys.stdout.write(" ".join(map(str, out)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(arr):
    # 정렬 결과 문자열 반환
    arr_sorted = sorted(arr)
    return " ".join(map(str, arr_sorted))

random.seed(81)

test_data = []

# 샘플 3개를 1~3번 케이스로 고정 (problem.md 예시와 일치)
samples = [
    [2, 0, 2, 1, 1, 0],
    [2, 2, 1, 0, 2],
    [1],
]
for s in samples:
    test_data.append(s)

# 나머지 17개 랜덤 생성 (총 20개)
# - 너무 단조롭지 않게: 길이/분포 다양화
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 5)

    if mode == 1:
        # 균등 분포
        arr = [random.randint(0, 2) for _ in range(n)]
    elif mode == 2:
        # 0이 많은 케이스
        arr = [random.choices([0, 1, 2], weights=[70, 20, 10])[0] for _ in range(n)]
    elif mode == 3:
        # 2가 많은 케이스
        arr = [random.choices([0, 1, 2], weights=[10, 20, 70])[0] for _ in range(n)]
    elif mode == 4:
        # 한 값만 반복
        v = random.randint(0, 2)
        arr = [v] * n
    else:
        # 이미 거의 정렬된 케이스(조금만 섞기)
        arr = sorted([random.randint(0, 2) for _ in range(n)])
        swaps = random.randint(0, min(20, n))
        for _ in range(swaps):
            i = random.randrange(n)
            j = random.randrange(n)
            arr[i], arr[j] = arr[j], arr[i]

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

print(f"✅ 'Level01/P081' 문제 생성이 완료되었습니다. ")
