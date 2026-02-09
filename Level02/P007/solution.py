import sys

def solve():
    # 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    energy = list(map(int, input_data[1:]))
    
    if n == 1:
        print(energy[0])
        return
    if n == 2:
        print(energy[1]) # 바로 2번 다리로 점프하는 것이 1번 거치는 것보다 항상 유리하거나 같음 (에너지는 양수이므로)
        # 하지만 문제 규칙상 '도착'이 목적이므로 시작점에서의 최소화를 고려합니다.
        print(min(energy[0] + energy[1], energy[1]))
        # 실제 로직에서는 아래 DP가 이를 처리합니다.
        return

    # dp[i]는 i번째 다리에 도달했을 때의 최소 에너지 합입니다.
    dp = [0] * n
    
    # 초기값 설정
    dp[0] = energy[0] # 첫 번째 다리로 시작
    dp[1] = energy[1] # 바로 두 번째 다리로 시작 (0번을 거치지 않음)
    
    # 3번째 다리(인덱스 2)부터 계산
    for i in range(2, n):
        # (바로 전 다리에서 왔을 때)와 (한 다리 건너뛰어 왔을 때) 중 최소 에너지를 선택
        dp[i] = min(dp[i-1], dp[i-2]) + energy[i]
        
    print(dp[n-1])

# 정확한 로직을 위해 n=2일 때의 처리를 포함한 코드를 다시 작성합니다.
def correct_solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    e = list(map(int, input_data[1:]))
    if n == 1:
        print(e[0])
        return
    dp = [0] * n
    dp[0] = e[0]
    dp[1] = e[1] # 시작할 때 1번 혹은 2번으로 바로 갈 수 있음
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + e[i]
    print(dp[n-1])

if __name__ == "__main__":
    correct_solve()
