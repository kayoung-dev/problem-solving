import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    line1 = deque(map(int, input_data[1:1+n]))
    line2 = deque(map(int, input_data[1+n:1+2*n]))
    
    sum1 = sum(line1)
    sum2 = sum(line2)
    total_sum = sum1 + sum2
    
    # 합이 홀수면 절대 같아질 수 없음
    if total_sum % 2 != 0:
        print(-1)
        return
    
    target = total_sum // 2
    moves = 0
    # 무한 루프 방지를 위한 최대 시도 횟수 설정
    limit = n * 4
    
    while moves <= limit:
        if sum1 == target:
            print(moves)
            return
        
        if sum1 > target:
            val = line1.popleft()
            sum1 -= val
            line2.append(val)
            sum2 += val
        else:
            val = line2.popleft()
            sum2 -= val
            line1.append(val)
            sum1 += val
        
        moves += 1
        
    print(-1)

if __name__ == "__main__":
    solve()
