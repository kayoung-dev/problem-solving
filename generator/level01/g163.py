import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P163 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P163")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 예산 초과 물건 찾기

## 문제 설명
여행가 철수는 기념품 가게에서 물건들의 가격표를 보고 있습니다. 가격표에는 총 $N$개의 물건 가격이 낮은 가격부터 높은 가격 순으로 정렬되어 있습니다.

철수는 현재 $K$원만큼의 예산을 가지고 있습니다. 철수는 자신이 가진 예산으로 살 수 없는, 즉 **처음으로 예산 $K$원을 초과하는 가격**이 장부의 몇 번째 위치(인덱스)에서 나타나는지 알고 싶습니다.

물건의 가격 리스트와 철수의 예산 $K$가 주어질 때, $K$보다 큰 값이 처음으로 등장하는 위치를 찾는 프로그램을 작성하세요. 장부의 위치는 $0$번부터 시작하며, 만약 모든 물건이 예산 이하의 가격이라면 $-1$을 출력해야 합니다. 이 작업은 데이터가 매우 많을 수 있으므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



---
## 입력 형식 (Input Format)
- 첫 번째 줄에는 물건의 개수 $N$과 철수의 예산 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N \le 100,000$
- $0 \le K \le 10^9$
- 두 번째 줄에는 오름차순으로 정렬된 $N$개의 물건 가격이 공백으로 구분되어 주어집니다. 각 가격은 $0$ 이상 $10^9$ 이하의 정수입니다.
## 출력 형식 (Output Format)
- 물건의 가격이 예산 $K$를 처음으로 초과하는 지점의 인덱스를 정수로 출력합니다.
- 예산을 초과하는 가격의 물건이 하나도 존재하지 않는 경우에는 $-1$을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 5000
1000 3000 5000 7000 9000
{TICK}
**Output:**
{TICK}
3
{TICK}
- 예산 5000원을 초과하는 첫 번째 가격은 7000원이며, 이 값은 인덱스 3에 위치합니다.

### 예시 2
**Input:**
{TICK}
6 100
20 40 60 80 90 100
{TICK}
**Output:**
{TICK}
-1
{TICK}
- 모든 물건의 가격이 예산 100원 이하이므로, 예산을 초과하는 위치가 존재하지 않아 -1을 출력합니다.

### 예시 3
**Input:**
{TICK}
4 10
15 20 25 30
{TICK}
**Output:**
{TICK}
0
{TICK}
- 모든 물건이 처음부터 예산 10원을 초과하고 있으므로, 가장 첫 번째 위치인 0을 출력합니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    prices = list(map(int, input_data[2:]))

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        # Upper Bound: Target보다 큰 값이 처음 나오는 위치
        if prices[mid] > k:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    if i <= 5:
        n = random.randint(1, 15)
    elif i <= 15:
        n = random.randint(100, 2000)
    else:
        n = random.randint(50000, 100000)
    
    # 중복 허용 오름차순 리스트 생성
    prices = sorted([random.randint(0, 10**9) for _ in range(n)])
    
    # 타겟 설정 전략
    rand_type = random.random()
    if rand_type < 0.3: # 결과가 -1인 경우 (모든 값이 k 이하)
        target = max(prices) + random.randint(0, 100)
    elif rand_type < 0.6: # 결과가 0인 경우 (모든 값이 k 초과)
        target = min(prices) - random.randint(1, 100)
        if target < 0: target = 0
    else: # 중간에 걸리는 경우
        target = prices[random.randint(0, n-1)]
    
    # 정답 계산 (Upper Bound)
    ans_val = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if prices[m] > target:
            ans_val = m
            r = m - 1
        else:
            l = m + 1
    
    ans = str(ans_val)
    input_str = f"{n} {target}\n" + " ".join(map(str, prices))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P163' 문제 생성이 완료되었습니다.")