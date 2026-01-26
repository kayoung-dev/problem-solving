import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    students = []
    for _ in range(n):
        line = input().split()
        if not line:
            continue
        sid = int(line[0])
        score = int(line[1])
        students.append((score, sid))

    # 점수 오름차순, 점수 같으면 학번 오름차순
    students.sort()

    out_lines = []
    for score, sid in students:
        out_lines.append(f"{sid} {score}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
