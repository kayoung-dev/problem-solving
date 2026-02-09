import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P008 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P008")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "연속된 열을 피하는 행렬의 최대 합"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP", "Mathematics"]
---

## description
$N$개의 행과 $3$개의 열로 구성된 행렬 $A$가 주어집니다. 각 행의 $j$번째 열에 있는 원소를 $A_{i,j}$라고 합니다. (단, $1 \le i \le N, 1 \le j \le 3$)<br />

우리는 각 행에서 정확히 하나의 원소를 선택하여 그 합을 최대화하려고 합니다. 원소를 선택할 때는 다음과 같은 제약 조건을 반드시 만족해야 합니다:<br />

**"연속된 두 행에서 선택한 원소의 열 번호는 서로 달라야 한다."**<br />

주어진 행렬에서 이 조건을 만족하며 선택할 수 있는 원소들의 합 중 최댓값을 구하는 프로그램을 작성하세요.<br />

## input_description
- 첫 번째 줄에 행의 개수 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 두 번째 줄부터 $N$개의 줄에 걸쳐 각 행의 원소 $A_{i,1}, A_{i,2}, A_{i,3}$이 공백으로 구분되어 주어집니다.
- $0 \le A_{i,j} \le 10,000$

## output_description
- 제약 조건을 만족하며 선택한 원소들의 합 중 최댓값을 정수로 출력합니다.

# samples

### input 1
{TICK}
3
10 40 70
50 10 20
40 60 50
{TICK}

### output 1
{TICK}
180
{TICK}


### input 2
{TICK}
3
10 20 30
100 1 1
1 100 1
{TICK}

### output 2
{TICK}
230
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 1행의 데이터로 초기값을 설정합니다.
    # dp_a, dp_b, dp_c는 각각 현재 행에서 1열, 2열, 3열을 선택했을 때의 최대 누적합입니다.
    dp_a = int(input_data[1])
    dp_b = int(input_data[2])
    dp_c = int(input_data[3])
    
    idx = 4
    for i in range(1, n):
        # 현재 행의 각 열 값을 읽어옵니다.
        cur_a = int(input_data[idx])
        cur_b = int(input_data[idx+1])
        cur_c = int(input_data[idx+2])
        idx += 3
        
        # 이전 행에서 다른 열을 선택했던 값들 중 큰 값을 더해 현재의 최댓값을 갱신합니다.
        next_a = cur_a + max(dp_b, dp_c)
        next_b = cur_b + max(dp_a, dp_c)
        next_c = cur_c + max(dp_a, dp_b)
        
        dp_a, dp_b, dp_c = next_a, next_b, next_c
        
    # 마지막 행까지 계산된 세 가지 상태 중 최댓값을 출력합니다.
    print(max(dp_a, dp_b, dp_c))

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
def get_ans(n, data):
    dp = [0, 0, 0]
    dp[0], dp[1], dp[2] = data[0]
    for i in range(1, n):
        na = data[i][0] + max(dp[1], dp[2])
        nb = data[i][1] + max(dp[0], dp[2])
        nc = data[i][2] + max(dp[0], dp[1])
        dp = [na, nb, nc]
    return max(dp)

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 5:
        n_val = i * 2 # 2, 4, 6...
    elif i <= 15:
        n_val = 1000 # 중규모
    else:
        n_val = 100000 # 대규모 (DP 최적화 확인용)
    
    matrix_data = [[random.randint(0, 5000) for _ in range(3)] for _ in range(n_val)]
    
    input_str = f"{n_val}\n"
    for row in matrix_data:
        input_str += f"{row[0]} {row[1]} {row[2]}\n"
        
    ans_str = str(get_ans(n_val, matrix_data))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P008' 문제 생성이 완료되었습니다.")