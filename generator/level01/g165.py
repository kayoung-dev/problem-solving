import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P165 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P165")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "중복 쿠폰 개수 세기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
수집가 준호는 번호순으로 정렬된 $N$개의 쿠폰을 가지고 있습니다. 준호는 특정 번호 $K$를 가진 쿠폰이 현재 리스트에 총 몇 장이나 있는지 알고 싶습니다.

정렬된 쿠폰 번호 리스트와 찾고자 하는 번호 $K$가 주어질 때, $K$의 전체 개수를 구하는 프로그램을 작성하세요. 데이터의 양이 많으므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



## input_description
- 첫 번째 줄에는 전체 쿠폰의 수 $N$과 개수를 확인하려는 번호 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N \le 100,000$
- $0 \le K \le 10^9$
- 두 번째 줄에는 오름차순으로 정렬된 $N$개의 쿠폰 번호가 공백으로 구분되어 주어집니다. 
- 각 번호는 $0$ 이상 $10^9$ 이하의 정수입니다.

## output_description
- 번호가 $K$인 쿠폰의 전체 개수를 정수로 출력합니다. 만약 해당 번호가 없다면 $0$을 출력합니다.

# samples

### input 1
{TICK}
8 7
1 3 5 7 7 7 10 12
{TICK}

### output 1
{TICK}
3
{TICK}
- 리스트에 7이 총 3개(인덱스 3, 4, 5) 존재하므로 3을 출력합니다.

### input 2
{TICK}
6 4
1 2 3 5 6 7
{TICK}

### output 2
{TICK}
0
{TICK}
- 리스트에 4가 없으므로 0을 출력합니다.

### input 3
{TICK}
5 2
2 2 2 2 2
{TICK}

### output 3
{TICK}
5
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    res = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    res = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:]))
    
    # O(log N) 방식으로 개수 계산
    count = upper_bound(arr, k) - lower_bound(arr, k)
    print(count)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def get_ans(arr, k):
    import bisect
    return bisect.bisect_right(arr, k) - bisect.bisect_left(arr, k)

for i in range(1, 21):
    # 11~20번은 대규모 데이터 (시간 복잡도 검증용)
    if i <= 10:
        n = random.randint(1, 500)
    else:
        n = random.randint(90000, 100000)
    
    # 중복이 많이 발생하도록 값의 범위 조절
    val_range = random.randint(10, 100) if i % 2 == 0 else 10**9
    
    # 정렬된 리스트 생성
    if i == 20: # 모든 값이 같은 특수 케이스
        target = 7
        coupons = [7] * n
    else:
        coupons = sorted([random.randint(0, val_range) for _ in range(n)])
        target = random.choice(coupons) if random.random() > 0.2 else random.randint(0, 10**9)

    ans_str = str(get_ans(coupons, target))
    input_str = f"{n} {target}\n" + " ".join(map(str, coupons))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level01/P165' 문제 생성이 완료되었습니다.")