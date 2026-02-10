import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P065 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P065")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 고집쟁이 자판기

## 문제 설명
한동대학교 기숙사에 있는 음료수 자판기는 지폐 인식기가 매우 까다롭기로 유명합니다. 지폐가 조금이라도 구겨져 있으면 "윙~" 소리와 함께 뱉어내기 일쑤입니다.

목이 마른 '노아'는 $N$장의 천 원짜리 지폐를 가지고 있습니다. 각 지폐는 주름 정도(Wrinkle Level)를 가지고 있으며, 자판기는 주름 정도가 **$K$ 이하**인 지폐만 받아들입니다.

진우는 다음과 같은 순서로 지폐를 넣습니다.

1. 가지고 있는 지폐 뭉치의 맨 앞에 있는 지폐를 자판기에 넣습니다.
2. **성공:** 지폐의 주름 정도가 $K$ 이하라면, 자판기가 지폐를 받아들이고 결제가 완료됩니다.
3. **실패:** 지폐의 주름 정도가 $K$보다 크다면, 자판기가 지폐를 뱉어냅니다.
   - 노아는 다시 나온 지폐를 손으로 펴서 주름 정도를 **$D$만큼 줄입니다.** (단, 0보다 작아지면 0이 됩니다.)
   - 이후 사용을 대비해 노아는 조금 더 펴진 지폐를 다시 지폐 뭉치의 **맨 뒤**로 보냅니다.
4. 모든 지폐가 자판기에 들어갈 때까지 이 과정을 반복합니다.

진우가 가진 지폐들이 자판기에 **최종적으로 들어가는 순서**를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 지폐의 개수 $N$, 자판기의 허용 주름 정도 $K$, 한 번에 펴지는 정도 $D$가 공백으로 구분되어 주어집니다.
  ($1 \le N \le 100$, $1 \le K \le 100$, $1 \le D \le 100$)
- 두 번째 줄에 각 지폐의 초기 주름 정도 $W_1, W_2, \dots, W_N$이 공백으로 구분되어 주어집니다.
  ($1 \le W_i \le 200$)
- 지폐의 번호는 입력된 순서대로 1번부터 $N$번까지입니다.

## 출력 형식 (Output Format)
- 지폐가 자판기에 수락되는 순서대로 지폐 번호를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 20 20
50 10 80
{TICK}

**Output:**
{TICK}
2 1 3
{TICK}

- 지폐 주름 허용치 $K=20$, 감소량 $D=20$. 
- 지폐뭉치 [(1번지폐, 주름정도 50), (2번지폐, 주름정도 10), (3번지폐, 주름정도 80)]
- **1번(50):** $50 > 20$ (거절). 주름 $50-20=30$. 맨 뒤로. 
  - 지폐뭉치 [(2, 10), (3, 80), (1, 30)]
- **2번(10):** $10 \le 20$ (수락). **출력: 2**. 
  - 지폐뭉치 [(3, 80), (1, 30)]
- **3번(80):** $80 > 20$ (거절). 주름 $80-20=60$. 맨 뒤로. 
  - 지폐뭉치 [(1, 30), (3, 60)]
- **1번(30):** $30 > 20$ (거절). 주름 $30-20=10$. 맨 뒤로. 
  - 지폐뭉치 [(3, 60), (1, 10)]
- **3번(60):** $60 > 20$ (거절). 주름 $60-20=40$. 맨 뒤로. 
  - 지폐뭉치 [(1, 10), (3, 40)]
- **1번(10):** $10 \le 20$ (수락). **출력: 1**. 
  - 지폐뭉치 [(3, 40)]
- **3번(40):** $40 > 20$ (거절). 주름 $40-20=20$. 맨 뒤로. 
  - 지폐뭉치 [(3, 20)]
- **3번(20):** $20 \le 20$ (수락). **출력: 3**.

### 예시 2
**Input:**
{TICK}
4 10 5
12 15 8 20
{TICK}

**Output:**
{TICK}
3 1 2 4
{TICK}

- 3번(8) 지폐는 바로 통과합니다.
- 나머지는 $K=10$ 이하가 될 때까지 $D=5$씩 줄어들며 순환합니다.

### 예시 3
**Input:**
{TICK}
2 5 1
100 100
{TICK}

**Output:**
{TICK}
1 2
{TICK}

- 둘 다 주름이 100으로 시작하지만, 1번 지폐가 먼저 줄어들어 통과하고 그 다음 2번 지폐가 통과합니다.
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1]) # 허용 주름
    d = int(input_data[2]) # 펴지는 정도
    
    # (지폐 번호, 주름 정도)
    queue = deque()
    wrinkles = list(map(int, input_data[3:]))
    for i in range(n):
        queue.append((i + 1, wrinkles[i]))
        
    results = []
    
    while queue:
        idx, current_wrinkle = queue.popleft()
        
        if current_wrinkle <= k:
            # 수락
            results.append(str(idx))
        else:
            # 거절 -> 주름 펴서 뒤로
            new_wrinkle = max(0, current_wrinkle - d)
            queue.append((idx, new_wrinkle))
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, k, d, w_list):
    from collections import deque
    queue = deque()
    for i in range(n):
        queue.append((i + 1, w_list[i]))
    
    results = []
    while queue:
        idx, curr = queue.popleft()
        if curr <= k:
            results.append(str(idx))
        else:
            new_w = max(0, curr - d)
            queue.append((idx, new_w))
            
    return " ".join(results)

test_data = []
# 예시 데이터
test_data.append((3, 20, 20, [50, 10, 80]))
test_data.append((4, 10, 5, [12, 15, 8, 20]))
test_data.append((2, 5, 1, [100, 100]))

# 랜덤 데이터 생성
for _ in range(17):
    n = random.randint(5, 50)
    k = random.randint(10, 50)
    d = random.randint(5, 30)
    w_list = [random.randint(1, 200) for _ in range(n)]
    test_data.append((n, k, d, w_list))

for i, (n, k, d, w_list) in enumerate(test_data, 1):
    input_str = f"{n} {k} {d}\n{' '.join(map(str, w_list))}"
    ans = solve_internal(n, k, d, w_list)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P065' 문제 생성이 완료되었습니다. ")