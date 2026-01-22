import sys
from collections import deque

def solution():
    # 입력 처리
    lines = sys.stdin.read().splitlines()
    if len(lines) < 3:
        return

    # 두 개의 컨베이어 벨트(Queue)와 목표 리스트 생성
    belt_a = deque(lines[0].split())
    belt_b = deque(lines[1].split())
    orders = lines[2].split()
    
    count = 0
    
    for item in orders:
        # A 벨트의 맨 앞 확인
        if belt_a and belt_a[0] == item:
            belt_a.popleft()
            count += 1
        # B 벨트의 맨 앞 확인
        elif belt_b and belt_b[0] == item:
            belt_b.popleft()
            count += 1
        # 둘 다 해당하지 않으면 중단
        else:
            break
            
    print(count)

if __name__ == "__main__":
    solution()
