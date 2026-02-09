import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P55 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P55")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 수학 증명 검증 시스템의 일괄 승인

## 문제 설명
수학자 민수는 거대한 수학적 난제를 풀기 위해 N개의 논리적 단계로 이루어진 증명을 작성했습니다. 슈퍼컴퓨터는 이 증명의 각 단계가 참인지 거짓인지 검증하는 작업을 수행합니다.

각 증명 단계는 현재 검수가 얼마나 완료되었는지를 나타내는 '검증 진도'와, 컴퓨터가 1시간 동안 추가로 검증할 수 있는 '검증 속도'가 서로 다릅니다.

수학적 논리의 특성상, 시스템은 다음과 같은 승인 규칙을 따릅니다.

1. 모든 증명 단계는 반드시 제출된 순서대로만 공식 승인될 수 있습니다.
2. 만약 뒤에 있는 단계의 검증이 이미 100% 완료되었더라도, 그보다 앞선 단계 중 하나라도 검증이 끝나지 않았다면 공식 승인을 받을 수 없습니다.
3. 앞 순서의 단계가 100% 검증 완료되어 승인되는 순간, 이미 검증이 끝나서 대기 중이던 뒤 순서의 단계들도 한꺼번에 공식 승인 처리됩니다.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 전체 증명 단계의 개수 N이 주어집니다. (1 <= N <= 100)
- 두 번째 줄에 각 단계의 현재 검증 진도가 순서대로 주어집니다.
- 세 번째 줄에 각 단계의 1시간당 검증 속도가 순서대로 주어집니다.

## 출력 형식 (Output Format)
- 한 번에 공식 승인되는 단계의 개수들을 승인되는 순서대로 공백으로 구분하여 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
93 30 55
1 30 5
{TICK}

**Output:**
{TICK}
2 1
{TICK}

- 각 단계별 완료 시간
  - 1단계: 완료까지 7시간 소요 ( (100 - 93) / 1 = 7 )
  - 2단계: 완료까지 3시간 소요 ( (100 - 30) / 30 = 2.33... 이므로 3시간 )
  - 3단계: 완료까지 9시간 소요 ( (100 - 55) / 5 = 9 )
- 7시간째에 1단계가 승인될 때, 이미 3시간 만에 검증이 끝나 대기하던 2단계가 함께 승인됩니다. (총 2개)
- 9시간째에 마지막 3단계가 승인됩니다. (총 1개)

### 예시 2
**Input:**
{TICK}
5
95 90 99 99 80
1 1 1 1 1
{TICK}

**Output:**
{TICK}
1 3 1
{TICK}

### 예시 3
**Input:**
{TICK}
5
40 40 40 40 40
10 20 30 5 40
{TICK}

**Output:**
{TICK}
3 2
{TICK}

- 각 단계별 완료 시간
  - 1단계: (100 - 40) / 10 = 6시간
  - 2단계: (100 - 40) / 20 = 3시간
  - 3단계: (100 - 40) / 30 = 2시간
  - 4단계: (100 - 40) / 5 = 12시간
  - 5단계: (100 - 40) / 40 = 1.5... -> 2시간
- 6시간째에 1단계가 완료됩니다. 이때 이미 완료된 2단계(3시간)와 3단계(2시간)가 함께 승인됩니다. (총 3개)
- 12시간째에 4단계가 완료됩니다. 이때 이미 완료된 5단계(2시간)가 함께 승인됩니다. (총 2개)
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
    
    finish_times = deque()
    for p, s in zip(progresses, speeds):
        finish_times.append(math.ceil((100 - p) / s))
        
    results = []
    while finish_times:
        standard_time = finish_times.popleft()
        count = 1
        
        while finish_times and finish_times[0] <= standard_time:
            finish_times.popleft()
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
    times = deque([math.ceil((100-curr_p)/curr_s) for curr_p, curr_s in zip(p, s)])
    res = []
    while times:
        std = times.popleft()
        cnt = 1
        while times and times[0] <= std:
            times.popleft()
            cnt += 1
        res.append(str(cnt))
    return " ".join(res)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (3, [93, 30, 55], [1, 30, 5]),
    (5, [95, 90, 99, 99, 80], [1, 1, 1, 1, 1]),
    (5, [40, 40, 40, 40, 40], [10, 20, 30, 5, 40]),
]

for _ in range(17):
    tn = random.randint(5, 30)
    tp = [random.randint(0, 99) for _ in range(tn)]
    ts = [random.randint(5, 40) for _ in range(tn)]
    test_cases.append((tn, tp, ts))

for i, (n, p, s) in enumerate(test_cases, 1):
    input_str = f"{n}\n" + " ".join(map(str, p)) + "\n" + " ".join(map(str, s))
    ans = solve_internal(n, p, s)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P55' 문제 생성이 완료되었습니다. ")