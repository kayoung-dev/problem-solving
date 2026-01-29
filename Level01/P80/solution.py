import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 1. N, K 읽기
    line = input().split()
    if not line: return
    n, k = int(line[0]), int(line[1])
    
    # dq: (y - x, x) 쌍을 저장하며 y-x 기준 내림차순 유지
    dq = deque()
    max_synergy = -float('inf')
    
    # 2. 히어로 정보 순차 처리
    for _ in range(n):
        xj, yj = map(int, input().split())
        
        # [A] 거리 제한을 벗어난 파트너 제거 (x_j - x_i > k)
        while dq and xj - dq[0][1] > k:
            dq.popleft()
            
        # [B] 최적의 파트너와 시너지 계산
        if dq:
            max_synergy = max(max_synergy, dq[0][0] + yj + xj)
            
        # [C] 자신의 잠재력(y-x)을 큐에 추가 (단조성 유지)
        current_potential = yj - xj
        while dq and current_potential >= dq[-1][0]:
            dq.pop()
        dq.append((current_potential, xj))
        
    # 3. 결과 출력
    print(max_synergy)

if __name__ == "__main__":
    solve()
