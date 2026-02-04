import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    scores = list(map(int, input_data[2:]))

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if scores[mid] >= k:
            result = mid  # 일단 후보로 저장
            high = mid - 1  # 더 앞쪽(왼쪽)에 조건 만족하는 값이 있는지 확인
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
