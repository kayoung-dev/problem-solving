import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P121 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P121")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 가장 키 큰 신입생 찾기

## 문제 설명
새 학기를 맞아 체육 교사 영수 선생님은 신입생들을 운동장에 일렬로 세웠습니다. 영수 선생님은 오늘 체육 수업의 반장을 선출하려고 하는데, **줄 서 있는 학생들 중 키가 가장 큰 학생**을 반장으로 뽑기로 했습니다.

운동장에는 총 $N$명의 학생이 왼쪽부터 순서대로 서 있습니다. 선생님은 왼쪽 끝에 있는 첫 번째 학생부터 차례대로 키를 확인하며 가장 키가 큰 학생을 찾으려고 합니다. 

만약 가장 키가 큰 학생이 여러 명이라면, 선생님에게서 가장 가까운(가장 왼쪽에 있는) 학생을 반장으로 임명합니다. 학생들의 키 정보가 주어졌을 때, 반장이 될 학생이 왼쪽에서 몇 번째에 서 있는지 찾아내는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 신입생의 수 $N$이 주어집니다 
- $1 \le N \le 100$
- 두 번째 줄에 왼쪽 첫 번째 학생부터 마지막 학생까지의 키 정보가 공백으로 구분되어 총 $N$개 주어집니다. 
- 키는 $100$ 이상 $200$ 이하의 정수입니다.

## 출력 형식 (Output Format)
- 가장 키가 큰 학생이 왼쪽에서 몇 번째에 있는지 그 번호를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
160 175 168 175 162
{TICK}
**Output:**
{TICK}
2
{TICK}
- 학생들의 키 중 가장 큰 값은 $175$입니다. $175$인 학생은 2번째와 4번째에 있지만, 가장 왼쪽에 있는 학생을 우선하므로 2를 출력합니다.

### 예시 2
**Input:**
{TICK}
3
180 150 140
{TICK}
**Output:**
{TICK}
1
{TICK}
- 첫 번째 학생의 키가 $180$으로 가장 크기 때문에 1을 출력합니다.

### 예시 3
**Input:**
{TICK}
4
155 155 155 155
{TICK}
**Output:**
{TICK}
1
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2:
            return
        heights = list(map(int, line2.split()))
        
        max_height = -1
        answer_pos = 0
        
        # 모든 학생을 한 명씩 확인하며 가장 큰 키를 찾음
        for i in range(n):
            if heights[i] > max_height:
                max_height = heights[i]
                answer_pos = i + 1  # 1번째부터 시작하므로 +1
                
        print(answer_pos)
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, heights):
    max_h = -1
    pos = 0
    for i in range(len(heights)):
        if heights[i] > max_h:
            max_h = heights[i]
            pos = i + 1
    return str(pos)

for i in range(1, 21):
    # 테스트 케이스 생성 로직
    if i <= 5:
        n = random.randint(1, 10) # 작은 규모
    else:
        n = random.randint(11, 100) # 큰 규모
        
    heights = [random.randint(140, 195) for _ in range(n)]
    
    # 특정 케이스들은 중복 최댓값이 나오도록 유도
    if i % 4 == 0:
        target = max(heights)
        heights[random.randint(0, n-1)] = target
        
    input_str = f"{n}\n" + " ".join(map(str, heights))
    ans = solve_internal(n, heights)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P121' 문제 생성이 완료되었습니다.")