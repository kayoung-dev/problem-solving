import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        n = int(line.strip())
        
        if n == 1:
            print(1)
            return
        if n == 2:
            print(2)
            return
            
        # 정보를 기록할 바구니(DP 테이블)를 준비합니다.
        # 각 칸에는 해당 계단까지 도달하는 방법의 수를 저장합니다.
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # 3번째 계단부터 N번째 계단까지 순서대로 계산합니다.
        # i번째 계단에 도달하는 방법 = (i-1번째에서 온 경우) + (i-2번째에서 온 경우)
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        print(dp[n])
        
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
