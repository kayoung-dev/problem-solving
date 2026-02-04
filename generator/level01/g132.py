import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P132 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P132")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 데이터 스트림의 신뢰성 분할

## 문제 설명
통신 엔지니어인 지원이는 우주 탐사선으로부터 전송된 $N$개의 센서 데이터 스트림을 분석하고 있습니다. 스트림은 일렬로 나열된 센서 식별 번호(ID)들로 구성되어 있습니다. 지원이는 이 스트림을 한 군데 잘라 두 개의 분석 장치(장치 A, 장치 B)에 나누어 입력하려고 합니다.

분석의 신뢰성을 높이기 위해, 지원이는 각 장치에 할당된 구간 내에서 '유일하게 한 번만 등장하는 센서 ID의 개수'가 서로 동일해지는 지점을 찾으려고 합니다. 이를 '신뢰 점검 지점'이라고 부릅니다.

예를 들어, 센서 ID 스트림이 `[1, 2, 1, 3, 2]` 순서로 들어왔을 때:
- **2번째 데이터 뒤를 자를 경우:** 
  - 장치 A: `[1, 2]` $\rightarrow$ 한 번만 등장하는 ID는 $1, 2$로 총 **2개**입니다.
  - 장치 B: `[1, 3, 2]` $\rightarrow$ 한 번만 등장하는 ID는 $1, 3, 2$로 총 **3개**입니다.
  - 두 장치의 유일 ID 개수가 다르므로 신뢰 점검 지점이 아닙니다.
- **3번째 데이터 뒤를 자를 경우:**
    - 장치 A: `[1, 2, 1]` $\rightarrow$ 한 번만 등장하는 ID는 $2$뿐이므로 **1개**입니다.
    - 장치 B: `[3, 2]` $\rightarrow$ 한 번만 등장하는 ID는 $3, 2$로 총 **2개**입니다.
    - 역시 신뢰 점검 지점이 아닙니다.

주어진 센서 데이터 스트림을 두 구간으로 나누었을 때, 양쪽 구간의 '유일 ID 개수'가 같아지는 신뢰 점검 지점은 총 몇 군데인지 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 센서 데이터의 개수 $N$이 주어집니다 
- $2 \le N \le 1,000,000$
- 두 번째 줄에 각 센서의 ID를 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 ID는 $1$ 이상 $10,000$ 이하의 자연수입니다.

## 출력 형식 (Output Format)
- 스트림을 두 구간으로 나누었을 때, 신뢰 점검 지점이 되는 위치의 총 개수를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
1 1 2 3 3 2
{TICK}
**Output:**
{TICK}
5
{TICK}

- **1번째 뒤:** A{1}(유일ID 1, 1개) / B{1, 2, 3, 3, 2}(유일 ID 1, 1개) $\rightarrow$ **일치 (1개)**
- **2번째 뒤:** A{1, 1}(유일 0개) / B{2, 3, 3, 2}(유일 0개) $\rightarrow$ **일치 (0개)**
- **3번째 뒤:** A{1, 1, 2}(유일 ID 2, 1개) / B{3, 3, 2}(유일 ID 2, 1개) $\rightarrow$ **일치 (1개)**
- **4번째 뒤:** A{1, 1, 2, 3}(유일 ID 2, 3, 2개) / B{3, 2}(유일 ID 3, 2, 2개) $\rightarrow$ **일치 (2개)**
- **5번째 뒤:** A{1, 1, 2, 3, 3}(유일 ID 2, 1개) / B{2}(유일 ID 2, 1개) $\rightarrow$ **일치 (1개)**
- 따라서 가능한 모든 5개의 절단 지점이 전부 신뢰 점검 지점이 됩니다.

### 예시 2
**Input:**
{TICK}
5
1 2 3 4 5
{TICK}
**Output:**
{TICK}
0
{TICK}

- 어떤 지점을 잘라도 왼쪽과 오른쪽의 데이터 개수가 다르므로, 모든 데이터가 유일한 이 상황에서는 유일 ID 개수를 같게 만들 수 없습니다. (예: 1번째 뒤 자르면 A:1개, B:4개)

### 예시 3
**Input:**
{TICK}
4
1 1 2 2
{TICK}
**Output:**
{TICK}
1
{TICK}
- 2번째 뒤를 자르면 A{1,1}(유일:0), B{2,2}(유일:0)으로 개수가 **0개**로 동일합니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 대량 데이터 처리를 위한 최적화된 입력 방식
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # ID 범위가 10,000 이하이므로 배열을 사용하여 속도 향상
    data = list(map(int, input_data[1:]))
    
    # 오른쪽 구간 빈도 측정
    right_freq = [0] * 10001
    right_unique_count = 0
    for x in data:
        right_freq[x] += 1
    
    # 초기에 오른쪽 구간에서 유일(빈도가 정확히 1)한 ID 개수 계산
    for f in right_freq:
        if f == 1:
            right_unique_count += 1
            
    left_freq = [0] * 10001
    left_unique_count = 0
    answer = 0
    
    # 슬라이딩 윈도우 방식으로 경계면 이동
    for i in range(n - 1):
        val = data[i]
        
        # 1. 왼쪽으로 데이터 추가
        old_l_f = left_freq[val]
        left_freq[val] += 1
        if left_freq[val] == 1: # 0에서 1이 되면 유일 ID 증가
            left_unique_count += 1
        elif old_l_f == 1: # 1에서 2가 되면 더 이상 유일하지 않음
            left_unique_count -= 1
            
        # 2. 오른쪽에서 데이터 제거
        old_r_f = right_freq[val]
        right_freq[val] -= 1
        if right_freq[val] == 1: # 2에서 1이 되면 유일 ID로 부활
            right_unique_count += 1
        elif old_r_f == 1: # 1에서 0이 되면 유일 ID 소멸
            right_unique_count -= 1
            
        # 3. 조건 비교
        if left_unique_count == right_unique_count:
            answer += 1
            
    sys.stdout.write(str(answer) + '\n')

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, data):
    r_f = [0] * 10001
    for x in data: r_f[x] += 1
    r_u = sum(1 for f in r_f if f == 1)
    l_f = [0] * 10001
    l_u = 0
    ans = 0
    for i in range(n - 1):
        v = data[i]
        # Left Update
        if l_f[v] == 0: l_u += 1
        elif l_f[v] == 1: l_u -= 1
        l_f[v] += 1
        # Right Update
        if r_f[v] == 1: r_u -= 1
        elif r_f[v] == 2: r_u += 1
        r_f[v] -= 1
        if l_u == r_u: ans += 1
    return str(ans)

for i in range(1, 21):
    if i <= 5: n = random.randint(2, 100)
    elif i <= 15: n = random.randint(1000, 10000)
    else: n = 1000000 # 성능 테스트를 위한 최대치
    
    # ID 범위를 좁게 설정해야 '유일 ID'가 변하는 상황이 자주 발생함
    max_id = random.randint(10, 100) if i % 2 == 0 else 10000
    tags = [random.randint(1, max_id) for _ in range(n)]
    
    input_str = f"{n}\n" + " ".join(map(str, tags))
    ans = solve_internal(n, tags)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P132' 문제 생성이 완료되었습니다.")