import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P005 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P005")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "로봇 청소기의 효율적인 청소"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP"]
---

## description
똑똑한 로봇 청소기가 가로 $M$, 세로 $N$ 크기의 직사각형 모양 거실을 청소하려고 합니다.<br />
거실의 바닥은 $1 \times 1$ 크기의 칸들로 나누어져 있으며, 각 칸에는 쌓여 있는 먼지의 양이 적혀 있습니다. 로봇 청소기는 왼쪽 맨 위 칸 $(1, 1)$에서 출발하여 오른쪽 맨 아래 칸 $(N, M)$까지 이동하며 청소를 진행합니다.<br />

로봇 청소기의 이동 규칙은 다음과 같습니다:<br />
1. 로봇은 효율적인 동선을 위해 오직 **오른쪽** 또는 **아래쪽**으로만 이동할 수 있습니다.<br />
2. 로봇은 방문하는 모든 칸에 있는 먼지를 모두 흡입합니다.<br />

로봇 청소기가 목적지까지 이동하면서 **흡입하게 되는 전체 먼지 양의 합 중 최솟값**을 구하는 프로그램을 작성하세요.<br />

## input_description
- 첫 번째 줄에 거실의 세로 크기 $N$과 가로 크기 $M$이 공백으로 구분되어 주어집니다. 
- $1 \le N, M \le 100$
- 두 번째 줄부터 $N$개의 줄에 걸쳐, 각 줄마다 $M$개의 칸에 쌓인 먼지의 양 $D_{i,j}$가 공백으로 구분되어 주어집니다. 
- $0 \le D_{i,j} \le 100$

## output_description
- 왼쪽 위에서 오른쪽 아래까지 이동하며 흡입하는 먼지 총량의 유일한 최솟값을 정수로 출력합니다.

# samples

### input 1
{TICK}
3 3
1 3 1
1 5 1
4 2 1
{TICK}

### output 1
{TICK}
7
{TICK}

### input 2
{TICK}
2 3
1 2 3
4 5 6
{TICK}

### output 2
{TICK}
12
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 표준 입력을 통해 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 거실 지도를 구성합니다.
    grid = []
    idx = 2
    for r in range(n):
        grid.append(list(map(int, input_data[idx:idx+m])))
        idx += m
        
    # 각 지점까지의 최소 먼지 합을 저장할 기록지(DP 테이블)
    dp = [[0] * m for _ in range(n)]
    
    # 시작 지점 설정
    dp[0][0] = grid[0][0]
    
    # 가장 윗줄은 왼쪽에서 오는 방법밖에 없습니다.
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        
    # 가장 왼쪽줄은 위쪽에서 오는 방법밖에 없습니다.
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        
    # 나머지 칸들을 순차적으로 채워 나갑니다.
    # 현재 칸까지의 최소 먼지 = 현재 칸의 먼지 + min(위에서 올 때의 최소합, 왼쪽에서 올 때의 최소합)
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            
    # 목적지인 오른쪽 아래 칸의 결과를 출력합니다.
    print(dp[n-1][m-1])

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

# 정답 생성을 위한 내부 함수
def get_ans(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for j in range(1, m): dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, n): dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[n-1][m-1]

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 5:
        n_val, m_val = i + 2, i + 2
    elif i <= 15:
        n_val, m_val = 30, 30
    else:
        n_val, m_val = 100, 100 # 대규모 데이터 (DP 변별력)
    
    grid_data = [[random.randint(0, 100) for _ in range(m_val)] for _ in range(n_val)]
    
    input_str = f"{n_val} {m_val}\n"
    for row in grid_data:
        input_str += " ".join(map(str, row)) + "\n"
        
    ans_str = str(get_ans(n_val, m_val, grid_data))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P005' 문제 생성이 완료되었습니다.")