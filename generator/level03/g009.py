import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P009 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P009")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "조건을 만족하는 최장 숫자 배열 찾기"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP", "Mathematics"]
---

## description
하나의 수열 $A$가 주어집니다. 이 수열은 $N$개의 정수로 이루어져 있으며, 각 원소는 $A_1, A_2, \dots, A_N$으로 표기합니다.<br />

우리는 이 수열에서 일부 원소들을 선택하여 새로운 부분 수열을 만들려고 합니다. 이때 선택한 원소들은 원래 수열에서의 **상대적인 순서를 유지**해야 하며, 다음과 같은 조건을 만족해야 합니다:<br />

**"부분 수열의 각 원소는 바로 앞의 원소보다 엄격히 커야 한다."**<br />

즉, 선택한 원소들이 $A_{i_1}, A_{i_2}, \dots, A_{i_k}$라고 할 때, 인덱스는 $i_1 < i_2 < \dots < i_k$를 만족해야 하며 값은 $A_{i_1} < A_{i_2} < \dots < A_{i_k}$를 만족해야 합니다.<br />

주어진 수열에서 이 규칙을 만족하며 만들 수 있는 **부분 수열의 최대 길이 $k$** 를 구하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 수열의 크기 $N$이 주어집니다. 
- $1 \le N \le 3,000$
- 두 번째 줄에 $N$개의 정수 $A_i$가 공백으로 구분되어 주어집니다. 
- $1 \le A_i \le 1,000,000$

## output_description
- 조건을 만족하는 부분 수열의 최대 길이를 정수로 출력합니다.

# samples

### input 1
{TICK}
6
10 20 10 30 20 50
{TICK}

### output 1
{TICK}
4
{TICK}


### input 2
{TICK}
5
5 4 3 2 1
{TICK}

### output 2
{TICK}
1
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py - O(N^2) DP 방식)
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 데이터를 효율적으로 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))
    
    # dp[i]는 a[i]를 마지막 원소로 포함하는 최장 증가 부분 수열의 길이입니다.
    # 모든 원소는 그 자체로 길이가 1인 부분 수열이 될 수 있으므로 1로 초기화합니다.
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            # 현재 숫자(a[i])가 이전 숫자(a[j])보다 크다면,
            # j번째에서 끝나는 부분 수열 뒤에 a[i]를 붙일 수 있습니다.
            if a[j] < a[i]:
                # 여러 가능한 j 중에서 가장 긴 길이에 1을 더한 값을 선택합니다.
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 전체 기록된 값 중 가장 큰 값을 출력합니다.
    print(max(dp))

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

# 정답 도출 함수 (내부용)
def get_ans(n, a):
    if not a: return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 5:
        n_val = i * 10 # 10, 20...
    elif i <= 15:
        n_val = i * 100 # 600... 1500
    else:
        n_val = 3000 # 대규모 (DP 저격 구간)
    
    # 데이터 생성
    if i % 4 == 0:
        # 완전히 내림차순 (최악의 케이스 중 하나)
        a_list = list(range(n_val, 0, -1))
    elif i % 5 == 0:
        # 완전히 오름차순 (최대 길이 보장)
        a_list = list(range(1, n_val + 1))
    else:
        # 무작위 데이터
        a_list = [random.randint(1, 1000000) for _ in range(n_val)]
    
    input_str = f"{n_val}\n" + " ".join(map(str, a_list))
    ans_str = str(get_ans(n_val, a_list))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P009' 문제 생성이 완료되었습니다.")