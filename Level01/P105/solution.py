import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    intervals = []

    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append((s, e))

    if not intervals:
        print(0)
        return

    # 시작 시점 기준 정렬
    intervals.sort()

    merged = []
    cur_s, cur_e = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_e:  # 겹치거나 이어지는 경우
            cur_e = max(cur_e, e)
        else:
            merged.append((cur_s, cur_e))
            cur_s, cur_e = s, e

    merged.append((cur_s, cur_e))

    print(len(merged))
    for s, e in merged:
        print(s, e)

if __name__ == "__main__":
    solve()
