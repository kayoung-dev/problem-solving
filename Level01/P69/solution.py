import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    students = []
    idx = 1
    for _ in range(n):
        students.append((input_data[idx], input_data[idx+1]))
        idx += 2
        
    blue_q = deque()
    white_q = deque()
    
    for team, name in students:
        if team == 'B':
            if white_q:
                partner = white_q.popleft()
                print(f"{name} - {partner}")
            else:
                blue_q.append(name)
        else: # team == 'W'
            if blue_q:
                partner = blue_q.popleft()
                print(f"{partner} - {name}")
            else:
                white_q.append(name)
                
    remaining = len(blue_q) + len(white_q)
    print(f"Remaining: {remaining}명")

if __name__ == "__main__":
    solve()
