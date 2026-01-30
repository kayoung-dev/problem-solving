import sys
import heapq

def solve():
    input = sys.stdin.readline
    R, C, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    N = R * C
    flat = [v for row in grid for v in row]
    visited = [False] * N
    pq = []

    def edge_cost(a, b):
        d = flat[a] - flat[b]
        if d < 0:
            d = -d
        return 0 if d <= H else 1

    def push(frm, to):
        heapq.heappush(pq, (edge_cost(frm, to), to))

    visited[0] = True
    visited_cnt = 1

    if C > 1:
        push(0, 1)
    if R > 1:
        push(0, C)

    total = 0
    while visited_cnt < N:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = True
        total += cost
        visited_cnt += 1

        r, c = divmod(node, C)
        if r > 0:
            nb = node - C
            if not visited[nb]:
                push(node, nb)
        if r < R - 1:
            nb = node + C
            if not visited[nb]:
                push(node, nb)
        if c > 0:
            nb = node - 1
            if not visited[nb]:
                push(node, nb)
        if c < C - 1:
            nb = node + 1
            if not visited[nb]:
                push(node, nb)

    print(total)

if __name__ == "__main__":
    solve()
