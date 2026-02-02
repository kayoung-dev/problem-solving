import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    limit = int(input_data[1])
    strengths = list(map(int, input_data[2:]))
    
    max_sum = 0
    
    # 3중 반복문을 이용해 서로 다른 3개의 지지대를 고르는 모든 조합을 확인
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_sum = strengths[i] + strengths[j] + strengths[k]
                
                # 제한치 이하이면서 현재까지 발견한 최대합보다 크면 갱신
                if current_sum <= limit:
                    if current_sum > max_sum:
                        max_sum = current_sum
                        
    print(max_sum)

if __name__ == "__main__":
    solve()
