import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, k = int(input_data[0]), int(input_data[1])
    
    # 1번부터 N번까지 유령들을 큐에 삽입
    q = deque(range(1, n + 1))
    result = []
    
    while q:
        # K-1번만큼 앞에서 빼서 뒤로 보냄 (회전)
        for _ in range(k - 1):
            q.append(q.popleft())
        
        # K번째 유령을 확정적으로 제거
        result.append(str(q.popleft()))
    
    # 순열 출력
    print(" ".join(result))

if __name__ == "__main__":
    solve()
