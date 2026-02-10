import sys

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
