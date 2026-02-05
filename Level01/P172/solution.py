import sys

def solve():
    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return
    
    try:
        n = int(line)
    except ValueError:
        return
    
    # 이진 탐색 로직 (세제곱근 탐색)
    low, high = 0, 10**6
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
            
        if mid * mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
