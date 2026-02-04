import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    prices = list(map(int, input_data[2:]))

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        # Upper Bound: Target보다 큰 값이 처음 나오는 위치
        if prices[mid] > k:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
