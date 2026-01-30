import sys

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, size, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    parent = list(range(N + 1))
    size = [1] * (N + 1)

    out = []
    for _ in range(Q):
        t, a, b = input().split()
        a = int(a); b = int(b)
        if t == 'U':
            union(parent, size, a, b)
        else:  # 'Q'
            out.append("YES" if find(parent, a) == find(parent, b) else "NO")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))

if __name__ == "__main__":
    main()
