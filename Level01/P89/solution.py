import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    prices = list(map(int, input().split()))[:n]
    coupons = list(map(int, input().split()))[:n]

    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    total = 0
    for p, c in zip(prices, coupons):
        v = p - c
        if v > 0:
            total += v
    print(total)

if __name__ == "__main__":
    solve()
