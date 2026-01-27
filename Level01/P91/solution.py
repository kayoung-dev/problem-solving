import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return
    digits = list(s)
    digits.sort(reverse=True)
    print("".join(digits))

if __name__ == "__main__":
    solve()
