import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    noise_levels = list(map(int, input_data[2:]))
    
    # 데이터를 담아둘 목록 (큐 역할)
    history = deque()
    results = []
    
    for x in noise_levels:
        # 최근 기록이 K개 가득 찼다면 평균과 비교
        if len(history) == k:
            avg = sum(history) / k
            diff = x - avg
            results.append(f"{diff:.1f}")
            
        # 새로운 기록 추가 및 오래된 기록 삭제
        history.append(x)
        if len(history) > k:
            history.popleft()
            
    if results:
        print(" ".join(results))

if __name__ == "__main__":
    solve()
