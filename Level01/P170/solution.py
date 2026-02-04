import sys

def solve():
    # 대량 데이터 처리를 위한 최적화된 입력 읽기
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, m, k = map(int, input_data[:3])
    red_gems = list(map(int, input_data[3:3+n]))
    blue_gems = list(map(int, input_data[3+n:3+n+m]))

    # 탐색 대상인 푸른 보석 리스트 정렬
    blue_gems.sort()
    
    for red in red_gems:
        # 타겟 방정식: y = 2x + k
        target = (red * 2) + k
        
        # 이진 탐색으로 유일한 해 찾기
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if blue_gems[mid] == target:
                print(f"{red} {target}")
                return
            elif blue_gems[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    solve()
