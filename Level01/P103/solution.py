import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline

    n = int(input().strip())
    doc_date = {}
    for _ in range(n):
        doc_id, ymd = map(int, input().split())
        doc_date[doc_id] = ymd

    w = int(input().strip())
    inv = defaultdict(list)
    for _ in range(w):
        parts = input().split()
        word = parts[0]
        k = int(parts[1])
        ids = list(map(int, parts[2:2+k]))
        inv[word] = ids

    q = int(input().strip())
    query_words = input().split()
    query_words = query_words[:q]

    match_count = defaultdict(int)
    for word in query_words:
        for doc_id in inv.get(word, []):
            match_count[doc_id] += 1

    # 결과가 없다면 빈 줄 출력
    if not match_count:
        print()
        return

    # 정렬: (일치 단어 수 desc, 작성일 desc, 문서ID asc)
    docs = list(match_count.keys())
    docs.sort(key=lambda d: (-match_count[d], -doc_date[d], d))

    print(" ".join(map(str, docs)))

if __name__ == "__main__":
    solve()
