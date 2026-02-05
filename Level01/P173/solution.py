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
    
    # n이 10^18일 때, k는 약 1,442,249 근처이므로 high를 2,000,000으로 설정
    low, high = 0, 2000000
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
        
        # 자연수 제곱의 합 공식: mid*(mid+1)*(2*mid+1) // 6
        total = mid * (mid + 1) * (2 * mid + 1) // 6
        
        if total <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
