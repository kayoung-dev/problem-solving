import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P164 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P164")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 게임 랭킹에서 점수 찾기

## 문제 설명
게임 운영자 지민이는 플레이어들의 점수가 기록된 실시간 랭킹 보드를 관리하고 있습니다. 이 랭킹 보드는 점수가 가장 높은 사람부터 낮은 사람 순서대로, 즉 **내림차순**으로 정렬되어 있습니다.

지민이는 특정 점수 $K$를 가진 플레이어가 현재 랭킹 보드의 몇 번째 위치(인덱스)에 있는지 확인하려고 합니다. 랭킹에 기록된 점수 리스트와 찾고자 하는 점수 $K$가 주어질 때, 해당 점수의 위치를 출력하는 프로그램을 작성하세요.

위치는 $0$번부터 시작하며, 만약 랭킹 보드에 점수 $K$가 존재하지 않는다면 $-1$을 출력해야 합니다. 데이터의 양이 많으므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



---
## 입력 형식 (Input Format)
- 첫 번째 줄에는 랭킹에 기록된 점수의 개수 $N$과 찾고자 하는 점수 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N \le 100,000$
- $0 \le K \le 10^9$
- 두 번째 줄에는 내림차순으로 정렬된 $N$개의 점수가 공백으로 구분되어 주어집니다. 
- 각 점수는 $0$ 이상 $10^9$ 이하의 정수입니다.

## 출력 형식 (Output Format)
- 찾고자 하는 점수 $K$가 랭킹 보드에 존재하는 경우 해당 위치(인덱스)를 정수로 출력합니다.
- 만약 점수 $K$가 랭킹 보드에 존재하지 않는 경우에는 $-1$을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 850
1000 920 850 770 600
{TICK}
**Output:**
{TICK}
2
{TICK}
- 내림차순으로 정렬된 리스트에서 850은 세 번째 위치인 인덱스 2에 해당합니다.

### 예시 2
**Input:**
{TICK}
6 500
900 800 700 600 400 300
{TICK}
**Output:**
{TICK}
-1
{TICK}
- 리스트에 정확히 500점인 데이터가 존재하지 않으므로 -1을 출력합니다.

### 예시 3
**Input:**
{TICK}
3 100
100 50 10
{TICK}
**Output:**
{TICK}
0
{TICK}
- 가장 첫 번째 위치에 100점이 존재하므로 인덱스 0을 출력합니다.
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
    scores = list(map(int, data[2:]))

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if scores[mid] == k:
            result = mid
            break
        # 내림차순이므로 중간값이 목표보다 작으면 왼쪽(더 큰 값들)을 탐색
        elif scores[mid] < k:
            high = mid - 1
        # 중간값이 목표보다 크면 오른쪽(더 작은 값들)을 탐색
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
        n = random.randint(1, 15)
    elif i <= 15:
        n = random.randint(100, 1000)
    else:
        n = random.randint(50000, 100000)
    
    # 내림차순 리스트 생성
    scores = sorted([random.randint(0, 10**9) for _ in range(n)], reverse=True)
    
    # 타겟 설정
    if i % 2 == 0:
        target = random.choice(scores)
    else:
        target = random.randint(0, 10**9)

    # 정답 계산 (내림차순 이진 탐색)
    ans_idx = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if scores[m] == target:
            ans_idx = m
            break
        elif scores[m] < target:
            r = m - 1
        else:
            l = m + 1
    
    input_str = f"{n} {target}\n" + " ".join(map(str, scores))
    ans_str = str(ans_idx)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level01/P164' 문제 생성이 완료되었습니다.")