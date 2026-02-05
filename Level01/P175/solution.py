import sys
import bisect

def solve():
    input = sys.stdin.readline
    line = input().strip()
    if not line: return
    n = int(line)
    
    # 시작 시간 기준으로 정렬된 상태를 유지할 리스트
    sessions = [] # (start, end)
    
    for _ in range(n):
        req = input().split()
        if not req: break
        s, e = map(int, req)
        
        # 이진 탐색으로 현재 시작 시간이 들어갈 위치 탐색 (O(log N))
        idx = bisect.bisect_left(sessions, (s, e))
        
        is_conflict = False
        # 1. 뒷집 확인 (내 종료 시간이 뒤 세션의 시작 시간보다 늦으면 충돌)
        if idx < len(sessions) and e > sessions[idx][0]:
            is_conflict = True
        
        # 2. 앞집 확인 (내 시작 시간이 앞 세션의 종료 시간보다 빠르면 충돌)
        if not is_conflict and idx > 0 and s < sessions[idx-1][1]:
            is_conflict = True
            
        if not is_conflict:
            sessions.insert(idx, (s, e))
            sys.stdout.write("BOOKED\n")
        else:
            sys.stdout.write("CONFLICT\n")

if __name__ == "__main__":
    solve()
