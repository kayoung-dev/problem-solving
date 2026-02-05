import sys
import bisect

def solve():
    input = sys.stdin.readline
    line = input().strip()
    if not line: return
    q = int(line)
    
    schedule = [] # (start, end)
    
    for _ in range(q):
        req = input().split()
        if not req: break
        s, e = map(int, req)
        
        # 시작 시간 기준으로 위치 찾기 (O(log N))
        idx = bisect.bisect_left(schedule, (s, e))
        
        can_assign = True
        # 뒷집 확인
        if idx < len(schedule) and e > schedule[idx][0]:
            can_assign = False
        # 앞집 확인
        if can_assign and idx > 0 and s < schedule[idx-1][1]:
            can_assign = False
            
        if can_assign:
            schedule.insert(idx, (s, e))
            sys.stdout.write("ALLOW\n")
        else:
            sys.stdout.write("DENY\n")

if __name__ == "__main__":
    solve()
