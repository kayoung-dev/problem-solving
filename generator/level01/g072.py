import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P72 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P72")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) - Raw String 적용으로 라텍스 오류 해결
# ---------------------------------------------------------
# r"""를 사용하여 \frac 등이 파이썬 탈출 문자로 해석되지 않게 합니다.
problem_template = r"""# 캠퍼스 식당의 분위기 메이커

## 문제 설명
캠퍼스 중앙 식당에는 최대 $K$명만 앉을 수 있는 '오늘의 대화 테이블'이 있습니다. 이 테이블은 식사하는 사람들의 **활기 에너지**가 조화를 이루어야 한다는 특별한 규칙이 있습니다.

새로운 학생이 이 테이블에 합류하려고 할 때, 테이블의 분위기를 유지하기 위해 다음과 같은 과정을 거칩니다.

1. **에너지 검사** 
    - 새로 앉으려는 학생의 활기 에너지가 $E_{new}$라고 할 때, 이 에너지는 현재 테이블에 앉아 있는 학생들의 **평균 활기 에너지**보다 크거나 같아야 합니다.
    - 즉, $E_{new} \ge \frac{\sum E_{current}}{C}$ 를 만족해야 합니다. 
    - 단, $\sum E_{current}$는 현재 앉아 있는 학생들의 에너지 총합, $C$는 현재 인원수
2. **자리 비워주기** 
    - 만약 새로운 학생의 에너지가 평균보다 낮다면, 테이블에서 **가장 오래 앉아 있었던 학생**부터 한 명씩 일어나서 테이블을 떠납니다. 
    - 이 과정은 새로운 학생의 에너지가 '남은 사람들의 평균'보다 크거나 같아질 때까지, 혹은 테이블이 완전히 비어버릴 때까지 반복됩니다.
3. **정원 확인** 
    - 새로운 학생의 에너지가 높아 위 과정을 거친 후에도 테이블에 빈 자리가 없다면(이미 $K$명이 앉아 있다면), 새로운 학생을 위해 가장 오래 앉아 있었던 학생이 무조건 일어나 자리를 비워줍니다.
4. **최종 합류** 
    - 모든 조건이 만족되면 새로운 학생이 테이블의 가장 마지막 자리에 앉습니다.

처음 테이블은 비어 있으며, 합류를 원하는 학생들의 이름과 에너지가 순서대로 주어집니다. 모든 학생의 시도가 끝난 후, 최종적으로 테이블에 남아 있는 학생들의 이름을 **앉아 있는 순서대로** 출력하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 합류를 시도하는 학생 수 $N$과 테이블의 최대 정원 $K$가 공백으로 구분되어 주어집니다. 
  ($1 \le N \le 10,000, 1 \le K \le 500$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 각 학생의 이름과 활기 에너지 $E$가 공백으로 구분되어 주어집니다.
  ($1 \le E \le 1,000$, 이름은 영문 대소문자 10자 이내)

## 출력 형식 (Output Format)
- 최종적으로 테이블에 남아 있는 학생들의 이름을 먼저 앉은 순서대로 공백으로 구분하여 한 줄에 출력합니다.
- 만약 아무도 남아 있지 않다면 `EMPTY`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1 
**Input:**
{TICK}
5 3
Alice 10
Bob 20
Charlie 14
David 18
Eve 15
{TICK}

**Output:**
{TICK}
Eve
{TICK}

- $K=3$:
- **Alice(10)** 비어있는 테이블에 입장. 
  - 상태: [Alice(10)], 평균: 10.0
- **Bob(20)** $20 \ge 10.0$ 이므로 입장.
  - 상태: [Alice(10), Bob(20)], 평균: 15.0
- **Charlie(14)** $14 < 15.0$ 이므로 Alice 퇴장. 남은 Bob의 평균은 20.0이며 $14 < 20.0$ 이므로 Bob도 퇴장. 테이블이 비었으므로 Charlie 입장. 
  - 상태: [Charlie(14)], 평균: 14.0
- **David(18)** $18 \ge 14.0$ 이므로 입장.
  - 상태: [Charlie(14), David(18)], 평균: 16.0
- **Eve(15):** $15 < 16.0$ 이므로 Charlie 퇴장. 남은 David의 평균은 18.0이며 $15 < 18.0$ 이므로 David도 퇴장. 테이블이 비었으므로 Eve 입장.
  - 상태: [Eve(15)]

### 예시 2 
**Input:**
{TICK}
4 2
Kim 50
Lee 60
Park 70
Choi 40
{TICK}

**Output:**
{TICK}
Choi
{TICK}

- **Kim(50), Lee(60)** 순서대로 입장. 
  - 상태: [Kim(50), Lee(60)], 평균: 55.0
- **Park(70)** $70 \ge 55.0$ 이므로 입장하려 하나 자리가 꽉 참. 가장 오래된 Kim 퇴장 후 Park 입장. 
  - 상태: [Lee(60), Park(70)], 평균: 65.0
- **Choi(40)** $40 < 65.0$ 이므로 Lee 퇴장. 남은 Park의 평균 70.0보다 $40$이 작으므로 Park도 퇴장. Choi 입장.

### 예시 3
**Input:**
{TICK}
3 2 
Alpha 80 
Beta 80 
Gamma 100
{TICK}

**Output:**
{TICK}
Beta Gamma
{TICK}
- Alpha(80): 테이블이 비어있으므로 입장합니다.
  - 상태: [Alpha], 평균: 80.0
- Beta(80): $80 \ge 80.0$이므로 에너지 조건을 만족하여 입장합니다. 
  - 상태: [Alpha, Beta], 평균: 80.0
- Gamma(100): $100 \ge 80.0$으로 에너지 조건은 완벽하게 통과했습니다.
  - 하지만 정원($K=2$)이 이미 꽉 찬 상태입니다.
  - 새로운 분위기 메이커 Gamma를 위해, 가장 오래 앉아 있었던 Alpha가 무조건 자리를 비워줍니다.
  - 최종적으로 Beta와 Gamma만 남게 됩니다.
"""

