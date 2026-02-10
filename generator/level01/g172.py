import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P172 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P172")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "입체 데이터 칩 설계"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Binary Search", "Math"]
---

## description
미래형 반도체 설계자 성민은 데이터를 3차원 공간에 효율적으로 저장하는 **큐브형 메모리 칩**을 개발하고 있습니다.

이 칩은 가로, 세로, 높이의 길이가 모두 $k$로 동일한 정육면체 구조를 가집니다. 즉, 한 변의 길이가 $k$인 칩을 완성하기 위해서는 총 **$k^3$** ($k$의 세제곱)개의 데이터 유닛이 필요합니다.

성민이는 현재 사용할 수 있는 데이터 유닛 $N$개를 확보했습니다. 성민이가 가진 유닛들을 사용하여 만들 수 있는 **가장 큰 정육면체 칩의 한 변의 길이 $k$** 를 구하는 프로그램을 작성하세요.

$N$이 최대 $10^{18}$에 달하므로, 1부터 차례대로 확인하는 방식으로는 제한 시간을 통과할 수 없습니다. 반드시 $O(\log N)$의 효율적인 이진 탐색을 사용해야 합니다.



## input_description
- 첫 번째 줄에 데이터 유닛의 총 개수 $N$이 주어집니다. 
- $0 \le N \le 10^{18}$

## output_description
- 완벽한 정육면체를 만들 수 있는 최대 한 변의 길이 $k$를 정수로 출력합니다.

# samples

### input 1
{TICK}
30
{TICK}

### output 1
{TICK}
3
{TICK}
- 한 변의 길이가 3이면 $3^3 = 27$개의 유닛이 필요합니다.
- 한 변의 길이가 4이면 $4^3 = 64$개의 유닛이 필요합니다.
- 가진 유닛이 30개이므로, 최대 한 변의 길이는 3입니다.

### input 2
{TICK}
1000
{TICK}

### output 2
{TICK}
10
{TICK}
- $10^3 = 1000$이므로 정확히 한 변의 길이가 10인 정육면체를 만들 수 있습니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)


# ---------------------------------------------------------
# 3. [정답 로직 함수] .out 파일 생성용
# ---------------------------------------------------------
def get_ans_p172(n):
    if n <= 0: return 0
    low, high = 0, 10**6 # 10^18의 세제곱근은 10^6
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
        # 정수 세제곱 연산 (오차 없음)
        if mid * mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

# ---------------------------------------------------------
# 4. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return
    
    try:
        n = int(line)
    except ValueError:
        return
    
    # 이진 탐색 로직 (세제곱근 탐색)
    low, high = 0, 10**6
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
            
        if mid * mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
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
    n = random.randint(0, 10**9) if i <= 10 else random.randint(10**16, 10**18)
    ans = get_ans_p172(n)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(str(n))
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(ans))

print(f"✅ 'Level01/P172' 문제 생성이 완료되었습니다. ")