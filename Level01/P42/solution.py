import sys
from collections import deque

def solution():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)

    if n == 1:
        print(1)
        return

    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:
        queue.popleft()            # 1. 맨 위 버리기
        queue.append(queue.popleft()) # 2. 다음 카드를 맨 뒤로
        
    print(queue[0])

if __name__ == "__main__":
    solution()
