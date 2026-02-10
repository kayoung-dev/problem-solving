import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P074 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P074")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 전공 서적 공동 구매 배송 시스템

## 문제 설명
학과 대표인 **안나**는 전공 서적 공동 구매를 진행하고 있습니다. 이번 학기 전공 서적은 '이론서'와 '실습서' 두 권이 한 세트로 구성되어 배송되어야 합니다.

재미있게도 이론서는 '가나 택배'를 통해 도착하고, 실습서는 '다라 택배'를 통해 별도로 도착합니다. 영희는 사무실에 이론서와 실습서를 각각 쌓아둘 수 있는 두 개의 보관 구역을 마련했습니다. 영희의 배송 규칙은 다음과 같습니다.

1. **도착 기록** 
    - 이론서가 도착하면 '이론서 구역'의 맨 뒤에 쌓고, 실습서가 도착하면 '실습서 구역'의 맨 뒤에 쌓습니다.
2. **세트 구성** 
    - 이론서 구역과 실습서 구역에 각각 최소 한 권 이상의 책이 존재하게 되는 즉시, 영희는 각 구역에서 **가장 오래전에 도착했던 책**을 한 권씩 꺼내어 한 세트로 포장합니다.
3. **배송** 
    - 포장된 세트는 즉시 학생들에게 배송됩니다.

택배들이 도착하는 순서 $N$개가 주어질 때, 각 세트가 구성되어 배송되는 순서대로 이론서와 실습서의 아이디를 출력하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 도착하는 택배의 총 개수 $N$이 주어집니다. ($1 \le N \le 10,000$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 도착 정보가 주어집니다.
    - `A 아이디`: 가나 택배를 통해 '이론서'가 도착함.
    - `B 아이디`: 다라 택배를 통해 '실습서'가 도착함.
    - 아이디는 영문과 숫자로 구성된 15자 이내의 문자열입니다.

## 출력 형식 (Output Format)
- 배송되는 순서대로 `이론서아이디 + 실습서아이디`를 한 줄에 하나씩 출력합니다.
- 만약 모든 과정이 끝날 때까지 배송된 세트가 하나도 없다면 `WAITING`을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
A Math_Vol1
B Math_Lab1
B Physics_Lab
A Physics_Vol
{TICK}

**Output:**
{TICK}
Math_Vol1 + Math_Lab1
Physics_Vol + Physics_Lab
{TICK}

- `A Math_Vol1` 도착: 이론서 구역에 보관.
- `B Math_Lab1` 도착: 실습서 구역에 보관. 두 구역에 책이 생겼으므로 `Math_Vol1 + Math_Lab1` 세트 배송.
- `B Physics_Lab` 도착: 실습서 구역에 보관. (이론서 부족으로 대기)
- `A Physics_Vol` 도착: 이론서 구역에 보관. 이제 짝이 맞으므로 `Physics_Vol + Physics_Lab` 세트 배송.

### 예시 2
**Input:**
{TICK}
3
A Calc_1
A Calc_2
B Calc_Lab_A
{TICK}

**Output:**
{TICK}
Calc_1 + Calc_Lab_A
{TICK}

- 이론서가 두 권(`Calc_1`, `Calc_2`) 먼저 왔지만 실습서는 하나(`Calc_Lab_A`)만 왔습니다.
- 가장 먼저 왔던 `Calc_1`과 `Calc_Lab_A`가 한 세트가 되어 배송되고, `Calc_2`는 실습서가 더 올 때까지 사무실에 남습니다.

### 예시 3
**Input:**
{TICK}
2
A CS_101
A CS_102
{TICK}

**Output:**
{TICK}
WAITING
{TICK}
"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------

solution_py = """import sys
from collections import deque

# 입력 방식 설정
input = sys.stdin.readline

def solve():
    # 1. N 읽기
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    
    storage_a = deque()
    storage_b = deque()
    results = [] # 결과를 모아둘 리스트
    
    # 2. 입력 처리 및 로직 수행
    for _ in range(n):
        line = input().strip().split()
        if not line:
            continue
            
        type, book_id = line[0], line[1]
        
        if type == 'A':
            storage_a.append(book_id)
        else:
            storage_b.append(book_id)
            
        # 세트 구성이 가능할 때마다 결과 리스트에 추가
        while storage_a and storage_b:
            theory = storage_a.popleft()
            lab = storage_b.popleft()
            results.append(f"{theory} + {lab}")
            
    # 3. 모든 입력이 끝난 후 한 번에 출력
    if not results:
        print("WAITING")
    else:
        print("\\n".join(results))

if __name__ == "__main__":
    solve()
"""

# 역슬래시 중복 방지를 위한 처리 후 저장
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py.replace("\\\\n", "\\n"))

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, events):
    from collections import deque
    sa, sb = deque(), deque()
    results = []
    for t, bid in events:
        if t == 'A': sa.append(bid)
        else: sb.append(bid)
        while sa and sb:
            results.append(f"{sa.popleft()} + {sb.popleft()}")
    return "\n".join(results) if results else "WAITING"

# 예시 데이터
test_data = [
    (4, [('A', 'Math_Vol1'), ('B', 'Math_Lab1'), ('B', 'Physics_Lab'), ('A', 'Physics_Vol')]),
    (3, [('A', 'Calc_1'), ('A', 'Calc_2'), ('B', 'Calc_Lab_A')]),
    (2, [('A', 'CS_101'), ('A', 'CS_102')])
]

# 랜덤 데이터 생성
id_prefix = ["Eng", "Bio", "Chem", "His", "Art", "Music", "Code", "Data", "AI", "Cloud"]
for _ in range(17):
    tn = random.randint(10, 100)
    tevents = []
    for j in range(tn):
        etype = random.choice(['A', 'B'])
        eid = f"{random.choice(id_prefix)}_{j:03d}"
        tevents.append((etype, eid))
    test_data.append((tn, tevents))

for i, (n, events) in enumerate(test_data, 1):
    input_str = f"{n}\n" + "\n".join([f"{e[0]} {e[1]}" for e in events])
    ans = solve_internal(n, events)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P074' 문제 생성이 완료되었습니다. ")