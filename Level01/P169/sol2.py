import sys
import time

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    k = int(data[1])
    ids = list(map(int, data[2:]))

    # --- 시간 측정 시작 ---
    start_time = time.time()
    
    found = False
    for i in range(n):
        if ids[i] == k:
            found = True
            break
            
    end_time = time.time()
    # --- 시간 측정 종료 ---

    print(f"[Linear Search Result] Found: {found}")
    print(f"Execution Time: {end_time - start_time:.10f} seconds")

if __name__ == "__main__":
    solve()