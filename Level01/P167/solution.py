import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    records = data[1:]

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        # 불량품(1)을 찾으면 일단 결과에 저장하고 더 앞쪽을 탐색
        if records[mid] == '1':
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
