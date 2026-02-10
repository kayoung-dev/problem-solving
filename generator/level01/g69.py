import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P69 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P69")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""#커플 라이드 매칭

## 문제 설명
대학교 축제의 하이라이트인 '커플 라이드'는 두 명의 학생이 모여야만 출발할 수 있는 놀이기구입니다. 이 기구는 공정한 매칭을 위해 **'청팀(Blue)'** 전용 줄과 **'백팀(White)'** 전용 줄을 따로 운영합니다.

매칭 규칙은 다음과 같습니다.

1. 기구 앞에 청팀 줄과 백팀 줄이 각각 존재하며, 처음에는 두 줄 모두 비어 있습니다.
2. 학생들은 자신의 소속 팀 정보와 이름을 가지고 있습니다. 
3. **매칭 시도:** 학생이 도착했을 때, **반대편 팀 줄**에 기다리고 있는 사람이 있다면 즉시 맨 앞사람과 짝이 되어 기구에 탑승합니다.
4. **대기:** 만약 반대편 팀 줄이 비어 있다면, 해당 학생은 자신의 팀 줄 맨 뒤에 서서 파트너가 올 때까지 기다려야 합니다.

축제 기간 동안 도착한 학생들의 명단이 순서대로 주어질 때, **최종적으로 매칭되어 탑승한 커플들의 목록**을 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 도착한 총 학생 수 $N$이 주어집니다. ($1 \le N \le 1,000$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 각 학생의 소속 팀($B$ 또는 $W$)과 이름이 공백으로 구분되어 도착한 순서대로 주어집니다. 
- 이름은 영문 대소문자로 구성된 $10$자 이내의 문자열입니다.

## 출력 형식 (Output Format)
- 매칭이 성공할 때마다 `(청팀 이름) - (백팀 이름)` 형식으로 한 줄씩 출력합니다.
- 마지막에 `Remaining: (남은 학생 수)명`을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
B Alice
B Bob
W Charlie
W Dave
{TICK}

**Output:**
{TICK}
Alice - Charlie
Bob - Dave
Remaining: 0명
{TICK}

- Alice(B) 도착: W 줄이 비었으므로 B 줄 대기. 
  - B: [Alice], W: []
- Bob(B) 도착: W 줄이 비었으므로 B 줄 대기.
  - B: [Alice, Bob], W: []
- Charlie(W) 도착: B 줄 맨 앞의 Alice와 매칭!
  - B: [Bob], W: []
- Dave(W) 도착: B 줄 맨 앞의 Bob과 매칭!
  - B: [], W: []

### 예시 2
**Input:**
{TICK}
5
W Tom
W Jerry
B Mickey
W Donald
B Goofy
{TICK}

**Output:**
{TICK}
Mickey - Tom
Goofy - Jerry
Remaining: 1명
{TICK}

- Tom(W), Jerry(W) 도착: W 줄 대기.
  - B: [], W: [Tom, Jerry]
- Mickey(B) 도착: W 줄 맨 앞 Tom과 매칭!
  - B: [], W: [Jerry]
- Donald(W) 도착: B 줄이 비었으므로 W 줄 대기.
  - B: [], W: [Jerry, Donald]
- Goofy(B) 도착: W 줄 맨 앞 Jerry와 매칭!
  - B: [], W: [Donald]
- 최종적으로 Donald가 W 줄에 혼자 남습니다.

### 예시 3
**Input:**
{TICK}
3
B Kim
B Lee
B Park
{TICK}

**Output:**
{TICK}
Remaining: 3명
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

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    students = []
    idx = 1
    for _ in range(n):
        students.append((input_data[idx], input_data[idx+1]))
        idx += 2
        
    blue_q = deque()
    white_q = deque()
    
    for team, name in students:
        if team == 'B':
            if white_q:
                partner = white_q.popleft()
                print(f"{name} - {partner}")
            else:
                blue_q.append(name)
        else: # team == 'W'
            if blue_q:
                partner = blue_q.popleft()
                print(f"{partner} - {name}")
            else:
                white_q.append(name)
                
    remaining = len(blue_q) + len(white_q)
    print(f"Remaining: {remaining}명")

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, students):
    blue_q = deque()
    white_q = deque()
    res = []
    for team, name in students:
        if team == 'B':
            if white_q:
                partner = white_q.popleft()
                res.append(f"{name} - {partner}")
            else:
                blue_q.append(name)
        else:
            if blue_q:
                partner = blue_q.popleft()
                res.append(f"{partner} - {name}")
            else:
                white_q.append(name)
    rem = len(blue_q) + len(white_q)
    res.append(f"Remaining: {rem}명")
    return "\n".join(res)

names_pool = ["Alex", "Blake", "Casey", "Drew", "Erin", "Finn", "Gail", "Hope", "Ivan", "Jade", "Kyle", "Lune", "Mina", "Nate", "Owen", "Pia", "Quinn", "Rose", "Seth", "Tess"]

test_data = [
    (4, [('B', 'Alice'), ('B', 'Bob'), ('W', 'Charlie'), ('W', 'Dave')]),
    (5, [('W', 'Tom'), ('W', 'Jerry'), ('B', 'Mickey'), ('W', 'Donald'), ('B', 'Goofy')]),
    (3, [('B', 'Kim'), ('B', 'Lee'), ('B', 'Park')])
]

# 랜덤 케이스 17개 생성
for _ in range(17):
    tn = random.randint(5, 50)
    tstudents = []
    for _ in range(tn):
        team = random.choice(['B', 'W'])
        name = random.choice(names_pool) + str(random.randint(1, 99))
        tstudents.append((team, name))
    test_data.append((tn, tstudents))

for i, (n, students) in enumerate(test_data, 1):
    input_str = f"{n}\n" + "\n".join([f"{t} {name}" for t, name in students])
    ans = solve_internal(n, students)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P69' 문제 생성이 완료되었습니다.")