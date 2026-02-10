import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P57 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P57")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 스마트 보안 카메라

## 문제 설명
최첨단 연구소의 천장에는 원형 레일을 따라 움직이며 N개의 센서를 점검하는 보안 카메라가 설치되어 있습니다. 이 카메라는 중앙 통제실과 **유선 전선**으로 연결되어 있습니다.

만약 카메라가 한쪽 방향으로만 계속 빙글빙글 돌면 전선이 꼬여서 결국 끊어지고 말 것입니다. 이를 방지하기 위해 제어 AI는 다음과 같은 규칙으로 센서를 점검합니다.

1. 원형 레일에는 1번부터 N번까지 센서가 시계 방향 순서대로 설치되어 있습니다.
2. 카메라는 처음에 **1번 센서 위치에서 시작하여 시계 방향**으로 이동하며 작업을 시작합니다.
3. 현재 위치에서 시작하여 해당 방향으로 **K번째**에 있는 센서에 도달하면 정밀 점검을 수행합니다.
4. 점검이 끝난 센서는 시스템에서 제외되며, 카메라는 전선이 꼬이지 않도록 **즉시 이동 방향을 반대로** 바꿉니다.
   - 방금 점검한 센서의 다음 센서(기존 방향 기준)부터 숫자를 세되, 이번에는 **반대 방향**으로 K번째 센서를 찾아 이동합니다.
5. 모든 센서의 점검이 끝날 때까지 이 과정을 반복합니다.

센서들이 점검받는 순서를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 센서의 개수 N과 점검대상 센서까지의 이동 간격 K가 공백으로 구분되어 주어집니다. (1 <= N, K <= 1,000)

## 출력 형식 (Output Format)
- 점검받는 센서의 번호를 순서대로 공백으로 구분하여 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1 
**Input:**
{TICK}
5 3
{TICK}

**Output:**
{TICK}
3 1 4 5 2
{TICK}

- **1회차 (시계):** $1 \rightarrow 2 \rightarrow 3$. **$3$번** 점검. 
  - (남은: $[1, 2, 4, 5]$, 다음 시작점: $4$)
- **2회차 (반대):** $4 \rightarrow 2 \rightarrow 1$. **$1$번** 점검. 
  - (남은: $[2, 4, 5]$, 다음 시작점: $5$)
- **3회차 (시계):** $5 \rightarrow 2 \rightarrow 4$. **$4$번** 점검. 
  - (남은: $[2, 5]$, 다음 시작점: $5$)
- **4회차 (반대):** $5 \rightarrow 2 \rightarrow 5$. **$5$번** 점검. 
  - (남은: $[2]$, 다음 시작점: $2$)
- **5회차 (시계):** 마지막 **$2$번** 점검.

### 예시 2
**Input:**
{TICK}
6 3
{TICK}

**Output:**
{TICK}
3 1 5 2 6 4
{TICK}

### 예시 3
**Input:**
{TICK}
4 5
{TICK}

**Output:**
{TICK}
1 4 3 2
{TICK}

"""

problem_md = problem_template.replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_content = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # 센서 번호를 담은 양방향 큐(Deque) 생성
    sensors = deque(range(1, n + 1))
    results = []
    is_clockwise = True # 시계 방향 플래그
    
    while sensors:
        if is_clockwise:
            # 시계 방향 회전 (앞에서 빼서 뒤로 보냄)
            for _ in range(k - 1):
                sensors.append(sensors.popleft())
            results.append(str(sensors.popleft()))
        else:
            # 반대 방향 회전 (뒤에서 빼서 앞으로 보냄)
            for _ in range(k - 1):
                sensors.appendleft(sensors.pop())
            results.append(str(sensors.pop()))
            
        # 전선 꼬임 방지를 위해 방향 전환
        is_clockwise = not is_clockwise
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k):
    from collections import deque
    dq = deque(range(1, n + 1))
    res = []
    cw = True
    while dq:
        if cw:
            dq.rotate(-(k - 1))
            res.append(str(dq.popleft()))
        else:
            dq.rotate(k - 1)
            res.append(str(dq.popleft()))
            if dq: dq.rotate(1)
        cw = not cw
    return " ".join(res)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

# 정밀 검증된 케이스 추가
test_cases = [(5, 3), (6, 3), (4, 5), (7, 4), (10, 2)]
for _ in range(15):
    test_cases.append((random.randint(5, 100), random.randint(2, 12)))

for i, (n, k) in enumerate(test_cases, 1):
    input_str = f"{n} {k}"
    ans = solve_internal(n, k)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P57' 문제 생성이 완료되었습니다.")