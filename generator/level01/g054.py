import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P54 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P054")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 은행원 지수의 창구 균형 맞추기

## 문제 설명
은행원 지수는 오늘 두 개의 창구를 관리하고 있습니다. 각 창구 앞에는 손님들이 줄을 서 있으며, 각 손님이 업무를 보는 데 걸리는 시간이 정해져 있습니다. 지수는 두 창구의 **전체 업무 시간 합계**를 똑같이 만들어 두 창구가 동시에 업무를 마칠 수 있게 하려고 합니다.

지수가 할 수 있는 행동은 다음과 같습니다.
1. 한쪽 줄의 **맨 앞에 서 있는 손님**을 꺼냅니다.
2. 꺼낸 손님을 다른 쪽 줄의 **맨 뒤**로 보냅니다.

각 줄에 서 있는 손님들의 업무 시간이 주어질 때, 두 줄의 업무 시간 합계를 똑같이 만들기 위해 필요한 **최소 이동 횟수**를 구하세요. 만약 아무리 옮겨도 합계를 똑같이 만들 수 없다면 -1을 출력합니다.

---

## 입력 형식 (Input Format)
- 첫 번째 줄에 각 줄에 서 있는 손님의 수 N이 주어집니다. (1 <= N <= 100)
- 두 번째 줄에 첫 번째 줄 손님들의 업무 시간이 공백으로 구분되어 주어집니다.
- 세 번째 줄에 두 번째 줄 손님들의 업무 시간이 공백으로 구분되어 주어집니다.

## 출력 형식 (Output Format)
- 두 줄의 합계를 똑같이 만들기 위한 최소 이동 횟수를 출력합니다.
- 합계를 똑같이 만들 수 없는 경우 -1을 출력합니다.

---
## 힌트 (Note)
합계를 똑같이 만들 수 없는 경우는 크게 두 가지입니다. 프로그램을 짤 때 이 조건을 고려하세요.

1. **전체 합계 확인:** 두 줄에 서 있는 모든 손님의 업무 시간을 다 더했을 때 그 값이 **홀수**라면, 정수 단위로는 절반으로 딱 나누는 것이 물리적으로 불가능합니다. 이 경우 즉시 -1을 출력합니다.
2. **상태의 반복(순환):** 손님을 계속 옮기다 보면 이전에 이미 확인했던 합계 상태(예: 줄1의 합이 다시 10이 되는 경우)가 반복되거나, 모든 손님이 한 바퀴를 다 돌아 제자리로 오는 경우가 생깁니다. 
   - 보통 손님 수 N의 4배(4*N) 정도 이동했는데도 답을 찾지 못했다면, 앞으로도 계속 같은 상태가 반복될 가능성이 높으므로 불가능(-1)으로 간주하고 탐색을 종료하는 것이 안전합니다.
---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
8 9 7 6
7 5 4 4
{TICK}

**Output:**
{TICK}
4
{TICK}

- 줄1, 줄2 전체 합계는 50이며, 목표 합계는 25입니다.
- 현재 줄1(30), 줄2(20). 줄1이 크므로 맨 앞 8을 줄2로 보냄. [이동 1]
   - 결과: 줄1(9, 7, 6), 줄2(7, 5, 4, 4, 8) | 합계: 줄1(22), 줄2(28)
- 현재 줄2(28)가 크므로 줄2의 맨 앞 7을 줄1로 보냄. [이동 2]
   - 결과: 줄1(9, 7, 6, 7), 줄2(5, 4, 4, 8) | 합계: 줄1(29), 줄2(21)
- 현재 줄1(29)이 크므로 줄1의 맨 앞 9를 줄2로 보냄. [이동 3]
   - 결과: 줄1(7, 6, 7), 줄2(5, 4, 4, 8, 9) | 합계: 줄1(20), 줄2(30)
- 현재 줄2(30)가 크므로 줄2의 맨 앞 5를 줄1로 보냄. [이동 4]
   - 결과: 줄1(7, 6, 7, 5), 줄2(4, 4, 8, 9) | 합계: 줄1(25), 줄2(25)
- 총 4번의 이동(주고받기) 끝에 균형이 맞았습니다.

### 예시 2
**Input:**
{TICK}
4
1 2 1 2
1 1 1 1
{TICK}

**Output:**
{TICK}
1
{TICK}

- 현재 합계: 줄1(6), 줄2(4). 전체 합이 10이므로 목표 합계는 5입니다.
- 줄1의 맨 앞 손님(1)을 줄2의 뒤로 보냅니다.
- 결과: 줄1(2, 1, 2) -> 합계 5 / 줄2(1, 1, 1, 1, 1) -> 합계 5.
- 단 1번의 이동으로 균형이 맞았습니다.

### 예시 3
**Input:**
{TICK}
3
1 2 1
1 1 1
{TICK}

**Output:**
{TICK}
-1
{TICK}

* 전체 업무 시간의 합이 7(홀수)이므로, 두 줄의 합계를 똑같이 나누는 것이 불가능합니다.
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
    line1 = deque(map(int, input_data[1:1+n]))
    line2 = deque(map(int, input_data[1+n:1+2*n]))
    
    sum1 = sum(line1)
    sum2 = sum(line2)
    total_sum = sum1 + sum2
    
    # 합이 홀수면 절대 같아질 수 없음
    if total_sum % 2 != 0:
        print(-1)
        return
    
    target = total_sum // 2
    moves = 0
    # 무한 루프 방지를 위한 최대 시도 횟수 설정
    limit = n * 4
    
    while moves <= limit:
        if sum1 == target:
            print(moves)
            return
        
        if sum1 > target:
            val = line1.popleft()
            sum1 -= val
            line2.append(val)
            sum2 += val
        else:
            val = line2.popleft()
            sum2 -= val
            line1.append(val)
            sum1 += val
        
        moves += 1
        
    print(-1)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, l1, l2):
    from collections import deque
    q1, q2 = deque(l1), deque(l2)
    s1, s2 = sum(q1), sum(q2)
    if (s1 + s2) % 2 != 0: return "-1"
    target = (s1 + s2) // 2
    moves, limit = 0, n * 4
    while moves <= limit:
        if s1 == target: return str(moves)
        if s1 > target:
            v = q1.popleft(); s1 -= v; q2.append(v); s2 += v
        else:
            v = q2.popleft(); s2 -= v; q1.append(v); s1 += v
        moves += 1
    return "-1"

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

test_cases = [
    (3, [3, 2, 7], [2, 8, 2]), # 예시 1
    (2, [1, 1], [1, 5]),       # 예시 2 (불가능할 수도 있는 조합)
    (3, [1, 2, 1], [1, 1, 1]), # 예시 3
    (4, [1, 2, 1, 2], [1, 1, 1, 1]),
    (1, [10], [10]),
]

for _ in range(15):
    tn = random.randint(2, 20)
    total = random.randint(20, 100)
    if total % 2 != 0 and random.random() > 0.5: total += 1
    
    # 랜덤 리스트 생성 (합계 조절)
    l1 = [random.randint(1, 10) for _ in range(tn)]
    l2 = [random.randint(1, 10) for _ in range(tn)]
    test_cases.append((tn, l1, l2))

for i, (n, l1, l2) in enumerate(test_cases, 1):
    input_str = f"{n}\n" + " ".join(map(str, l1)) + "\n" + " ".join(map(str, l2))
    ans = solve_internal(n, l1, l2)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P054' 문제 생성이 완료되었습니다.")