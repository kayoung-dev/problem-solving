import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    people = []
    for _ in range(n):
        name, t, reg = input().split()
        t = int(t)
        reg = int(reg)
        people.append((t, reg, name))

    people.sort()  # (time asc, reg asc, name) - name은 동률 깨기용(문제에 영향 없음)
    for _, __, name in people:
        print(name)

if __name__ == "__main__":
    solve()
