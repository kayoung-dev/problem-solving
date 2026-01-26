import sys
import math
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    progresses = list(map(int, input_data[1:1+n]))
    speeds = list(map(int, input_data[1+n:1+2*n]))
    
    finish_times = deque()
    for p, s in zip(progresses, speeds):
        finish_times.append(math.ceil((100 - p) / s))
        
    results = []
    while finish_times:
        standard_time = finish_times.popleft()
        count = 1
        
        while finish_times and finish_times[0] <= standard_time:
            finish_times.popleft()
            count += 1
            
        results.append(str(count))
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
