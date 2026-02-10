import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P135 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P135")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 메모리 정리 시뮬레이션

## 문제 설명
운영체제 개발자인 태호는 메모리 파편화를 해결하기 위해 메모리 블록을 재배치하는 시뮬레이션을 진행하고 있습니다. 메모리 상태는 $0$(빈 공간)과 $1$(사용 중인 데이터)로 구성된 문자열로 표현됩니다. 태호는 메모리가 안정적인 상태인 "$11$"이 될 때까지 아래의 **정리 규칙**을 반복합니다.

**[정리 규칙]**
1. 현재 메모리 문자열에서 모든 $0$을 제거하여 데이터를 한곳으로 모읍니다. 이때 제거된 $0$의 개수를 기록합니다.
2. $0$이 제거되고 남은 데이터의 길이를 $L$이라고 할 때, 새로운 메모리 상태를 $L + 2$의 값을 **이진법**으로 변환한 문자열로 교체합니다.

예를 들어, 초기 상태가 "$1101$"이라면 다음과 같은 과정을 거칩니다:
- **1회차:** $0$을 $1$개 제거합니다. 남은 데이터의 길이는 $L=3$입니다. $L+2 = 5$를 이진법으로 변환하면 "$101$"이 됩니다.
- **2회차:** "$101$"에서 $0$을 $1$개 제거합니다. 남은 데이터의 길이는 $L=2$입니다. $L+2 = 4$를 이진법으로 변환하면 "$100$"이 됩니다.
- **3회차:** "$100$"에서 $0$을 $2$개 제거합니다. 남은 데이터의 길이는 $L=1$입니다. $L+2 = 3$을 이진법으로 변환하면 "$11$"이 됩니다.
- **종료:** 메모리 상태가 "$11$"이 되었으므로 시뮬레이션을 종료합니다.

태호를 도와 초기 메모리 상태 $s$가 주어졌을 때, 종료될 때까지의 **총 정리 횟수**와 **제거된 $0$의 총 개수**를 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 $0$과 $1$로 이루어진 문자열 $s$가 주어집니다.
- $s$의 길이는 $2$ 이상 $150,000$ 이하입니다.
- $s$에는 적어도 하나 이상의 '$1$'이 포함되어 있으며, 초기 상태가 이미 "$11$"인 경우는 주어지지 않습니다.

## 출력 형식 (Output Format)
- 총 정리 횟수와 제거된 $0$의 총 개수를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
1101
{TICK}
**Output:**
{TICK}
3 4
{TICK}

- 1회: `1101` 
  - $0$ 1개 제거, $L=3$ -> $3+2=5$(`101`)
- 2회: `101` 
  - $0$ 1개 제거, $L=2$ -> $2+2=4$(`100`)
- 3회: `100` 
  - $0$ 2개 제거, $L=1$ -> $1+2=3$(`11`)
- 종료 조건 `11`에 도달했습니다. 횟수 3회, $0$ 제거 합계 4개입니다.

### 예시 2
**Input:**
{TICK}
111
{TICK}
**Output:**
{TICK}
2 1
{TICK}

- 1회: `111` 
  - $0$ 0개 제거, $L=3$ -> $3+2=5$(`101`)
- 2회: `101` 
  - $0$ 1개 제거, $L=2$ -> $2+2=4$(`100`)
- 3회: `100` 
  - $0$ 2개 제거, $L=1$ -> $1+2=3$(`11`)
- 총 3회의 변환과 3개의 $0$이 제거됩니다.

### 예시 3
**Input:**
{TICK}
1000001
{TICK}
**Output:**
{TICK}
2 7
{TICK}

- `1000001` 
  - 길이 7, $0$ 5개 제거, $L=2$ -> $2+2=4$(`100`)
- `100` 
  - 길이 3, $0$ 2개 제거, $L=1$ -> $1+2=3$(`11`)
- 총 2회 변환, $0$ 제거 합계 7개입니다.
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
    
    # 종료 조건 "11"을 만족할 때까지 루프
    while s != "11":
        steps += 1
        
        ones_count = s.count('1')
        zeros_count = s.count('0')
        total_zeros += zeros_count
        
        # 새로운 신호 = (L + 2)의 이진법 변환
        s = bin(ones_count + 2)[2:]
        
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
    while s != "11":
        steps += 1
        ones = s.count('1')
        zeros += s.count('0')
        s = bin(ones + 2)[2:]
    return f"{steps} {zeros}"

for i in range(1, 21):
    if i <= 5: n = random.randint(3, 20)
    elif i <= 15: n = random.randint(100, 5000)
    else: n = 150000
    
    s_list = [random.choice(['0', '1']) for _ in range(n)]
    if s_list.count('1') == 0:
        s_list[random.randint(0, n-1)] = '1'
    
    input_str = "".join(s_list)
    # 초기값이 이미 "11"이면 안 되므로 조정
    if input_str == "11": input_str = "111"
    
    ans = solve_internal(input_str)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P135' 문제 생성이 완료되었습니다. ")