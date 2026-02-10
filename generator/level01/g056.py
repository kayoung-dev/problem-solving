import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P056 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P056")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 정수기 앞의 매너 있는 물병 채우기

## 문제 설명
등산로 입구의 정수기 앞에 사람들이 물을 받기 위해 줄을 서 있습니다. 어떤 사람은 물병을 한개만 가져왔지만, 어떤 사람은 큰 물통을 여러 개 가져오기도 했습니다. 뒤에 서 있는 사람들을 배려하여, 정수기에는 다음과 같은 **매너 규칙**이 적혀 있습니다.

1. 사람들은 처음에 도착한 순서대로 줄을 섭니다.
2. 한 번 정수기 앞에 서면 **최대 K리터**까지만 물을 받을 수 있습니다.
3. 만약 받아야 할 물이 더 남았다면, 남은 물통을 들고 다시 대기 줄의 **맨 끝**으로 가서 차례를 기다려야 합니다.
4. 물을 다 받은 사람은 집으로 돌아갑니다. 그 다음 순서의 사람이 바로 물을 받기 시작합니다.

각 사람이 총 몇 리터의 물을 받아야 하는지 주어질 때, 사람들이 물을 다 채우고 떠나는 순서를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 줄을 선 사람의 수 N과 한 번에 받을 수 있는 최대 양 K가 공백으로 구분되어 주어집니다. (1 <= N, K <= 100)
- 두 번째 줄에 1번 사람부터 순서대로 각자 채워야 할 총 물의 양(리터)이 주어집니다.

## 출력 형식 (Output Format)
- 물을 모두 채우고 떠나는 사람의 번호를 순서대로 공백으로 구분하여 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 2
4 1 2
{TICK}

**Output:**
{TICK}
2 3 1
{TICK}

- 한 번에 최대 2리터(K=2)씩 받을 수 있습니다.
- 처음 줄: [1번(4L), 2번(1L), 3번(2L)]
- 1단계: 1번이 2L를 받음. 2L가 남았으므로 줄 끝으로 이동. 
  - 줄: [2번(1L), 3번(2L), 1번(2L)]
- 2단계: 2번이 1L를 받음. 모두 채웠으므로 귀가. -> **2번 퇴장**
  - 줄: [3번(2L), 1번(2L)] 
- 3단계: 3번이 2L를 받음. 모두 채웠으므로 귀가. -> **3번 퇴장**
  - 줄: [1번(2L)] 
- 4단계: 1번이 남은 2L를 받음. 모두 채웠으므로 귀가. -> **1번 퇴장**

### 예시 2
**Input:**
{TICK}
4 3
2 8 1 5
{TICK}

**Output:**
{TICK}
1 3 4 2
{TICK}

### 예시 3
**Input:**
{TICK}
3 4
2 9 3
{TICK}

**Output:**
{TICK}
1 3 2
{TICK}

- 한 번에 최대 4리터(K=4)씩 받을 수 있습니다.
- 처음 줄: [1번(2L), 2번(9L), 3번(3L)]
- 1단계: 1번이 2L를 받음. 모두 채웠으므로 귀가. -> 1 출력
  - 줄: [2번(9L), 3번(3L)]
- 2단계: 2번이 4L를 받음. 아직 5L가 남았으므로 줄 끝으로 이동 
  - 줄: [3번(3L), 2번(5L)]
- 3단계: 3번이 3L를 받음. 모두 채웠으므로 귀가. -> 3번 출력
  - 줄: [2번(5L)]
- 4단계: 2번이 4L를 받음. 아직 1L가 남았으므로 줄 끝으로 이동
  - 줄: [2번(1L)]
- 5단계: 2번이 1L를 받음. 모두 채웠으므로 귀가. -> 2번 출력

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
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # (사람 번호, 남은 물의 양)을 저장할 공간
    waiting_line = deque()
    for i in range(n):
        waiting_line.append((i + 1, int(input_data[2 + i])))
        
    finished_order = []
    
    while waiting_line:
        person_id, remaining_water = waiting_line.popleft()
        
        # 이번 차례에 받을 물의 양 (K와 남은 양 중 작은 값)
        fill_amount = min(remaining_water, k)
        new_remaining = remaining_water - fill_amount
        
        if new_remaining > 0:
            # 물이 더 남았다면 줄의 맨 뒤로
            waiting_line.append((person_id, new_remaining))
        else:
            # 다 채웠다면 순서 기록
            finished_order.append(str(person_id))
            
    print(" ".join(finished_order))

if __name__ == "__main__":
    solve()
"""
# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k, waters):
    from collections import deque
    dq = deque([(i+1, w) for i, w in enumerate(waters)])
    res = []
    while dq:
        pid, rem = dq.popleft()
        fill = min(rem, k)
        if rem - fill > 0:
            dq.append((pid, rem - fill))
        else:
            res.append(str(pid))
    return " ".join(res)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (3, 2, [4, 1, 2]),
    (4, 3, [2, 8, 1, 5]),
]

for _ in range(18):
    tn = random.randint(3, 20)
    tk = random.randint(1, 10)
    twaters = [random.randint(1, 30) for _ in range(tn)]
    test_cases.append((tn, tk, twaters))

for i, (n, k, waters) in enumerate(test_cases, 1):
    input_str = f"{n} {k}\n" + " ".join(map(str, waters))
    ans = solve_internal(n, k, waters)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P056' 문제 생성이 완료되었습니다. ")