import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except ValueError:
        return

    # 큐 생성
    queue = deque()

    for _ in range(n):
        command_line = input().split()
        if not command_line: break
        
        cmd = command_line[0]

        if cmd == "in":
            number = int(command_line[1])
            queue.append(number) # 줄 서기
            
        elif cmd == "out":
            if queue:
                # 맨 앞사람 입장 (출력)
                print(queue.popleft())
            else:
                # 줄 선 사람이 없음
                print("-1")

if __name__ == "__main__":
    main()
