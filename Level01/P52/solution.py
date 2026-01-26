import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    l = int(input_data[0])
    w = int(input_data[1])
    n = int(input_data[2])
    packages = deque(map(int, input_data[3:]))
    
    # 무빙워크의 각 칸을 0으로 초기화
    moving_walk = deque([0] * l)
    current_weight = 0
    time = 0
    
    while moving_walk:
        time += 1
        # 맨 끝 칸에서 밖으로 나가는 짐 처리
        out = moving_walk.popleft()
        current_weight -= out
        
        if packages:
            # 새로운 짐이 들어올 수 있는지 하중 체크
            if current_weight + packages[0] <= w:
                p = packages.popleft()
                moving_walk.append(p)
                current_weight += p
            else:
                # 못 들어오면 빈 공간(0)을 채워 넣음
                moving_walk.append(0)
                
    print(time)

if __name__ == "__main__":
    solve()
