import sys

class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    edges.sort(key=lambda x: (x[2], min(x[0], x[1]), max(x[0], x[1])))

    dsu = DSU(N)
    total = 0
    chosen = []

    for u, v, w in edges:
        if dsu.union(u, v):
            total += w
            a, b = (u, v) if u < v else (v, u)
            chosen.append((a, b))
            if len(chosen) == N - 1:
                break

    if len(chosen) != N - 1:
        print(-1)
        return

    chosen.sort()
    print(total)
    for a, b in chosen:
        print(a, b)

if __name__ == "__main__":
    solve()
