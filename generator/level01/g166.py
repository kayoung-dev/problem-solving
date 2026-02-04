import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P166 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P166")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 새 문서 삽입 위치 찾기

## 문제 설명
직장인 현우는 날짜별로 정렬된 문서함에 새 문서를 추가하려고 합니다. 문서함에는 $N$개의 문서 번호가 오름차순으로 정렬되어 있습니다. 

현우는 기존 문서들의 순서를 유지하면서 새 문서 $K$를 넣으려 합니다. 만약 문서함에 이미 $K$와 같은 번호가 있다면 그 위치의 인덱스를 반환하고, 없다면 $K$가 순서에 맞게 들어갈 수 있는 위치의 인덱스를 구하는 프로그램을 작성하세요.

위치는 $0$번부터 시작합니다. 대규모 데이터를 처리해야 하므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에는 기존 문서의 개수 $N$과 새 문서의 번호 $K$가 공백으로 구분되어 주어집니다.
- $1 \le N \le 100,000$
- $0 \le K \le 10^9$
- 두 번째 줄에는 오름차순으로 정렬된 $N$개의 문서 번호가 공백으로 구분되어 주어집니다. 
- 중복된 번호는 주어지지 않으며, 각 번호는 $0$ 이상 $10^9$ 이하의 정수입니다.

## 출력 형식 (Output Format)
- 문서 번호 $K$가 존재한다면 해당 인덱스를, 존재하지 않는다면 정렬된 순서를 유지하며 삽입될 수 있는 인덱스를 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4 5
1 3 5 6
{TICK}
**Output:**
{TICK}
2
{TICK}
- 숫자 5는 리스트의 인덱스 2에 이미 존재하므로 2를 출력합니다.

### 예시 2
**Input:**
{TICK}
4 2
1 3 5 6
{TICK}
**Output:**
{TICK}
1
{TICK}
- 숫자 2는 리스트에 없지만, 순서를 유지하며 삽입된다면 1과 3 사이인 인덱스 1에 위치해야 합니다.

### 예시 3
**Input:**
{TICK}
4 7
1 3 5 6
{TICK}
**Output:**
{TICK}
4
{TICK}
- 숫자 7은 리스트의 모든 값보다 크므로 가장 마지막 뒤쪽인 인덱스 4에 삽입되어야 합니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    nums = list(map(int, data[2:]))

    low = 0
    high = n - 1
    
    # 이진 탐색으로 삽입 위치(Lower Bound와 유사) 찾기
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            print(mid)
            return
        elif nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    
    # 탐색 실패 시 low 값이 삽입될 위치가 됨
    print(low)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    # 11~20번은 시간복잡도 검증을 위해 대규모 데이터 생성
    if i <= 10:
        n = random.randint(1, 1000)
    else:
        n = random.randint(90000, 100000)
    
    # 중복 없는 오름차순 리스트
    # 대규모 데이터 생성을 위해 간격을 두고 생성
    step = 10**9 // (n + 1)
    nums = [j * step + random.randint(0, step-1) for j in range(1, n + 1)]
    
    # 타겟 설정 (존재하는 경우와 없는 경우 섞음)
    if i % 2 == 0:
        target = nums[random.randint(0, n-1)]
    else:
        target = random.randint(0, 10**9)

    # 정답 계산 (bisect_left와 동일 로직)
    import bisect
    ans_val = bisect.bisect_left(nums, target)
    
    input_str = f"{n} {target}\n" + " ".join(map(str, nums))
    ans_str = str(ans_val)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level01/P166' 문제 생성이 완료되었습니다.")