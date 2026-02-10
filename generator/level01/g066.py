import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P066 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P066")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = """# 학식의 3단 배식 전쟁

## 문제 설명
두동대학교 점심시간, $N$명의 학생들이 학식 맛집으로 소문난 '학생 식당'에 줄을 섰습니다. 이 식당의 배식 구조는 효율성을 위해 3단계 코너로 나누어져 있습니다.

1. **1코너 (밥 & 국):** 식판을 들고 밥과 국을 받습니다. (소요시간 $A$)
2. **2코너 (메인 반찬):** 영양사님에게 맛있는 메인 반찬을 배식받습니다. (소요시간 $B$)
3. **3코너 (디저트):** 후식 음료나 과일을 챙깁니다. (소요시간 $C$)

모든 학생은 반드시 1코너 $\\rightarrow$ 2코너 $\\rightarrow$ 3코너 순서대로 이동해야 하며, 각 코너는 한 번에 한 명의 학생만 이용할 수 있습니다.

$i$번째 학생이 $k$코너에서 배식을 시작하려면 다음 두 가지 조건이 모두 충족되어야 합니다.

1. **내 이전 단계 완료:** $i$번째 학생이 $k-1$코너에서의 배식을 마쳐야 다음 코너로 갈 수 있습니다.
2. **앞사람 이동 완료:** $i-1$번째 학생이 $k$코너 이용을 마쳐서 자리가 비어야 들어갈 수 있습니다.

즉, 특정 코너의 시작 시각은 **내가 이전 코너에서 나온 시각**과 **앞사람이 이 코너에서 나간 시각** 중 **더 늦은 시간**이 됩니다.

$N$명의 학생에 대해 각 코너별 소요 시간이 주어질 때, 각 학생이 **3코너까지 모든 배식을 마치고 식당 홀로 나가는 시각**을 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 줄을 선 학생의 수 $N$이 주어집니다. ($1 \le N \le 1,000$)
- 두 번째 줄에 각 학생의 1코너 소요 시간 $A_1, A_2, \dots, A_N$이 공백으로 구분되어 주어집니다.
- 세 번째 줄에 각 학생의 2코너 소요 시간 $B_1, B_2, \dots, B_N$이 공백으로 구분되어 주어집니다.
- 네 번째 줄에 각 학생의 3코너 소요 시간 $C_1, C_2, \dots, C_N$이 공백으로 구분되어 주어집니다.
- (모든 소요 시간은 $1$ 이상 $100$ 이하의 정수입니다.)

## 출력 형식 (Output Format)
- 각 학생이 모든 배식을 마치는 시각을 순서대로 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
2
10 5
5 10
5 10
{TICK}

**Output:**
{TICK}
20 35
{TICK}

- **1번 학생:** 
  - 1코너(10초 완료)
  - 2코너(15초 완료)
  - 3코너(20초 완료)
- **2번 학생:**
  - 1코너: 1번이 10초에 비켜줌. (10초) + 5초 = 15초 완료.
  - 2코너: 1코너를 15초에 마쳤고, 1번도 2코너를 15초에 마침. 15초 시작 + 10초 = 25초 완료.
  - 3코너: 2코너를 25초에 마쳤지만, 1번은 3코너를 20초에 이미 비웠음. 25초 시작 + 10초 = 35초 완료.

### 예시 2
**Input:**
{TICK}
3
4 2 6
5 3 2
2 4 3
{TICK}

**Output:**
{TICK}
11 16 19
{TICK}

- **1번 학생** 
  - 4+5+2 = 11초 완료.
- **2번 학생**
  - 1코너: 4초(1번 완료 후) + 2초 = 6초.
  - 2코너: 대기(내 1코너 6초, 앞 2코너 9초) = 9초 시작 + 3초 = 12초.
  - 3코너: 진입(내 2코너 12초, 앞 3코너 11초) = 12초 시작 + 4초 = 16초.
- **3번 학생**
  - 1코너: 6초 시작 + 6초 = 12초
  - 2코너: 진입 = 12초 시작 + 2초 = 14초
  - 3코너: 대기 = 16초 + 3초 = 19초

### 예시 3
**Input:**
{TICK}
1
10
10
10
{TICK}

**Output:**
{TICK}
30
{TICK}
"""

problem_md = problem_template.replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    
    # 데이터 파싱
    line_a = list(map(int, input_data[1:1+n]))
    line_b = list(map(int, input_data[1+n:1+2*n]))
    line_c = list(map(int, input_data[1+2*n:1+3*n]))
    
    # 이전 학생의 각 코너 완료 시각 (초기값 0)
    prev_end_a = 0
    prev_end_b = 0
    prev_end_c = 0
    
    results = []
    
    for i in range(n):
        # 1코너: 앞사람이 비워줘야 시작 (prev_end_a) + 내 소요시간
        curr_end_a = prev_end_a + line_a[i]
        
        # 2코너: 내가 1코너에서 와야 하고(curr_end_a), 앞사람이 2코너를 비워줘야 함(prev_end_b)
        curr_end_b = max(curr_end_a, prev_end_b) + line_b[i]
        
        # 3코너: 내가 2코너에서 와야 하고(curr_end_b), 앞사람이 3코너를 비워줘야 함(prev_end_c)
        curr_end_c = max(curr_end_b, prev_end_c) + line_c[i]
        
        results.append(str(curr_end_c))
        
        # 다음 학생을 위해 완료 시간 갱신
        prev_end_a = curr_end_a
        prev_end_b = curr_end_b
        prev_end_c = curr_end_c
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, a, b, c):
    # 이전 학생의 각 코너 완료 시각 (초기값 0)
    prev_end_a = 0
    prev_end_b = 0
    prev_end_c = 0
    
    results = []
    
    for i in range(n):
        # 1코너: 앞사람 완료(prev_end_a) + 내 소요시간
        curr_end_a = prev_end_a + a[i]
        
        # 2코너: max(내 1코너 완료, 앞사람 2코너 완료) + 내 소요시간
        curr_end_b = max(curr_end_a, prev_end_b) + b[i]
        
        # 3코너: max(내 2코너 완료, 앞사람 3코너 완료) + 내 소요시간
        curr_end_c = max(curr_end_b, prev_end_c) + c[i]
        
        results.append(str(curr_end_c))
        
        # 다음 학생을 위해 완료 시간 갱신
        prev_end_a = curr_end_a
        prev_end_b = curr_end_b
        prev_end_c = curr_end_c
        
    return " ".join(results)

test_data = []

# [예시 1]
test_data.append((2, [10, 5], [5, 10], [5, 10]))

# [예시 2] (수정된 로직: 11 16 19)
test_data.append((3, [4, 2, 6], [5, 3, 2], [2, 4, 3]))

# [예시 3]
test_data.append((1, [10], [10], [10]))

# [랜덤 케이스] 17개 추가 (총 20개)
for _ in range(17):
    n = random.randint(5, 50)
    # 소요시간 1~20 사이 랜덤
    ta = [random.randint(1, 20) for _ in range(n)]
    tb = [random.randint(1, 20) for _ in range(n)]
    tc = [random.randint(1, 20) for _ in range(n)]
    test_data.append((n, ta, tb, tc))

# 파일 저장 루프
for i, (n, a, b, c) in enumerate(test_data, 1):
    input_str = f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}\n{' '.join(map(str, c))}"
    ans = solve_internal(n, a, b, c)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P066' 문제 생성이 완료되었습니다. ")