import sys
from collections import deque

# 입력 방식 설정
input = sys.stdin.readline

def solve():
    # 1. N 읽기
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    
    storage_a = deque()
    storage_b = deque()
    results = [] # 결과를 모아둘 리스트
    
    # 2. 입력 처리 및 로직 수행
    for _ in range(n):
        line = input().strip().split()
        if not line:
            continue
            
        type, book_id = line[0], line[1]
        
        if type == 'A':
            storage_a.append(book_id)
        else:
            storage_b.append(book_id)
            
        # 세트 구성이 가능할 때마다 결과 리스트에 추가
        while storage_a and storage_b:
            theory = storage_a.popleft()
            lab = storage_b.popleft()
            results.append(f"{theory} + {lab}")
            
    # 3. 모든 입력이 끝난 후 한 번에 출력
    if not results:
        print("WAITING")
    else:
        print("\n".join(results))

if __name__ == "__main__":
    solve()
