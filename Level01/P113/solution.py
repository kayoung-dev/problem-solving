import sys

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

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
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    dsu = DSU(N)
    for _ in range(M):
        a, b = map(int, input().split())
        dsu.union(a - 1, b - 1)

    edges = []
    for i in range(N):
        xi, yi = pts[i]
        for j in range(i + 1, N):
            xj, yj = pts[j]
            w = abs(xi - xj) + abs(yi - yj)
            edges.append((w, i, j))

    edges.sort()
    total = 0
    for w, i, j in edges:
        if dsu.union(i, j):
            total += w

    print(total)

if __name__ == "__main__":
    solve()
