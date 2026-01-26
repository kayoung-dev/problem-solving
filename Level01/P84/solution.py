import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))
    arr = arr[:n]

    arr.sort()
    sys.stdout.write(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
