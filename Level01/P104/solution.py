import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline

    n = int(input().strip())
    doc_date = {}
    for _ in range(n):
        doc_id, ymd = map(int, input().split())
        doc_date[doc_id] = ymd

    m = int(input().strip())
    # word -> list of doc_id occurrences (duplicates allowed)
    inv = defaultdict(list)
    # doc -> word -> count (for hit & freq calc)
    doc_word_cnt = defaultdict(lambda: defaultdict(int))

    for _ in range(m):
        doc_id_s, word = input().split()
        doc_id = int(doc_id_s)
        inv[word].append(doc_id)
        doc_word_cnt[doc_id][word] += 1

    q = int(input().strip())
    query = input().split()[:q]
    k = int(input().strip())

    hit = defaultdict(int)
    freq = defaultdict(int)

    for doc_id, wm in doc_word_cnt.items():
        h = 0
        f = 0
        for w in query:
            c = wm.get(w, 0)
            if c > 0:
                h += 1
                f += c
        if h > 0:
            hit[doc_id] = h
            freq[doc_id] = f

    if not hit:
        print()
        return

    docs = list(hit.keys())
    docs.sort(key=lambda d: (-hit[d], -freq[d], -doc_date[d], d))
    docs = docs[:k]
    print(" ".join(map(str, docs)))

if __name__ == "__main__":
    solve()
