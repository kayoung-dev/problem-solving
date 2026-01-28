import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    posts = []
    for _ in range(n):
        pid, t, l, c = map(int, input().split())
        s = 2*l + 3*c
        posts.append((s, t, pid))

    # 정렬: s desc, t desc, id asc
    posts.sort(key=lambda x: (-x[0], -x[1], x[2]))

    top = posts[:k]
    print(" ".join(str(x[2]) for x in top))

if __name__ == "__main__":
    solve()
