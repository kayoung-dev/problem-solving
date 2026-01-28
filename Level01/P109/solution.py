import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    arr1 = list(map(int, input().split()))
    m = int(input().strip())
    arr2 = list(map(int, input().split()))

    b = sorted(set(arr2))
    INF = 10**15

    dp = {-(10**18): 0}

    for a in arr1:
        ndp = {}

        for prev, cost in dp.items():
            # 1) 그대로 사용
            if a > prev:
                old = ndp.get(a, INF)
                if cost < old:
                    ndp[a] = cost

            # 2) 수정해서 후보 점수로 교체 (수정 후 점수는 낮아지면 안 됨)
            need = max(a, prev + 1)
            k = bisect_left(b, need)
            if k < len(b):
                x = b[k]
                old = ndp.get(x, INF)
                if cost + 1 < old:
                    ndp[x] = cost + 1

        if not ndp:
            print(-1)
            return

        # 지배 상태 제거
        items = sorted(ndp.items())
        pruned = {}
        best = INF
        for v, c in items:
            if c < best:
                pruned[v] = c
                best = c
        dp = pruned

    print(min(dp.values()))

if __name__ == "__main__":
    solve()
