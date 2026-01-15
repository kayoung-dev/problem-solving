import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P11")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 서아의 푸드트럭 정산 (Food Truck)

## 문제 설명
푸드트럭을 운영하는 서아는 오늘 판매한 주문들을 정산하려고 합니다.
메뉴는 1번부터 N번까지 번호가 붙어 있고, 각 메뉴의 가격이 정해져 있습니다.

손님들이 주문한 메뉴 번호들이 주어질 때,
서아가 받아야 할 총 결제 금액을 계산하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 메뉴 개수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수(각 메뉴의 가격)가 공백으로 구분되어 주어집니다.
- 셋째 줄에 주문 횟수 M이 주어집니다. (1 ≤ M ≤ 1000)
- 넷째 줄에 M개의 정수(주문한 메뉴 번호)가 공백으로 구분되어 주어집니다.

## 출력 형식 (Output Format)
- 총 결제 금액을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1

입력
{TICK}
5
1000 2500 1500 3000 500
4
1 3 5 2
{TICK}

출력
{TICK}
5500
{TICK}

---

### 예시 2

입력
{TICK}
3
200 300 400
5
2 2 2 1 3
{TICK}

출력
{TICK}
1700
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        n = int(input().strip())
        prices = list(map(int, input().split()))
        m = int(input().strip())
        orders = list(map(int, input().split()))

        total = 0
        for o in orders[:m]:
            total += prices[o - 1]

        print(total)

    except EOFError:
        pass

if __name__ == "__main__":
    main()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 테스트 케이스 생성 (20개)
fixed_cases = [
    (5, [1000, 2500, 1500, 3000, 500], 4, [1, 3, 5, 2]),
    (3, [200, 300, 400], 5, [2, 2, 2, 1, 3]),
    (1, [999], 3, [1, 1, 1]),
    (4, [0, 0, 0, 0], 6, [1, 2, 3, 4, 4, 1]),
    (6, [100, 200, 300, 400, 500, 600], 5, [6, 5, 4, 3, 2]),
    (2, [12345, 54321], 7, [1, 2, 1, 2, 1, 2, 2]),
    (8, [10, 20, 30, 40, 50, 60, 70, 80], 8, [8, 7, 6, 5, 4, 3, 2, 1]),
    (5, [5000, 4000, 3000, 2000, 1000], 4, [5, 5, 5, 5]),
    (3, [1, 1, 1], 10, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]),
    (10, [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100], 3, [10, 1, 5]),
]

def calc_total(prices, orders):
    total = 0
    for o in orders:
        total += prices[o - 1]
    return total

for i in range(1, 21):
    if i <= len(fixed_cases):
        n, prices, m, orders = fixed_cases[i - 1]
    else:
        n = random.randint(1, 100)
        prices = [random.randint(0, 100000) for _ in range(n)]
        m = random.randint(1, 1000)
        orders = [random.randint(1, n) for _ in range(m)]

    input_str = (
        f"{n}\n"
        + " ".join(map(str, prices)) + "\n"
        + f"{m}\n"
        + " ".join(map(str, orders))
    )
    output_str = str(calc_total(prices, orders))

    save_file(os.path.join(base_dir, f"input_{i:02d}.txt"), input_str)
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), output_str)

print("✅ 'Easy/P11' 생성이 완료되었습니다.")
