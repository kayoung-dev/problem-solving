import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P006 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P006")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "과일 가게의 연속 대박 기간 찾기"
level: "3"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP", "Kadane"]
---

## description
동네에서 작은 과일 가게를 운영하는 사장님은 지난 $N$일 동안 매일매일의 순이익을 장부에 기록해 왔습니다.<br />

순이익은 장사가 잘된 날은 양수($+$)로 기록되지만, 태풍이 오거나 과일값이 폭등하여 손해를 본 날은 음수($-$)로 기록되기도 합니다.
사장님은 문득 장부를 보며 이런 궁금증이 생겼습니다.<br />
**"지난 $N$일 중에서, 연속된 며칠 동안의 이익을 합쳤을 때 가장 큰 금액은 얼마였을까?"**<br />

예를 들어, $5$일 동안의 순이익이 순서대로 $[3, -2, 5, -1, 2]$였다면, 전체를 합친 금액은 $7$이지만, 첫째 날부터 셋째 날까지($3, -2, 5$)만 합치면 $6$이 됩니다.
하지만 이보다 더 좋은 구간이 있을 수도 있습니다. 사장님이 궁금해하는 **연속된 기간의 최대 이익 합**을 구하는 프로그램을 작성해 주세요.<br /><br />

단, 기록된 기간 중 적어도 하루 이상은 포함해야 하며, 모든 날의 순이익이 마이너스라면 그중 가장 손해가 적은 날의 금액이 정답이 됩니다.

## input_description
- 첫 번째 줄에 장부를 기록한 일수 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 두 번째 줄에 $N$일 동안의 일일 순이익 $P_i$가 공백으로 구분되어 주어집니다. 
- $-10,000 \le P_i \le 10,000$

## output_description
- 연속된 며칠 동안 얻을 수 있는 최대 이익 합을 정수로 출력합니다.

# samples

### input 1
{TICK}
5
3 -2 5 -1 2
{TICK}

### output 1
{TICK}
7
{TICK}


### input 2
{TICK}
6
-2 1 -3 4 -1 2
{TICK}

### output 2
{TICK}
5
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py - DP 방식)
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 대량의 데이터를 효율적으로 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    profits = list(map(int, input_data[1:]))
    
    # dp[i]는 i번째 날을 반드시 포함했을 때 얻을 수 있는 연속된 구간의 최대 합입니다.
    # 공간을 절약하기 위해 배열 대신 변수 하나만 사용할 수도 있습니다.
    current_max = profits[0]
    total_max = profits[0]
    
    for i in range(1, n):
        # "이전까지의 최대합에 나를 더하는 것"과 "오늘 새로 시작하는 것" 중 더 큰 것을 선택합니다.
        current_max = max(profits[i], current_max + profits[i])
        
        # 지금까지 발견한 전체 최댓값을 갱신합니다.
        if current_max > total_max:
            total_max = current_max
            
    print(total_max)

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
def get_ans(n, profits):
    curr = profits[0]
    total = profits[0]
    for i in range(1, n):
        curr = max(profits[i], curr + profits[i])
        if curr > total:
            total = curr
    return total

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 5:
        # 소규모 테스트 (N=1~20)
        n_val = i * 4
    elif i <= 15:
        # 중규모 테스트 (N=1,000~5,000)
        n_val = i * 300
    else:
        # 대규모 테스트 (N=100,000) - DP 저격 구간
        n_val = 100000
    
    # 양수와 음수가 섞인 무작위 이익 생성
    profits_list = [random.randint(-1000, 1000) for _ in range(n_val)]
    
    # 특정 구간에 아주 큰 대박이나 손실을 임의로 삽입하여 변별력 강화
    if i > 15:
        profits_list[random.randint(0, n_val-1)] = 10000
        profits_list[random.randint(0, n_val-1)] = -10000
    
    input_str = f"{n_val}\n" + " ".join(map(str, profits_list))
    ans_str = str(get_ans(n_val, profits_list))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P006' 문제 생성이 완료되었습니다.")