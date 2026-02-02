import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P124 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P124")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 잊어버린 가방 비밀번호

## 문제 설명
여행을 떠나려던 지혜는 가방의 세 자리 숫자로 된 자물쇠 비밀번호를 잊어버리고 말았습니다. 다행히 지혜는 비밀번호에 대해 한 가지 단서를 기억하고 있습니다. 바로 **세 자리 숫자의 각 자릿수를 모두 더했을 때 특정 숫자 $S$가 된다**는 사실입니다.

예를 들어, 비밀번호가 `123`이라면 각 자릿수의 합은 $1 + 2 + 3 = 6$이 됩니다.

지혜는 비밀번호를 찾기 위해 `000`부터 `999`까지 모든 번호를 하나씩 돌려보려고 합니다. 각 자릿수의 합인 단서 $S$가 주어질 때, 조건을 만족하는 비밀번호 경우의 수는 총 몇 가지인지 출력하세요. 비밀번호의 각 자리는 $0$부터 $9$까지의 숫자로 이루어져 있으며, `001`처럼 앞자리가 $0$인 경우도 하나의 번호로 취급합니다.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 각 자릿수의 합인 $S$가 주어집니다 
- $0 \le S \le 27$

## 출력 형식 (Output Format)
- `000`부터 `999`까지의 숫자 중 각 자릿수의 합이 $S$인 경우의 수를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
1
{TICK}
**Output:**
{TICK}
3
{TICK}
- 각 자릿수의 합이 1인 경우는 `001`, `010`, `100`으로 총 3가지입니다.

### 예시 2
**Input:**
{TICK}
26
{TICK}
**Output:**
{TICK}
3
{TICK}
- 각 자릿수의 합이 26인 경우는 `899`, `989`, `998`으로 총 3가지입니다.

### 예시 3
**Input:**
{TICK}
0
{TICK}
**Output:**
{TICK}
1
{TICK}
- 합이 0인 경우는 `000` 한 가지뿐입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    line = sys.stdin.read().strip()
    if not line:
        return
    
    s = int(line)
    count = 0
    
    # 000부터 999까지 모든 경우를 확인
    for i in range(10):      # 첫 번째 자리
        for j in range(10):  # 두 번째 자리
            for k in range(10): # 세 번째 자리
                if i + j + k == s:
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(s):
    count = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i + j + k == s:
                    count += 1
    return str(count)

# S는 0부터 27까지 가능하므로, 20개의 서로 다른 S를 생성
test_cases = random.sample(range(0, 28), 20)

for i, s_val in enumerate(test_cases, 1):
    input_str = str(s_val)
    ans = solve_internal(s_val)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P124' 문제 생성이 완료되었습니다.")