import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P007 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P007")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "최소 비용 징검다리 건너기"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP", "Kadane"]
---

## description
민수는 강 건너편으로 가기 위해 일렬로 놓인 $N$개의 징검다리를 건너야 합니다.<br />

각 징검다리는 이끼가 끼어 있어 밟을 때마다 미끄러지지 않기 위해 소모되는 에너지가 다릅니다. $i$번째 징검다리를 밟을 때 소모되는 에너지 $E_i$가 각각 정해져 있습니다.<br />

민수는 한 번에 **$1$칸**을 점프하여 바로 다음 다리로 가거나, 혹은 힘을 내어 **$2$칸**을 한꺼번에 점프하여 한 다리를 건너뛸 수 있습니다.<br />

민수의 목표는 **가장 마지막($N$번째) 징검다리에 도달**하는 것입니다. 민수는 처음에 강가에서 출발하며, 첫 번째 다리 혹은 두 번째 다리로 바로 점프하며 시작할 수 있습니다.<br />

마지막 다리에 발을 내디뎠을 때까지 소모된 **에너지 합의 최솟값**을 구하는 프로그램을 작성하세요.<br />


## input_description
- 첫 번째 줄에 징검다리의 개수 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 두 번째 줄에 각 징검다리를 밟을 때 소모되는 에너지 $E_i$가 $N$개 공백으로 구분되어 주어집니다. 
- $1 \le E_i \le 1,000$

## output_description
- 마지막 $N$번째 징검다리에 도달했을 때 소모된 에너지 합의 최솟값을 출력합니다.

# samples

### input 1
{TICK}
3
10 20 30
{TICK}

### output 1
{TICK}
40
{TICK}


### input 2
{TICK}
4
10 15 20 10
{TICK}

### output 2
{TICK}
25
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py - DP 방식)
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    energy = list(map(int, input_data[1:]))
    
    if n == 1:
        print(energy[0])
        return
    if n == 2:
        print(energy[1]) # 바로 2번 다리로 점프하는 것이 1번 거치는 것보다 항상 유리하거나 같음 (에너지는 양수이므로)
        # 하지만 문제 규칙상 '도착'이 목적이므로 시작점에서의 최소화를 고려합니다.
        print(min(energy[0] + energy[1], energy[1]))
        # 실제 로직에서는 아래 DP가 이를 처리합니다.
        return

    # dp[i]는 i번째 다리에 도달했을 때의 최소 에너지 합입니다.
    dp = [0] * n
    
    # 초기값 설정
    dp[0] = energy[0] # 첫 번째 다리로 시작
    dp[1] = energy[1] # 바로 두 번째 다리로 시작 (0번을 거치지 않음)
    
    # 3번째 다리(인덱스 2)부터 계산
    for i in range(2, n):
        # (바로 전 다리에서 왔을 때)와 (한 다리 건너뛰어 왔을 때) 중 최소 에너지를 선택
        dp[i] = min(dp[i-1], dp[i-2]) + energy[i]
        
    print(dp[n-1])

# 정확한 로직을 위해 n=2일 때의 처리를 포함한 코드를 다시 작성합니다.
def correct_solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    e = list(map(int, input_data[1:]))
    if n == 1:
        print(e[0])
        return
    dp = [0] * n
    dp[0] = e[0]
    dp[1] = e[1] # 시작할 때 1번 혹은 2번으로 바로 갈 수 있음
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + e[i]
    print(dp[n-1])

if __name__ == "__main__":
    correct_solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# 정답 생성용 내부 함수
def get_ans(n, e):
    if n == 1: return e[0]
    dp = [0] * n
    dp[0] = e[0]
    dp[1] = e[1]
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + e[i]
    return dp[n-1]

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 5:
        n_val = i * 2 # 2, 4, 6... 10
    elif i <= 15:
        n_val = i * 100 # 600... 1500
    else:
        n_val = 100000 # 대규모 (DP 변별)
    
    energy_list = [random.randint(1, 1000) for _ in range(n_val)]
    
    input_str = f"{n_val}\n" + " ".join(map(str, energy_list))
    ans_str = str(get_ans(n_val, energy_list))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P007' 문제 생성이 완료되었습니다.")
