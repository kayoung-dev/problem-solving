import sys

def solve():
    input = sys.stdin.readline

    n = int(input().strip())
    arr = list(map(int, input().split()))
    i, j, k = map(int, input().split())

    part = arr[i-1:j]
    part.sort(reverse=True)
    print(part[k-1])

if __name__ == "__main__":
    solve()
