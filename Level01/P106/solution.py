import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    n = int(input().strip())

    # log_id -> (time, severity, word_counts)
    time_map = {}
    sev_map = {}
    word_cnt = defaultdict(lambda: defaultdict(int))
    inv = defaultdict(set)  # word -> set(log_id) (for fast candidate union)

    for _ in range(n):
        parts = input().split()
        log_id = int(parts[0])
        t = int(parts[1])
        sev = int(parts[2])
        c = int(parts[3])
        words = parts[4:4+c]

        time_map[log_id] = t
        sev_map[log_id] = sev
        for w in words:
            word_cnt[log_id][w] += 1
            inv[w].add(log_id)

    q = int(input().strip())
    query = input().split()[:q]
    k = int(input().strip())

    # 후보 로그 모으기 (역색인 활용)
    candidates = set()
    for w in query:
        candidates |= inv.get(w, set())

    if not candidates:
        print()
        return

    hit = {}
    freq = {}

    for log_id in candidates:
        h = 0
        f = 0
        wm = word_cnt[log_id]
        for w in query:
            c = wm.get(w, 0)
            if c > 0:
                h += 1
                f += c
        if h > 0:
            hit[log_id] = h
            freq[log_id] = f

    if not hit:
        print()
        return

    logs = list(hit.keys())
    logs.sort(key=lambda x: (-hit[x], -sev_map[x], -freq[x], -time_map[x], x))
    logs = logs[:k]
    print(" ".join(map(str, logs)))

if __name__ == "__main__":
    solve()
