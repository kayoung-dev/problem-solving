import sys
from collections import deque

input = sys.stdin.readline

def solve():
    stamp = input().strip()
    target = input().strip()
    if not stamp or not target: return
    
    m, n = len(stamp), len(target)
    goal = "?" * n
    
    # 목표에서 시작하여 초기상태로 가는 최단 경로 탐색
    queue = deque([(target, [])])
    visited = {target}
    
    while queue:
        curr, path = queue.popleft()
        
        if curr == goal:
            # 역순 탐색이므로 결과를 뒤집어서 출력
            print(*(path[::-1]))
            return
            
        for i in range(n - m + 1):
            match = True
            has_val = False
            temp = list(curr)
            
            for j in range(m):
                if curr[i+j] == '?': continue
                if curr[i+j] == stamp[j]:
                    has_val = True
                    temp[i+j] = '?'
                else:
                    match = False
                    break
            
            if match and has_val:
                nxt = "".join(temp)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [i]))
                    
    print("FAILED")

if __name__ == "__main__":
    solve()
