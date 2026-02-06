import os

# ---------------------------------------------------------
# 1. 경로 설정 (Level02/P001 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level02", "P001")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "친환경 수직 농장 설계"
level: "2"
time_limit: 1000
memory_limit: 256
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["DP"]
---

## description
친환경 도시 설계 전문가인 수빈이는 좁은 부지에서도 많은 식물을 재배할 수 있는 '수직 농장'을 설계하고 있습니다. 이 농장은 층이 높아질수록 식물이 더 잘 자라는 특수한 구조를 가지고 있으며, 각 층에 배치할 수 있는 화분의 수는 특별한 규칙을 따릅니다.

수빈이가 세운 규칙은 다음과 같습니다.<br/>
- 가장 아래층인 $1$층에는 $1$개의 화분을 놓습니다. <br/>
- 그 위층인 $2$층에도 $1$개의 화분을 놓습니다. <br/>
- $3$층부터는 바로 아래에 있는 두 개 층의 화분 개수를 합친 만큼 화분을 놓습니다. <br/>

즉, $3$층에는 $1$층과 $2$층의 화분 개수를 더한 $2$개의 화분이 놓이게 됩니다. 수빈이는 농장이 아주 높게 설계되었을 때, 특정 층 $k$에 놓이게 될 화분의 총개수가 몇 개인지 미리 계산하여 자재를 준비하려고 합니다.

수빈이를 도와 $k$층에 놓일 화분의 개수를 구하는 프로그램을 작성하세요. 단, 층수가 높아질수록 계산이 매우 복잡해질 수 있으므로, 효율적인 계산 방법을 고민해야 합니다.

## input_description
- 첫 번째 줄에 화분의 개수를 알고자 하는 수직 농장의 층수 $k$가 주어집니다.
- $1 \le k \le 80$

## output_description
- $k$층에 배치될 화분의 개수를 정수로 출력합니다.

# samples

### input 1
{TICK}
3
{TICK}

### output 1
{TICK}
2
{TICK}


### input 2
{TICK}
7
{TICK}

### output 2
{TICK}
13
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
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    
    if k <= 2:
        print(1)
        return
    
    # 중복 계산을 피하기 위해 각 층의 결과를 순차적으로 저장
    floor_info = [0] * (k + 1)
    floor_info[1] = 1
    floor_info[2] = 1
    
    for i in range(3, k + 1):
        # 이전 두 층의 정보를 합산하여 현재 층의 정보 생성
        floor_info[i] = floor_info[i-1] + floor_info[i-2]
        
    print(floor_info[k])

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

# [정답 로직 함수] .out 파일 생성용
def calculate_ans(n):
    if n <= 2: return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# 20개의 테스트 케이스 생성
for i in range(1, 21):
    if i <= 10:
        # 1~10번: 작은 값 (로직 확인용)
        k_val = i * 3 
    else:
        # 11~20번: 큰 값 (DP 변별력 강화 구간)
        # k가 40 이상이면 일반 재귀(O(2^n))는 1초 내에 통과할 수 없음
        k_val = 35 + (i - 10) * 4 # 39, 43, 47 ... 75, 79
        if k_val > 80: k_val = 80
        
    input_str = str(k_val)
    ans_str = str(calculate_ans(k_val))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level02/P001' 문제 생성이 완료되었습니다.")