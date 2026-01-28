import sys

def time_to_min(t: str) -> int:
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    records = []

    for _ in range(n):
        emp, t = input().split()
        emp = int(emp)
        records.append((time_to_min(t), emp, t))

    records.sort()  # (time, emp)

    for _, emp, t in records:
        print(emp, t)

if __name__ == "__main__":
    solve()
