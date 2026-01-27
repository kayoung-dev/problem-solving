import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    current_battery = int(input_data[1])
    charge_rate = int(input_data[2])
    
    # (쓰레기 번호, 필요 배터리)
    queue = deque()
    costs = list(map(int, input_data[3:]))
    for i in range(n):
        queue.append((i + 1, costs[i]))
        
    results = []
    
    while queue:
        idx, cost = queue.popleft()
        
        if current_battery >= cost:
            # 청소 가능
            current_battery -= cost
            results.append(str(idx))
        else:
            # 청소 불가: 뒤로 보내고 충전
            current_battery += charge_rate
            queue.append((idx, cost))
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
