import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력 (사실 Python에서는 리스트를 바로 읽으면 되므로 크게 필요 없지만 형식상 받음)
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 배열 입력
    arr_line = input().strip()
    if not arr_line:
        # 빈 배열일 경우
        print("") 
        return
        
    arr = list(map(int, arr_line.split()))
    
    stack = []
    
    for num in arr:
        # 스택이 비어있거나, 스택의 마지막 요소(직전에 넣은 값)가 현재 값과 다르면 추가
        if not stack or stack[-1] != num:
            stack.append(num)
            
    # 결과 출력 (공백으로 구분)
    print(*(stack))

if __name__ == "__main__":
    solve()
