import sys

def solve():
    # 입력 받기
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, k = map(int, line1)
        
        nums = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    # 이진 탐색 로직 (O(log N))
    low = 0
    high = n - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            answer = mid
            break
        elif nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    print(answer)

if __name__ == "__main__":
    solve()
