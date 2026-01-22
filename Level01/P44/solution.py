import sys
from collections import deque

def solution():
    # 입력 처리
    lines = sys.stdin.read().splitlines()
    if len(lines) < 3:
        return

    # 대기 줄 A, B와 목표 명단 Target을 큐로 변환
    queue_a = deque(lines[0].split())
    queue_b = deque(lines[1].split())
    target = deque(lines[2].split())
    
    # 목표 명단을 순서대로 하나씩 확인
    for person in target:
        # 1. A 줄의 맨 앞 사람과 일치하는지 확인
        if queue_a and queue_a[0] == person:
            queue_a.popleft()
            
        # 2. B 줄의 맨 앞 사람과 일치하는지 확인
        elif queue_b and queue_b[0] == person:
            queue_b.popleft()
            
        # 3. 둘 다 아니라면 더 이상 진행 불가
        else:
            print("No")
            return
            
    # 반복문이 끝날 때까지 문제가 없었다면 성공
    print("Yes")

if __name__ == "__main__":
    solution()
