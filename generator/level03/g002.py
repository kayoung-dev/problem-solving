import os

# ---------------------------------------------------------
# 1. 경로 설정 (Level03/P002 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level03", "P002")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "지우의 건강 계단"
level: "3"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP"]
---

## description
지우는 아파트 계단을 오르며 운동을 합니다. 지우는 계단을 오를 때 특별한 규칙을 가지고 있습니다.<br />
1. 한 번에 **$1$계단**을 오르거나, 혹은 **$2$계단**을 한꺼번에 뛰어오를 수 있습니다.<br />
2. 목표는 정확히 목적지 층에 도달하는 것입니다.<br />

예를 들어, $3$번째 계단에 도착하는 방법은 다음과 같이 총 $3$가지가 있습니다:<br />
- $1$층 → $2$층 → $3$층 (모두 한칸씩 이동)<br />
- $1$층 → $3$층 (한칸 이동 후 두칸 이동)<br />
- $2$층 → $3$층 (두칸 이동 후 한칸 이동)<br />

지우가 총 $N$개의 계단으로 이루어진 목적지에 도착하려고 할 때, 가능한 모든 경로의 가짓수를 계산하는 프로그램을 작성하세요.<br />
단, 계단의 개수 $N$이 커질수록 경로의 수가 급격히 많아지므로, 이전에 계산한 정보를 활용하는 효율적인 알고리즘이 필요합니다.

## input_description
- 첫 번째 줄에 목적지 계단의 총 개수 $N$이 주어집니다.
- $1 \le N \le 45$

## output_description
- $N$번째 계단에 도달할 수 있는 총 방법의 수를 정수로 출력합니다.

# samples

### input 1
{TICK}
3
{TICK}

### output 1
{TICK}
3
{TICK}


### input 2
{TICK}
4
{TICK}

### output 2
{TICK}
5
{TICK}

### input 3
{TICK}
45
{TICK}

### output 3
{TICK}
1836311903
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
        
        if n == 1:
            print(1)
            return
        if n == 2:
            print(2)
            return
            
        # 정보를 기록할 바구니(DP 테이블)를 준비합니다.
        # 각 칸에는 해당 계단까지 도달하는 방법의 수를 저장합니다.
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # 3번째 계단부터 N번째 계단까지 순서대로 계산합니다.
        # i번째 계단에 도달하는 방법 = (i-1번째에서 온 경우) + (i-2번째에서 온 경우)
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

# 테스트케이스 생성을 위한 정답 도출 함수
def get_ans(n):
    if n == 1: return 1
    if n == 2: return 2
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# 20개의 테스트 케이스 생성 (1.in, 1.out 형식)
for i in range(1, 21):
    # 1~10번은 작은 값, 11~20번은 큰 값(35~45)으로 구성하여 DP 성능 테스트
    if i <= 10:
        n_val = i * 2 # 2, 4, 6... 20
    else:
        n_val = 30 + (i - 10) + 5 # 36, 37... 45
        if n_val > 45: n_val = 45
        
    input_str = str(n_val)
    ans_str = str(get_ans(n_val))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level03/P002' 문제 생성이 완료되었습니다.")