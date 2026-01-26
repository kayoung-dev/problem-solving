import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    s = int(input_data[0])
    n = int(input_data[1])
    operations = input_data[2:]
    
    buffer = deque()
    
    for op in operations:
        if op == 'P':
            # 처리 명령: 가장 오래된 것 삭제
            if buffer:
                buffer.popleft()
        else:
            # 데이터 진입
            val = int(op)
            if len(buffer) == s:
                # 가득 찼으면 가장 오래된 것 버리고 추가
                buffer.popleft()
                buffer.append(val)
            else:
                # 빈 자리 있으면 그냥 추가
                buffer.append(val)
                
    if not buffer:
        print("empty")
    else:
        print(" ".join(map(str, buffer)))

if __name__ == "__main__":
    solve()
