import os
import random
import sys
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P44 폴더 생성 - 덮어쓰기)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P44")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 놀이공원 입장 줄 합치기

## 문제 설명
주말을 맞아 놀이공원에 엄청난 인파가 몰렸습니다. 
놀이기구 입구에는 두 개의 대기 줄(**Queue A**, **Queue B**)이 형성되어 있습니다.

놀이공원 직원은 효율적인 입장을 위해 **두 대기 줄의 맨 앞에 서 있는 사람 중 한 명을 선택하여** 놀이기구에 태우려고 합니다. 
하지만, 이미 예약된 **단체 관람객 명단(Target)** 이 있어서, 이 명단에 적힌 순서대로 정확하게 사람들을 입장시켜야만 합니다.

직원은 다음과 같은 규칙으로만 사람을 입장시킬 수 있습니다.

1.  두 대기 줄(**Queue A**, **Queue B**)의 **가장 앞에 있는 사람**만 선택할 수 있습니다.
2.  대기 줄에 있는 사람은 순서를 바꿀 수 없으며, 건너뛸 수도 없습니다. (새치기 불가)
3.  선택된 사람은 즉시 입장하며 대기 줄에서 사라집니다.
4.  만약 명단에 있는 순서대로 사람을 입장시킬 수 없다면, 입장은 중단됩니다.

두 개의 대기 줄(**A**, **B**)과 목표 명단(**Target**)이 주어졌을 때, 명단에 적힌 순서대로 **모두** 입장시키는 것이 가능한지 판별하는 프로그램을 작성하세요.

가능하다면 `Yes`, 불가능하다면 `No`를 출력합니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 대기 줄 **A**에 서 있는 사람들의 이름이 공백으로 구분되어 주어집니다.
* 두 번째 줄에 대기 줄 **B**에 서 있는 사람들의 이름이 공백으로 구분되어 주어집니다.
* 세 번째 줄에 입장을 희망하는 **Target** 명단의 이름이 공백으로 구분되어 주어집니다.
* 각 줄의 이름 개수는 1개 이상 20개 이하이며, 이름은 영문 소문자로 주어집니다.

## 출력 형식 (Output Format)
* 명단 순서대로 입장이 가능하다면 `Yes`, 불가능하다면 `No`를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
tom amy
john kate
tom john amy kate
{TICK}

**Output:**
{TICK}
Yes
{TICK}

* 줄 A: `[tom, amy]`
* 줄 B: `[john, kate]`
* 목표: `[tom, john, amy, kate]`
* **진행 과정**:
    * 목표 'tom'은 A의 맨 앞에 있음 $\\rightarrow$ 입장 (줄 A 남은 인원: `[amy]`)
    * 목표 'john'은 B의 맨 앞에 있음 $\\rightarrow$ 입장 (줄 B 남은 인원: `[kate]`)
    * 목표 'amy'는 A의 맨 앞에 있음 $\\rightarrow$ 입장 (줄 A 남은 인원: `[]`)
    * 목표 'kate'는 B의 맨 앞에 있음 $\\rightarrow$ 입장 (줄 B 남은 인원: `[]`)
* 순서대로 모두 입장이 가능하므로 `Yes`입니다.

### 예시 2
**Input:**
{TICK}
ann ben
carl dan
ann dan carl
{TICK}

**Output:**
{TICK}
No
{TICK}

* 줄 A: `[ann, ben]`
* 줄 B: `[carl, dan]`
* 목표: `[ann, dan, carl]`
* **진행 과정**:
    * 목표 'ann'은 A의 맨 앞에 있음 $\\rightarrow$ 입장 (줄 A 남은인원: `[ben]`)
    * 다음 목표 'dan' 을 입장시켜야 합니다.
    * 현재 A의 맨 앞은 'ben', B의 맨 앞은 'carl'입니다.
    * 두 줄의 맨 앞 사람 중 누구도 'dan'이 아니므로, 입장이 불가능합니다.

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

    # 대기 줄 A, B와 목표 명단 Target을 큐로 변환
    queue_a = deque(lines[0].split())
    queue_b = deque(lines[1].split())
    target = deque(lines[2].split())
    
    # 목표 명단을 순서대로 하나씩 확인
    for person in target:
        # 1. A 줄의 맨 앞 사람과 일치하는지 확인
        if queue_a and queue_a[0] == person:
            queue_a.popleft()
            
        # 2. B 줄의 맨 앞 사람과 일치하는지 확인
        elif queue_b and queue_b[0] == person:
            queue_b.popleft()
            
        # 3. 둘 다 아니라면 더 이상 진행 불가
        else:
            print("No")
            return
            
    # 반복문이 끝날 때까지 문제가 없었다면 성공
    print("Yes")

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
def solve_internal(a_list, b_list, t_list):
    q1 = deque(a_list)
    q2 = deque(b_list)
    
    for item in t_list:
        if q1 and q1[0] == item:
            q1.popleft()
        elif q2 and q2[0] == item:
            q2.popleft()
        else:
            return "No"
    return "Yes"

# 테스트 데이터 생성 로직
test_data = []

# (1) 예제 케이스 - 이름을 문제 설명과 동일하게 수정
test_data.append((
    ["tom", "amy"], 
    ["john", "kate"], 
    ["tom", "john", "amy", "kate"]
))
test_data.append((
    ["ann", "ben"], 
    ["carl", "dan"], 
    ["ann", "dan", "carl"]
))

# (2) Yes 케이스 생성 (랜덤 병합)
for _ in range(9):
    # 랜덤 이름 생성을 위한 접두사+숫자
    q1 = [f"a{i}" for i in range(random.randint(2, 10))]
    q2 = [f"b{i}" for i in range(random.randint(2, 10))]
    
    # 두 큐를 합치되, 내부 순서는 유지하면서 섞음
    target = []
    idx1, idx2 = 0, 0
    while idx1 < len(q1) and idx2 < len(q2):
        if random.random() < 0.5:
            target.append(q1[idx1])
            idx1 += 1
        else:
            target.append(q2[idx2])
            idx2 += 1
    target.extend(q1[idx1:])
    target.extend(q2[idx2:])
    
    test_data.append((q1, q2, target))

# (3) No 케이스 생성 (순서 꼬기)
for _ in range(9):
    q1 = [f"x{i}" for i in range(random.randint(3, 8))]
    q2 = [f"y{i}" for i in range(random.randint(3, 8))]
    
    # 일단 유효하게 섞음
    target = []
    temp_q1 = q1[:]
    temp_q2 = q2[:]
    while temp_q1 or temp_q2:
        if temp_q1 and (not temp_q2 or random.random() < 0.5):
            target.append(temp_q1.pop(0))
        else:
            target.append(temp_q2.pop(0))
            
    # 고의로 망가뜨리기 (인접한 두 요소의 순서를 바꿈)
    if len(target) >= 2:
        idx = random.randint(0, len(target) - 2)
        target[idx], target[idx+1] = target[idx+1], target[idx]
        
    test_data.append((q1, q2, target))

# 파일 저장
for i, (a, b, t) in enumerate(test_data, 1):
    input_str = f"{' '.join(a)}\n{' '.join(b)}\n{' '.join(t)}"
    ans = solve_internal(a, b, t)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P44' 문제 생성이 완료되었습니다.")