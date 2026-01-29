import sys
from collections import deque

def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = get_input()
    
    try:
        n = int(next(tokens))
        k = int(next(tokens))
    except (StopIteration, ValueError):
        return
        
    table = deque()
    total_energy = 0
    
    for _ in range(n):
        try:
            name = next(tokens)
            energy = int(next(tokens))
        except StopIteration:
            break
            
        # 1. 평균 에너지 조건 검사 및 제거
        while table:
            avg = total_energy / len(table)
            if energy >= avg:
                break
            _, e = table.popleft()
            total_energy -= e
            
        # 2. 정원 초과 검사
        if len(table) == k:
            _, e = table.popleft()
            total_energy -= e
            
        # 3. 학생 합류
        table.append((name, energy))
        total_energy += energy
        
    if not table:
        print("EMPTY")
    else:
        print(" ".join([s[0] for s in table]))

if __name__ == "__main__":
    solve()
