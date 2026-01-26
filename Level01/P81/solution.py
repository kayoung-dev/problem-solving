import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    arr = list(map(int, input().split()))
    # 혹시 n과 길이가 다를 수 있으니 안전하게 처리 (코테 환경에서 가끔 발생)
    arr = arr[:n]

    cnt0 = cnt1 = cnt2 = 0
    for x in arr:
        if x == 0:
            cnt0 += 1
        elif x == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    out = ([0] * cnt0) + ([1] * cnt1) + ([2] * cnt2)
    sys.stdout.write(" ".join(map(str, out)))

if __name__ == "__main__":
    solve()
