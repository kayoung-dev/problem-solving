import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P133 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P133")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 보안 키 생성기

## 문제 설명
보안 전문가 지원이는 새로운 암호화 시스템을 위한 보안 키 생성 로직을 설계하고 있습니다. 이 시스템은 초기 키 값으로 주어진 긴 숫자열을 아래의 규칙에 따라 **단 한 자리의 문자**가 될 때까지 반복해서 변형합니다.

**[변형 규칙]**
1. 현재 숫자열에서 모든 **짝수**($0, 2, 4, 6, 8$)를 찾아 제거합니다. <br />(변환중 문자가 있다면 문자도 제외)
2. 남은 숫자들을 모두 더한 합계를 $S$라고 합니다. 만약 남은 숫자가 하나도 없다면 $S$는 $0$이 됩니다.
3. 이 합계 $S$를 **16진법**($0 \sim 9, A \sim F$)으로 변환한 문자열을 새로운 키 값으로 삼습니다. 
   *(단, 16진법 변환 시 알파벳은 모두 대문자를 사용합니다.)*

예를 들어, 초기 키 값이 "$24378$"이라면 다음과 같은 과정을 거칩니다:
- **1회차:** 짝수($2, 4, 8$)를 제거하면 "$37$"이 남습니다. 숫자의 합 $S = 3 + 7 = 10$입니다. $10$을 16진법으로 변환하면 "$A$"가 됩니다.
- **종료:** 결과가 단 한 자리("$A$")가 되었으므로 변환을 멈춥니다.

지원을 도와 초기 키 값 $s$가 주어졌을 때, 최종 보안 키가 생성될 때까지 수행한 **총 변환 횟수**와 최종적으로 생성된 **보안 키**를 출력하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 숫자로 이루어진 문자열 $s$가 주어집니다.
- $s$의 길이는 $1$ 이상 $100,000$ 이하입니다.

## 출력 형식 (Output Format)
- 변환 수행 횟수와 최종 생성된 한 자리 보안 키를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
777777777777777
{TICK}
**Output:**
{TICK}
2 9
{TICK}

- **1회차:** `7`이 15개인 문자열입니다. 짝수가 없으므로 합계는 $7 \times 15 = 105$입니다. 
  - $105$를 16진법으로 변환하면 `69`가 됩니다. ($16 \times 6 + 9 = 105$)
- **2회차:** `69`에서 짝수 `6`을 제거하면 `9`만 남습니다. 합계는 $9$입니다. 
  - $9$를 16진법으로 변환하면 `9`입니다.
- 한 자리가 되었으므로 종료합니다. 총 변환 횟수는 2회, 최종 키는 `9`입니다.

### 예시 2
**Input:**
{TICK}
999
{TICK}
**Output:**
{TICK}
2 B
{TICK}

- **1회차:** `999`에서 짝수가 없으므로 그대로 `999`입니다. 
  - 합계 $9+9+9=27$. $27$을 16진법으로 변환하면 `1B`입니다. (아직 두 자리이므로 계속 진행)
- **2회차:** `1B`에서 짝수를 체크합니다. `B`는 숫자가 아니므로 제외되고, `1`은 홀수이므로 남습니다. 합계 $S=1$입니다. $1$을 16진법으로 변환하면 `1`입니다.
- 한 자리가 되었으므로 종료합니다. 총 변환 횟수는 2회입니다.

### 예시 3
**Input:**
{TICK}
2024
{TICK}
**Output:**
{TICK}
1 0
{TICK}

- 모든 숫자가 짝수($2, 0, 2, 4$)이므로 제거하면 남는 것이 없습니다. 합계 $0$을 16진법으로 바꾸면 `0`이 되어 1회 만에 종료됩니다.

---

## 힌트(Note)
임의의 수 $S$를 16진법으로 바꾸려면, $S$가 $0$이 될 때까지 $16$으로 나눈 나머지를 기록한 뒤 이를 역순으로 읽으면 됩니다.
- 나머지가 $10, 11, 12, 13, 14, 15$인 경우 각각 $A, B, C, D, E, F$로 변환합니다.
- 예: $S = 27$
  -  $27$을 $16$으로 나누면 몫은 $1$, 나머지는 $11$($B$)입니다.
  - $1$을 $16$으로 나누면 몫은 $0$, 나머지는 $1$입니다.
  - 나머지를 역순으로 조합하면 "$1B$"가 됩니다.


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
    while len(s) > 1:
        steps += 1
        current_sum = 0
        
        # 현재 문자열에서 숫자만 골라내어 짝수인지 확인
        for char in s:
            if char.isdigit():
                digit = int(char)
                if digit % 2 != 0: # 홀수인 경우만 합산
                    current_sum += digit
        
        # 합계를 16진법 대문자로 변환 (hex()는 '0x'를 붙이고 소문자임)
        s = hex(current_sum)[2:].upper()
        
    print(f"{steps} {s}")

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
    while len(s) > 1:
        steps += 1
        s_sum = 0
        for c in s:
            if '0' <= c <= '9':
                d = int(c)
                if d % 2 != 0: s_sum += d
        s = hex(s_sum)[2:].upper()
    return f"{steps} {s}"

for i in range(1, 21):
    if i <= 5:
        n = random.randint(1, 10)
    elif i <= 15:
        n = random.randint(100, 1000)
    else:
        n = random.randint(5000, 100000)
    
    s_val = "".join([str(random.randint(0, 9)) for _ in range(n)])
    ans = solve_internal(s_val)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(s_val)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P133' 문제 생성이 완료되었습니다.")