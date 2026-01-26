import sys

def solve():
    input = sys.stdin.readline
    first = input().split()
    if not first:
        return
    n = int(first[0])
    k = int(first[1])
    arr = list(map(int, input().split()))
    arr = arr[:n]

    arr.sort(reverse=True)
    sys.stdout.write(str(arr[k - 1]))

if __name__ == "__main__":
    solve()
