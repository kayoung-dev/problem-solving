import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level02/P010 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level02", "P010")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "거듭제곱 수열의 분해 법칙"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP", "Mathematics"]
---


## description

수학자 가우스는 모든 양의 정수가 $1, 2, 4, 8, 16, \dots$ 와 같은 $2^k$ ($k$는 $0$ 이상의 정수) 형태의 서로 다른 수들의 합으로 단 한 가지 방법으로만 표현될 수 있다는 사실에 주목했습니다. 

예를 들어, 숫자 $13$은 다음과 같이 분해됩니다:
$$13 = 8 + 4 + 1$$
이때 사용된 항의 개수는 총 $3$개입니다. 반면, 숫자 $16$은 $16$ 그 자체로 표현되므로 항의 개수는 $1$개입니다. 

우리는 임의의 정수 $n$이 주어졌을 때, $0$부터 $n$까지의 모든 정수들이 각각 몇 개의 항으로 분해되는지 그 개수를 조사하려고 합니다. 

여기에는 흥미로운 수학적 규칙이 숨어 있습니다. 짝수 $2m$을 분해할 때 필요한 항의 개수는 그 절반인 $m$을 분해할 때와 정확히 같습니다. 반면, 홀수 $2m+1$을 분해할 때 필요한 항의 개수는 그 절반의 몫인 $m$을 분해할 때보다 정확히 $1$이 더 큽니다.

이러한 수의 성질을 이용하여, $0$부터 $n$까지 각 숫자를 분해하는 데 필요한 **항의 개수**를 순서대로 나열하는 프로그램을 작성해 주세요.


## input_description
- 첫 번째 줄에 조사할 범위의 상한선인 정수 $n$이 주어집니다.
- $0 \le n \le 100,000$

## output_description
- $0$부터 $n$까지 각 숫자를 분해할 때 필요한 항의 개수를 공백으로 구분하여 한 줄에 출력합니다.

# samples

### input 1
**Input:**
{TICK}
2
{TICK}
**Output:**
{TICK}
0 1 1
{TICK}

### output 1
**Input:**
{TICK}
5
{TICK}
**Output:**
{TICK}
0 1 1 2 1 2
{TICK}


### input 2
**Input:**
{TICK}
0
{TICK}

### output 2
{TICK}
0
{TICK}
""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 입력을 읽어 정수로 변환합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 결과를 저장할 리스트를 생성합니다.
    # dp[i]는 숫자 i를 분해할 때 필요한 항의 개수입니다.
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # 수학적 귀납법에 따른 점화식:
        # i를 2로 나눈 몫의 결과에 i를 2로 나눈 나머지를 더합니다.
        dp[i] = dp[i // 2] + (i % 2)
        
    # 리스트의 요소들을 공백으로 구분하여 출력합니다.
    print(*(dp))

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

def solve_internal(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i // 2] + (i % 2)
    return " ".join(map(str, dp))

# 테스트 케이스 생성 (20개)
test_inputs = [
    0, 1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 63, 64, 100, 512, 1024, 12345, 67890, 99999, 100000
]

for i, n_val in enumerate(test_inputs, 1):
    input_str = str(n_val)
    ans_str = solve_internal(n_val)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level02/P010' 문제 생성이 완료되었습니다.")