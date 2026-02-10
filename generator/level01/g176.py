import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P176 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P176")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "도서관 사서의 책꽂이 나누기"
level: "1"
time_limit: 1000
memory_limit: 131072
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Binary Search", "Parametric Search"]
---

## description
도서관 사서 민수는 새로 들어온 $N$권의 책을 $K$개의 칸이 있는 책꽂이에 나누어 꽂으려 합니다. 
책들은 주제별로 분류되어 나열되어 있으며, **현재 나열된 순서를 절대 바꿀 수 없습니다.** 각 칸에는 반드시 **연속된 순서**의 책들만 꽂아야 합니다.

각 책은 고유한 두께 $W_i$를 가집니다. 민수는 $K$개의 칸 중 **가장 두꺼운 책 뭉치가 들어가는 칸의 두께(너비)**를 최소화하고 싶어 합니다. 

모든 책을 $K$개 이하의 칸에 나누어 꽂을 수 있는 **최소한의 칸 너비**를 구하는 프로그램을 작성하세요.



## input_description
- 첫 번째 줄에 책의 권수 $N$과 책꽂이 칸의 수 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le K \le N \le 100,000$
- 두 번째 줄에 $N$권의 책 두께 $W_i$가 순서대로 주어집니다. 
- $1 \le W_i \le 10,000$

## output_description
- 모든 책을 $K$개 이하의 칸에 나누어 담을 수 있는 최소 칸 너비를 정수로 출력합니다.

# samples

### input 1
{TICK}
5 2
1 2 3 4 5
{TICK}

### output 1
{TICK}
9
{TICK}
- [1, 2, 3] (합 6), [4, 5] (합 9)로 나누면 최대 너비가 9가 되어 2칸에 담을 수 있습니다. 
- 너비를 8로 줄이면 [1, 2, 3], [4], [5]로 3칸이 필요하게 되어 불가능합니다.

### input 2
{TICK}
7 3
10 20 30 40 50 60 70
{TICK}

### output 2
{TICK}
110
{TICK}
- [10, 20, 30, 40] (100), [50, 60] (110), [70] (70)으로 나누면 최대 너비 110으로 3칸 이내 배송 가능합니다.

### input 3
{TICK}
9 3
1 2 3 4 5 6 7 8 9
{TICK}

### output 3
{TICK}
17
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def can_split(weights, k, limit):
    # 주어진 limit 너비로 k개 이내의 칸에 담을 수 있는지 확인 (Greedy)
    count = 1
    current_sum = 0
    for w in weights:
        if current_sum + w > limit:
            count += 1
            current_sum = w
        else:
            current_sum += w
    return count <= k

def solve():
    # 대량의 데이터를 위해 sys.stdin.read() 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    weights = list(map(int, input_data[2:]))
    
    # 이진 탐색 범위 설정
    # low: 가장 두꺼운 책 한 권은 무조건 담아야 하므로 max(weights)
    # high: 모든 책을 한 칸에 다 담는 경우인 sum(weights)
    low = max(weights)
    high = sum(weights)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_split(weights, k, mid):
            ans = mid
            high = mid - 1 # 더 작은 너비가 가능한지 확인
        else:
            low = mid + 1 # 너비를 키워야 함
            
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
"""
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성
# ---------------------------------------------------------
def calculate_ans(n, k, weights):
    low = max(weights)
    high = sum(weights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        count = 1
        current_sum = 0
        for w in weights:
            if current_sum + w > mid:
                count += 1
                current_sum = w
            else:
                current_sum += w
        if count <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

for i in range(1, 21):
    if i <= 5: # 소규모
        n = random.randint(1, 100)
        k = random.randint(1, n)
        weights = [random.randint(1, 100) for _ in range(n)]
    elif i <= 10: # 중규모
        n = 5000
        k = random.randint(10, 500)
        weights = [random.randint(1, 1000) for _ in range(n)]
    else: # 대규모 (저격용) N = 100,000
        n = 100000
        k = random.randint(100, 50000)
        weights = [random.randint(1, 10000) for _ in range(n)]
    
    ans = calculate_ans(n, k, weights)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(f"{n} {k}\n")
        f.write(" ".join(map(str, weights)) + "\n")
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(ans) + "\n")

print(f"✅ 'Level01/P175' 문제 생성이 완료되었습니다.")