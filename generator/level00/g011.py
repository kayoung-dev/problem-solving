import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P011")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "서아의 푸드트럭 정산"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Loop"]
---

## description
푸드트럭을 운영하는 서아는 오늘 판매한 주문들을 정산하려고 합니다.<br/>
메뉴는 1번부터 N번까지 번호가 붙어 있고, 각 메뉴의 가격이 정해져 있습니다.<br/>
손님들이 주문한 메뉴 번호들이 주어질 때, 서아가 받아야 할 총 결제 금액을 계산하는 프로그램을 작성하세요.

## input_description
- 첫째 줄에 메뉴 개수 N이 주어집니다. ($1 \\le N \\le 100$)
- 둘째 줄에 N개의 정수(각 메뉴의 가격)가 공백으로 구분되어 주어집니다.
- 셋째 줄에 주문 횟수 M이 주어집니다. ($1 \\le M \\le 1000$)
- 넷째 줄에 M개의 정수(주문한 메뉴 번호)가 공백으로 구분되어 주어집니다.

## output_description
- 총 결제 금액을 출력합니다.

# samples

### input 1
{TICK}
5
1000 2500 1500 3000 500
4
1 3 5 2
{TICK}

### output 1
{TICK}
5500
{TICK}


### input 2
{TICK}
3
200 300 400
5
2 2 2 1 3
{TICK}

### output 2
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

    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)

print("✅ 'Level00/P011' 생성이 완료되었습니다.")
