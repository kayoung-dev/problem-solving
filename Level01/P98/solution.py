import sys
from collections import Counter

def solve():
    s = sys.stdin.readline().strip()

    # 중괄호 제거 및 집합 분리
    s = s[2:-2]
    parts = s.split("},{")

    counter = Counter()
    for part in parts:
        nums = map(int, part.split(","))
        for x in nums:
            counter[x] += 1

    # 등장 횟수 내림차순 정렬
    result = sorted(counter.items(), key=lambda x: -x[1])
    print(" ".join(str(x[0]) for x in result))

if __name__ == "__main__":
    solve()
