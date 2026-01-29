import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    # 1. 데이터 읽기
    line = input().split()
    if not line: return
    n, k = int(line[0]), int(line[1])
    scores = list(map(int, input().split()))
    
    # dp[i]: i번째 시점을 마지막으로 방문했을 때의 최대 승리 기여도
    dp = [0] * n
    # 단조 감소 큐: 윈도우 내의 dp 최댓값을 O(1)에 찾기 위해 사용
    dq = deque()
    
    for i in range(n):
        # 윈도우 범위를 벗어난(거리가 K 초과) 인덱스 제거
        if dq and dq[0] < i - k:
            dq.popleft()
            
        # 이전 최적값 중 양수인 것만 가져와 현재 점수에 더함
        # 큐의 맨 앞에는 항상 현재 범위 내 최대 dp 인덱스가 있음
        prev_best = dp[dq[0]] if dq else 0
        dp[i] = scores[i] + max(0, prev_best)
        
        # 현재 dp[i]보다 작은 이전 값들은 필요 없으므로 제거 (단조성 유지)
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        dq.append(i)
        
    # 결과 출력: 모든 시점 중 도달 가능한 최대 점수
    print(max(dp))

if __name__ == "__main__":
    solve()
