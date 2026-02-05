import sys
from bisect import bisect_left

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    q = int(next(it))

    scores = [int(next(it)) for _ in range(n)]

    out = []
    for _ in range(q):
        k = int(next(it))
        idx = bisect_left(scores, k)
        out.append(str(idx if idx < n else -1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
