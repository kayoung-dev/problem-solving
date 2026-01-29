import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    # 1. N 읽기
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    
    # 2. 덤벨 무게 데이터 읽기 (여러 줄에 걸쳐 있을 수 있음)
    nums = []
    while len(nums) < n:
        line = input().strip()
        if not line:
            break
        nums.extend(map(int, line.split()))
    
    # 3. 누적 합(Prefix Sum) 계산
    s = [0] * (n + 1)
    for i in range(n):
        s[i+1] = s[i] + nums[i]
        
    # dp[i]: i번째 덤벨까지 사용했을 때의 최대 세트 수
    # last_sum[i]: i번째 덤벨까지 사용하여 만든 마지막 세트의 무게 합
    dp = [0] * (n + 1)
    last_sum = [0] * (n + 1)
    
    # 단조 대기열(Monotonic Deque)을 이용한 최적화
    dq = deque([0])
    
    for i in range(1, n + 1):
        # s[i] >= s[j] + last_sum[j] 를 만족하는 가장 큰 j 찾기
        while len(dq) >= 2 and s[i] >= s[dq[1]] + last_sum[dq[1]]:
            dq.popleft()
            
        best_j = dq[0]
        dp[i] = dp[best_j] + 1
        last_sum[i] = s[i] - s[best_j]
        
        # 새로운 후보 i 추가 (s[i] + last_sum[i]가 작을수록 유리)
        while dq and s[i] + last_sum[i] <= s[dq[-1]] + last_sum[dq[-1]]:
            dq.pop()
        dq.append(i)
        
    print(dp[n])

if __name__ == "__main__":
    solve()
