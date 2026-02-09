import os

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P003 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P003")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "태호의 복도 타일 공사"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP"]
---

## description
인테리어 디자이너인 태호는 새로 지어진 건물의 복도 바닥을 타일로 꾸미는 작업을 맡았습니다.<br />

복도의 크기는 가로가 $N$, 세로가 $2$인 $N \times 2$ 직사각형 형태입니다. 태호가 가진 타일은 가로 $1$, 세로 $2$ 크기의 $1 \times 2$ 직사각형 타일뿐입니다.<br />
태호는 이 타일을 세워서 $1 \times 2$ 모양으로 붙이거나, 옆으로 눕혀서 $2 \times 1$ 모양으로 붙일 수 있습니다.<br />

태호의 목표는 이 타일들을 빈틈없이 사용하여 $N \times 2$ 크기의 복도 바닥을 완전히 채우는 것입니다. 복도의 가로 길이 $N$이 주어졌을 때, 태호가 바닥을 채울 수 있는 모든 경우의 수를 계산하는 프로그램을 작성하세요.<br />

예를 들어, 가로 길이 $N=3$인 경우의 수는 다음과 같이 $3$가지입니다:<br />
1. 타일 3개를 모두 세로로 세워서 배치하는 경우<br />
2. 타일 1개를 세로로 세우고, 나머지 2개를 가로로 눕혀서 쌓는 경우 <br />
3. 타일 2개를 가로로 눕혀서 쌓고, 나머지 1개를 세로로 세우는 경우 <br />

복도의 길이 $N$이 커질수록 가능한 조합이 매우 많아지므로, 효율적인 계산 방식이 필요합니다.

## input_description
- 첫 번째 줄에 복도의 가로 길이 $N$이 주어집니다.
- $1 \le N \le 80$

## output_description
- $2 \times N$ 크기의 바닥을 채울 수 있는 모든 방법의 수를 정수로 출력합니다.

# samples

### input 1
{TICK}
2
{TICK}

### output 1
{TICK}
2
{TICK}

### input 2
{TICK}
3
{TICK}

### output 2
{TICK}
3
{TICK}

### input 3
{TICK}
50
{TICK}

### output 3
{TICK}
12586269025
{TICK}

""".replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py - DP 방식)
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        n = int(line.strip())
        
        # 가로 길이가 1이면 세로 타일 1개만 놓을 수 있습니다.
        if n == 1:
            print(1)
            return
        
        # n이 2일 때까지 초기값을 설정합니다.
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # n이 3 이상일 때부터 점화식을 적용합니다.
        # 가로 i를 채우는 방법은:
        # 1. (i-1)까지 채우고 세로 타일 1개를 붙이는 경우
        # 2. (i-2)까지 채우고 가로 타일 2개를 눕혀서 붙이는 경우
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        print(dp[n])
        
    except ValueError:
        pass

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

# 정답 생성 로직
def get_ans(n):
    if n == 1: return 1
    if n == 2: return 2
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    # 1~10번은 로직 확인용 작은 값
    if i <= 10:
        n_val = i * 2 
    # 11~20번은 DP 저격용 큰 값 (N=40~80)
    else:
        n_val = 40 + (i - 10) * 4
        if n_val > 80: n_val = 80
        
    input_str = str(n_val)
    ans_str = str(get_ans(n_val))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P003' 문제 생성이 완료되었습니다.")