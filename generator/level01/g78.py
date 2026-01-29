import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P78 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P78")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 캠퍼스 스마트 주차 관제 시스템

## 문제 설명
캠퍼스 내의 교통 혼잡을 줄이기 위해 새로운 '스마트 주차 관제 시스템'이 도입되었습니다. 이 시스템은 입차하는 차량의 정보를 임시 버퍼에 저장하고 처리하는 역할을 합니다. 시스템은 하드웨어 한계로 인해 동시에 저장할 수 있는 차량 정보의 개수가 제한되어 있습니다.

시스템이 처리해야 할 차량 데이터는 다음과 같습니다:
- **차량 번호 (Source):** 차량을 식별하는 고유 번호
- **주차장 번호 (Destination):** 입차하려는 주차장 구역 번호
- **입차 시간 (Timestamp):** 차량이 센서를 통과한 시간

시스템은 다음 규칙에 따라 작동하도록 설계해야 합니다:

- **메모리 제한** 
  - 시스템은 최대 $L$개의 차량 정보만 동시에 저장할 수 있습니다. 새로운 정보를 추가할 때 저장 공간이 꽉 찼다면, 가장 오래된 정보를 삭제하여 공간을 확보한 뒤 새 정보를 추가합니다.
- **중복 입차 방지** 
  - 현재 시스템에 저장된 정보 중 **차량 번호, 주차장 번호, 입차 시간**이 모두 동일한 데이터가 이미 존재한다면, 이는 센서 오류에 의한 중복 데이터로 간주하여 추가하지 않습니다.
- **데이터 처리** 
  - 처리 요청이 들어오면 현재 저장된 데이터 중 **가장 먼저 들어온 데이터**를 꺼내어 결과를 반환하고 시스템에서 삭제합니다.
- **구역 조회** 
  - 특정 주차장 번호와 시간 범위 $[startTime, endTime]$가 주어질 때, 현재 시스템에 저장된 데이터 중 해당 구역으로 향하며 시간 범위 내에 입차한 차량이 몇 대인지 계산합니다.

차량 데이터 입력은 항상 **입차 시간(Timestamp)이 증가하거나 같은 순서**로 들어옵니다.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 시스템의 최대 저장 용량 $L$이 주어집니다. ($1 \le L \le 1,000$)
- 두 번째 줄에 수행할 명령의 개수 $Q$가 주어집니다. ($1 \le Q \le 5,000$)
- 세 번째 줄부터 $Q$개의 줄에 걸쳐 명령이 주어집니다:
    - `ADD car_id lot_id timestamp`: 차량 정보를 시스템에 추가합니다. 성공하면 `true`, 중복이면 `false`를 출력합니다.
    - `PROCESS`: 가장 오래된 데이터를 처리하고 `[car_id, lot_id, timestamp]` 형태로 출력합니다. 저장된 데이터가 없으면 `EMPTY`를 출력합니다.
    - `COUNT lot_id startTime endTime`: 조건에 맞는 차량 수를 출력합니다.

## 출력 형식 (Output Format)
- 각 명령의 결과를 한 줄에 하나씩 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
9
ADD 1 4 90
ADD 2 5 90
ADD 1 4 90
ADD 3 5 95
ADD 4 5 105
PROCESS
ADD 5 2 110
COUNT 5 100 110
COUNT 5 90 110
{TICK}

**Output:**
{TICK}
true
true
false
true
true
[2, 5, 90]
true
1
2
{TICK}

- 용량 3인 시스템에 `(1, 4, 90)`, `(2, 5, 90)` 추가 (true 출력)
- `(1, 4, 90)` 재유입 (중복이므로 false 출력)
- `(3, 5, 95)` 추가 
  - 현재 `[(1,4,90), (2,5,90), (3,5,95)]`
- `(4, 5, 105)` 추가 
  - 용량 초과로 가장 오래된 `(1,4,90)` 삭제 후 추가
  - 현재 `[(2,5,90), (3,5,95), (4, 5, 105)]`
- `PROCESS`
  - 가장 오래된 `(2, 5, 90)` 반환 및 삭제
- `(5 2 110)` 추가
  - 현재 `[(3,5,95), (4, 5, 105), (5,2,110)]`
- `COUNT 5 100 110` 
  - 현재 남은 `(3,5,95), (4,5,105), (5,2,110)` 중 주차장 5번이며 시간이 100~110 사이인 차량은 `(4,5,105)` 1대입니다.
- `COUNT 5 90 110` 
  - 주차장 5번이며 시간이 90~110 사이인 차량은 `(3,5,95), (4,5,105)` 2대입니다.

### 예시 2
**Input:**
{TICK}
2
5
ADD 10 1 1000
ADD 20 1 1010
ADD 30 2 1020
COUNT 1 1000 1100
PROCESS
{TICK}

**Output:**
{TICK}
true
true
true
1
[20, 1, 1010]
{TICK}

- $L=2$
  - `(10, 1, 1000)`과 `(20, 1, 1010)`이 차례로 저장됩니다.
