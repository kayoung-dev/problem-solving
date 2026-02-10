import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P070 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P070")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 캠퍼스 복도의 Wi-Fi 명당 찾기

## 문제 설명
대학교 학생회장인 '온유'는 캠퍼스 중앙 복도에 앉아 공부하는 학생들의 불만 사항을 접수했습니다. 바로 복도의 특정 구간마다 **Wi-Fi 신호 세기**가 너무 차이 난다는 것입니다. 줌(Zoom) 수업 중 끊기기라도 하면 큰일이니까요!

복도는 $N$개의 구역으로 나뉘어 있으며, 현재 각 구역에는 이미 설치된 Wi-Fi 공유기들이 있습니다. 

1. **신호 범위:** 각 공유기는 설치된 구역을 중심으로 앞뒤 $R$만큼의 구역까지 신호를 전달합니다. 
   - 예를 들어, $i$번 구역에 공유기가 있다면 $[i-R, i+R]$ 범위의 모든 구역에 신호 세기가 $1$씩 추가됩니다.
2. **현재 신호:** 각 구역의 현재 신호 세기는 해당 구역을 커버하는 모든 공유기의 신호 세기 합입니다.
3. **추가 설치:** 학생회는 예산을 확보하여 **$K$개의 추가 와이파이 증폭기**를 샀습니다. 증폭기도 기존 공유기와 똑같이 $R$의 범위를 가집니다.

온유의 목표는 이 $K$개의 증폭기를 적절히 배치하여, **전체 구역 중 신호 세기가 가장 약한 곳의 신호를 최대한 강하게** 만드는 것입니다. 즉, **최소 신호 세기의 최댓값**을 구하세요.



---
## 입력 형식 (Input Format)
- 첫 번째 줄에 구역의 수 $N$, 신호 범위 $R$, 추가 가능한 증폭기 수 $K$가 공백으로 구분되어 주어집니다.
  ($1 \le N \le 10,000$, $0 \le R \le N$, $1 \le K \le 10^9$)
- 두 번째 줄에 $1$번 구역부터 $N$번 구역까지 이미 설치된 공유기의 개수가 공백으로 구분되어 주어집니다.
  ($0 \le$ 기존 공유기 수 $\le 10,000$)

## 출력 형식 (Output Format)
- 증폭기 $K$개를 모두 설치했을 때, 달성할 수 있는 **최소 신호 세기의 최댓값**을 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 1 2
1 2 1 2 1
{TICK}

**Output:**
{TICK}
4
{TICK}

- $R=1$이므로 각 구역의 초기 신호 세기는 다음과 같습니다.
  - 1구역: 1+2 = 3  <br/>영향 주는 범위 [0-1, 0+1] = [0,1]
  - 2구역: 1+2+1 = 4 <br/>영향 주는 범위 [1-1, 1+1] = [0,2]
  - 3구역: 2+1+2 = 5 <br/>영향 주는 범위 [2-1, 2+1] = [1,3]
  - 4구역: 1+2+1 = 4 <br/>영향 주는 범위 [3-1, 3+1] = [2,4]
  - 5구역: 2+1 = 3 <br/>영향 주는 범위 [4-1, 4+1] = [3,4]
- 최소 신호는 3입니다. 증폭기를 1구역에 1개, 5구역에 1개를 각각 놓으면 모든 구역의 신호가 4 이상이 됩니다.

### 예시 2
**Input:**
{TICK}
4 0 3
5 10 2 3
{TICK}

**Output:**
{TICK}
4
{TICK}

- $R=0$ 이므로 각 구역은 자기 자신의 공유기 신호만 받습니다.
- 현재 최소 신호 세기는 2(3구역)입니다. 
- 3구역에 증폭기 2개, 4구역에 1개를 설치하면 $[5, 10, 4, 4]$가 되어 최소 신호 세기는 4가 됩니다. 

### 예시 3
**Input:**
{TICK}
6 2 4
1 1 1 1 1 1
{TICK}

**Output:**
{TICK}
5
{TICK}

- $R=2$이므로 초기 신호는 $[3, 4, 5, 5, 4, 3]$입니다. 
  - 1구역: 1+1+1 = 3
  - 2구역: 1+1+1+1 = 4
  - 3구역: 1+1+1+1 = 5
  - 4구역: 1+1+1+1+1 = 5
  - 5구역: 1+1+1+1 = 4
  - 6구역: 1+1+1 = 3
- 3구역에 증폭기 2개(1~5구역 커버), 6구역에 2개(4~6구역 커버)를 설치하면 최소 신호가 5 이상이 됩니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - [수정됨] 딱 2줄만 읽기
# ---------------------------------------------------------
# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - 입력 즉시 실행 로직
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    # 데이터를 단어 단위로 하나씩 끊어서 가져오는 도구
    def get_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    tokens = get_tokens()
    
    try:
        # 1. N, R, K를 먼저 읽음
        n = int(next(tokens))
        r = int(next(tokens))
        k = int(next(tokens))
        
        # 2. 정확히 n개의 데이터만 읽음 (n개가 차면 즉시 루프 종료)
        stations = []
        for _ in range(n):
            stations.append(int(next(tokens)))
            
    except (StopIteration, ValueError):
        return

    # 3. 초기 신호 계산 (Sliding Window)
    current_power = [0] * n
    # 초기 0번 구역 윈도우 합
    ws = sum(stations[:r+1])
    for i in range(n):
        current_power[i] = ws
        if i + r + 1 < n: ws += stations[i + r + 1]
        if i - r >= 0: ws -= stations[i - r]

    # 4. 결정 함수 (Deque 활용)
    def check(target):
        dq = deque()
        added_sum = 0
        used_k = 0
        for i in range(n):
            while dq and dq[0][1] < i:
                added_sum -= dq.popleft()[0]
            actual = current_power[i] + added_sum
            if actual < target:
                diff = target - actual
                used_k += diff
                if used_k > k: return False
                added_sum += diff
                dq.append([diff, i + 2 * r])
        return used_k <= k

    # 5. 이진 탐색
    low, high = 0, sum(stations) + k
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(ans)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성 
# ---------------------------------------------------------
def solve_internal(n, r, k, stations):
    from collections import deque
    
    cp = [0] * n
    ws = sum(stations[:r+1])
    for i in range(n):
        cp[i] = ws
        if i+r+1 < n: ws += stations[i+r+1]
        if i-r >= 0: ws -= stations[i-r]
    
    def check(target):
        # 여기도 혹시 모르니 deque 사용 확인
        dq = deque()
        added, used = 0, 0
        for i in range(n):
            while dq and dq[0][1] < i:
                added -= dq.popleft()[0]
            actual = cp[i] + added
            if actual < target:
                diff = target - actual
                used += diff
                if used > k: return False
                added += diff
                dq.append([diff, i + 2*r])
        return used <= k

    low, high, res = 0, sum(stations) + k, 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(res)

test_data = [
    (5, 1, 2, [1, 2, 1, 2, 1]),
    (4, 0, 3, [5, 10, 2, 3]),
    (6, 2, 4, [1, 1, 1, 1, 1, 1])
]

for _ in range(17):
    tn = random.randint(10, 200)
    tr = random.randint(0, 5)
    tk = random.randint(10, 1000)
    ts = [random.randint(0, 20) for _ in range(tn)]
    test_data.append((tn, tr, tk, ts))

for i, (n, r, k, stations) in enumerate(test_data, 1):
    input_str = f"{n} {r} {k}\n" + " ".join(map(str, stations))
    ans = solve_internal(n, r, k, stations)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P070' 문제 생성이 완료되었습니다. ")