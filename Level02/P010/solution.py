import sys

def solve():
    # 입력을 읽어 정수로 변환합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 결과를 저장할 리스트를 생성합니다.
    # dp[i]는 숫자 i를 분해할 때 필요한 항의 개수입니다.
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # 수학적 귀납법에 따른 점화식:
        # i를 2로 나눈 몫의 결과에 i를 2로 나눈 나머지를 더합니다.
        dp[i] = dp[i // 2] + (i % 2)
        
    # 리스트의 요소들을 공백으로 구분하여 출력합니다.
    print(*(dp))

if __name__ == "__main__":
    solve()
