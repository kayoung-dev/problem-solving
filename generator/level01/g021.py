import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P21 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P021")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "연금술사의 물약 제조"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack", "Simulation"]
---

## description
왕국 최고의 연금술사 **지수**는 마법의 물약을 만들기 위해 재료 창고에 왔습니다. <br />
재료 창고에는 $N \\times N$ 크기의 격자 모양 선반이 있고, 각 칸에는 다양한 마법 재료들이 쌓여 있습니다. (0은 빈 칸을 의미합니다.) <br />

지수는 마법의 집게를 이용해 특정 열(Column)을 선택하여 가장 위에 있는 재료를 하나 꺼냅니다. 꺼낸 재료는 즉시 옆에 있는 **마법의 솥**에 넣습니다.

마법의 솥은 **스택(Stack)** 구조로 되어 있어 재료가 아래서부터 차곡차곡 쌓입니다. 이때, 솥 안에 **같은 종류의 재료 두 개가 연속해서 닿게 되면**, 두 재료는 화학 반응을 일으켜 **폭발하며 사라집니다.**

지수가 재료를 꺼내는 순서가 담긴 배열 `moves`가 주어질 때, 모든 과정을 마친 후 **폭발하여 사라진 재료의 총 개수**를 구하는 프로그램을 작성하세요. <br />

규칙은 다음과 같습니다:
1. 격자의 각 칸에는 정수로 표현된 재료가 들어있으며, 0은 빈 칸입니다.
2. 집게는 해당 열의 가장 위에 있는 재료를 집어 올립니다. 만약 해당 열에 재료가 없다면 아무 일도 일어나지 않습니다.
3. 솥에 넣을 때, 솥의 가장 위에 있는 재료와 현재 넣는 재료가 같다면 둘 다 사라집니다. (폭발)
4. 폭발은 연쇄적으로 일어날 수 있습니다. (예: `1`이 있는 상태에서 `1`이 들어와 폭발해 사라졌는데, 그 아래에 `2`가 있었고, 솥에 원래 `2`가 있었다면 또 폭발)

## input_description
- 첫 번째 줄에 격자의 크기 $N$이 주어집니다. ($5 \\le N \\le 30$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 격자의 상태가 주어집니다. 각 줄은 $N$개의 정수(재료 번호)로 이루어져 있습니다. ($0 \\le$ 재료 $\\le 100$)
- 그 다음 줄에 지수가 움직인 횟수 $M$이 주어집니다. ($1 \\le M \\le 1,000$)
- 마지막 줄에 지수가 선택한 열의 번호 moves가 공백으로 구분되어 주어집니다. (열 번호는 $1$부터 $N$까지입니다.)

## output_description
- 폭발하여 사라진 재료의 총 개수를 출력합니다.

# samples

### input 1
{TICK}
5
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1
8
1 5 3 5 1 2 1 4
{TICK}

### output 1
{TICK}
4
{TICK}


### input 2
{TICK}
4
0 0 0 0
0 0 0 0
1 2 3 4
1 2 3 4
8
1 2 3 4 4 3 2 1
{TICK}

### output 2
{TICK}
8
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
  f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
 input = sys.stdin.readline
 
 # 입력 처리
 try:
     line1 = input().strip()
     if not line1: return # End of input
     n = int(line1)
     
     board = []
     for _ in range(n):
         board.append(list(map(int, input().split())))
         
     m = int(input().strip())
     moves = list(map(int, input().split()))
 except ValueError:
     return

 stack = []
 answer = 0
 
 for move in moves:
     col = move - 1  # 0-based index 변환
     
     for row in range(n):
         if board[row][col] != 0:
             picked_item = board[row][col]
             board[row][col] = 0  # 집어간 자리는 빈칸(0)으로 만듦
             
             # 스택 로직
             if stack and stack[-1] == picked_item:
                 stack.pop()
                 answer += 2
             else:
                 stack.append(picked_item)
             
             break # 인형을 하나 집었으면 해당 열 탐색 종료

 print(answer)

if __name__ == "__main__":
 solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
 f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(n, board_origin, moves):
 # board_origin이 수정되지 않도록 깊은 복사
 board = [row[:] for row in board_origin]
 stack = []
 answer = 0
 
 for move in moves:
     col = move - 1
     for row in range(n):
         if board[row][col] != 0:
             picked = board[row][col]
             board[row][col] = 0
             
             if stack and stack[-1] == picked:
                 stack.pop()
                 answer += 2
             else:
                 stack.append(picked)
             break
 return answer

# 수동 케이스 (예제 1)
manual_n = 5
manual_board = [
 [0, 0, 0, 0, 0],
 [0, 0, 1, 0, 3],
 [0, 2, 5, 0, 1],
 [4, 2, 4, 4, 2],
 [3, 5, 1, 3, 1]
]
manual_moves = [1, 5, 3, 5, 1, 2, 1, 4]
manual_ans = solve_internal(manual_n, manual_board, manual_moves)

test_cases = []
# 입력 문자열 포맷팅 함수
def format_input(n, board, moves):
 res = f"{n}\n"
 for row in board:
     res += " ".join(map(str, row)) + "\n"
 res += f"{len(moves)}\n"
 res += " ".join(map(str, moves))
 return res

test_cases.append((format_input(manual_n, manual_board, manual_moves), str(manual_ans)))

# 랜덤 케이스 생성
for _ in range(19):
 n = random.randint(5, 30)
 # 0(빈칸)을 포함하여 재료 채우기 (빈칸 비율 30% 정도)
 board = []
 for __ in range(n):
     row = []
     for ___ in range(n):
         if random.random() < 0.3:
             row.append(0)
         else:
             row.append(random.randint(1, 100))
     board.append(row)
 
 # moves 생성
 m = random.randint(10, 500)
 moves = [random.randint(1, n) for _ in range(m)]
 
 # 정답 계산
 ans = solve_internal(n, board, moves)
 
 test_cases.append((format_input(n, board, moves), str(ans)))

# 파일 저장 
for i, (inp, out) in enumerate(test_cases, 1):
 with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
     f.write(inp)
 with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
     f.write(out)

print(f"✅ 'Level01/P021' 문제 생성이 완료되었습니다.")