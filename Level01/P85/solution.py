import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    total = 0
    for i in range(n):
        total += abs(a[i] - b[i])

    print(total)

if __name__ == "__main__":
    solve()
