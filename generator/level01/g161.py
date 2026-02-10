import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P161 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P161")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "장부에서 책 찾기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
도서관 장부에 $N$개의 책 고유 번호가 **오름차순**으로 정렬되어 기록되어 있습니다. 방문객이 찾고자 하는 특정 책 번호 $K$가 주어질 때, 이 번호가 장부의 몇 번째 위치(인덱스)에 있는지 찾아야 합니다.

장부의 인덱스는 $0$번부터 시작합니다. 만약 장부에 $K$와 일치하는 번호가 없다면 $-1$을 출력하세요. 데이터의 양이 많으므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



## input_description
- 첫 번째 줄에 장부에 기록된 책의 수 $N$과 찾으려는 책 번호 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N \le 100,000$
- $1 \le K \le 10^9$
- 두 번째 줄에 $N$개의 책 고유 번호가 오름차순으로 정렬되어 주어집니다. 
- 각 번호는 $1$ 이상 $10^9$ 이하의 정수입니다.

## output_description
- 책 번호 $K$가 장부에 존재하는 경우 해당 인덱스(위치)를 출력합니다.
- 존재하지 않는 경우 $-1$을 출력합니다.

# samples

### input 1
{TICK}
5 12
3 7 12 15 22
{TICK}

### output 1
{TICK}
2
{TICK}
- 장부에는 `[3, 7, 12, 15, 22]`가 기록되어 있습니다. 찾고자 하는 번호 `12`는 세 번째 위치인 인덱스 `2`에 존재합니다.

### input 2
{TICK}
6 10
2 4 6 8 12 14
{TICK}

### output 2
{TICK}
-1
{TICK}
- 장부에는 `2, 4, 6, 8, 12, 14`가 있지만, 찾고자 하는 번호 `10`은 목록에 존재하지 않으므로 `-1`을 출력합니다.

### input 3
{TICK}
1 5
5
{TICK}

### output 3
{TICK}
0
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 입력 받기
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, k = map(int, line1)
        
        nums = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    # 이진 탐색 로직 (O(log N))
    low = 0
    high = n - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            answer = mid
            break
        elif nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    print(answer)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    if i <= 5:
        n = random.randint(1, 20)
    elif i <= 15:
        n = random.randint(100, 1000)
    else:
        n = random.randint(50000, 100000)
    
    # 중복 없는 오름차순 리스트 생성
    nums = sorted(random.sample(range(1, 10**9), n))
    
    # 50% 확률로 존재하는 값, 50% 확률로 존재하지 않는 값 설정
    if random.random() > 0.5:
        target = nums[random.randint(0, n-1)]
    else:
        target = random.randint(1, 10**9)
    
    # 정답 계산 (이진 탐색)
    ans_val = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            ans_val = m
            break
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    
    ans = str(ans_val)
    input_str = f"{n} {target}\n" + " ".join(map(str, nums))
    
    # 파일 저장 (요청하신 대로 1.in, 1.out 형태)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P161' 문제 생성이 완료되었습니다. ")