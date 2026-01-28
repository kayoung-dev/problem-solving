import sys
import re

def split_file(name: str):
    # 이름(알파벳)+번호(숫자) 형태를 가정
    m = re.match(r"([a-zA-Z]+)(\d+)$", name)
    head = m.group(1).lower()
    num = int(m.group(2))
    return head, num

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    files = [input().strip() for _ in range(n)]

    files.sort(key=split_file)

    for f in files:
        print(f)

if __name__ == "__main__":
    solve()
