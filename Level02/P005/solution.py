import sys

def solve():
    # 표준 입력을 통해 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 거실 지도를 구성합니다.
    grid = []
    idx = 2
    for r in range(n):
        grid.append(list(map(int, input_data[idx:idx+m])))
        idx += m
        
    # 각 지점까지의 최소 먼지 합을 저장할 기록지(DP 테이블)
    dp = [[0] * m for _ in range(n)]
    
    # 시작 지점 설정
    dp[0][0] = grid[0][0]
    
    # 가장 윗줄은 왼쪽에서 오는 방법밖에 없습니다.
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        
    # 가장 왼쪽줄은 위쪽에서 오는 방법밖에 없습니다.
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        
    # 나머지 칸들을 순차적으로 채워 나갑니다.
    # 현재 칸까지의 최소 먼지 = 현재 칸의 먼지 + min(위에서 올 때의 최소합, 왼쪽에서 올 때의 최소합)
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            
    # 목적지인 오른쪽 아래 칸의 결과를 출력합니다.
    print(dp[n-1][m-1])

if __name__ == "__main__":
    solve()
