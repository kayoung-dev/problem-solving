import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P53 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P053")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 인터넷 공유기의 패킷 보관함

## 문제 설명
IT 전문가 민수는 인터넷 공유기의 성능을 최적화하고 있습니다. 공유기에는 외부에서 들어오는 데이터(패킷)를 잠시 저장해두는 보관함이 있는데, 이 보관함의 크기는 제한되어 있습니다. 민수는 보관함이 가득 찼을 때 가장 효율적으로 데이터를 처리하기 위해 다음과 같은 규칙을 세웠습니다.

1. 보관함은 최대 S개의 데이터만 담을 수 있습니다.
2. 새로운 데이터가 들어올 때의 규칙은 다음과 같습니다.
   - 보관함에 빈 자리가 있다면, 새로운 데이터를 맨 뒤에 추가합니다.
   - 보관함이 이미 가득 차 있다면, 보관함에 들어있는 데이터 중 가장 오래된 것(맨 앞의 것)을 하나 버리고, 그 자리에 새로운 데이터를 추가합니다.
3. 처리 명령(P)이 들어올 때의 규칙은 다음과 같습니다.
   - 보관함에 데이터가 있다면, 가장 오래된 데이터 하나를 꺼내서 처리합니다.
   - 보관함이 비어 있다면, 아무 일도 일어나지 않습니다.

민수가 모든 데이터를 받고 처리 명령을 수행한 뒤, 마지막에 보관함에 남아있는 데이터들은 무엇인지 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 보관함의 크기 S와 수행할 작업의 총 횟수 N이 공백으로 구분되어 주어집니다. (1 <= S <= 100, 1 <= N <= 1,000)
- 두 번째 줄부터 N개의 작업이 순서대로 주어집니다.
  - 숫자가 주어지면 해당 번호를 가진 데이터가 들어온 것입니다.
  - 문자 'P'가 주어지면 현재 보관함에서 가장 오래된 데이터를 하나 처리하여 꺼냅니다.

## 출력 형식 (Output Format)
- 모든 작업이 끝난 후 보관함에 남아있는 데이터를 **가장 오래된 순서대로** 공백으로 구분하여 출력합니다.
- 만약 보관함이 비어 있다면 "empty"를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 5
10 20 30 P 40
{TICK}

**Output:**
{TICK}
20 30 40
{TICK}

- 10, 20, 30 진입: [10, 20, 30]
- P (처리): 10이 나가고 [20, 30] 남음
- 40 진입: 빈 자리가 있으므로 [20, 30, 40]

### 예시 2
**Input:**
{TICK}
2 4
1 2 3 4
{TICK}

**Output:**
{TICK}
3 4
{TICK}

- 1, 2 진입: [1, 2]
- 3 진입: 보관함이 꽉 참. 가장 오래된 1을 버리고 3 추가 -> [2, 3]
- 4 진입: 보관함이 꽉 참. 가장 오래된 2를 버리고 4 추가 -> [3, 4]

### 예시 3
**Input:**
{TICK}
3 6
100 200 P P P 300
{TICK}

**Output:**
{TICK}
300
{TICK}

- 100, 200 진입: [100, 200]
- P 세 번: 100 처리, 200 처리, 그다음 P는 보관함이 비어있어 무시됨.
- 300 진입: [300]
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
    
    s = int(input_data[0])
    n = int(input_data[1])
    operations = input_data[2:]
    
    buffer = deque()
    
    for op in operations:
        if op == 'P':
            # 처리 명령: 가장 오래된 것 삭제
            if buffer:
                buffer.popleft()
        else:
            # 데이터 진입
            val = int(op)
            if len(buffer) == s:
                # 가득 찼으면 가장 오래된 것 버리고 추가
                buffer.popleft()
                buffer.append(val)
            else:
                # 빈 자리 있으면 그냥 추가
                buffer.append(val)
                
    if not buffer:
        print("empty")
    else:
        print(" ".join(map(str, buffer)))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(s, ops):
    from collections import deque
    buf = deque()
    for op in ops:
        if op == 'P':
            if buf: buf.popleft()
        else:
            v = int(op)
            if len(buf) == s:
                buf.popleft()
            buf.append(v)
    if not buf: return "empty"
    return " ".join(map(str, buf))

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (3, ["10", "20", "30", "P", "40"]),
    (2, ["1", "2", "3", "4"]),
    (3, ["100", "200", "P", "P", "P", "300"]),
    (5, ["P", "P", "P"]),
    (1, ["10", "20", "30"]),
]

for _ in range(15):
    ts = random.randint(2, 10)
    tn = random.randint(10, 30)
    tops = []
    for _ in range(tn):
        if random.random() < 0.3:
            tops.append("P")
        else:
            tops.append(str(random.randint(1, 999)))
    test_cases.append((ts, tops))

for i, (s, ops) in enumerate(test_cases, 1):
    input_str = f"{s} {len(ops)}\n" + " ".join(ops)
    ans = solve_internal(s, ops)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P053' 문제 생성이 완료되었습니다.")