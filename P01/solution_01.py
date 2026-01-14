import sys
data = list(map(int, sys.stdin.read().split()))
if data:
    n, k = data[0], data[1]
    weights = data[2:2+n]
    res = [w for w in weights if w >= k]
    if not res:
        print("0 0")
    else:
        print(f"{len(res)} {sum(res)}")
