import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # (사람 번호, 남은 물의 양)을 저장할 공간
    waiting_line = deque()
    for i in range(n):
        waiting_line.append((i + 1, int(input_data[2 + i])))
        
    finished_order = []
    
    while waiting_line:
        person_id, remaining_water = waiting_line.popleft()
        
        # 이번 차례에 받을 물의 양 (K와 남은 양 중 작은 값)
        fill_amount = min(remaining_water, k)
        new_remaining = remaining_water - fill_amount
        
        if new_remaining > 0:
            # 물이 더 남았다면 줄의 맨 뒤로
            waiting_line.append((person_id, new_remaining))
        else:
            # 다 채웠다면 순서 기록
            finished_order.append(str(person_id))
            
    print(" ".join(finished_order))

if __name__ == "__main__":
    solve()
