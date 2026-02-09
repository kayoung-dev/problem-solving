import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P73 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P73")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 점진적인 근력 운동 계획

## 문제 설명
신입생 **민수**는 이번 학기 근성장을 위해 운동을 계획하고 있습니다. 민수는 헬스장에 일렬로 놓인 여러 개의 덤벨을 순서대로 사용하여 운동 세트를 구성하려고 합니다. 효과적인 근육 자극을 위해 민수는 다음과 같은 엄격한 규칙을 세웠습니다.

1. **세트 구성** 
    - 나열된 덤벨들 중 연속된 몇 개를 묶어서 하나의 '운동 세트'를 만듭니다. 덤벨의 순서는 절대로 바꿀 수 없습니다.
2. **점진적 과부하** 
    - 나중에 수행하는 세트의 총 무게 합은 반드시 바로 직전 세트의 총 무게 합보다 **크거나 같아야** 합니다.
    - 즉, $i$번째 세트의 무게 합을 $W_i$라고 할 때, 모든 $i$에 대해 $W_i \ge W_{i-1}$ 이 성립해야 합니다.
3. **최적화** 
    - 민수는 최대한 많은 번수의 세트를 수행하여 운동 강도를 높이고 싶어 합니다.

준비된 덤벨들의 무게가 순서대로 주어질 때, 규칙을 어기지 않으면서 민수가 구성할 수 있는 **최대 세트 수**를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 준비된 덤벨의 개수 $N$이 주어집니다. ($1 \le N \le 100,000$)
- 두 번째 줄에 각 덤벨의 무게 $w_1, w_2, \dots, w_N$이 공백으로 구분되어 주어집니다. 
- 각 무게 $w_i$는 $1$ 이상 $10^6$ 이하의 정수입니다.

## 출력 형식 (Output Format)
- 규칙을 만족하며 나눌 수 있는 **최대 세트 수**를 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
1 3 5 6
{TICK}

**Output:**
{TICK}
4
{TICK}

- 각각의 덤벨을 하나의 세트로 둡니다: $[1], [3], [5], [6]$.
- 각 세트의 무게는 $1 \le 3 \le 5 \le 6$으로 점진적으로 증가하므로 규칙을 만족합니다. 총 **4개**의 세트가 가능합니다.

### 예시 2
**Input:**
{TICK}
5
4 3 2 1 10
{TICK}

**Output:**
{TICK}
2
{TICK}

- 만약 $[4], [3], [2], [1], [10]$으로 나누면 무게가 줄어드는 구간이 생겨 규칙에 어긋납니다.
- $[4, 3, 2, 1]$을 첫 번째 세트로 묶으면 무게 합은 $10$이 됩니다.
- 그 뒤의 $[10]$을 두 번째 세트로 두면 무게 합은 $10$이 됩니다.
- $10 \ge 10$이므로 규칙을 만족하며, 이때 세트 수는 **2개**로 최대가 됩니다.

### 예시 3
**Input:**
{TICK}
6
1 2 1 2 1 2
{TICK}

**Output:**
{TICK}
3
{TICK}
"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    # 1. N 읽기
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    
    # 2. 덤벨 무게 데이터 읽기 (여러 줄에 걸쳐 있을 수 있음)
    nums = []
    while len(nums) < n:
        line = input().strip()
        if not line:
            break
        nums.extend(map(int, line.split()))
    
    # 3. 누적 합(Prefix Sum) 계산
    s = [0] * (n + 1)
    for i in range(n):
        s[i+1] = s[i] + nums[i]
        
    # dp[i]: i번째 덤벨까지 사용했을 때의 최대 세트 수
    # last_sum[i]: i번째 덤벨까지 사용하여 만든 마지막 세트의 무게 합
    dp = [0] * (n + 1)
    last_sum = [0] * (n + 1)
    
    # 단조 대기열(Monotonic Deque)을 이용한 최적화
    dq = deque([0])
    
    for i in range(1, n + 1):
        # s[i] >= s[j] + last_sum[j] 를 만족하는 가장 큰 j 찾기
        while len(dq) >= 2 and s[i] >= s[dq[1]] + last_sum[dq[1]]:
            dq.popleft()
            
        best_j = dq[0]
        dp[i] = dp[best_j] + 1
        last_sum[i] = s[i] - s[best_j]
        
        # 새로운 후보 i 추가 (s[i] + last_sum[i]가 작을수록 유리)
        while dq and s[i] + last_sum[i] <= s[dq[-1]] + last_sum[dq[-1]]:
            dq.pop()
        dq.append(i)
        
    print(dp[n])

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, nums):
    s = [0] * (n + 1)
    for i in range(n): s[i+1] = s[i] + nums[i]
    dp = [0] * (n + 1)
    lgs = [0] * (n + 1)
    dq = deque([0])
    for i in range(1, n + 1):
        while len(dq) >= 2 and s[i] >= s[dq[1]] + lgs[dq[1]]:
            dq.popleft()
        bj = dq[0]
        dp[i] = dp[bj] + 1
        lgs[i] = s[i] - s[bj]
        while dq and s[i] + lgs[i] <= s[dq[-1]] + lgs[dq[-1]]:
            dq.pop()
        dq.append(i)
    return str(dp[n])

test_data = [
    (4, [1, 3, 5, 6]),
    (5, [4, 3, 2, 1, 10]),
    (6, [1, 2, 1, 2, 1, 2])
]

# 랜덤 테스트케이스 생성
for _ in range(17):
    tn = random.randint(10, 500)
    tnums = [random.randint(1, 50) for _ in range(tn)]
    test_data.append((tn, tnums))

for i, (n, nums) in enumerate(test_data, 1):
    input_str = f"{n}\n" + " ".join(map(str, nums))
    ans = solve_internal(n, nums)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P73' 문제 생성이 완료되었습니다.")