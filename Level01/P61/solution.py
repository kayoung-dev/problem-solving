import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = int(input_data[1])
    a = list(map(int, input_data[2:]))
    
    queue = deque()
    for i in range(n):
        queue.append([i + 1, a[i]]) # [번호, 남은 양]
        
    results = []
    while queue:
        idx, remain = queue.popleft()
        remain -= s
        
        if remain <= 0:
            results.append(str(idx))
        else:
            queue.append([idx, remain])
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
