import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P168 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P168")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "가장 가까운 온도 찾기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
연구원 미나는 실험 데이터가 기록된 리스트를 분석하고 있습니다. 이 리스트에는 총 $N$개의 온도가 낮은 순서대로 정렬되어 기록되어 있습니다.

미나는 이론상 도출된 특정 온도 $K$와 가장 유사한 실제 측정 값을 찾으려고 합니다. 즉, 리스트에 기록된 온도 중 $K$와의 차이(절댓값)가 가장 작은 값을 찾아야 합니다.

온도 리스트와 타겟 온도 $K$가 주어질 때, $K$와 가장 가까운 온도를 출력하는 프로그램을 작성하세요. 만약 $K$와의 차이가 똑같은 온도가 두 개 있다면, 더 낮은 온도를 출력합니다. 데이터의 양이 많으므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



## input_description
- 첫 번째 줄에는 기록된 온도의 개수 $N$과 타겟 온도 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N \le 100,000$
- $-10^9 \le K \le 10^9$
- 두 번째 줄에는 오름차순으로 정렬된 $N$개의 온도 데이터가 공백으로 구분되어 주어집니다. 
- 각 온도는 $-10^9$ 이상 $10^9$ 이하의 정수입니다.

## output_description
- 리스트의 온도 중 $K$와 가장 가까운(차이가 가장 작은) 온도 값을 정수로 출력합니다.

# samples

### input 1
{TICK}
4 36
10 30 40 50
{TICK}

### output 1
{TICK}
40
{TICK}
- 타겟 36과 30의 차이는 6이며, 40과의 차이는 4입니다. 따라서 차이가 더 적은 40을 출력합니다.

### input 2
{TICK}
3 20
10 20 30
{TICK}

### output 2
{TICK}
20
{TICK}
- 리스트에 타겟과 정확히 일치하는 20이 존재하므로 20을 출력합니다.

### input 3
{TICK}
5 -5
-20 -10 0 10 20
{TICK}

### output 3
{TICK}
-10
{TICK}
- 타겟 -5와 리스트 내 값들의 차이를 비교하면 -10과의 차이는 5, 0과의 차이도 5로 동일합니다. 
- 이처럼 차이가 같은 값이 두 개일 때는 더 낮은 온도인 -10을 출력합니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    temps = list(map(int, data[2:]))

    low = 0
    high = n - 1
    
    # 이진 탐색으로 k의 위치 탐색
    while low <= high:
        mid = (low + high) // 2
        if temps[mid] == k:
            print(temps[mid])
            return
        elif temps[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    # 반복문 종료 후 high < k < low 상태임
    if low >= n:
        print(temps[n-1])
    elif high < 0:
        print(temps[0])
    else:
        # 양옆 값 중 더 가까운 것 선택 (차이가 같으면 더 작은 값인 high 선택)
        if abs(temps[high] - k) <= abs(temps[low] - k):
            print(temps[high])
        else:
            print(temps[low])

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    # 11~20번은 대규모 데이터 (시간 복잡도 검증)
    if i <= 10:
        n = random.randint(1, 100)
    else:
        n = random.randint(90000, 100000)
    
    # 음수 범위를 포함한 랜덤 샘플링
    temps = sorted(random.sample(range(-10**9, 10**9), n))
    target = random.randint(-10**9, 10**9)

    # 정답 계산 (검증용)
    import bisect
    idx = bisect.bisect_left(temps, target)
    
    if idx == 0:
        ans_val = temps[0]
    elif idx == n:
        ans_val = temps[n-1]
    else:
        v1 = temps[idx-1]
        v2 = temps[idx]
        # 차이가 같으면 v1(작은 값) 선택
        if abs(v1 - target) <= abs(v2 - target):
            ans_val = v1
        else:
            ans_val = v2
    
    input_str = f"{n} {target}\n" + " ".join(map(str, temps))
    ans_str = str(ans_val)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level01/P168' 문제 생성이 완료되었습니다. ")