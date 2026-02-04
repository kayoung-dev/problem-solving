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
    
    low = 0
    high = n - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == k:
            found = True
            break
        elif ids[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    end_time = time.time()
    # --- 시간 측정 종료 ---

    print(f"[Binary Search Result] Found: {found}")
    print(f"Execution Time: {end_time - start_time:.10f} seconds")

if __name__ == "__main__":
    solve()