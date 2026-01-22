import sys
from collections import deque

def solution():
    # 입력 처리
    line = sys.stdin.readline().split()
    if not line:
        return
    n, k = map(int, line)

    # 1부터 N까지 큐에 삽입
    queue = deque(range(1, n + 1))
    result = []

    # 큐가 빌 때까지 반복
    while queue:
        # K-1번만큼 앞에서 꺼내서 뒤로 보냄 (회전)
        for _ in range(k - 1):
            queue.append(queue.popleft())
        
        # K번째 사람(현재 맨 앞)을 제거하여 결과 리스트에 추가
        result.append(str(queue.popleft()))
    
    # 형식에 맞춰 출력 (<3, 6, ...>)
    sys.stdout.write("<" + ", ".join(result) + ">\n")

if __name__ == "__main__":
    solution()
