import sys
from collections import deque

def solve():
    # 데이터를 단어 단위로 하나씩 끊어서 가져오는 도구
    def get_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    tokens = get_tokens()
    
    try:
        # 1. N, R, K를 먼저 읽음
        n = int(next(tokens))
        r = int(next(tokens))
        k = int(next(tokens))
        
        # 2. 정확히 n개의 데이터만 읽음 (n개가 차면 즉시 루프 종료)
        stations = []
        for _ in range(n):
            stations.append(int(next(tokens)))
            
    except (StopIteration, ValueError):
        return

    # 3. 초기 신호 계산 (Sliding Window)
    current_power = [0] * n
    # 초기 0번 구역 윈도우 합
    ws = sum(stations[:r+1])
    for i in range(n):
        current_power[i] = ws
        if i + r + 1 < n: ws += stations[i + r + 1]
        if i - r >= 0: ws -= stations[i - r]

    # 4. 결정 함수 (Deque 활용)
    def check(target):
        dq = deque()
        added_sum = 0
        used_k = 0
        for i in range(n):
            while dq and dq[0][1] < i:
                added_sum -= dq.popleft()[0]
            actual = current_power[i] + added_sum
            if actual < target:
                diff = target - actual
                used_k += diff
                if used_k > k: return False
                added_sum += diff
                dq.append([diff, i + 2 * r])
        return used_k <= k

    # 5. 이진 탐색
    low, high = 0, sum(stations) + k
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(ans)

if __name__ == "__main__":
    solve()
