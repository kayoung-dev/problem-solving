import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    m = int(input_data[1])
    priorities = list(map(int, input_data[2:]))
    
    # (긴급도, 초기위치) 형태로 큐에 삽입
    q = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0
    
    while q:
        current = q.popleft()
        # 현재 큐에 나보다 더 긴급한 게 있는지 확인
        if any(current[0] < item[0] for item in q):
            q.append(current) # 뒤로 보냄
        else:
            order += 1 # 배송 완료
            if current[1] == m:
                print(order)
                return

if __name__ == "__main__":
    solve()
