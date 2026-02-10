import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P058 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P058")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 스마트 공장의 품질 검수와 일괄 포장

## 문제 설명
스마트 공장의 컨베이어 벨트 위로 N개의 부품이 순서대로 지나가며 품질 검수 센서를 통과합니다. 모든 부품은 반드시 **제작된 순서(번호 순서)대로** 포장 박스에 담겨 출고되어야 합니다.

각 부품은 현재 검사가 얼마나 진행되었는지를 나타내는 '검수 진도'와, 센서가 1초당 처리하는 '검수 속도'가 서로 다릅니다. 시스템은 다음과 같은 공정 규칙을 따릅니다.

1. 모든 부품은 반드시 번호 순서(1번, 2번, ...)대로만 포장 박스에 들어갈 수 있습니다.
2. 만약 뒤에 있는 부품의 검수가 이미 100% 완료되었더라도, 그보다 앞 번호의 부품 검사가 아직 끝나지 않았다면 박스에 들어가지 못하고 벨트 위에서 대기해야 합니다.
3. 가장 앞 순서의 부품 검사가 100% 완료되는 순간, 이미 검수가 끝나서 대기 중이던 뒤 순서의 부품들도 **한꺼번에** 박스에 담겨 출고됩니다.

각 부품의 현재 진도와 1초당 검수 속도가 주어질 때, 한 번에 몇 개의 부품이 일괄 포장될 수 있는지 그 개수들을 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 전체 부품의 개수 N이 주어집니다. (1 <= N <= 100)
- 두 번째 줄에 각 부품의 현재 검수 진도(0~99 사이의 정수)가 순서대로 주어집니다.
- 세 번째 줄에 각 부품의 1초당 검수 속도(1~100 사이의 정수)가 순서대로 주어집니다.

## 출력 형식 (Output Format)
- 한 번에 일괄 포장되어 나갈수 있는 부품의 개수들을 출고 순서대로 공백으로 구분하여 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
90 30 50 90
1 30 5 1
{TICK}

**Output:**
{TICK}
3 1
{TICK}

- 각 부품이 100% 완료될 때까지 걸리는 시간(초)을 계산합니다. (나머지가 생기면 1초가 더 필요하므로 올림 처리)
  - 1번 부품: (100 - 90) / 1 = **10초**
  - 2번 부품: (100 - 30) / 30 = 2.33... → **3초**
  - 3번 부품: (100 - 50) / 5 = **10초**
  - 4번 부품: (100 - 80) / 1 = **20초**
- 출고과정
  - **10초 시점:** 가장 앞선 1번 부품(10초 소요)이 완료됩니다. 이때 이미 검수가 끝난 2번(3초)과 방금 완료된 3번(10초)이 **함께(3개)** 포장되어 나갑니다.
  - **20초 시점:** 남은 4번 부품(20초 소요)이 완료되어 **홀로(1개)** 나갑니다.

### 예시 2
**Input:**
{TICK}
3
95 90 85
1 1 1
{TICK}

**Output:**
{TICK}
1 1 1
{TICK}

- 1번 부품: (100 - 95) / 1 = **5초**
- 2번 부품: (100 - 90) / 1 = **10초**
- 3번 부품: (100 - 85) / 1 = **15초**
- 출고 과정
  -  **5초 시점:** 1번이 끝났을 때 2, 3번은 아직 검수 중이므로 **1번만(1개)** 나갑니다.
  - **10초 시점:** 2번이 끝났을 때 3번은 아직 검수 중이므로 **2번만(1개)** 나갑니다.
  - **15초 시점:** 마지막 3번(1개)이 나갑니다.

### 예시 3 
**Input:**
{TICK}
3
40 40 40
10 20 30
{TICK}

**Output:**
{TICK}
3
{TICK}

- 소요 시간: 1번(6초), 2번(3초), 3번(2초)
- 6초가 되는 시점에 1번이 완료되는데, 이때 2번과 3번은 이미 완료되어 대기 중이므로 3개가 한꺼번에 출고됩니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_content = """import sys
import math
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    progresses = list(map(int, input_data[1:1+n]))
    speeds = list(map(int, input_data[1+n:1+2*n]))
    
    # 각 부품의 소요 시간 계산 (올림 처리)
    days = deque()
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
        
    results = []
    while days:
        # 현재 가장 앞 부품의 소요 시간을 기준(Standard)으로 설정
        standard = days.popleft()
        count = 1
        
        # 뒤에 있는 부품들 중 기준 시간보다 일찍 혹은 동시에 끝난 것들을 모두 포함
        while days and days[0] <= standard:
            days.popleft()
            count += 1
        results.append(str(count))
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, p, s):
    import math
    from collections import deque
    days = deque([math.ceil((100-curr_p)/curr_s) for curr_p, curr_s in zip(p, s)])
    res = []
    while days:
        std = days.popleft()
        cnt = 1
        while days and days[0] <= std:
            days.popleft()
            cnt += 1
        res.append(str(cnt))
    return " ".join(res)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (4, [90, 30, 50, 80], [1, 30, 5, 1]), # [3, 1] 결과 유도
    (3, [95, 90, 85], [1, 1, 1]),
    (3, [40, 40, 40], [10, 20, 30]),
]

for _ in range(17):
    tn = random.randint(5, 30)
    tp = [random.randint(0, 99) for _ in range(tn)]
    ts = [random.randint(1, 20) for _ in range(tn)]
    test_cases.append((tn, tp, ts))

for i, (n, p, s) in enumerate(test_cases, 1):
    input_str = f"{n}\n" + " ".join(map(str, p)) + "\n" + " ".join(map(str, s))
    ans = solve_internal(n, p, s)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P058' 문제 생성이 완료되었습니다. ")