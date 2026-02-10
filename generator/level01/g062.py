import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P062 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P062")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
# 수정 사항: f-string 대신 일반 문자열을 사용하여 LaTeX 중괄호 충돌 방지
problem_template = """# 우체국장 베리의 줄 세우기

## 문제 설명
우체국장 '베리'는 두 개의 창구($A$와 $B$) 앞에 늘어선 대기열이 불공평하게 길어지는 것을 매우 싫어합니다. 베리는 두 줄의 인원수 차이가 $1$보다 커지면, 더 긴 줄의 **맨 앞사람**을 다른 줄의 **맨 뒷자리**로 옮겨 균형을 맞춥니다.

베리의 줄 세우기 규칙은 다음과 같습니다:
1. 두 줄의 인원수를 각각 $L_A$와 $L_B$라고 할 때, $|L_A - L_B| \le 1$이 될 때까지 다음 과정을 반복합니다.
2. 만약 $L_A > L_B + 1$ 이라면, $A$ 줄의 가장 앞에 있는 사람을 꺼내 $B$ 줄의 가장 뒤에 세웁니다.
3. 만약 $L_B > L_A + 1$ 이라면, $B$ 줄의 가장 앞에 있는 사람을 꺼내 $A$ 줄의 가장 뒤에 세웁니다.
4. 모든 이동은 한 번에 한 명씩 차례대로 일어납니다.

처음 두 창구의 대기열 상태가 주어질 때, 베리의 관리가 끝난 후 두 줄의 최종 상태를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 $A$ 줄의 인원수 $N_A$와 $B$ 줄의 인원수 $N_B$가 공백으로 구분되어 주어집니다. ($0 \le N_A, N_B \le 500$)
- 두 번째 줄에 $A$ 줄에 서 있는 사람들의 이름이 공백으로 구분되어 주어집니다. ($N_A=0$이면 빈 줄입니다.)
- 세 번째 줄에 $B$ 줄에 서 있는 사람들의 이름이 공백으로 구분되어 주어집니다. ($N_B=0$이면 빈 줄입니다.)

## 출력 형식 (Output Format)
- 첫 번째 줄에 최종 $A$ 줄의 상태를 이름 사이 공백을 두어 출력합니다.
- 두 번째 줄에 최종 $B$ 줄의 상태를 이름 사이 공백을 두어 출력합니다.
- 줄이 비어있다면 `Empty`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 1
Alice Bob Charlie Dave Eve
Frank
{TICK}

**Output:**
{TICK}
Charlie Dave Eve
Frank Alice Bob
{TICK}

- 초기 상태
  - $A = [\\text{Alice, Bob, Charlie, Dave, Eve}]$
  - $B = [\\text{Frank}]$ 
  - ($5:1$ 차이 $4$)
- 1차 이동
  - $A$ 앞의 Alice를 $B$ 뒤로. 
  - $A = [\\text{Bob, Charlie, Dave, Eve}]$
  - $B = [\\text{Frank, Alice}]$ 
  - ($4:2$ 차이 $2$)
- 2차 이동
  - $A$ 앞의 Bob을 $B$ 뒤로. 
  - $A = [\\text{Charlie, Dave, Eve}]$
  - $B = [\\text{Frank, Alice, Bob}]$ 
  - ($3:3$ 차이 $0$)
- 차이가 $1$ 이하이므로 종료.

### 예시 2
**Input:**
{TICK}
1 4
Tom
Jerry Mickey Donald Goofy
{TICK}

**Output:**
{TICK}
Tom Jerry
Mickey Donald Goofy
{TICK}

- 초기 상태 
  - $1:4$ (차이 $3$)
- $B$ 앞의 Jerry를 $A$ 뒤로 이동
  - $A = [\\text{Tom, Jerry}]$
  - $B = [\\text{Mickey, Donald, Goofy}]$ 
  - ($2:3$ 차이 $1$)
- 차이가 $1$ 이하이므로 종료.

### 예시 3
**Input:**
{TICK}
2 2
Pikachu Raichu
Charmander Squirtle
{TICK}

**Output:**
{TICK}
Pikachu Raichu
Charmander Squirtle
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
    input_data = sys.stdin.read().splitlines()
    if not input_data: return
    
    first_line = input_data[0].split()
    n_a, n_b = int(first_line[0]), int(first_line[1])
    
    line_a = deque()
    line_b = deque()
    
    if n_a > 0 and len(input_data) > 1:
        line_a = deque(input_data[1].split())
        
    # line_b의 데이터 위치는 n_a의 존재 여부에 따라 달라질 수 있음
    # 안전하게 파싱하기 위해 모든 라인을 읽고 처리
    current_line_idx = 2
    if n_a == 0:
        current_line_idx = 1
        
    if n_b > 0 and len(input_data) > current_line_idx:
        line_b = deque(input_data[current_line_idx].split())
    
    while abs(len(line_a) - len(line_b)) > 1:
        if len(line_a) > len(line_b):
            person = line_a.popleft()
            line_b.append(person)
        else:
            person = line_b.popleft()
            line_a.append(person)
            
    print(" ".join(line_a) if line_a else "Empty")
    print(" ".join(line_b) if line_b else "Empty")

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n_a, n_b, a_list, b_list):
    line_a = deque(a_list)
    line_b = deque(b_list)
    while abs(len(line_a) - len(line_b)) > 1:
        if len(line_a) > len(line_b):
            line_b.append(line_a.popleft())
        else:
            line_a.append(line_b.popleft())
    
    res_a = " ".join(line_a) if line_a else "Empty"
    res_b = " ".join(line_b) if line_b else "Empty"
    return f"{res_a}\n{res_b}"

names = ["Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Cho", "Yoon", "Jang", "Lim", "Han", "Oh", "Seo", "Shin", "Kwon", "Hwang", "An", "Song", "Ryu", "Jeon"]

test_data = []
# 예시 케이스 3개
test_data.append((5, 1, ["Alice", "Bob", "Charlie", "Dave", "Eve"], ["Frank"]))
test_data.append((1, 4, ["Tom"], ["Jerry", "Mickey", "Donald", "Goofy"]))
test_data.append((2, 2, ["Pikachu", "Raichu"], ["Charmander", "Squirtle"]))

# 랜덤 케이스 17개 생성
for _ in range(17):
    na = random.randint(0, 20)
    nb = random.randint(0, 20)
    la = [random.choice(names) + str(i) for i in range(na)]
    lb = [random.choice(names) + str(i) for i in range(nb)]
    test_data.append((na, nb, la, lb))

for i, (na, nb, la, lb) in enumerate(test_data, 1):
    input_str = ""
    # 입력 형식 맞추기 (빈 줄 고려)
    input_str += f"{na} {nb}"
    if na > 0:
        input_str += f"\n{' '.join(la)}"
    else:
        input_str += "\n" # 빈 줄
        
    if nb > 0:
        input_str += f"\n{' '.join(lb)}"
    else:
        input_str += "\n" # 빈 줄

    ans = solve_internal(na, nb, la, lb)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P062' 문제 생성이 완료되었습니다. ")