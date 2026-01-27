import sys
import math
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    progresses = list(map(int, input_data[1:1+n]))
    speeds = list(map(int, input_data[1+n:1+2*n]))
    
    # 각 부품의 소요 시간 계산 (올림 처리)
    days = deque()
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
        
    results = []
    while days:
        # 현재 가장 앞 부품의 소요 시간을 기준(Standard)으로 설정
        standard = days.popleft()
        count = 1
        
        # 뒤에 있는 부품들 중 기준 시간보다 일찍 혹은 동시에 끝난 것들을 모두 포함
        while days and days[0] <= standard:
            days.popleft()
            count += 1
        results.append(str(count))
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
