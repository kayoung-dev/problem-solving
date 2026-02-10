import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P076 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P076")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 교수님 오피스 아워 대기 순서 조정

## 문제 설명
상담심리학과 조교 **나래**는 인기 많은 교수님의 오피스 아워 상담 효율을 위해 새로운 대기 시스템을 도입했습니다. 상담실 앞에는 '일반 질문군'과 '긴급 질문군'이라는 두 개의 명단이 있습니다.

교수님은 긴급한 사안을 우선적으로 처리하기를 원하셨기에, 다음과 같은 **$1:3$ 상담 규칙**을 세웠습니다.

1. **상담 비율** 
    - 상담 세트마다 **일반 질문군에서 최대 $1$명**, 그 다음 **긴급 질문군에서 최대 $3$명**의 순서로 오피스에 입장합니다.
2. **순환 처리** 
    - 일반 질문군에서 $1$명이 입장했다면, 긴급 질문군에 대기자가 있는 한 반드시 긴급 질문군 학생을 최대 $3$명까지 연달아 입장시킵니다. 그 후 다시 일반 질문군 $1$명을 입장시키는 과정을 반복합니다.
3. **예외 상황** 
    - 만약 어느 한 쪽 명단이 비어 있다면, 기다릴 필요 없이 다른 명단에 있는 학생들을 원래의 순서대로 계속 입장시킵니다.
4. **대기 순서** 
    - 각 명단 내에서는 먼저 도착하여 이름을 적은 학생이 먼저 상담을 받습니다.

오피스 아워 시작 시점에 두 명단에 적힌 학생들의 정보가 주어질 때, 최종적으로 상담실에 입장하게 되는 학생들의 순서를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 일반 질문군 학생 수 $N$과 긴급 질문군 학생 수 $U$가 공백으로 구분되어 주어집니다. ($0 \le N, U \le 5,000$)
- 두 번째 줄에 일반 질문군 학생들의 이름이 적힌 순서대로 공백으로 구분되어 주어집니다.
- 세 번째 줄에 긴급 질문군 학생들의 이름이 적힌 순서대로 공백으로 구분되어 주어집니다.
- 학생 이름은 영문 대소문자로 구성된 10자 이내의 문자열입니다.

## 출력 형식 (Output Format)
- 상담실에 입장하는 순서대로 학생들의 이름을 공백으로 구분하여 한 줄에 출력합니다.
- 대기 중인 학생이 한 명도 없다면 `EMPTY`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
2 5
Alice Bob
James Mary John Linda Tom
{TICK}

**Output:**
{TICK}
Alice James Mary John Bob Linda Tom
{TICK}

- $1:3$ 규칙에 따라 일반 질문군에서 **Alice**가 먼저 입장합니다.
- 이어서 긴급 질문군에서 최대 3명인 **James, Mary, John**이 연달아 입장합니다.
- 다시 일반 질문군 차례가 되어 **Bob**이 입장합니다.
- 마지막으로 긴급 질문군의 남은 학생들인 **Linda, Tom**이 입장합니다.

### 예시 2
**Input:**
{TICK}
4 2
Katie Minsu Jiwoo Seo
Chris Sarah
{TICK}

**Output:**
{TICK}
Katie Chris Sarah Minsu Jiwoo Seo
{TICK}

- 일반 질문군에서 **Katie**가 먼저 입장합니다.
- 이어서 긴급 질문군에서 **Chris, Sarah**가 모두 입장합니다.
- 긴급 질문군 명단이 비었으므로, 남은 일반 질문군 학생들인 **Minsu, Jiwoo, Seo**가 순서대로 입장합니다.

### 예시 3
**Input:**
{TICK}
0 0
{TICK}

**Output:**
{TICK}
EMPTY
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

# 입력 방식 설정 및 최적화
input = sys.stdin.readline

def solve():
    # 1. N, U 읽기
    first_line = input().split()
    if not first_line:
        return
    n, u = int(first_line[0]), int(first_line[1])
    
    # 2. 학생 명단 읽기 (줄바꿈 및 공백 처리)
    reg_names = input().split()
    urg_names = input().split()
    
    reg_q = deque(reg_names)
    urg_q = deque(urg_names)
    
    results = []
    
    # 3. 1:3 가중치 기반 동기화 로직
    while reg_q or urg_q:
        # 일반 질문군에서 최대 1명 입장
        if reg_q:
            results.append(reg_q.popleft())
            
        # 긴급 질문군에서 최대 3명 입장
        count = 0
        while urg_q and count < 3:
            results.append(urg_q.popleft())
            count += 1
            
    # 4. 결과 일괄 출력
    if not results:
        print("EMPTY")
    else:
        print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(reg, urg):
    rq, uq = deque(reg), deque(urg)
    res = []
    while rq or uq:
        if rq: res.append(rq.popleft())
        c = 0
        while uq and c < 3:
            res.append(uq.popleft())
            c += 1
    return " ".join(res) if res else "EMPTY"

test_data = [
    (["Reg1", "Reg2"], ["Urgent1", "Urgent2", "Urgent3", "Urgent4", "Urgent5"]),
    (["Alice", "Bob", "Charlie", "David"], ["Emergency1", "Emergency2"]),
    ([], [])
]

# 랜덤 데이터 생성 (17개)
names_pool = ["Min", "Ji", "Seo", "Yeon", "Han", "Sung", "Hee", "Ho", "Woo", "Rin"]
for _ in range(17):
    tn = random.randint(0, 30)
    tu = random.randint(0, 30)
    tr = [f"{random.choice(names_pool)}{j}" for j in range(tn)]
    tu_list = [f"Urg{j}" for j in range(tu)]
    test_data.append((tr, tu_list))

for i, (reg, urg) in enumerate(test_data, 1):
    input_str = f"{len(reg)} {len(urg)}\n"
    input_str += " ".join(reg) + "\n"
    input_str += " ".join(urg)
    
    ans = solve_internal(reg, urg)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P076' 문제 생성이 완료되었습니다. ")