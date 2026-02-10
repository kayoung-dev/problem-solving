import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P089 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P089")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = """# 할인 쿠폰 최적 적용

## 문제 설명
점장 **라라**는 손님들에게 줄 할인 쿠폰을 정리하고 있습니다.

- 상품은 $N$개이고, 각 상품의 가격 배열 $P$가 주어집니다.
- 쿠폰도 $N$장이고, 각 쿠폰의 할인 금액 배열 $C$가 주어집니다.
- 각 상품에는 쿠폰을 **정확히 1장**씩 적용해야 합니다. (모든 쿠폰도 정확히 1번 사용)

쿠폰을 적용한 뒤 상품의 최종 가격은 `가격 - 할인금액` 입니다.  
단, 최종 가격은 음수가 될 수 없으므로 `0`보다 작아지면 `0`으로 처리합니다.

라라는 **전체 최종 가격의 합을 최소**로 만들고 싶습니다.  
전체 최종 가격의 합 중 최솟값을 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 둘째 줄에 $N$개의 정수 $P_1, P_2, \\dots, P_N$이 공백으로 구분되어 주어집니다.  
  $(0 \\le P_i \\le 10^9)$
- 셋째 줄에 $N$개의 정수 $C_1, C_2, \\dots, C_N$이 공백으로 구분되어 주어집니다.  
  $(0 \\le C_i \\le 10^9)$

## 출력 형식 (Output Format)
- 가능한 전체 최종 가격 합의 최솟값을 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
100 50 80 10
30 60 20 10
{TICK}
**Output:**
{TICK}
120
{TICK}
- 가격은 큰 것부터, 쿠폰은 큰 것부터 매칭하면 총합을 최소로 만들 수 있습니다.
- (100-60) + (80-30) + (50-20) + (10-10) = 40 + 50 + 30 + 0 = 120

### 예시 2
**Input:**
{TICK}
3
5 3 2
10 1 1
{TICK}
**Output:**
{TICK}
3
{TICK}
- (5-10)은 0으로 처리됩니다.
- 최솟값은 (5-10) + (3-1) +(2-1) = 3 

### 예시 3
**Input:**
{TICK}
1
0
999
{TICK}
**Output:**
{TICK}
0
{TICK}
""".format(TICK=TICK)

problem_md = problem_md.replace("\n1\n", "\n3\n", 1)

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

    prices = list(map(int, input().split()))[:n]
    coupons = list(map(int, input().split()))[:n]

    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    total = 0
    for p, c in zip(prices, coupons):
        v = p - c
        if v > 0:
            total += v
    print(total)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(prices, coupons):
    prices = sorted(prices, reverse=True)
    coupons = sorted(coupons, reverse=True)
    total = 0
    for p, c in zip(prices, coupons):
        if p > c:
            total += (p - c)
    return str(total)

random.seed(89)

test_data = []

# 샘플 3개 (예시와 일치하도록 고정)
test_data.append(([100, 50, 80, 10], [30, 60, 20, 10]))  # ans 120
test_data.append(([5, 3, 2], [10, 1, 1]))                 # ans 3
test_data.append(([0], [999]))                            # ans 0

# 나머지 17개 랜덤 생성 (총 20개)
for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 7)

    if mode == 1:
        # 완전 랜덤
        prices = [random.randint(0, 1000) for _ in range(n)]
        coupons = [random.randint(0, 1000) for _ in range(n)]

    elif mode == 2:
        # 큰 범위 랜덤
        prices = [random.randint(0, 10**9) for _ in range(n)]
        coupons = [random.randint(0, 10**9) for _ in range(n)]

    elif mode == 3:
        # 쿠폰이 전반적으로 큼(0 많이 나올 것)
        prices = [random.randint(0, 1000) for _ in range(n)]
        coupons = [random.randint(500, 2000) for _ in range(n)]

    elif mode == 4:
        # 가격이 전반적으로 큼(양수 많이 나올 것)
        prices = [random.randint(500, 2000) for _ in range(n)]
        coupons = [random.randint(0, 1000) for _ in range(n)]

    elif mode == 5:
        # 중복 많음
        p_pool = [random.randint(0, 200) for _ in range(random.randint(1, 5))]
        c_pool = [random.randint(0, 200) for _ in range(random.randint(1, 5))]
        prices = [random.choice(p_pool) for _ in range(n)]
        coupons = [random.choice(c_pool) for _ in range(n)]

    elif mode == 6:
        # 모두 0 섞기
        prices = [random.choices([0, random.randint(1, 1000)], weights=[60, 40])[0] for _ in range(n)]
        coupons = [random.choices([0, random.randint(1, 1000)], weights=[60, 40])[0] for _ in range(n)]

    else:
        # 극단값 섞기
        prices = [random.choice([0, 10**9, random.randint(1, 1000)]) for _ in range(n)]
        coupons = [random.choice([0, 10**9, random.randint(1, 1000)]) for _ in range(n)]

    test_data.append((prices, coupons))

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, (prices, coupons) in enumerate(test_data, 1):
    n = len(prices)
    input_str = f"{n}\n" + " ".join(map(str, prices)) + "\n" + " ".join(map(str, coupons)) + "\n"
    ans = solve_internal(prices, coupons)

    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P089' 문제 생성이 완료되었습니다. ")
