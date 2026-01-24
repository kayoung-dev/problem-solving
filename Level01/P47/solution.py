import sys
from collections import deque

def solve():
    s = sys.stdin.read().strip()
    if not s:
        print(0)
        return
    
    q = deque(list(s))
    
    # 더 이상 제거가 일어나지 않을 때까지 반복 (최대 회전 수 제한)
    changed = True
    while changed and len(q) >= 2:
        changed = False
        # 한 바퀴를 도는 동안 제거가 일어나는지 확인
        for _ in range(len(q)):
            if len(q) < 2: break
            
            if q[0] == q[1]:
                q.popleft()
                q.popleft()
                changed = True
                break # 제거되면 다시 처음부터 검사
            else:
                q.append(q.popleft()) # 회전
                
    print(len(q))

if __name__ == "__main__":
    solve()
