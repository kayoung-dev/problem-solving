import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P171 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P171")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "공원 가로등 구역 확장"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Binary Search", "Math"]
---

## description
도시 계획가 '지우'는 도심 공원에 가로등을 설치하는 프로젝트를 맡았습니다. 공원은 중앙 광장을 중심으로 여러 개의 동심원 구역으로 나뉩니다.

- 1구역(가장 안쪽)에는 가로등 1개를 설치합니다.
- 2구역부터는 바로 안쪽 구역보다 가로등을 3개씩 더 많이 설치합니다.
- 즉, $i$구역에 설치되는 가로등 개수는 $1 + (i-1) \times 3$개입니다. 
- 1구역: 1개, 2구역: 4개, 3구역: 7개, 4구역: 10개 ...

지우가 가진 가로등 총 개수 $N$이 주어질 때, 완벽하게 채울 수 있는 최대 구역 수 $k$를 구하세요.


## input_description
- 첫 번째 줄에 가로등의 총 개수 $N$이 주어집니다. 
- $0 \le N \le 10^{18}$

## output_description
- 완벽하게 채울 수 있는 최대 구역 수 $k$를 정수로 출력합니다.

# samples

### input 1
{TICK}
12
{TICK}

### output 1
{TICK}
3
{TICK}
- 1구역(1개) + 2구역(4개) + 3구역(7개) = 총 12개를 사용합니다.
- 3구역까지 정확히 채울 수 있습니다.

### input 2
{TICK}
25
{TICK}

### output 2
{TICK}
4
{TICK}
- 4구역까지 채우는 데 필요한 총 가로등은 $1+4+7+10 = 22$개입니다. 
- 25개로는 4구역까지만 완벽하게 채울 수 있습니다.

### input 3
{TICK}
4
{TICK}

### output 3
{TICK}
1
{TICK}

""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. [정답 로직 함수] .out 파일 생성용
# ---------------------------------------------------------
def get_ans_p171(n):
    if n <= 0: return 0
    low, high = 0, 10**9
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
        # 등차수열의 합: S = k(3k - 1) // 2
        total = mid * (3 * mid - 1) // 2
        if total <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

solution_py = r"""import sys

# ---------------------------------------------------------
# 4. 정답 코드 (solution.py) 
# ---------------------------------------------------------
def solve():
    # sys.stdin.readline()을 사용해 한 줄이 들어오는 즉시 처리합니다.
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    try:
        n = int(line)
    except ValueError:
        return
    
    # 이진 탐색 로직
    low, high = 0, 10**9
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
            
        # S = k(3k - 1) // 2
        total = mid * (3 * mid - 1) // 2
        
        if total <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    # 결과를 출력하고 즉시 종료합니다.
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
"""
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 5. 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    # 선형 탐색을 저격하기 위해 11번부터는 매우 큰 수를 생성합니다.
    n = random.randint(0, 10**6) if i <= 10 else random.randint(10**16, 10**18)
    ans = get_ans_p171(n)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(str(n))
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(ans))

print(f"✅ 'Level01/P171' 문제 생성이 완료되었습니다. ")