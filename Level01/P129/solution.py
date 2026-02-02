import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    times = list(map(int, input_data[1:]))
    
    min_total_wait = float('inf')
    
    # 모든 가능한 작업 순서(순열)를 생성하여 전수 조사 (O(N! * N))
    for p in permutations(times):
        current_total_wait = 0
        current_time = 0
        # 선택된 순서대로 대기 시간 계산
        for t in p:
            current_time += t
            current_total_wait += current_time
        
        # 최솟값 갱신
        if current_total_wait < min_total_wait:
            min_total_wait = current_total_wait
            
    print(min_total_wait)

if __name__ == "__main__":
    solve()
