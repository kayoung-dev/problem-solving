import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    m = int(input_data[1])
    item_ids = list(map(int, input_data[2:2+n]))
    
    # M개의 큐(라인) 생성
    lines = [deque() for _ in range(m)]
    
    # 규칙에 따라 분배
    for item_id in item_ids:
        line_idx = item_id % m
        lines[line_idx].append(item_id)
        
    # 결과 출력
    for i in range(m):
        if not lines[i]:
            print(f"Line {i}: Empty")
        else:
            print(f"Line {i}: {' '.join(map(str, lines[i]))}")

if __name__ == "__main__":
    solve()