- `ADD 30 2 1020`
  - 용량이 꽉 찼으므로 가장 오래된 `(10, 1, 1000)`이 삭제되고 추가됩니다.
  - 현재 `[(20, 1, 1010)), (30, 2, 1020)]`
- `COUNT 1 1000 1100`
  - 주차장 1번 데이터중 1000-1100 사이 기록은 1개뿐입니다.
- `PROCESS`: 현재 가장 오래된 데이터인 `[20, 1, 1010]`을 꺼내고 삭제합니다.

### 예시 3 
**Input:**
{TICK}
5
3
PROCESS
ADD 100 10 500
PROCESS
{TICK}

**Output:**
{TICK}
EMPTY
true
[100, 10, 500]
{TICK}

- 데이터가 없는 상태에서 `PROCESS` 호출 시 `EMPTY`를 출력하며, 이후 추가된 데이터는 정상적으로 처리됩니다.
"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

# 입력 최적화
input = sys.stdin.readline

def solve():
    # 1. 초기 설정 읽기
    line1 = input().strip()
    if not line1: return
    limit = int(line1)
    
    line2 = input().strip()
    if not line2: return
    q_count = int(line2)
    
    # 2. 시스템 데이터 구조
    queue = deque() # FIFO 저장소
    lookup_set = set() # 중복 체크용 (car_id, lot_id, ts)
    
    results = []
    
    # 3. 명령 처리
    for _ in range(q_count):
        cmd = input().strip().split()
        if not cmd: continue
        
        type = cmd[0]
        
        if type == "ADD":
            car_id, lot_id, ts = int(cmd[1]), int(cmd[2]), int(cmd[3])
            item = (car_id, lot_id, ts)
            
            if item in lookup_set:
                results.append("false")
            else:
                # 용량 초과 시 오래된 데이터 삭제
                if len(queue) >= limit:
                    oldest = queue.popleft()
                    lookup_set.remove(oldest)
                
                queue.append(item)
                lookup_set.add(item)
                results.append("true")
                
        elif type == "PROCESS":
            if not queue:
                results.append("EMPTY")
            else:
                item = queue.popleft()
                lookup_set.remove(item)
                results.append(f"[{item[0]}, {item[1]}, {item[2]}]")
                
        elif type == "COUNT":
            target_lot = int(cmd[1])
            start_t, end_t = int(cmd[2]), int(cmd[3])
            
            count = 0
            # 현재 저장된 모든 차량 전수 조사
            for car, lot, ts in queue:
                if lot == target_lot and start_t <= ts <= end_t:
                    count += 1
            results.append(str(count))
            
    # 4. 일괄 출력
    print("\\n".join(results))

if __name__ == "__main__":
    solve()
"""

# solution.py 저장 시 이스케이프 문자 처리
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py.replace("\\\\n", "\\n"))

# ---------------------------------------------------------
# 4. 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(limit, cmds):
    queue = deque()
    lookup = set()
    res = []
    for c in cmds:
        if c[0] == "ADD":
            item = (c[1], c[2], c[3])
            if item in lookup: res.append("false")
            else:
                if len(queue) >= limit: lookup.remove(queue.popleft())
                queue.append(item); lookup.add(item); res.append("true")
        elif c[0] == "PROCESS":
            if not queue: res.append("EMPTY")
            else:
                item = queue.popleft(); lookup.remove(item)
                res.append(f"[{item[0]}, {item[1]}, {item[2]}]")
        elif c[0] == "COUNT":
            count = sum(1 for x in queue if x[1] == c[1] and c[2] <= x[2] <= c[3])
            res.append(str(count))
    return "\n".join(res)

# 샘플 및 랜덤 데이터
test_data = []
# 예시 1
test_data.append((3, [
    ("ADD", 1, 4, 90), ("ADD", 2, 5, 90), ("ADD", 1, 4, 90),
    ("ADD", 3, 5, 95), ("ADD", 4, 5, 105), ("PROCESS",),
    ("ADD", 5, 2, 110), ("COUNT", 5, 100, 110), ("COUNT", 5, 90, 110)
]))

# 랜덤 19개
for _ in range(19):
    l = random.randint(5, 50)
    qc = random.randint(50, 200)
    t_cmds = []
    curr_t = 100
    for _ in range(qc):
        rtype = random.choice(["ADD", "ADD", "PROCESS", "COUNT"])
        if rtype == "ADD":
            curr_t += random.randint(0, 10)
            t_cmds.append(("ADD", random.randint(1, 20), random.randint(1, 10), curr_t))
        elif rtype == "PROCESS":
            t_cmds.append(("PROCESS",))
        else:
            st = curr_t - 50
            t_cmds.append(("COUNT", random.randint(1, 10), st, curr_t))
    test_data.append((l, t_cmds))

for i, (l, cmds) in enumerate(test_data, 1):
    input_str = f"{l}\n{len(cmds)}\n"
    for c in cmds:
        input_str += " ".join(map(str, c)) + "\n"
    ans = solve_internal(l, cmds)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P78' 문제 생성이 완료되었습니다.")