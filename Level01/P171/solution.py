import sys

# ---------------------------------------------------------
# 4. 정답 코드 (solution.py) 
# ---------------------------------------------------------
def solve():
    # sys.stdin.readline()을 사용해 한 줄이 들어오는 즉시 처리합니다.
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    try:
        n = int(line)
    except ValueError:
        return
    
    # 이진 탐색 로직
    low, high = 0, 10**9
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
            
        # S = k(3k - 1) // 2
        total = mid * (3 * mid - 1) // 2
        
        if total <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    # 결과를 출력하고 즉시 종료합니다.
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
