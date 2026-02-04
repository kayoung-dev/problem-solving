import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    ids = list(map(int, data[2:]))

    low = 0
    high = n - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == k:
            found = True
            break
        elif ids[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    if found:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()
