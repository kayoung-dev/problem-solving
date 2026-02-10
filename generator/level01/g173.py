import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P173 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P173")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "친환경 수직 농장 설계"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진 탐색", "매개 변수 탐색", "수학"]
---

## description
미래 도시의 설계자 수빈이는 제한된 부지에서 최대한 많은 작물을 재배하기 위해 **피라미드형 수직 농장**을 설계하고 있습니다. 

이 농장은 맨 위층부터 아래로 내려갈수록 바닥 면적이 넓어지는 구조입니다.
- 1층(맨 위)은 $1 \times 1$ 크기로, 총 1개의 재배 타일이 들어갑니다.
- 2층은 $2 \times 2$ 크기로, 총 4개의 재배 타일이 들어갑니다.
- $i$층은 $i \times i$ 크기로, 총 $i^2$개의 재배 타일이 들어갑니다.

수빈이는 현재 총 $N$개의 재배 타일을 보유하고 있습니다. 농장을 규칙에 맞게 맨 위층부터 빈틈없이 채워 나갈 때, **완벽하게 채울 수 있는 농장의 최대 층수**를 구하는 프로그램을 작성하세요.

이 문제는 $N$의 범위가 매우 크기 때문에, 단순히 한 층씩 더해가는 방식으로는 제한 시간 내에 해결할 수 없습니다. $O(\log \sqrt[3]{N})$의 효율로 해결해야 합니다.



## input_description
- 첫 번째 줄에 수빈이가 가진 재배 타일의 총 개수 $N$이 주어집니다. 
- $0 \le N \le 10^{18}$

## output_description
- 완벽하게 채울 수 있는 수직 농장의 최대 층수 $k$를 정수로 출력합니다.

# samples

### input 1
{TICK}
14
{TICK}

### output 1
{TICK}
3
{TICK}
- 1층(1개) + 2층(4개) + 3층(9개) = 총 14개입니다. 3층까지 딱 맞춰서 완벽하게 채울 수 있습니다.

### input 2
{TICK}
50
{TICK}

### output 2
{TICK}
4
{TICK}
- 4층까지의 총 타일: $1 + 4 + 9 + 16 = 30$개 (가능)
- 5층까지의 총 타일: $30 + 25 = 55$개 (불가능)
- 따라서 최대 층수는 4층입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)


# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
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
    
    # n이 10^18일 때, k는 약 1,442,249 근처이므로 high를 2,000,000으로 설정
    low, high = 0, 2000000
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
        
        # 자연수 제곱의 합 공식: mid*(mid+1)*(2*mid+1) // 6
        total = mid * (mid + 1) * (2 * mid + 1) // 6
        
        if total <= n:
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
# 4. 테스트케이스 생성
# ---------------------------------------------------------
# [정답 로직 함수] .out 파일 생성용
def get_ans_p173(n):
    if n <= 0: return 0
    # k가 10^6일 때 k^3 계열이므로 약 10^18에 도달
    low, high = 0, 2000000 
    ans = 0
    while low <= high:
        k = (low + high) // 2
        if k == 0:
            low = 1
            continue
        
        # 자연수 제곱의 합 공식: S = k(k+1)(2k+1) / 6
        total_needed = k * (k + 1) * (2 * k + 1) // 6
        
        if total_needed <= n:
            ans = k
            low = k + 1
        else:
            high = k - 1
    return ans


for i in range(1, 21):
    if i <= 10:
        n = random.randint(0, 10**6)
    else:
        # 대규모 데이터 저격 (10^18)
        n = random.randint(10**16, 10**18)
    
    ans = get_ans_p173(n)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(str(n))
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(ans))

print(f"✅ 'Level01/P173' 문제 생성이 완료되었습니다. ")