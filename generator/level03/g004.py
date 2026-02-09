import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P004 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P004")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "배달원의 효율적 휴식"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP"]
---

## description
성실한 배달원 민수는 일직선으로 늘어선 마을의 집들에 음식을 배달하고 있습니다. 각 집에서는 배달을 완료할 때마다 민수에게 정해진 금액의 팁을 줍니다. 하지만 민수에게는 체력을 관리하기 위한 한 가지 철칙이 있습니다.<br />

**"연속해서 붙어 있는 두 집을 방문하지 않는다."**<br />

만약 어떤 집에서 배달을 했다면, 바로 옆에 붙어 있는 집은 건너뛰고 쉬어야 합니다. 즉, 최소한 한 집 이상은 건너뛰어야 다음 배달을 진행할 수 있습니다.<br />

마을에 있는 각 집이 주는 배달 팁의 액수가 순서대로 주어질 때, 민수가 규칙을 지키면서 얻을 수 있는 **팁의 총합 중 최댓값**을 구하는 프로그램을 작성하세요.<br />

## input_description
- 첫 번째 줄에 마을에 있는 집의 개수 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 두 번째 줄에 각 집이 주는 팁 액수 $T_i$가 공백으로 구분되어 $N$개 주어집니다. 
- $0 \le T_i \le 10,000$

## output_description
- 민수가 얻을 수 있는 팁 총합의 최댓값을 정수로 출력합니다.

# samples

### input 1
{TICK}
4
1 2 3 1
{TICK}

### output 1
{TICK}
4
{TICK}

### input 2
{TICK}
5
2 7 9 3 1
{TICK}

### output 2
{TICK}
12
{TICK}

### input 3
{TICK}
10
100 1 1 100 1 1 100 1 1 100
{TICK}

### output 3
{TICK}
400
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py - DP 방식)
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    tips = list(map(int, input_data[1:]))
    
    if n == 1:
        print(tips[0])
        return
    
    # dp[i]는 i번째 집까지 고려했을 때 얻을 수 있는 최대 팁입니다.
    dp = [0] * n
    
    # 초기값 설정
    dp[0] = tips[0]
    dp[1] = max(tips[0], tips[1])
    
    # 점화식: i번째 집을 선택하는 경우(dp[i-2] + 현재팁) vs 선택하지 않는 경우(dp[i-1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + tips[i])
        
    print(dp[n-1])

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 정답 생성 로직 함수 (내부용)
def get_ans(n, tips):
    if n == 1: return tips[0]
    dp = [0] * n
    dp[0] = tips[0]
    dp[1] = max(tips[0], tips[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + tips[i])
    return dp[n-1]

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 5:
        # 소규모 테스트 (N=1~10)
        n_val = i * 2
    elif i <= 10:
        # 중규모 테스트 (N=100~500)
        n_val = i * 50
    else:
        # 대규모 테스트 (N=10,000~100,000) - DP 저격 구간
        n_val = (i - 10) * 10000
    
    tips_list = [random.randint(0, 1000) for _ in range(n_val)]
    
    input_str = f"{n_val}\n" + " ".join(map(str, tips_list))
    ans_str = str(get_ans(n_val, tips_list))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P004' 문제 생성이 완료되었습니다.")