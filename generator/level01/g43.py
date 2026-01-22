import os
import random
import sys
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P43)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P43")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 요세푸스의 둥근 탁자

## 문제 설명
고대 역사가 **요세푸스**는 동료들과 함께 둥근 탁자에 둘러앉아 게임을 하고 있습니다. 
$1$번부터 $N$번까지의 사람들이 원을 이루어 앉아 있고, 양의 정수 $K$가 주어집니다.

이제 순서대로 $K$번째 사람을 탁자에서 제외합니다. 한 사람이 제외되면 남은 사람들로 이루어진 원을 따라 이 과정을 반복해 나갑니다. 
이 과정은 $N$명의 사람이 모두 제외될 때까지 계속됩니다.

탁자에서 사람들이 제외되는 순서를 **요세푸스 순열**이라고 합니다. 
예를 들어 $N=7, K=3$일 때의 과정은 다음과 같습니다.
1. `[1, 2, 3, 4, 5, 6, 7]` -> 3번째인 **3** 제거
2. `[4, 5, 6, 7, 1, 2]` -> 3번째인 **6** 제거
3. `[7, 1, 2, 4, 5]` -> 3번째인 **2** 제거
4. ... 이 과정을 반복하면 `<3, 6, 2, 7, 5, 1, 4>` 순서가 됩니다.

$N$과 $K$가 주어질 때, 요세푸스 순열을 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫째 줄에 $N$과 $K$가 빈칸을 사이에 두고 주어집니다. ($1 \\le K \\le N \\le 5,000$)

## 출력 형식 (Output Format)
* 요세푸스 순열을 다음 형식으로 출력합니다.
* `<`로 시작해서 `, `(쉼표+공백)로 구분된 번호들을 출력하고 `>`로 닫습니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
7 3
{TICK}

**Output:**
{TICK}
<3, 6, 2, 7, 5, 1, 4>
{TICK}

### 예시 2
**Input:**
{TICK}
5 2
{TICK}

**Output:**
{TICK}
<2, 4, 1, 5, 3>
{TICK}

* **1회차**: 2번째 사람인 **2**를 제거합니다. (남은 인원: `[3, 4, 5, 1]`)
* **2회차**: 2번째 사람인 **4**를 제거합니다. (남은 인원: `[5, 1, 3]`)
* **3회차**: 2번째 사람인 **1**을 제거합니다. (남은 인원: `[3, 5]`)
* **4회차**: 2번째 사람인 **5**를 제거합니다. (남은 인원: `[3]`)
* **5회차**: 마지막 남은 **3**을 제거합니다.
* **결과**: 제거된 순서대로 `<2, 4, 1, 5, 3>`이 됩니다.
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
    line = sys.stdin.readline().split()
    if not line:
        return
    n, k = map(int, line)

    # 1부터 N까지 큐에 삽입
    queue = deque(range(1, n + 1))
    result = []

    # 큐가 빌 때까지 반복
    while queue:
        # K-1번만큼 앞에서 꺼내서 뒤로 보냄 (회전)
        for _ in range(k - 1):
            queue.append(queue.popleft())
        
        # K번째 사람(현재 맨 앞)을 제거하여 결과 리스트에 추가
        result.append(str(queue.popleft()))
    
    # 형식에 맞춰 출력 (<3, 6, ...>)
    sys.stdout.write("<" + ", ".join(result) + ">\\n")

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(n, k):
    q = deque(range(1, n + 1))
    res = []
    while q:
        for _ in range(k - 1):
            q.append(q.popleft())
        res.append(str(q.popleft()))
    return "<" + ", ".join(res) + ">"

test_cases = [
    (7, 3), (5, 2), # 예제
    (1, 1), # 최소값
    (10, 1), # K=1인 경우 (순서대로 나옴)
    (10, 10), # N=K인 경우
]

# 랜덤 케이스 추가 (총 20개 채우기)
while len(test_cases) < 20:
    n_val = random.randint(10, 5000)
    k_val = random.randint(1, n_val)
    # 중복 방지
    if (n_val, k_val) not in test_cases:
        test_cases.append((n_val, k_val))

# 파일 저장
for i, (n, k) in enumerate(test_cases, 1):
    inp = f"{n} {k}"
    ans = solve_internal(n, k)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P43' 문제 생성이 완료되었습니다.")