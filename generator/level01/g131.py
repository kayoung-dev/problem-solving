import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P131 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P131")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 데이터 신호의 단계적 응축

## 문제 설명
통신 연구원인 다현이는 우주에서 수신된 정체불명의 신호를 분석하고 있습니다. 이 신호는 $0$과 $1$로 구성된 긴 문자열 형태이며, 다현이는 이 신호를 특정 기준점인 "$10$"이 될 때까지 아래의 **응축 규칙**에 따라 변환하려고 합니다.

**[규칙]**
1. 현재 신호 문자열에서 모든 $0$을 찾아 제거합니다. 이때 제거된 $0$의 개수를 모두 합산하여 기록합니다.
2. $0$을 제거하고 남은 문자열의 길이를 $L$이라고 할 때, 이 길이의 **2배**에 해당하는 값($L \times 2$)을 다시 이진법(2진수) 문자열로 변환하여 새로운 신호로 삼습니다.

예를 들어, 초기 신호가 "$110$"이라면 다음과 같은 과정을 거칩니다:
- **1회차:** $0$을 모두(1개) 제거합니다. 남은 문자열은 "$11$"이며 길이 $L=2$입니다. $L \times 2 = 4$를 이진법으로 변환하면 "$100$"이 됩니다.
- **2회차:** "$100$"에서 $0$을 모두(2개) 제거합니다. 남은 문자열은 "$1$"이며 길이 $L=1$입니다. $L \times 2 = 2$를 이진법으로 변환하면 "$10$"이 됩니다.
- **종료:** 신호가 "$10$"이 되었으므로 변환을 멈춥니다.

다현이를 도와 초기 신호 문자열 $s$가 주어졌을 때, 응축이 끝날 때까지 수행한 **총 변환 횟수**와 그 과정에서 **제거된 $0$의 총 개수**를 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 $0$과 $1$로 이루어진 문자열 $s$가 주어집니다.
- $s$의 길이는 $2$ 이상 $150,000$ 이하입니다.
- $s$에는 적어도 하나 이상의 '$1$'이 포함되어 있으며, 초기 신호가 이미 "$10$"인 경우는 주어지지 않습니다.

## 출력 형식 (Output Format)
- 변환 횟수와 제거된 $0$의 총 개수를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
110
{TICK}
**Output:**
{TICK}
2 3
{TICK}

- `110` 
  - $0$ 제거(1개), 남은 길이 $L=2$. 
  - $2 \times 2 = 4$를 이진수로 바꾸면 `100`.
- `100` 
  - $0$ 제거(2개), 남은 길이 $L=1$. 
  - $1 \times 2 = 2$를 이진수로 바꾸면 `10`.
  - 종료 조건인 `10`에 도달했습니다. 
  - 변환은 2회, 제거된 $0$은 $1+2=3$개입니다.

### 예시 2
**Input:**
{TICK}
1111
{TICK}
**Output:**
{TICK}
2 3
{TICK}

- `1111` 
  - $0$ 제거(0개), 남은 길이 $L=4$. 
  - $4 \times 2 = 8$을 이진수로 바꾸면 `1000`.
- `1000` 
  - $0$ 제거(3개), 남은 길이 $L=1$. 
  - $1 \times 2 = 2$를 이진수로 바꾸면 `10`.
  - 변환은 2회, 제거된 $0$은 $0+3=3$개입니다.

### 예시 3
**Input:**
{TICK}
1101111010
{TICK}
**Output:**
{TICK}
4 7
{TICK}

- `1101111010`에서 $0$을 3개 제거합니다. 
  - 남은 길이는 $L=7$입니다. 
  - $7 \times 2 = 14$를 이진수로 변환하면 `1110`이 됩니다.
- `1110`에서 $0$을 1개 제거합니다. 
  - 남은 길이는 $L=3$입니다. 
  - $3 \times 2 = 6$을 이진수로 변환하면 `110`이 됩니다.
- `110`에서 $0$을 1개 제거합니다. 
  - 남은 길이는 $L=2$입니다. 
  - $2 \times 2 = 4$를 이진수로 변환하면 `100`이 됩니다.
- `100`에서 $0$을 2개 제거합니다. 
  - 남은 길이는 $L=1$입니다. 
  - $1 \times 2 = 2$를 이진수로 변환하면 `10`이 됩니다.
최종적으로 4회 변환이 수행되었고, 제거된 $0$의 총합은 $3+1+1+2 = 7$개입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    steps = 0
    total_zeros = 0
    
    # 신호가 "10"이 될 때까지 반복
    while s != "10":
        steps += 1
        
        # 현재 문자열에서 1의 개수(L)와 0의 개수 파악
        ones_count = s.count('1')
        zeros_count = s.count('0')
        
        total_zeros += zeros_count
        
        # L * 2를 이진법으로 변환
        # bin(n)은 '0b...' 형태이므로 [2:]로 슬라이싱
        s = bin(ones_count * 2)[2:]
        
    print(f"{steps} {total_zeros}")

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(s):
    steps = 0
    zeros = 0
    while s != "10":
        steps += 1
        ones = s.count('1')
        zeros += s.count('0')
        s = bin(ones * 2)[2:]
    return f"{steps} {zeros}"

for i in range(1, 21):
    if i <= 5:
        n = random.randint(2, 50)
    elif i <= 15:
        n = random.randint(100, 5000)
    else:
        n = random.randint(10000, 150000)
    
    # 1이 포함된 무작위 이진 문자열 생성
    s_list = [random.choice(['0', '1']) for _ in range(n)]
    if s_list.count('1') == 0:
        s_list[random.randint(0, n-1)] = '1'
    
    # 초기값이 "10"이 되지 않도록 조정
    temp_s = "".join(s_list)
    if temp_s == "10":
        temp_s = "110"
        
    input_str = temp_s
    ans = solve_internal(input_str)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)


print(f"✅ 'Level01/P131' 문제 생성이 완료되었습니다.")