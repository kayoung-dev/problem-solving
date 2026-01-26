import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P52 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P52")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 무너지는 다리를 건너라

## 문제 설명
트럭 운전사 철수는 여러 대의 트럭을 이끌고 일정한 길이를 가진 다리를 건너려고 합니다. 이 다리는 매우 낡아서 한꺼번에 버틸 수 있는 최대 하중(무게 제한)이 정해져 있습니다. 철수는 모든 트럭이 다리를 안전하게 건너는 데 걸리는 최소 시간을 계산해야 합니다.

다리와 트럭의 이동 규칙은 다음과 같습니다.

1. 다리의 길이는 L입니다. 트럭은 1초에 거리 1만큼 이동하며, 다리를 완전히 건너려면 L초가 걸립니다.
2. 다리 위에는 최대 W만큼의 무게만 동시에 올라갈 수 있습니다.
3. 트럭은 정해진 순서대로만 다리에 진입할 수 있습니다.
4. 다리 위에 빈 자리가 있고, 새로 들어올 트럭의 무게를 더해도 다리의 무게 제한 W를 넘지 않는다면 다음 트럭이 즉시 다리에 올라갈 수 있습니다.
5. 다리에 진입하는 데 1초가 소요되며, 다리 끝에 도달한 트럭은 다음 1초에 다리 밖으로 완전히 나갑니다.

모든 트럭이 다리를 완전히 통과하는 데 걸리는 총 시간을 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 다리의 길이 L, 다리가 견딜 수 있는 최대 하중 W, 그리고 트럭의 개수 N이 공백으로 구분되어 주어집니다. (1 <= L, W, N <= 10,000)
- 두 번째 줄에 각 트럭의 무게가 순서대로 주어집니다. 각 트럭의 무게는 W보다 작거나 같습니다.

## 출력 형식 (Output Format)
- 모든 트럭이 다리를 완전히 건너는 데 걸리는 최소 시간을 정수로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
2 10 2
7 4
{TICK}

**Output:**
{TICK}
8
{TICK}

**설명:**
- 1초: 7번 트럭이 다리에 올라갑니다.
- 2초: 7번 트럭이 다리 중간으로 이동합니다. 4번 트럭은 무게 제한(7+4=11) 때문에 대기합니다.
- 3초: 7번 트럭이 다리를 나감과 동시에 4번 트럭이 다리에 올라갑니다.
- 5초: 4번 트럭이 다리를 완전히 빠져나옵니다.

### 예시 2
**Input:**
{TICK}
100 100 1
10
{TICK}

**Output:**
{TICK}
101
{TICK}

### 예시 3
**Input:**
{TICK}
5 20 4
5 10 5 10
{TICK}

**Output:**
{TICK}
14
{TICK}

**설명:**
- 다리 길이 5, 무게 제한 20인 상황입니다.
- 첫 두 대(5, 10)는 무게 합이 15로 제한 안이라 연속 진입이 가능하지만, 세 번째 5가 들어오면 합이 20이 되어 아슬아슬하게 진입 가능합니다.
- 하지만 네 번째 10은 앞의 트럭이 빠질 때까지 대기해야 하므로 시간이 추가로 소요됩니다.
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
    
    l = int(input_data[0])
    w = int(input_data[1])
    n = int(input_data[2])
    trucks = deque(map(int, input_data[3:]))
    
    # 다리 위 상황을 0으로 채워진 공간으로 표현
    bridge = deque([0] * l)
    current_bridge_weight = 0
    time = 0
    
    while bridge:
        time += 1
        # 다리 맨 끝에 도달한 트럭(혹은 빈 공간) 제거
        arrived = bridge.popleft()
        current_bridge_weight -= arrived
        
        if trucks:
            # 다음 트럭이 진입 가능한지 확인
            if current_bridge_weight + trucks[0] <= w:
                next_truck = trucks.popleft()
                bridge.append(next_truck)
                current_bridge_weight += next_truck
            else:
                # 진입 불가 시 빈 공간 추가하여 이동 유지
                bridge.append(0)
                
    print(time)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(l, w, n, weights):
    from collections import deque
    trucks = deque(weights)
    bridge = deque([0] * l)
    cur_w = 0
    time = 0
    while bridge:
        time += 1
        cur_w -= bridge.popleft()
        if trucks:
            if cur_w + trucks[0] <= w:
                t = trucks.popleft()
                bridge.append(t)
                cur_w += t
            else:
                bridge.append(0)
    return str(time)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

# 테스트 케이스 20개 생성
test_cases = [
    (2, 10, 2, [7, 4]),
    (100, 100, 1, [10]),
    (5, 20, 4, [5, 10, 5, 10]),
    (10, 10, 10, [10]*10),
    (5, 5, 5, [1, 1, 1, 1, 1])
]

for _ in range(15):
    tl = random.randint(10, 100)
    tw = random.randint(20, 200)
    tn = random.randint(5, 30)
    tweights = [random.randint(1, tw // 2) for _ in range(tn)]
    test_cases.append((tl, tw, tn, tweights))

for i, (l, w, n, weights) in enumerate(test_cases, 1):
    input_str = f"{l} {w} {n}\n" + " ".join(map(str, weights))
    ans = solve_internal(l, w, n, weights)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P52' 문제 생성이 완료되었습니다.")