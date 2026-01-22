import sys
from collections import deque

def solution():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    queue = deque()
    results = []

    for i in range(1, n + 1):
        command = input_data[i].split()
        cmd_type = command[0]
        
        if cmd_type == "enqueue":
            queue.append(command[1])
        elif cmd_type == "dequeue":
            if queue:
                results.append(queue.popleft())
            else:
                results.append("-1")
        elif cmd_type == "size":
            results.append(str(len(queue)))
        elif cmd_type == "empty":
            results.append("1" if not queue else "0")
        elif cmd_type == "front":
            if queue:
                results.append(queue[0])
            else:
                results.append("-1")
                
    if results:
        sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solution()
