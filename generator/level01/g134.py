import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P134 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P134")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 조립 라인 검수

## 문제 설명
자동차 부품 공장의 현석이는 컨베이어 벨트를 통해 운반되는 $N$개의 부품을 두 명의 검수원에게 배분하려고 합니다. 모든 부품은 일렬로 줄지어 들어오며, 각 부품에는 모델 번호가 적혀 있습니다.

현석이는 벨트의 특정 지점을 한 군데 잘라서, 왼쪽 구간은 1번 검수원에게, 오른쪽 구간은 2번 검수원에게 맡길 계획입니다. 이때 현석이는 두 검수원이 각각 맡게 되는 '부품 모델의 종류 수'가 동일해지도록 나누고 싶어 합니다. 

예를 들어, 부품 모델 번호가 `[10, 20, 10, 30, 10, 40]` 순서로 들어온다고 가정해 봅시다.
- 3번째 부품(10)과 4번째 부품(30) 사이를 자를 경우:
    - 1번 검수원: `[10, 20, 10]` → 부품 종류는 2가지($10, 20$)입니다.
    - 2번 검수원: `[30, 10, 40]` → 부품 종류는 3가지($30, 10, 40$)입니다.
    - 종류 수가 다르므로 공평하지 않습니다.
- 4번째 부품(30)과 5번째 부품(10) 사이를 자를 경우:
    - 1번 검수원: `[10, 20, 10, 30]` → 부품 종류는 3가지($10, 20, 30$)입니다.
    - 2번 검수원: `[10, 40]` → 부품 종류는 2가지($10, 40$)입니다.
    - 종류 수가 다르므로 공평하지 않습니다.

부품 모델 번호 리스트가 주어질 때, 두 검수원이 맡는 부품 모델의 종류 수가 같아지도록 벨트를 자르는 방법은 총 몇 가지인지 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 부품의 개수 $N$이 주어집니다 (
- $2 \le N \le 1,000,000$
- 두 번째 줄에 각 부품의 모델 번호를 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 번호는 $1$ 이상 $10,000$ 이하의 자연수입니다.

## 출력 형식 (Output Format)
- 양쪽 구간의 서로 다른 부품 종류 수가 같아지는 절단 위치의 총 개수를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
10 20 10 30 10 40
{TICK}
**Output:**
{TICK}
0
{TICK}
- 어느 지점을 잘라도 한쪽은 항상 종류가 더 많거나 적습니다. 조건을 만족하는 지점이 없습니다.

### 예시 2
**Input:**
{TICK}
5
1 2 1 2 1
{TICK}
**Output:**
{TICK}
2
{TICK}

- 2번째 뒤를 자를 때:  A{1,2}(2종), B{1,2,1}(2종) → **일치**
- 3번째 뒤를 자를 때:  A{1,2,1}(2종), B{2,1}(2종) → **일치**
- 총 2가지 방법이 있습니다.

### 예시 3
**Input:**
{TICK}
8
1 1 2 3 4 4 3 2
{TICK}
**Output:**
{TICK}
1
{TICK}

- **1번째 뒤:** A{1}(1종) / B{1, 2, 3, 4, 4, 3, 2}(4종) 
  - 불일치
- **2번째 뒤:** A{1, 1}(1종) / B{2, 3, 4, 4, 3, 2}(3종)
  - 불일치
- **3번째 뒤:** A{1, 1, 2}(2종) / B{3, 4, 4, 3, 2}(3종) 
  - 불일치
- **4번째 뒤:** A{1, 1, 2, 3}(3종) / B{4, 4, 3, 2}(3종) 
  - **일치 (성공!)**
- **5번째 뒤:** A{1, 1, 2, 3, 4}(4종) / B{4, 3, 2}(3종) 
  - 불일치
- **6번째 뒤:** A{1, 1, 2, 3, 4, 4}(4종) / B{3, 2}(2종)
  - 불일치
- **7번째 뒤:** A{1, 1, 2, 3, 4, 4, 3}(4종) / B{2}(1종)
  - 불일치
- 따라서 조건을 만족하는 지점은 4번째 부품 뒤, 단 1군데입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 대용량 입력 처리를 위해 표준 입력 전체를 읽음
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    parts = list(map(int, input_data[1:]))
    
    # 오른쪽 그룹(2번 검수원)의 초기 상태 설정
    right_freq = {}
    for p in parts:
        right_freq[p] = right_freq.get(p, 0) + 1
    
    right_types = len(right_freq)
    left_freq = {}
    left_types = 0
    answer = 0
    
    # 벨트를 1번째 부품 뒤부터 N-1번째 부품 뒤까지 하나씩 잘라봄
    for i in range(n - 1):
        p = parts[i]
        
        # 왼쪽 그룹에 부품 추가
        if left_freq.get(p, 0) == 0:
            left_types += 1
        left_freq[p] = left_freq.get(p, 0) + 1
        
        # 오른쪽 그룹에서 부품 제거
        right_freq[p] -= 1
        if right_freq[p] == 0:
            right_types -= 1
            
        # 두 그룹의 고유 모델 종류 수 비교
        if left_types == right_types:
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
    r_f = {}
    for x in data: r_f[x] = r_f.get(x, 0) + 1
    r_t = len(r_f)
    l_f = {}
    l_t = 0
    ans = 0
    for i in range(n - 1):
        v = data[i]
        if l_f.get(v, 0) == 0: l_t += 1
        l_f[v] = l_f.get(v, 0) + 1
        r_f[v] -= 1
        if r_f[v] == 0: r_t -= 1
        if l_t == r_t: ans += 1
    return str(ans)

for i in range(1, 21):
    if i <= 5: n = random.randint(2, 100)
    elif i <= 15: n = random.randint(1000, 10000)
    else: n = 1000000
    
    max_id = random.randint(2, 500) if i % 2 == 0 else 10000
    data = [random.randint(1, max_id) for _ in range(n)]
    
    input_str = f"{n}\n" + " ".join(map(str, data))
    ans = solve_internal(n, data)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P134' 문제 생성이 완료되었습니다. ")