import sys

def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    res = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    res = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:]))
    
    # O(log N) 방식으로 개수 계산
    count = upper_bound(arr, k) - lower_bound(arr, k)
    print(count)

if __name__ == "__main__":
    solve()
