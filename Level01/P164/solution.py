import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    scores = list(map(int, data[2:]))

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if scores[mid] == k:
            result = mid
            break
        # 내림차순이므로 중간값이 목표보다 작으면 왼쪽(더 큰 값들)을 탐색
        elif scores[mid] < k:
            high = mid - 1
        # 중간값이 목표보다 크면 오른쪽(더 작은 값들)을 탐색
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
