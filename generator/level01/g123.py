import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P123 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P123")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 숨은 거스름돈 찾기

## 문제 설명
주인공 준서는 어제 방 안에서 현금을 세다가 실수로 동전 한 개를 떨어뜨렸습니다. 준서의 방바닥은 세로 $N$칸, 가로 $M$칸인 격자 모양의 타일로 되어 있습니다. 

준서는 방의 왼쪽 위 구석$(1, 1)$부터 시작하여 오른쪽 아래 구석$(N, M)$까지 한 칸씩 꼼꼼하게 살피며 동전을 찾으려고 합니다. 준서는 위쪽 줄부터 확인하고, 한 줄의 확인이 끝나면 바로 아래 줄의 왼쪽부터 다시 확인을 이어갑니다.

방바닥 각 칸의 정보가 주어질 때, 동전이 있는 위치의 좌표(행, 열)를 찾아 출력하는 프로그램을 작성해 주세요. 동전은 방 안에 단 하나만 존재하며, 동전이 있는 칸은 숫자 $1$로, 나머지 빈칸은 $0$으로 표시됩니다.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 방바닥의 세로 크기 $N$과 가로 크기 $M$이 공백으로 구분되어 주어집니다 
- $1 \le N, M \le 50$
- 두 번째 줄부터 $N$개의 줄에 걸쳐 각 줄마다 $M$개의 숫자가 공백으로 구분되어 주어집니다.

## 출력 형식 (Output Format)
- 동전이 놓인 위치의 행 번호와 열 번호를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3 4
0 0 0 0
0 0 1 0
0 0 0 0
{TICK}
**Output:**
{TICK}
2 3
{TICK}
- 동전(숫자 1)이 2번째 줄(행)의 3번째 칸(열)에 있으므로 $2$ $3$을 출력합니다.

### 예시 2
**Input:**
{TICK}
2 2
1 0
0 0
{TICK}
**Output:**
{TICK}
1 1
{TICK}
- 첫 번째 줄의 첫 번째 칸에 동전이 있으므로 $1$ $1$을 출력합니다.

### 예시 3
**Input:**
{TICK}
4 1
0
0
0
1
{TICK}
**Output:**
{TICK}
4 1
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
    m = int(input_data[1])
    grid = input_data[2:]
    
    # 2차원 격자를 순회하며 1을 찾음
    for r in range(n):
        for c in range(m):
            # 1차원 리스트로 읽어들인 grid에서 현재 위치 계산
            if int(grid[r * m + c]) == 1:
                print(f"{r + 1} {c + 1}")
                return

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    n = random.randint(1, 50)
    m = random.randint(1, 50)
    
    # 동전 위치 무작위 설정
    target_r = random.randint(0, n - 1)
    target_c = random.randint(0, m - 1)
    
    input_lines = [f"{n} {m}"]
    for r in range(n):
        row = []
        for c in range(m):
            if r == target_r and c == target_c:
                row.append("1")
            else:
                row.append("0")
        input_lines.append(" ".join(row))
    
    input_str = "\n".join(input_lines)
    ans = f"{target_r + 1} {target_c + 1}"
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P123' 문제 생성이 완료되었습니다. ")