import sys
import heapq

def solve():
    input = sys.stdin.readline
    N, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 인접 경계 비용: max(0, |a-b| - H)
    N2 = N * N
    flat = [v for row in grid for v in row]
    visited = [False] * N2
    pq = []

    def edge_cost(a, b):
        d = flat[a] - flat[b]
        if d < 0:
            d = -d
        d -= H
        return 0 if d <= 0 else d

    def push(frm, to):
        heapq.heappush(pq, (edge_cost(frm, to), to))

    visited[0] = True
    visited_cnt = 1

    if N > 1:
        push(0, 1)
        push(0, N)

    total = 0
    while visited_cnt < N2:
        c, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total += c
        visited_cnt += 1

        r, col = divmod(node, N)
        if r > 0:
            nb = node - N
            if not visited[nb]:
                push(node, nb)
        if r < N - 1:
            nb = node + N
            if not visited[nb]:
                push(node, nb)
        if col > 0:
            nb = node - 1
            if not visited[nb]:
                push(node, nb)
        if col < N - 1:
            nb = node + 1
            if not visited[nb]:
                push(node, nb)

    print(total)

if __name__ == "__main__":
    solve()
