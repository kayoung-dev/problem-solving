import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1])
    packets = list(map(int, input_data[2:2+n]))
    
    queue = deque()
    current_sum = 0
    results = []
    
    for p in packets:
        # 1. 새로운 데이터를 큐에 추가하고 합계 갱신
        queue.append(p)
        current_sum += p
        
        # 2. 큐의 크기가 K를 초과하면 가장 오래된 데이터 제거
        if len(queue) > k:
            oldest = queue.popleft()
            current_sum -= oldest
            
        # 3. 데이터가 K개 모인 시점부터 평균 계산
        if len(queue) == k:
            results.append(str(current_sum // k))
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
