import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 1행의 데이터로 초기값을 설정합니다.
    # dp_a, dp_b, dp_c는 각각 현재 행에서 1열, 2열, 3열을 선택했을 때의 최대 누적합입니다.
    dp_a = int(input_data[1])
    dp_b = int(input_data[2])
    dp_c = int(input_data[3])
    
    idx = 4
    for i in range(1, n):
        # 현재 행의 각 열 값을 읽어옵니다.
        cur_a = int(input_data[idx])
        cur_b = int(input_data[idx+1])
        cur_c = int(input_data[idx+2])
        idx += 3
        
        # 이전 행에서 다른 열을 선택했던 값들 중 큰 값을 더해 현재의 최댓값을 갱신합니다.
        next_a = cur_a + max(dp_b, dp_c)
        next_b = cur_b + max(dp_a, dp_c)
        next_c = cur_c + max(dp_a, dp_b)
        
        dp_a, dp_b, dp_c = next_a, next_b, next_c
        
    # 마지막 행까지 계산된 세 가지 상태 중 최댓값을 출력합니다.
    print(max(dp_a, dp_b, dp_c))

if __name__ == "__main__":
    solve()
