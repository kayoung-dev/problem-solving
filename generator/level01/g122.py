import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P122 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P122")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 불량 사과 골라내기

## 문제 설명
과수원 주인 미나 씨는 오늘 수확한 사과들을 시장에 내다 팔기 위해 분류 작업을 하고 있습니다. 시장에 납품하기 위해서는 사과의 무게가 일정 기준 이상이어야 합니다. 

미나 씨는 무게가 기준치인 $K$ 미만인 사과들을 '불량 사과'로 분류하여 따로 빼두려고 합니다. 수확한 사과 $N$개의 무게가 순서대로 주어질 때, 미나 씨가 골라내야 할 불량 사과는 총 몇 개인지 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 수확한 사과의 개수 $N$과 기준 무게 $K$가 공백으로 구분되어 주어집니다 
- $1 \le N \le 100$, $1 \le K \le 500$
- 두 번째 줄에 각 사과의 무게를 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 무게는 $1$ 이상 $1,000$ 이하입니다.

## 출력 형식 (Output Format)
- 기준 무게 $K$보다 가벼운 사과의 총 개수를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6 150
140 160 150 130 170 145
{TICK}
**Output:**
{TICK}
3
{TICK}
- 기준 무게 $150$ 미만인 사과는 $140, 130, 145$로 총 3개입니다. ($150$은 기준과 같으므로 불량 사과가 아닙니다.)

### 예시 2
**Input:**
{TICK}
4 200
210 220 230 240
{TICK}
**Output:**
{TICK}
0
{TICK}
- 모든 사과가 기준 무게 $200$ 이상이므로 불량 사과는 0개입니다.

### 예시 3
**Input:**
{TICK}
3 100
99 98 97
{TICK}
**Output:**
{TICK}
3
{TICK}
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
    weights = list(map(int, input_data[2:]))
    
    bad_apple_count = 0
    
    # 각 사과를 하나씩 확인하며 기준 무게 K 미만인지 검사
    for w in weights:
        if w < k:
            bad_apple_count += 1
            
    print(bad_apple_count)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(k, weights):
    count = 0
    for w in weights:
        if w < k:
            count += 1
    return str(count)

for i in range(1, 21):
    # 테스트 데이터 생성 로직
    n = random.randint(1, 100)
    k = random.randint(100, 300)
    
    # 다양한 분포의 무게 생성
    weights = [random.randint(k - 50, k + 100) for _ in range(n)]
    
    input_str = f"{n} {k}\n" + " ".join(map(str, weights))
    ans = solve_internal(k, weights)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P122' 문제 생성이 완료되었습니다.")