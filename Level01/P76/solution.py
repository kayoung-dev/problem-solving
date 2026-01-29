import sys
from collections import deque

# 입력 방식 설정 및 최적화
input = sys.stdin.readline

def solve():
    # 1. N, U 읽기
    first_line = input().split()
    if not first_line:
        return
    n, u = int(first_line[0]), int(first_line[1])
    
    # 2. 학생 명단 읽기 (줄바꿈 및 공백 처리)
    reg_names = input().split()
    urg_names = input().split()
    
    reg_q = deque(reg_names)
    urg_q = deque(urg_names)
    
    results = []
    
    # 3. 1:3 가중치 기반 동기화 로직
    while reg_q or urg_q:
        # 일반 질문군에서 최대 1명 입장
        if reg_q:
            results.append(reg_q.popleft())
            
        # 긴급 질문군에서 최대 3명 입장
        count = 0
        while urg_q and count < 3:
            results.append(urg_q.popleft())
            count += 1
            
    # 4. 결과 일괄 출력
    if not results:
        print("EMPTY")
    else:
        print(" ".join(results))

if __name__ == "__main__":
    solve()
