import os
import random
import sys
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P45 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P45")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 컨베이어 벨트

## 문제 설명
스마트 물류 센터에는 두 개의 컨베이어 벨트(**Belt A**, **Belt B**)가 있습니다. 
각 벨트 위에는 택배 상자들이 일렬로 놓여서 이동하고 있습니다.

물류 로봇은 두 벨트의 **가장 앞에 있는 상자 중 하나**를 골라 트럭에 실어야 합니다.
트럭에는 실어야 할 **배송 순서(Order List)** 가 정해져 있으며, 이 순서를 반드시 지켜야 합니다.

로봇의 작동 규칙은 다음과 같습니다.
1.  두 벨트(**A**, **B**)의 **맨 앞에 있는 상자**만 꺼낼 수 있습니다.
2.  현재 트럭에 실어야 할 순서와 일치하는 상자가 있다면 즉시 꺼내서 싣습니다.
3.  만약 두 벨트의 맨 앞 상자 모두 현재 필요한 순서와 다르다면, 더 이상 작업을 진행할 수 없어 **작업을 중단**합니다.
4.  벨트 중간에 있는 상자를 미리 꺼내거나 순서를 바꿀 수는 없습니다.

두 컨베이어 벨트의 상태와 배송 순서가 주어졌을 때, **최대 몇 번째 상자까지** 순서대로 실을 수 있는지 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 **Belt A**에 놓인 상자들의 이름(문자열)이 공백으로 구분되어 주어집니다.
* 두 번째 줄에 **Belt B**에 놓인 상자들의 이름(문자열)이 공백으로 구분되어 주어집니다.
* 세 번째 줄에 트럭에 실어야 할 **배송 순서(Order)** 가 공백으로 구분되어 주어집니다.
* 상자의 이름은 영문 소문자 및 숫자로 구성됩니다.

## 출력 형식 (Output Format)
* 순서대로 실을 수 있는 상자의 **최대 개수**를 정수로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
apple banana
cherry date
apple cherry date banana
{TICK}

**Output:**
{TICK}
4
{TICK}

* **초기 상태**:
    * Belt A: `[apple, banana]`
    * Belt B: `[cherry, date]`
    * 목표: `[apple, cherry, date, banana]`

* **진행 과정**:
    * **목표 'apple'**: Belt A의 맨 앞에 있습니다. $\\rightarrow$ 싣기 성공 (현재 1개) <br/>
        (Belt A : `[banana]`, Belt B : `[cherry, date]`)
    * **목표 'cherry'**: Belt B의 맨 앞에 있습니다. $\\rightarrow$ 싣기 성공 (현재 2개) <br/>
        (Belt A : `[banana]`, Belt B : `[date]`)
    * **목표 'date'**: Belt B의 맨 앞에 있습니다. $\\rightarrow$ 싣기 성공 (현재 3개) <br/>
        (Belt A : `[banana]`, Belt B : `[]`)
    * **목표 'banana'**: Belt A의 맨 앞에 있습니다. $\\rightarrow$ 싣기 성공 (현재 4개) <br/>
        (Belt A : `[]`, Belt B : `[]`)
        
* 모든 상자를 순서대로 실었으므로 정답은 **4**입니다.

### 예시 2
**Input:**
{TICK}
box1 box2
toy1 toy2
box1 toy2 box2
{TICK}

**Output:**
{TICK}
1
{TICK}

* **초기 상태**:
    * Belt A: `[box1, box2]`
    * Belt B: `[toy1, toy2]`
    * 목표: `[box1, toy2, box2]`

* **진행 과정**:
    * **목표 'box1'**: Belt A의 맨 앞에 있습니다. $\\rightarrow$ 싣기 성공 (현재 1개) <br/>
        (Belt A : `[box2]`, Belt B : `[toy1, toy2]`)
    * **목표 'toy2'**: <br/>
      Belt A 맨 앞은 `box2`입니다. (불일치) <br/>
      Belt B 맨 앞은 `toy1`입니다. (불일치)
        
* 두 벨트의 맨 앞 상자가 모두 목표와 다르므로 여기서 작업을 중단합니다.
* 따라서 실을 수 있는 최대 개수는 **1**입니다.

"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_code = """import sys
from collections import deque

def solution():
    # 입력 처리
    lines = sys.stdin.read().splitlines()
    if len(lines) < 3:
        return

    # 두 개의 컨베이어 벨트(Queue)와 목표 리스트 생성
    belt_a = deque(lines[0].split())
    belt_b = deque(lines[1].split())
    orders = lines[2].split()
    
    count = 0
    
    for item in orders:
        # A 벨트의 맨 앞 확인
        if belt_a and belt_a[0] == item:
            belt_a.popleft()
            count += 1
        # B 벨트의 맨 앞 확인
        elif belt_b and belt_b[0] == item:
            belt_b.popleft()
            count += 1
        # 둘 다 해당하지 않으면 중단
        else:
            break
            
    print(count)

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
def solve_internal(a_list, b_list, target_list):
    q1 = deque(a_list)
    q2 = deque(b_list)
    cnt = 0
    for item in target_list:
        if q1 and q1[0] == item:
            q1.popleft()
            cnt += 1
        elif q2 and q2[0] == item:
            q2.popleft()
            cnt += 1
        else:
            break
    return str(cnt)

test_data = []

# (1) 예제 케이스 1 (모두 성공)
test_data.append((
    ["apple", "banana"],
    ["cherry", "date"],
    ["apple", "cherry", "date", "banana"]
))

# (2) 예제 케이스 2 (중단)
test_data.append((
    ["box1", "box2"],
    ["toy1", "toy2"],
    ["box1", "toy2", "box2"]
))

# (3) 랜덤 케이스 생성 (성공/실패 혼합)
for i in range(18):
    # 아이템 생성
    len_a = random.randint(2, 10)
    len_b = random.randint(2, 10)
    q1 = [f"A{k}" for k in range(len_a)]
    q2 = [f"B{k}" for k in range(len_b)]
    
    # 기본적으로 유효한 순서를 만듦
    valid_order = []
    temp_q1 = deque(q1)
    temp_q2 = deque(q2)
    
    while temp_q1 or temp_q2:
        if temp_q1 and (not temp_q2 or random.random() < 0.5):
            valid_order.append(temp_q1.popleft())
        else:
            valid_order.append(temp_q2.popleft())
            
    # 절반은 끝까지 성공하는 케이스
    if i < 9:
        test_data.append((q1, q2, valid_order))
    # 절반은 중간에 훼방을 놓는 케이스 (실패 유도)
    else:
        if len(valid_order) > 2:
            # 중간 지점의 값을 임의의 값으로 변경하여 끊기게 만듦
            break_point = random.randint(1, len(valid_order)-1)
            valid_order[break_point] = "UNKNOWN"
        test_data.append((q1, q2, valid_order))

# 파일 저장
for i, (a, b, t) in enumerate(test_data, 1):
    input_str = f"{' '.join(a)}\n{' '.join(b)}\n{' '.join(t)}"
    ans = solve_internal(a, b, t)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P45' 문제 생성이 완료되었습니다.")