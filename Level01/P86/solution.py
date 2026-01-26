import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))[:n]

    arr.sort()

    out = []
    i = 0
    while i < n:
        v = arr[i]
        j = i
        while j < n and arr[j] == v:
            j += 1
        out.append(f"{v} {j - i}")
        i = j

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
