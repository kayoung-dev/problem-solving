import sys
import heapq

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    tasks = []
    for _ in range(n):
        d, p = map(int, input().split())
        tasks.append((d, p))

    tasks.sort()  # deadline 오름차순

    heap = []  # 선택한 과제들의 점수(최소 힙)
    for d, p in tasks:
        heapq.heappush(heap, p)
        # d일까지는 최대 d개만 제출 가능
        if len(heap) > d:
            heapq.heappop(heap)

    print(sum(heap))

if __name__ == "__main__":
    solve()