# f-string 대신 .replace()를 사용하여 안전하게 TICK 삽입
problem_md = problem_template.replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = get_input()
    
    try:
        n = int(next(tokens))
        k = int(next(tokens))
    except (StopIteration, ValueError):
        return
        
    table = deque()
    total_energy = 0
    
    for _ in range(n):
        try:
            name = next(tokens)
            energy = int(next(tokens))
        except StopIteration:
            break
            
        # 1. 평균 에너지 조건 검사 및 제거
        while table:
            avg = total_energy / len(table)
            if energy >= avg:
                break
            _, e = table.popleft()
            total_energy -= e
            
        # 2. 정원 초과 검사
        if len(table) == k:
            _, e = table.popleft()
            total_energy -= e
            
        # 3. 학생 합류
        table.append((name, energy))
        total_energy += energy
        
    if not table:
        print("EMPTY")
    else:
        print(" ".join([s[0] for s in table]))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k, students):
    dq = deque()
    total = 0
    for name, energy in students:
        while dq:
            if energy >= (total / len(dq)):
                break
            _, e = dq.popleft()
            total -= e
        if len(dq) == k:
            _, e = dq.popleft()
            total -= e
        dq.append((name, energy))
        total += energy
    return " ".join([s[0] for s in dq]) if dq else "EMPTY"

test_data = [
    (3, 3, [("Alice", 10), ("Bob", 20), ("Charlie", 12)]),
    (4, 2, [("Kim", 50), ("Lee", 60), ("Park", 70), ("Choi", 40)]),
    (3, 5, [("A", 100), ("B", 100), ("C", 100)])
]

names_pool = ["Min", "Ji", "Seo", "Yeon", "Han", "Sung", "Hee", "Ho", "Woo", "Rin"]
for _ in range(17):
    tn = random.randint(10, 100)
    tk = random.randint(5, 30)
    ts = [(random.choice(names_pool) + str(i), random.randint(1, 100)) for i in range(tn)]
    test_data.append((tn, tk, ts))

for i, (n, k, students) in enumerate(test_data, 1):
    input_str = f"{n} {k}\\n".replace("\\n", "\n")
    for s in students:
        input_str += f"{s[0]} {s[1]}\\n".replace("\\n", "\n")
    
    ans = solve_internal(n, k, students)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P72' 문제 생성이 완료되었습니다.")