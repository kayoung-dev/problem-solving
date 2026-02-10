import sys

def solve():
    # 대량의 데이터를 효율적으로 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    profits = list(map(int, input_data[1:]))
    
    # dp[i]는 i번째 날을 반드시 포함했을 때 얻을 수 있는 연속된 구간의 최대 합입니다.
    # 공간을 절약하기 위해 배열 대신 변수 하나만 사용할 수도 있습니다.
    current_max = profits[0]
    total_max = profits[0]
    
    for i in range(1, n):
        # "이전까지의 최대합에 나를 더하는 것"과 "오늘 새로 시작하는 것" 중 더 큰 것을 선택합니다.
        current_max = max(profits[i], current_max + profits[i])
        
        # 지금까지 발견한 전체 최댓값을 갱신합니다.
        if current_max > total_max:
            total_max = current_max
            
    print(total_max)

if __name__ == "__main__":
    solve()
