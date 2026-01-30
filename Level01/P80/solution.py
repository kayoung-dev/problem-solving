import sys
from collections import deque

input = sys.stdin.readline

def solve():
    line = input().split()
    if not line: return
    n, k = int(line[0]), int(line[1])
    
    energies = list(map(int, input().split()))
    dq = deque() # 히어로의 인덱스 저장
    
    for i in range(n):
        # 1. [왼쪽 문] 범위를 벗어난 인덱스 제거
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. [오른쪽 문] 현재보다 약한 이전 멤버들 제거 (단조성 유지)
        while dq and energies[dq[-1]] <= energies[i]:
            dq.pop()
            
        dq.append(i)
        
        # 3. 요새가 K명을 채운 시점부터 최강자 출력
        if i >= k - 1:
            print(energies[dq[0]], end=' ')
    print()

if __name__ == "__main__":
    solve()
