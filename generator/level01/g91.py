import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P91 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P91")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 자릿수 내림차순 코드 만들기

## 문제 설명
데이터 담당자 **지훈**은 숫자로 된 식별 코드를 점검하고 있습니다.  
지훈은 코드의 자릿수를 **큰 숫자부터 내림차순으로 재배치**해 새로운 점검용 코드를 만들려고 합니다.

정수 N이 주어질 때, N을 구성하는 자릿수들을 내림차순으로 정렬하여 만든 정수를 출력하세요.

- 예: N = 31042이면 자릿수는 3, 1, 0, 4, 2 이고  
  내림차순 정렬 결과는 4, 3, 2, 1, 0 이므로 결과는 43210 입니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 N이 주어집니다.  
  (0 ≤ N ≤ 10^18)

## 출력 형식 (Output Format)
- N의 자릿수를 내림차순으로 정렬해 만든 정수를 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
31042
{TICK}
**Output:**
{TICK}
43210
{TICK}
- 자릿수는 3, 1, 0, 4, 2 입니다.
- 내림차순 정렬 결과는 4, 3, 2, 1, 0 입니다.

### 예시 2
**Input:**
{TICK}
1000
{TICK}
**Output:**
{TICK}
1000
{TICK}
- 자릿수는 1, 0, 0, 0 입니다.
- 내림차순 정렬 결과도 1, 0, 0, 0 입니다.

### 예시 3
**Input:**
{TICK}
0
{TICK}
**Output:**
{TICK}
0
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return
    digits = list(s)
    digits.sort(reverse=True)
    print("".join(digits))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(n_str: str) -> str:
    return "".join(sorted(n_str, reverse=True))

random.seed(91)

test_data = ["31042", "1000", "0"]

for _ in range(17):
    length = random.randint(1, 19)
    first = str(random.randint(1, 9))
    rest = "".join(str(random.randint(0, 9)) for _ in range(length - 1))
    test_data.append(first + rest)

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, n_str in enumerate(test_data, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w") as f:
        f.write(n_str + "\n")
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w") as f:
        f.write(solve_internal(n_str) + "\n")

print("✅ 'Level01/P91' 문제 생성이 완료되었습니다.")
