import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))[:n]

    arr.sort(key=lambda x: (x % 2, -x if x % 2 == 0 else x))
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
