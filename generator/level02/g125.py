import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P125 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P125")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 정밀 지지대 조립

## 문제 설명
신제품 프로토타입을 제작 중인 엔지니어 지민이는 정밀 기계의 틀을 완성하기 위해 두 개의 금속 막대를 일렬로 연결하여 길이가 정확히 $100cm$인 지지대를 만들려고 합니다.

창고에는 총 $N$개의 금속 막대가 보관되어 있으며, 각 막대의 길이는 서로 다를 수 있습니다. 지후는 이 중에서 **두 개의 막대**를 골라 합쳤을 때, 그 길의 합이 오차 없이 정확히 $100cm$가 되는 조합이 있는지 확인해야 합니다.

창고에 있는 막대 $N$개의 길이 정보가 주어질 때, 두 막대를 조합하여 $100cm$ 지지대를 만들 수 있으면 `YES`를, 어떤 조합으로도 만들 수 없으면 `NO`를 출력하는 프로그램을 작성하세요. (단, 하나의 막대를 중복해서 사용할 수는 없습니다.)

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 보관된 금속 막대의 개수 $N$이 주어집니다 
- $2 \le N \le 100$
- 두 번째 줄에 각 막대의 길이를 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 길이는 $1cm$ 이상 $99cm$ 이하입니다.

## 출력 형식 (Output Format)
- 정확히 $100cm$를 만들 수 있는 막대 쌍이 존재하면 `YES`, 존재하지 않으면 `NO`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
40 50 60 55
{TICK}
**Output:**
{TICK}
YES
{TICK}
- 40cm 막대와 60cm 막대를 연결하면 $40 + 60 = 100$이 되므로 `YES`를 출력합니다.

### 예시 2
**Input:**
{TICK}
3
45 50 45
{TICK}
**Output:**
{TICK}
NO
{TICK}
- 어떤 두 막대를 골라도 합이 $100cm$가 되지 않습니다. (
- 45+50=95, 45+45=90

### 예시 3
**Input:**
{TICK}
5
10 20 30 40 50
{TICK}
**Output:**
{TICK}
NO
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
    lengths = list(map(int, input_data[1:]))
    
    # 이중 반복문을 통해 모든 가능한 두 막대의 조합(Pair)을 전수 조사
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            if lengths[i] + lengths[j] == 100:
                found = True
                break
        if found:
            break
            
    if found:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, lengths):
    for i in range(n):
        for j in range(i + 1, n):
            if lengths[i] + lengths[j] == 100:
                return "YES"
    return "NO"

for i in range(1, 21):
    n = random.randint(2, 100)
    
    # YES와 NO 케이스를 약 50:50 비율로 생성
    if i % 2 == 0:
        # YES 케이스: 무작위 두 위치를 골라 합이 100이 되도록 설정
        lengths = [random.randint(10, 90) for _ in range(n)]
        idx1, idx2 = random.sample(range(n), 2)
        val1 = random.randint(10, 90)
        lengths[idx1] = val1
        lengths[idx2] = 100 - val1
    else:
        # NO 케이스: 모든 합이 100이 되지 않도록 유도 (예: 모두 49 이하)
        lengths = [random.randint(10, 49) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, lengths))
    ans = solve_internal(n, lengths)
    
    # 1.in, 1.out 형식으로 저장
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P125' 문제 생성이 완료되었습니다.")