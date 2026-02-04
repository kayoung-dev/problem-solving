import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    nums = list(map(int, data[2:]))

    low = 0
    high = n - 1
    
    # 이진 탐색으로 삽입 위치(Lower Bound와 유사) 찾기
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            print(mid)
            return
        elif nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    
    # 탐색 실패 시 low 값이 삽입될 위치가 됨
    print(low)

if __name__ == "__main__":
    solve()
