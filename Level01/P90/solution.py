import sys
from collections import deque

def can(k, tasks, workers, pills, strength):
    if k == 0:
        return True

    # 쉬운 작업 k개, 강한 드론 k명만 고려
    t = tasks[:k]                  # 오름차순
    w = workers[len(workers)-k:]   # 오름차순 (강한 k명)

    dq = deque()  # 후보 드론 출력들을 오름차순으로 유지
    j = k - 1     # w의 끝(가장 강한)부터 내려오며 추가
    p = pills

    # 어려운 작업부터 처리
    for i in range(k - 1, -1, -1):
        need = t[i]

        # 보조 배터리를 쓰면 가능한 드론(need <= w[j] + strength)을 후보에 추가
        while j >= 0 and w[j] + strength >= need:
            # w는 오름차순, j는 감소 => 큰 값 -> 작은 값 순으로 들어옴
            # appendleft 하면 dq는 오름차순 유지 (left=작은, right=큰)
            dq.appendleft(w[j])
            j -= 1

        if not dq:
            return False

        # 배터리 없이 가능한 드론이 있으면(가장 큰 값이 need 이상) 우선 사용
        if dq[-1] >= need:
            dq.pop()
        else:
            # 배터리 사용: 가장 작은 후보에게 배터리를 주는 게 낭비가 적음
            if p == 0:
                return False
            dq.popleft()
            p -= 1

    return True

def solve():
    input = sys.stdin.readline
    first = input().split()
    if not first:
        return
    n, m, pills, strength = map(int, first)
    tasks = list(map(int, input().split()))[:n]
    workers = list(map(int, input().split()))[:m]

    tasks.sort()
    workers.sort()

    lo, hi = 0, min(n, m)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid, tasks, workers, pills, strength):
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == "__main__":
    solve()
