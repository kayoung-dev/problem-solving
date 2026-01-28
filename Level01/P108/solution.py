import sys

def solve():
    input = sys.stdin.readline
    L, N = map(int, input().split())
    people = []
    for _ in range(N):
        p, v = map(int, input().split())
        people.append((p, v))

    # 끝 지점에 가까운 순(위치 내림차순) 정렬
    people.sort(key=lambda x: x[0], reverse=True)

    groups = 0
    max_time = -1.0

    for p, v in people:
        t = (L - p) / v
        # 뒤 사람이 도착 시간이 더 늦으면(큰 값이면) 앞 그룹을 따라잡지 못해 새 그룹
        if t > max_time:
            groups += 1
            max_time = t
        # t <= max_time 이면 앞 그룹을 따라잡아 합쳐짐

    print(groups)

if __name__ == "__main__":
    solve()
