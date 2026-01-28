import sys

def digit_sum(x: int) -> int:
    x = abs(x)
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))[:n]

    arr.sort(key=lambda v: (digit_sum(v), v))
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
