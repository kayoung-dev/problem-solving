import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    meetings = []

    for _ in range(n):
        mid, s, e, p = map(int, input().split())
        meetings.append((mid, s, e, p))

    # 시작 시각 기준 정렬
    meetings.sort(key=lambda x: x[1])

    selected = []

    for m in meetings:
        if not selected:
            selected.append(m)
            continue

        last = selected[-1]
        # 겹치지 않으면 그대로 추가
        if m[1] >= last[2]:
            selected.append(m)
        else:
            # 겹치면 우선순위 비교
            _, s1, e1, p1 = last
            _, s2, e2, p2 = m

            dur1 = e1 - s1
            dur2 = e2 - s2

            replace = False
            if p2 > p1:
                replace = True
            elif p2 == p1:
                if dur2 < dur1:
                    replace = True
                elif dur2 == dur1:
                    if m[0] < last[0]:
                        replace = True

            if replace:
                selected[-1] = m

    # 출력은 시작 시각 기준
    selected.sort(key=lambda x: x[1])

    print(len(selected))
    for m in selected:
        print(*m)

if __name__ == "__main__":
    solve()
