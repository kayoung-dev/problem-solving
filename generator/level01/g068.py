import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P068 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P068")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 도서관의 전설적인 침묵 파수꾼

## 문제 설명
중앙도서관의 전설적인 관리인 '최관리' 씨는 학생들의 집중력을 위해 아주 특별한 **소음 모니터링 시스템**을 도입했습니다. 이 시스템은 매분마다 현재 소음을 측정하여, **'최근 소음 수준에 비해 지금 얼마나 시끄러워졌는가'** 를 실시간으로 분석합니다.

시스템 작동 방식은 다음과 같습니다.

1. **최근 기록 유지:** 시스템은 항상 가장 최근 **$K$분** 동안의 소음 수치들만 따로 모아 관리합니다.
2. **소음 비교:** 매분 새로운 소음 수치 $X$가 측정될 때마다 다음 과정을 거칩니다.
   - **평균 계산:** 만약 이미 최근 기록이 **$K$개**가 가득 차 있다면, 그 $K$개 수치들의 평균($Avg$)을 계산합니다.
   - **변화량 출력:** "현재 측정값($X$) - 최근 평균($Avg$)" 값을 계산하여 알림판에 띄웁니다.
   - **기록 업데이트:** 방금 측정한 수치 $X$를 기록 목록에 추가합니다. 이때 목록에 담긴 기록이 $K$개를 넘어가게 되면, **가장 오래된 기록(제일 먼저 들어온 기록)을 하나 지워서** 항상 최신 $K$개만 남도록 유지합니다.
3. **대기 상태:** 아직 소음 기록이 $K$개 미만으로 쌓여 있다면, 비교할 과거 데이터가 충분하지 않으므로 아무것도 출력하지 않습니다.

$N$분 동안 측정된 소음 수치들이 순서대로 주어질 때, 알림판에 표시될 변화량들을 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 총 측정 시간 $N$분과 최근 기록 유지 범위 $K$가 공백으로 구분되어 주어집니다. ($1 \le N \le 1,000, 1 \le K \le 100$)
- 두 번째 줄에 $N$개의 분단위 소음 수치 $X_1, X_2, \dots, X_N$이 정수 형태로 주어집니다. ($0 \le X_i \le 100$)

## 출력 형식 (Output Format)
- 계산된 변화량 값을 공백으로 구분하여 출력합니다. 
- 모든 값은 **소수점 첫째 자리까지** 출력합니다. (예: `5.0`, `-2.3`)
- 만약 출력할 값이 하나도 없다면 아무것도 출력하지 않습니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 3
30 40 50 80 40
{TICK}

**Output:**
{TICK}
40.0 -16.7
{TICK}

- $K=3$이므로 1~3분까지는 기록만 쌓습니다. 기록 $[30, 40, 50]$.
- **4분(80) 입력:** 기존 기록 $[30, 40, 50]$의 평균은 $40.0$입니다.
  - $80 - 40.0 = 40.0$ 출력. 
  - 이후 기록은 $30$이 빠지고 $80$이 들어와 $[40, 50, 80]$이 됩니다.
- **5분(40) 입력:** 기록 $[40, 50, 80]$의 평균은 $56.66...$입니다.
  - $40 - 56.7 = -16.7$ 출력. (소수점 둘째 자리 반올림)

### 예시 2
**Input:**
{TICK}
4 2
10 20 15 25
{TICK}

**Output:**
{TICK}
0.0 7.5
{TICK}

- $K=2$입니다.
- 1~2분 ($10, 20$): 기록을 채웁니다. (기록 $[10, 20]$)
- **3분 ($15$) 측정:** 현재 기록 $[10, 20]$의 평균은 $15.0$입니다. 
  - $15 - 15.0 = 0.0$ 출력. 
  - 이후 기록은 $10$이 빠지고 $15$가 추가되어 $[20, 15]$가 됩니다.
- **4분 ($25$) 측정:** 현재 기록 $[20, 15]$의 평균은 $17.5$입니다.
  - $25 - 17.5 = 7.5$ 출력. 
  - 이후 기록은 $20$이 빠지고 $25$가 추가되어 $[15, 25]$가 됩니다.

### 예시 3
**Input:**
{TICK}
2 5
50 60
{TICK}

**Output:**
{TICK}
{TICK}

- 측정 시간($N=2$)이 기록 유지 범위($K=5$)보다 짧아 비교할 평균 데이터가 만들어지지 않으므로 아무것도 출력하지 않습니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    noise_levels = list(map(int, input_data[2:]))
    
    # 데이터를 담아둘 목록 (큐 역할)
    history = deque()
    results = []
    
    for x in noise_levels:
        # 최근 기록이 K개 가득 찼다면 평균과 비교
        if len(history) == k:
            avg = sum(history) / k
            diff = x - avg
            results.append(f"{diff:.1f}")
            
        # 새로운 기록 추가 및 오래된 기록 삭제
        history.append(x)
        if len(history) > k:
            history.popleft()
            
    if results:
        print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k, noise):
    from collections import deque
    history = deque()
    res = []
    for x in noise:
        if len(history) == k:
            avg = sum(history) / k
            res.append(f"{x - avg:.1f}")
        history.append(x)
        if len(history) > k:
            history.popleft()
    return " ".join(res)

test_data = [
    (5, 3, [30, 40, 50, 80, 40]),
    (4, 2, [10, 20, 15, 25]),
    (2, 5, [50, 60])
]

# 랜덤 데이터 17개 생성
for _ in range(17):
    tn = random.randint(10, 100)
    tk = random.randint(2, 10)
    tnoise = [random.randint(20, 90) for _ in range(tn)]
    test_data.append((tn, tk, tnoise))

for i, (n, k, noise) in enumerate(test_data, 1):
    input_str = f"{n} {k}\n{' '.join(map(str, noise))}"
    ans = solve_internal(n, k, noise)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P068' 문제 생성이 완료되었습니다. ")