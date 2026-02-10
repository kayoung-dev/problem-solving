import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P060 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P060")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 스마트 물류 센터의 라인 분배

## 문제 설명
스마트 물류 센터의 중앙 제어 시스템을 설계하고 있습니다. 컨베이어 벨트를 통해 들어오는 물품들은 효율적인 처리를 위해 여러 개의 서브 라인(Sub-line)으로 분배되어야 합니다.

시스템은 다음과 같은 규칙으로 물품을 분배합니다.

1. 물류 센터에는 총 $M$개의 서브 라인이 있으며, 각 라인은 독립적인 큐(Queue)를 가지고 있습니다. 라인 번호는 0번부터 $M-1$번까지입니다.
2. 물품은 고유 번호(ID)를 가지고 들어옵니다.
3. 물품 분배 규칙은 **"물품 ID % M"** 연산을 통해 결정됩니다. 
   - 결과가 0이면 0번 라인으로, 1이면 1번 라인으로 보내집니다.
4. 모든 물품이 분배된 후, 각 라인에 쌓인 물품들의 ID를 순서대로 확인해야 합니다.

입력된 물품들을 규칙에 따라 분배하고, 각 라인의 최종 상태를 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 물품의 개수 $N$과 서브 라인의 개수 $M$이 공백으로 구분되어 주어집니다. ($1 \le N \le 1,000$, $1 \le M \le 20$)
- 두 번째 줄에 $N$개의 물품 ID가 들어온 순서대로 공백으로 구분되어 주어집니다.

## 출력 형식 (Output Format)
- 0번 라인부터 $M-1$번 라인까지, 각 라인에 쌓인 물품 ID를 한 줄씩 출력합니다.
- 만약 특정 라인에 물품이 하나도 없다면 `Empty`를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6 3
10 11 12 13 14 15
{TICK}

**Output:**
{TICK}
Line 0: 12 15
Line 1: 10 13
Line 2: 11 14
{TICK}

- 10 % 3 = 1 -> Line 1
- 11 % 3 = 2 -> Line 2
- 12 % 3 = 0 -> Line 0
- 13 % 3 = 1 -> Line 1
- 14 % 3 = 2 -> Line 2
- 15 % 3 = 0 -> Line 0

### 예시 2
**Input:**
{TICK}
3 5
5 10 15
{TICK}

**Output:**
{TICK}
Line 0: 5 10 15
Line 1: Empty
Line 2: Empty
Line 3: Empty
Line 4: Empty
{TICK}
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
    m = int(input_data[1])
    item_ids = list(map(int, input_data[2:2+n]))
    
    # M개의 큐(라인) 생성
    lines = [deque() for _ in range(m)]
    
    # 규칙에 따라 분배
    for item_id in item_ids:
        line_idx = item_id % m
        lines[line_idx].append(item_id)
        
    # 결과 출력
    for i in range(m):
        if not lines[i]:
            print(f"Line {i}: Empty")
        else:
            print(f"Line {i}: {' '.join(map(str, lines[i]))}")

if __name__ == "__main__":
    solve()
"""
# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, m, ids):
    lines = [[] for _ in range(m)]
    for item_id in ids:
        lines[item_id % m].append(str(item_id))
    
    output = []
    for i in range(m):
        if not lines[i]:
            output.append(f"Line {i}: Empty")
        else:
            output.append(f"Line {i}: {' '.join(lines[i])}")
    return "\n".join(output)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (6, 3, [10, 11, 12, 13, 14, 15]),
    (3, 5, [5, 10, 15]),
]

for _ in range(18):
    tn = random.randint(10, 100)
    tm = random.randint(2, 10)
    tids = [random.randint(1, 1000) for _ in range(tn)]
    test_cases.append((tn, tm, tids))

for i, (n, m, ids) in enumerate(test_cases, 1):
    input_str = f"{n} {m}\n" + " ".join(map(str, ids))
    ans = solve_internal(n, m, ids)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P060' 문제 생성이 완료되었습니다. ")