import sys

def solve():
    # 데이터를 효율적으로 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))
    
    # dp[i]는 a[i]를 마지막 원소로 포함하는 최장 증가 부분 수열의 길이입니다.
    # 모든 원소는 그 자체로 길이가 1인 부분 수열이 될 수 있으므로 1로 초기화합니다.
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            # 현재 숫자(a[i])가 이전 숫자(a[j])보다 크다면,
            # j번째에서 끝나는 부분 수열 뒤에 a[i]를 붙일 수 있습니다.
            if a[j] < a[i]:
                # 여러 가능한 j 중에서 가장 긴 길이에 1을 더한 값을 선택합니다.
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 전체 기록된 값 중 가장 큰 값을 출력합니다.
    print(max(dp))

if __name__ == "__main__":
    solve()
