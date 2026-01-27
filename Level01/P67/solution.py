import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k_values = list(map(int, input_data[1:]))
    
    # (풍선 번호, 쪽지 숫자)를 덱에 저장
    dq = deque()
    for i in range(n):
        dq.append((i + 1, k_values[i]))
        
    results = []
    
    while dq:
        # 1. 현재 풍선을 터트림
        idx, jump = dq.popleft()
        results.append(str(idx))
        
        # 풍선이 더 이상 없으면 종료
        if not dq:
            break
            
        # 2. 다음 풍선을 찾기 위해 회전
        # popleft()로 인해 이미 한 칸이 시계 방향으로 당겨진 상태임
        # 따라서 (jump - 1)번 만큼 시계 방향(왼쪽)으로 회전시키면 
        # 다음 터질 풍선이 맨 앞으로 오게 됨
        dq.rotate(-(jump - 1))
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
