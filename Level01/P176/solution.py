import sys

def can_split(weights, k, limit):
    # 주어진 limit 너비로 k개 이내의 칸에 담을 수 있는지 확인 (Greedy)
    count = 1
    current_sum = 0
    for w in weights:
        if current_sum + w > limit:
            count += 1
            current_sum = w
        else:
            current_sum += w
    return count <= k

def solve():
    # 대량의 데이터를 위해 sys.stdin.read() 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    weights = list(map(int, input_data[2:]))
    
    # 이진 탐색 범위 설정
    # low: 가장 두꺼운 책 한 권은 무조건 담아야 하므로 max(weights)
    # high: 모든 책을 한 칸에 다 담는 경우인 sum(weights)
    low = max(weights)
    high = sum(weights)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_split(weights, k, mid):
            ans = mid
            high = mid - 1 # 더 작은 너비가 가능한지 확인
        else:
            low = mid + 1 # 너비를 키워야 함
            
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
