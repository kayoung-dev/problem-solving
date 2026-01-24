import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P50 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P50")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 긴급 택배 분류 작전

## 문제 설명
택배 센터의 관리자 민호는 컨베이어 벨트 위에 놓인 $N$개의 택배 상자를 처리해야 합니다. 각 상자에는 **긴급도(1~9)** 가 적혀 있으며, 숫자가 클수록 더 빨리 배송되어야 하는 물건입니다.

민호는 다음과 같은 규칙으로 택배를 배송합니다:
1. 벨트의 **맨 앞(Front)** 에 있는 상자를 하나 꺼냅니다.
2. 현재 벨트 위에 남아있는 상자들 중, 방금 꺼낸 상자보다 **긴급도가 더 높은** 상자가 하나라도 있다면, 꺼낸 상자를 즉시 벨트의 **맨 뒤(Rear)** 로 보냅니다.
3. 만약 방금 꺼낸 상자가 가장 긴급한 물건이라면(긴급도가 가장 높다면), 그 상자를 즉시 **배송**합니다.

민호는 당신에게 특정 위치에 있던 상자가 **몇 번째로 배송되는지** 알아봐 달라고 부탁했습니다. 현재 벨트 위 상자들의 긴급도 순서와, 당신이 궁금한 상자의 초기 위치 $M$이 주어질 때 배송 순서를 구하세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 택배의 개수 $N$과 궁금한 상자의 초기 위치 $M$이 주어집니다. ($1 \le N \le 100$, $0 \le M < N$)
  - 위치 $M$은 0부터 시작합니다 (0은 맨 앞).
* 두 번째 줄에 $N$개 상자의 긴급도가 정수형태로 순서대로 주어집니다.

## 출력 형식 (Output Format)
* 위치 $M$에 있던 상자가 몇 번째로 배송되는지 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
```
1 0
5
```

**Output:**
```
1
```

* 상자가 하나뿐이므로, 그 상자가 즉시 1번째로 배송됩니다.

### 예시 2
**Input:**
```
4 2
1 2 3 4
```

**Output:**
```
2
```

* 초기 상태: `[1, 2, 3(M), 4]` (M은 2번 인덱스)
* 첫번째 배송 ( 가장 높은 긴급도 4 )
  * `1`을 확인: 뒤에 가장 높은 긴급도 `4`가 있으므로 뒤로 보냄 <br/> 
  `[2, 3(M), 4, 1]`
  * `2`를 확인: 뒤에 가장 높은 긴급도 `4`가 있으므로 뒤로 보냄  <br />
  `[3(M), 4, 1, 2]`
  * `3(M)`을 확인: 뒤에 가장 높은 긴급도 `4`가 있으므로 뒤로 보냄 <br />
  `[4, 1, 2, 3(M)]`
  * `4`를 확인하여 배송 완료 (남은 벨트: `[1, 2, 3(M)]`)
* 두번째 배송 ( 가장 높은 긴급도 3 )
  * `1`을 확인: 뒤에 `3(M)`이 있으므로 뒤로 보냄 $\rightarrow$ `[2, 3(M), 1]`
  * `2`를 확인: 뒤에 `3(M)`이 있으므로 뒤로 보냄 $\rightarrow$ `[3(M), 1, 2]`
  * `3(M)`을 확인하여 배송 완료

### 예시 3
**Input:**
```
6 0
1 1 9 1 1 1
```

**Output:**
```
5
```
* 맨 앞의 긴급도 `1`은 긴급도 `9` 때문에 계속 뒤로 밀리게 됩니다. `9`가 먼저 배송된 후 나머지 `1`들 사이의 순서에 따라 5번째로 배송됩니다.
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
    priorities = list(map(int, input_data[2:]))
    
    # (긴급도, 초기위치) 형태로 큐에 삽입
    q = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0
    
    while q:
        current = q.popleft()
        # 현재 큐에 나보다 더 긴급한 게 있는지 확인
        if any(current[0] < item[0] for item in q):
            q.append(current) # 뒤로 보냄
        else:
            order += 1 # 배송 완료
            if current[1] == m:
                print(order)
                return

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(n, m, ps):
    from collections import deque
    q = deque([(p, i) for i, p in enumerate(ps)])
    order = 0
    while q:
        curr = q.popleft()
        if any(curr[0] < x[0] for x in q):
            q.append(curr)
        else:
            order += 1
            if curr[1] == m: return str(order)
    return ""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

# 테스트 데이터 생성
test_cases = [
    (1, 0, [5]),
    (4, 2, [1, 2, 3, 4]),
    (6, 0, [1, 1, 9, 1, 1, 1]),
    (4, 2, [5, 5, 5, 5]),
    (10, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
]

# 랜덤 케이스 15개
for _ in range(15):
    tn = random.randint(5, 50)
    tm = random.randint(0, tn - 1)
    tps = [random.randint(1, 9) for _ in range(tn)]
    test_cases.append((tn, tm, tps))

for i, (n, m, ps) in enumerate(test_cases, 1):
    input_str = f"{n} {m}\n" + " ".join(map(str, ps))
    ans = solve_internal(n, m, ps)
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P50' 최종 문제 생성이 완료되었습니다.")