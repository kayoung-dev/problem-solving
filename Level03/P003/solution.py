import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        n = int(line.strip())
        
        # 가로 길이가 1이면 세로 타일 1개만 놓을 수 있습니다.
        if n == 1:
            print(1)
            return
        
        # n이 2일 때까지 초기값을 설정합니다.
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # n이 3 이상일 때부터 점화식을 적용합니다.
        # 가로 i를 채우는 방법은:
        # 1. (i-1)까지 채우고 세로 타일 1개를 붙이는 경우
        # 2. (i-2)까지 채우고 가로 타일 2개를 눕혀서 붙이는 경우
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        print(dp[n])
        
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
