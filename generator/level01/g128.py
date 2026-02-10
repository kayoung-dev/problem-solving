import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P128 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P128")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 서버실 정밀 냉각 제어

## 문제 설명
대규모 데이터 센터를 운영하는 엔지니어 민규는 서버실의 온도 관리를 담당하고 있습니다. 서버실은 가로 $N$칸, 세로 $N$칸의 격자 형태로 구역이 나뉘어 있으며, 각 구역마다 설치된 온도 센서가 현재 발생 중인 열기(Heat)의 수치를 실시간으로 보고합니다.

최근 특정 구역의 서버들이 과열되는 문제를 해결하기 위해, 민규는 **가로 3칸, 세로 3칸(총 9개 구역)** 을 한꺼번에 커버할 수 있는 강력한 정밀 냉각 장치를 도입했습니다. 이 장치는 서버실의 경계를 벗어나지 않게 딱 한 곳에만 설치할 수 있습니다.

냉각 효율을 극대화하기 위해, 민규는 **열기 수치의 합계가 가장 높은 $3 \times 3$ 구역**을 찾아 그곳에 장치를 가동하려고 합니다. 서버실의 온도 지도 정보가 주어질 때, 장치가 해결할 수 있는 열기 수치의 최댓값을 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 서버실의 크기 $N$이 주어집니다 
- $3 \le N \le 50$
- 두 번째 줄부터 $N$개의 줄에 걸쳐, 각 줄마다 해당 구역의 열기 수치 정보 $N$개가 공백으로 구분되어 정수로 주어집니다.
- 각 구역의 열기 수치는 $0$ 이상 $100$ 이하의 정수입니다.

## 출력 형식 (Output Format)
- 냉각 장치가 커버할 수 있는 $3 \times 3$ 구역의 열기 수치 합계 중 최댓값을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
10 10 10 10
10 20 20 10
10 20 20 10
10 10 10 10
{TICK}
**Output:**
{TICK}
130
{TICK}
- $4 \times 4$ 공간에서 $3 \times 3$ 장치를 설치할 수 있는 위치는 총 4곳입니다. 
- 어떤 위치를 선택하더라도 중앙의 열기 수치 $20$인 구역들이 포함되어 합계는 $130$으로 동일합니다.

### 예시 2
**Input:**
{TICK}
5
1 1 1 1 1
1 50 50 50 1
1 50 80 50 1
1 50 50 50 1
1 1 1 1 1
{TICK}
**Output:**
{TICK}
480
{TICK}

- 정가운데(2행 2열부터 시작하는 $3 \times 3$ 구역)를 확인합니다.
- 해당 구역의 수치들은 $50$이 8개, $80$이 1개입니다.
- 합계는 $50 \times 8 + 80 = 480$이 되며, 이것이 전체에서 가장 높은 열기 합계입니다.

### 예시 3
**Input:**
{TICK}
3
5 5 5
5 5 5
5 5 5
{TICK}
**Output:**
{TICK}
45
{TICK}

- 서버실 크기가 장치 크기와 같은 $3 \times 3$이므로, 설치 가능한 위치는 단 하나입니다.
- 모든 구역의 합인 $5 \times 9 = 45$를 출력합니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 데이터를 모두 읽어와 공백 단위로 분리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 1차원 리스트를 2차원 서버실 격자로 변환
    grid = []
    for i in range(n):
        row = list(map(int, input_data[1 + i*n : 1 + (i+1)*n]))
        grid.append(row)
    
    max_heat_sum = 0
    
    # 냉각 장치의 왼쪽 위 시작점 (r, c)를 이동하며 모든 경우의 수 확인
    # 장치가 3x3이므로 n-2까지만 탐색 가능
    for r in range(n - 2):
        for c in range(n - 2):
            current_sum = 0
            # 시작점 (r, c)로부터 3x3 범위의 열기 합산
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    current_sum += grid[i][j]
            
            # 발견한 합계 중 최댓값 유지
            if current_sum > max_heat_sum:
                max_heat_sum = current_sum
                
    print(max_heat_sum)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, grid):
    max_val = 0
    for r in range(n - 2):
        for c in range(n - 2):
            s = sum(grid[i][j] for i in range(r, r + 3) for j in range(c, c + 3))
            if s > max_val:
                max_val = s
    return str(max_val)

for i in range(1, 21):
    n = random.randint(3, 50)
    grid = [[random.randint(0, 30) for _ in range(n)] for _ in range(n)]
    
    # 20개 중 일부는 무작위 위치에 아주 뜨거운 "Hot Spot" 주입
    if i % 2 == 0:
        start_r = random.randint(0, n - 3)
        start_c = random.randint(0, n - 3)
        for r in range(start_r, start_r + 3):
            for c in range(start_c, start_c + 3):
                grid[r][c] = random.randint(70, 100)
    
    input_str = f"{n}\n" + "\n".join(" ".join(map(str, row)) for row in grid)
    ans = solve_internal(n, grid)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P128' 문제 생성이 완료되었습니다. ")