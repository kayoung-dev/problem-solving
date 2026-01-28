import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    meetings = []

    for _ in range(n):
        s, e = map(int, input().split())
        meetings.append((e, s))  # 종료 시각 기준 정렬

    meetings.sort()

    count = 0
    current_end = -1

    for e, s in meetings:
        if s >= current_end:
            count += 1
            current_end = e

    print(count)

if __name__ == "__main__":
    solve()
