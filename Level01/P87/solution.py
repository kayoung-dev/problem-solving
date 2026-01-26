import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    intervals = []
    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append((e, s))  # (end, start)

    intervals.sort()  # end 오름차순, end 같으면 start 오름차순

    keep = 0
    last_end = -10**18
    for end, start in intervals:
        if start >= last_end:
            keep += 1
            last_end = end

    print(n - keep)

if __name__ == "__main__":
    solve()
