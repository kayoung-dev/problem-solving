import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data: return
    
    first_line = input_data[0].split()
    n_a, n_b = int(first_line[0]), int(first_line[1])
    
    line_a = deque()
    line_b = deque()
    
    if n_a > 0 and len(input_data) > 1:
        line_a = deque(input_data[1].split())
        
    # line_b의 데이터 위치는 n_a의 존재 여부에 따라 달라질 수 있음
    # 안전하게 파싱하기 위해 모든 라인을 읽고 처리
    current_line_idx = 2
    if n_a == 0:
        current_line_idx = 1
        
    if n_b > 0 and len(input_data) > current_line_idx:
        line_b = deque(input_data[current_line_idx].split())
    
    while abs(len(line_a) - len(line_b)) > 1:
        if len(line_a) > len(line_b):
            person = line_a.popleft()
            line_b.append(person)
        else:
            person = line_b.popleft()
            line_a.append(person)
            
    print(" ".join(line_a) if line_a else "Empty")
    print(" ".join(line_b) if line_b else "Empty")

if __name__ == "__main__":
    solve()
