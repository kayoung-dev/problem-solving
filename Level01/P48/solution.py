import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, m = int(input_data[0]), int(input_data[1])
    targets = list(map(int, input_data[2:]))
    
    # 데크(Deque)로 석판 시뮬레이션
    dq = deque(range(1, n + 1))
    ans = 0
    
    for t in targets:
        idx = dq.index(t)
        
        # 왼쪽으로 돌리는게 빠른지, 오른쪽이 빠른지 판단
        if idx <= len(dq) // 2:
            # 왼쪽 회전
            dq.rotate(-idx)
            ans += idx
        else:
            # 오른쪽 회전
            move_right = len(dq) - idx
            dq.rotate(move_right)
            ans += move_right
            
        # 입구에 온 칸을 열어 제거
        dq.popleft()
        
    print(ans)

if __name__ == "__main__":
    solve()
