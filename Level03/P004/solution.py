import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    tips = list(map(int, input_data[1:]))
    
    if n == 1:
        print(tips[0])
        return
    
    # dp[i]는 i번째 집까지 고려했을 때 얻을 수 있는 최대 팁입니다.
    dp = [0] * n
    
    # 초기값 설정
    dp[0] = tips[0]
    dp[1] = max(tips[0], tips[1])
    
    # 점화식: i번째 집을 선택하는 경우(dp[i-2] + 현재팁) vs 선택하지 않는 경우(dp[i-1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + tips[i])
        
    print(dp[n-1])

if __name__ == "__main__":
    solve()
