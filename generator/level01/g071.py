import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P071 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P071")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 캠퍼스 셔틀버스 승하차 관리

## 문제 설명
신입생 **민수**는 캠퍼스를 순환하는 긴 셔틀버스의 승하차 명단을 기록하는 아르바이트를 하고 있습니다. 이 버스는 특이하게도 차체의 앞쪽과 뒤쪽에 각각 문이 하나씩 있어서, 학생들은 양쪽 문을 통해 자유롭게 타고 내릴 수 있습니다.

버스의 좌석은 일렬로 길게 배치되어 있으며, 학생들은 다음과 같은 규칙으로 버스를 이용합니다.

1. **앞문으로 타기 ($F\_IN$):** 학생이 앞문으로 승차하면 현재 앉아 있는 학생들의 가장 앞자리에 앉습니다.
2. **뒷문으로 타기 ($B\_IN$):** 학생이 뒷문으로 승차하면 현재 앉아 있는 학생들의 가장 뒷자리에 앉습니다.
3. **앞문으로 내리기 ($F\_OUT$):** 앞문과 가장 가까운 곳(가장 앞자리)에 앉아 있는 학생이 먼저 내립니다.
4. **뒷문으로 내리기 ($B\_OUT$):** 뒷문과 가장 가까운 곳(가장 뒷자리)에 앉아 있는 학생이 먼저 내립니다.

만약 버스가 비어있는데 내리려는 시도가 있다면 민수는 해당 기록을 무시합니다. 모든 승하차 기록 $N$개가 주어질 때, 모든 과정이 끝난 후 버스에 앉아 있는 학생들의 이름을 **가장 앞자리부터 뒷자리 순서대로** 출력하는 프로그램을 작성하세요.



---
## 입력 형식 (Input Format)
- 첫 번째 줄에 승하차 기록의 개수 $N$이 주어집니다. ($1 \le N \le 1,000$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 각 기록이 주어집니다.
    - 승차의 경우: `F_IN 이름` 또는 `B_IN 이름` (이름은 영문 대소문자로 구성된 10자 이내의 문자열)
    - 하차의 경우: `F_OUT` 또는 `B_OUT`

## 출력 형식 (Output Format)
- 마지막에 버스에 남아 있는 학생들의 이름을 가장 앞자리부터 공백으로 구분하여 한 줄에 출력합니다.
- 만약 남아 있는 학생이 한 명도 없다면 `EMPTY`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
F_IN Alice
B_IN Bob
F_IN Charlie
B_OUT
{TICK}

**Output:**
{TICK}
Charlie Alice
{TICK}

- `F_IN Alice`: 앞자리에 Alice가 앉음. 
  - 버스: Alice
- `B_IN Bob`: Alice 뒤에 Bob이 앉음. 
  - 버스: Alice, Bob
- `F_IN Charlie`: Alice 앞에 Charlie가 앉음.
  - 버스: Charlie, Alice, Bob
- `B_OUT`: 가장 뒷자리인 Bob이 내림. 
  - 최종 버스: Charlie, Alice

### 예시 2
**Input:**
{TICK}
3
B_IN Kim
F_OUT
F_OUT
{TICK}

**Output:**
{TICK}
EMPTY
{TICK}

- `B_IN Kim`: 뒷문으로 Kim이 승차함. 
  - 버스: Kim
- `F_OUT`: 앞문에 가장 가까운 Kim이 하차함.
  - 버스: 비었음
- `F_OUT`: 버스가 비어 있으므로 이 기록은 무시됨.

### 예시 3
**Input:**
{TICK}
5
F_IN Lee
F_IN Park
B_IN Choi
B_OUT
F_IN Kim
{TICK}

**Output:**
{TICK}
Kim Park Lee
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    # 데이터를 토큰 단위로 읽어오는 제너레이터
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    tokens = get_input()
    
    try:
        line = next(tokens)
        if not line: return
        n = int(line)
    except (StopIteration, ValueError):
        return

    bus = deque()

    for _ in range(n):
        try:
            cmd = next(tokens)
            if cmd == "F_IN":
                name = next(tokens)
                bus.appendleft(name)
            elif cmd == "B_IN":
                name = next(tokens)
                bus.append(name)
            elif cmd == "F_OUT":
                if bus:
                    bus.popleft()
            elif cmd == "B_OUT":
                if bus:
                    bus.pop()
        except StopIteration:
            break

    if not bus:
        print("EMPTY")
    else:
        print(" ".join(bus))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(ops):
    bus = deque()
    for op in ops:
        cmd = op[0]
        if cmd == "F_IN":
            bus.appendleft(op[1])
        elif cmd == "B_IN":
            bus.append(op[1])
        elif cmd == "F_OUT":
            if bus: bus.popleft()
        elif cmd == "B_OUT":
            if bus: bus.pop()
    
    if not bus:
        return "EMPTY"
    return " ".join(bus)

# 수동 예시 데이터
test_data = [
    [("F_IN", "Alice"), ("B_IN", "Bob"), ("F_IN", "Charlie"), ("B_OUT")],
    [("B_IN", "Kim"), ("F_OUT"), ("F_OUT")],
    [("F_IN", "Lee"), ("F_IN", "Park"), ("B_IN", "Choi"), ("B_OUT"), ("F_IN", "Kim")]
]

# 랜덤 데이터 생성 (17개 추가하여 총 20개)
names_pool = ["Min", "Ji", "Seo", "Yeon", "Han", "Sung", "Hee", "Ho", "Woo", "Rin"]

for _ in range(17):
    n = random.randint(10, 50)
    ops = []
    for _ in range(n):
        r = random.random()
        if r < 0.3: # F_IN
            ops.append(("F_IN", random.choice(names_pool) + str(random.randint(1, 99))))
        elif r < 0.6: # B_IN
            ops.append(("B_IN", random.choice(names_pool) + str(random.randint(1, 99))))
        elif r < 0.8: # F_OUT
            ops.append(("F_OUT",))
        else: # B_OUT
            ops.append(("B_OUT",))
    test_data.append(ops)

for i, ops in enumerate(test_data, 1):
    n = len(ops)
    input_lines = [str(n)]
    for op in ops:
        input_lines.append(" ".join(op))
    
    input_str = "\\n".join(input_lines).replace("\\n", "\n")
    ans = solve_internal(ops)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P071' 문제 생성이 완료되었습니다. ")