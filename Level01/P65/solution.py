import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1]) # 허용 주름
    d = int(input_data[2]) # 펴지는 정도
    
    # (지폐 번호, 주름 정도)
    queue = deque()
    wrinkles = list(map(int, input_data[3:]))
    for i in range(n):
        queue.append((i + 1, wrinkles[i]))
        
    results = []
    
    while queue:
        idx, current_wrinkle = queue.popleft()
        
        if current_wrinkle <= k:
            # 수락
            results.append(str(idx))
        else:
            # 거절 -> 주름 펴서 뒤로
            new_wrinkle = max(0, current_wrinkle - d)
            queue.append((idx, new_wrinkle))
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()
