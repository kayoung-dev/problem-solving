import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P162 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P162")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "시험 합격자 찾기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
시험 관리자 영희는 학생들의 시험 점수를 낮은 점수부터 높은 점수까지 순서대로 정렬하여 보관하고 있습니다. 이번 시험에서 점수가 $K$점 이상인 학생들을 모두 합격시키기로 결정했습니다.

영희는 장부에서 **처음으로 $K$점 이상을 받은 학생**이 몇 번째 위치(인덱스)에 있는지 알고 싶습니다. 점수가 기록된 리스트와 기준 점수 $K$가 주어질 때, 조건을 만족하는 가장 첫 번째 위치를 찾으세요.

장부의 위치는 $0$번부터 시작하며, 만약 $K$점 이상을 받은 학생이 한 명도 없다면 $-1$을 출력합니다. 데이터의 양이 방대하므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



## input_description
- 첫 번째 줄에 점수의 개수 $N$과 합격 기준 점수 $K$가 주어집니다.
- $1 \le N \le 100,000$
- $0 \le K \le 10^9$
- 두 번째 줄에 오름차순으로 정렬된 $N$개의 점수가 주어집니다. 
- 각 점수는 $0$ 이상 $10^9$ 이하의 정수 입니다.

## output_description
- 점수가 $K$ 이상인 값이 처음으로 나타나는 위치(인덱스)를 출력합니다. 조건을 만족하는 값이 없으면 $-1$을 출력합니다.

# samples

### input 1
{TICK}
5 80
70 75 80 85 90
{TICK}

### output 1
{TICK}
2
{TICK}
- 80점 이상인 점수는 80, 85, 90이며, 이 중 가장 처음 등장하는 위치는 인덱스 2입니다.

### input 2
{TICK}
6 95
10 25 40 55 70 85
{TICK}

### output 2
{TICK}
-1
{TICK}
- 모든 점수가 95점 미만이므로 조건을 만족하는 위치가 없어 -1을 출력합니다.

### input 3
{TICK}
4 50
50 50 60 70
{TICK}

### output 3
{TICK}
0
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    scores = list(map(int, input_data[2:]))

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if scores[mid] >= k:
            result = mid  # 일단 후보로 저장
            high = mid - 1  # 더 앞쪽(왼쪽)에 조건 만족하는 값이 있는지 확인
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    if i <= 5:
        n = random.randint(1, 10)
    elif i <= 15:
        n = random.randint(100, 1000)
    else:
        n = random.randint(50000, 100000)
    
    # 중복을 허용하는 오름차순 리스트 생성
    scores = sorted([random.randint(0, 10**9) for _ in range(n)])
    
    # 타겟 값 설정
    if i % 3 == 0: # 일부러 모두 작게 만듦 (결과 -1)
        target = max(scores) + 10
    elif i % 3 == 1: # 리스트 중 하나 선택
        target = random.choice(scores)
    else: # 임의의 값
        target = random.randint(0, 10**9)
    
    # 정답 계산 (Lower Bound)
    ans_val = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if scores[m] >= target:
            ans_val = m
            r = m - 1
        else:
            l = m + 1
    
    ans = str(ans_val)
    input_str = f"{n} {target}\n" + " ".join(map(str, scores))
    
    # 파일 저장 (1.in, 1.out 형태)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P162' 문제 생성이 완료되었습니다.")