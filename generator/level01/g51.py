import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P51 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P51")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 기상 캐스터의 실시간 평균 기온

## 문제 설명
기상 캐스터 진아는 실시간으로 변하는 기온 데이터를 시청자들에게 전달하고 있습니다. 기온은 매초 불규칙하게 요동치기 때문에, 진아는 수치의 급격한 변화를 줄여서 부드럽게 보여주기 위해 **'최근 $K$초 동안의 평균'** 을 화면에 띄우기로 했습니다.

평균 기온을 계산하는 규칙은 다음과 같습니다:
1. 진아는 항상 **최근 $K$개**의 기온 데이터만 기록장에 남겨둡니다.
2. 매초 새로운 기온 데이터가 들어올 때마다 기록장을 업데이트합니다:
   - 만약 기록장에 이미 $K$개의 기온이 적혀 있다면, **가장 오래전에 적었던** 기온 하나를 지웁니다.
   - 방금 들어온 새로운 기온을 기록장의 **맨 끝**에 추가합니다.
3. 새로운 값을 추가한 직후, **현재 기록장에 적혀 있는 모든 기온의 평균**을 구하여 방송 화면에 표시합니다.

총 $N$초 동안 수집된 기온 데이터가 순서대로 주어질 때, 진아가 매초 화면에 표시하게 될 평균값들을 계산하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 전체 데이터의 개수 $N$과 기록장에 남겨둘 개수 $K$가 주어집니다. ($1 \le K \le N \le 10,000$)
* 두 번째 줄에 $N$개의 기온 데이터(정수)가 시간 순서대로 주어집니다.

## 출력 형식 (Output Format)
* 매초 데이터를 기록장에 반영한 직후의 평균값을 공백으로 구분하여 출력합니다.
* 평균값은 소수점 첫째 자리까지 출력합니다. (예: `20.0`, `15.5`)

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 3
10 20 30 40 50
{TICK}

**Output:**
{TICK}
10.0 15.0 20.0 30.0 40.0
{TICK}

- **1초(10):** 기록장 `[10]`, 평균 $10 / 1 = 10.0$
- **2초(20):** 기록장 `[10, 20]`, 평균 $(10+20) / 2 = 15.0$
- **3초(30):** 기록장 `[10, 20, 30]`, 평균 $(10+20+30) / 3 = 20.0$
- **4초(40):** 기록장이 꽉 참($K=3$). 가장 오래된 **10**을 지우고 **40** 추가. 기록장 `[20, 30, 40]`, 평균 $(20+30+40) / 3 = 30.0$
- **5초(50):** 기록장에서 가장 오래된 **20**을 지우고 **50** 추가. 기록장 `[30, 40, 50]`, 평균 $(30+40+50) / 3 = 40.0$

### 예시 2
**Input:**
{TICK}
3 1
15 25 35
{TICK}

**Output:**
{TICK}
15.0 25.0 35.0
{TICK}

### 예시 3
**Input:**
{TICK}
4 2
10 20 10 20
{TICK}

**Output:**
{TICK}
10.0 15.0 15.0 15.0
{TICK}

- 1초(10): 기록장 [10], 평균 10.0
- 2초(20): 기록장 [10, 20], 평균 15.0
- 3초(10): 기록장이 꽉 참(K=2). 가장 오래된 10을 지우고 새로운 10 추가. 기록장 [20, 10], 평균 15.0
- 4초(20): 가장 오래된 20을 지우고 새로운 20 추가. 기록장 [10, 20], 평균 15.0
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
    temps = list(map(int, input_data[2:]))
    
    # 최근 기록을 담을 공간 (최대 K개)
    records = deque()
    current_sum = 0
    results = []
    
    for t in temps:
        # 기록장이 가득 찼다면 가장 오래된 데이터 제거
        if len(records) == k:
            oldest = records.popleft()
            current_sum -= oldest
            
        # 새로운 기온 추가
        records.append(t)
        current_sum += t
        
        # 현재 기록된 개수만큼 나누어 평균 계산
        avg = current_sum / len(records)
        results.append(f"{avg:.1f}")
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(n, k, temps):
    from collections import deque
    dq = deque()
    curr_sum = 0
    res = []
    for t in temps:
        if len(dq) == k:
            curr_sum -= dq.popleft()
        dq.append(t)
        curr_sum += t
        avg = curr_sum / len(dq)
        res.append(f"{avg:.1f}")
    return " ".join(res)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (5, 3, [10, 20, 30, 40, 50]),
    (3, 1, [15, 25, 35]),
    (4, 5, [10, 10, 10, 10]),
    (10, 2, [1, 5, 2, 8, 3, 7, 4, 9, 6, 10]),
    (8, 3, [20, 21, 19, 22, 20, 18, 20, 21])
]

for _ in range(15):
    tn = random.randint(10, 100)
    tk = random.randint(1, 10)
    ttemps = [random.randint(-10, 35) for _ in range(tn)]
    test_cases.append((tn, tk, ttemps))

for i, (n, k, temps) in enumerate(test_cases, 1):
    input_str = f"{n} {k}\n" + " ".join(map(str, temps))
    ans = solve_internal(n, k, temps)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P51' 문제 생성이 완료되었습니다.")