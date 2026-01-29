import sys
from collections import deque

# 입력 방식 최적화
input = sys.stdin.readline

def solve():
    # 1. N 읽기
    line_n = input().strip()
    if not line_n: return
    n = int(line_n)
    
    # 2. 동아리 소속 데이터 읽기
    senate = input().strip()
    if not senate: return

    # 각 동아리 부원들의 초기 인덱스를 보관
    blue = deque()
    red = deque()
    
    for i, s in enumerate(senate):
        if s == 'B':
            blue.append(i)
        else:
            red.append(i)
            
    # 3. 토론 시뮬레이션
    while blue and red:
        b_idx = blue.popleft()
        r_idx = red.popleft()
        
        # 더 앞 순서인 부원이 상대방을 퇴장시키고 뒤로 가서 줄을 섬
        # 다음 라운드(인덱스 + N)로 위치를 갱신
        if b_idx < r_idx:
            blue.append(b_idx + n)
        else:
            red.append(r_idx + n)
            
    # 4. 결과 출력
    if blue:
        print("Blue Wave")
    else:
        print("Red Passion")

if __name__ == "__main__":
    solve()
