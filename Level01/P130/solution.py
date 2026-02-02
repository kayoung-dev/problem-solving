import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k_limit = int(input_data[1])
    capacities = list(map(int, input_data[2:]))
    
    max_sum = 0
    
    # 2^n 가지의 모든 부분집합을 비트마스킹으로 탐색
    for i in range(1 << n):
        current_sum = 0
        for j in range(n):
            # i의 j번째 비트가 1이면 j번째 장치를 선택한 것으로 간주
            if (i & (1 << j)):
                current_sum += capacities[j]
        
        # 합계가 한계치 이하이고 현재 최댓값보다 크면 갱신
        if current_sum <= k_limit:
            if current_sum > max_sum:
                max_sum = current_sum
                
    print(max_sum)

if __name__ == "__main__":
    solve()
