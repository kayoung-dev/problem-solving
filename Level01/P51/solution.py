import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1])
    temps = list(map(int, input_data[2:]))
    
    # 최근 기록을 담을 공간 (최대 K개)
    records = deque()
    current_sum = 0
    results = []
    
    for t in temps:
        # 기록장이 가득 찼다면 가장 오래된 데이터 제거
        if len(records) == k:
            oldest = records.popleft()
            current_sum -= oldest
            
        # 새로운 기온 추가
        records.append(t)
        current_sum += t
        
        # 현재 기록된 개수만큼 나누어 평균 계산
        avg = current_sum / len(records)
        results.append(f"{avg:.1f}")
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
