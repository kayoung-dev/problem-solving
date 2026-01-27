import sys
from functools import cmp_to_key

def cmp(a: str, b: str) -> int:
    if a + b < b + a:
        return -1
    if a + b > b + a:
        return 1
    return 0

def is_all_zero_tokens(tokens):
    # 모든 토큰이 '0'만으로 구성되면 True
    for t in tokens:
        if any(ch != '0' for ch in t):
            return False
    return True

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    tokens = input().split()
    tokens = tokens[:n]

    tokens.sort(key=cmp_to_key(cmp))
    if is_all_zero_tokens(tokens):
        print("0")
    else:
        print("".join(tokens))

if __name__ == "__main__":
    solve()
