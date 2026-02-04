import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    temps = list(map(int, data[2:]))

    low = 0
    high = n - 1
    
    # 이진 탐색으로 k의 위치 탐색
    while low <= high:
        mid = (low + high) // 2
        if temps[mid] == k:
            print(temps[mid])
            return
        elif temps[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    # 반복문 종료 후 high < k < low 상태임
    if low >= n:
        print(temps[n-1])
    elif high < 0:
        print(temps[0])
    else:
        # 양옆 값 중 더 가까운 것 선택 (차이가 같으면 더 작은 값인 high 선택)
        if abs(temps[high] - k) <= abs(temps[low] - k):
            print(temps[high])
        else:
            print(temps[low])

if __name__ == "__main__":
    solve()
