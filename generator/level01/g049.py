import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P49 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P049")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 꼬마 유령들의 술래잡기

## 문제 설명
숲속의 꼬마 유령들이 모여서 특별한 술래잡기 게임을 하려고 합니다. $N$마리의 유령들이 $1$번부터 $N$번까지 번호표를 달고 동그랗게 둘러앉아 있습니다.

게임의 규칙은 다음과 같습니다:
1. 유령들은 시계 방향 순서대로 앉아 있으며, $1$번 유령부터 숫자를 세기 시작합니다.
2. 매번 $K$번째 유령이 술래가 되어 원 밖으로 나갑니다.
3. 한 유령이 나가면, **그다음 유령부터** 다시 숫자를 세어 $K$번째 유령을 찾습니다.
4. 원에 유령이 한 마리도 남지 않을 때까지 이 과정을 반복합니다.

유령들이 원을 떠나는 순서대로 번호를 나열한 것을 **'술래잡기 순열'** 이라고 합니다. $N$과 $K$가 주어질 때, 이 순열을 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 유령의 수 $N$과 세는 단위인 정수 $K$가 공백으로 구분되어 주어집니다.
* ($1 \le K \le N \le 1,000$)

## 출력 형식 (Output Format)
* 유령들이 나가는 순서대로 번호를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
7 3
{TICK}

**Output:**
{TICK}
3 6 2 7 5 1 4
{TICK}

**설명:**
- `[1, 2, 3, 4, 5, 6, 7]` 에서 3번째인 **3** 제거
- `[4, 5, 6, 7, 1, 2]` 에서 3번째인 **6** 제거
- `[7, 1, 2, 4, 5]` 에서 3번째인 **2** 제거
- `[4, 5, 7, 1]` 에서 3번째인 **7** 제거
- `[1, 4, 5]` 에서 3번째인 **5** 제거
- `[1, 4]` 에서 3번째인 **1** 제거 (3번째는 1번째와 같습니다)
- 마지막 4 제거

### 예시 2
**Input:**
{TICK}
5 2
{TICK}

**Output:**
{TICK}
2 4 1 5 3
{TICK}

* 매번 2번째에 위치한 유령이 나갑니다.
* `[1, 2, 3, 4, 5]` 에서 2번째인 **2** 제거
* `[3, 4, 5, 1]` 에서 2번째인 **4** 제거
* `[5, 1, 3]` 에서 2번째인 **1** 제거
* `[3, 5]` 에서 2번째인 **5** 제거
* `[3]` 에서 2번째인 **3** 제거
### 예시 3
**Input:**
{TICK}
3 1
{TICK}

**Output:**
{TICK}
1 2 3
{TICK}

* 매번 1번째 유령이 바로 나가게 되므로, 앉아있는 순서대로인 1, 2, 3이 출력됩니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_content = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, k = int(input_data[0]), int(input_data[1])
    
    # 1번부터 N번까지 유령들을 큐에 삽입
    q = deque(range(1, n + 1))
    result = []
    
    while q:
        # K-1번만큼 앞에서 빼서 뒤로 보냄 (회전)
        for _ in range(k - 1):
            q.append(q.popleft())
        
        # K번째 유령을 확정적으로 제거
        result.append(str(q.popleft()))
    
    # 순열 출력
    print(" ".join(result))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(n, k):
    from collections import deque
    q = deque(range(1, n + 1))
    res = []
    while q:
        for _ in range(k - 1):
            q.append(q.popleft())
        res.append(str(q.popleft()))
    return " ".join(res)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

# 테스트 데이터 생성
test_cases = [
    (7, 3), (5, 2), (3, 1), (10, 5), (6, 2),
    (1, 1), (10, 1), (2, 2), (5, 5), (10, 3)
]

# 나머지 10개 랜덤 생성
for _ in range(10):
    tn = random.randint(10, 100)
    tk = random.randint(1, tn)
    test_cases.append((tn, tk))

for i, (n, k) in enumerate(test_cases, 1):
    input_str = f"{n} {k}"
    ans = solve_internal(n, k)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P049' 문제 생성이 완료되었습니다.")