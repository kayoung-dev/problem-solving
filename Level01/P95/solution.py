import sys
from functools import cmp_to_key

def cmp(a: str, b: str) -> int:
    # a가 앞에 오는 것이 더 큰 수를 만들면 -1 (내림차순 정렬)
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    nums = list(map(int, input().split()))[:n]

    strs = list(map(str, nums))
    strs.sort(key=cmp_to_key(cmp))

    # all zero 처리
    if strs and strs[0] == "0":
        print("0")
    else:
        print("".join(strs))

if __name__ == "__main__":
    solve()
