import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # 센서 번호를 담은 양방향 큐(Deque) 생성
    sensors = deque(range(1, n + 1))
    results = []
    is_clockwise = True # 시계 방향 플래그
    
    while sensors:
        if is_clockwise:
            # 시계 방향 회전 (앞에서 빼서 뒤로 보냄)
            for _ in range(k - 1):
                sensors.append(sensors.popleft())
            results.append(str(sensors.popleft()))
        else:
            # 반대 방향 회전 (뒤에서 빼서 앞으로 보냄)
            for _ in range(k - 1):
                sensors.appendleft(sensors.pop())
            results.append(str(sensors.pop()))
            
        # 전선 꼬임 방지를 위해 방향 전환
        is_clockwise = not is_clockwise
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
