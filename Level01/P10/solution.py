import sys

def solve():
    # 빠른 입출력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline
    
    # 초기 문자열 읽기 (개행문자 제거)
    initial_str = input().strip()
    
    try:
        line = input().strip()
        if not line: return
        m = int(line)
    except ValueError:
        return

    # 두 개의 스택을 사용 (커서 기준 왼쪽 스택, 오른쪽 스택)
    # 예: "abc|de" 상태라면 left=['a','b','c'], right=['e','d'] (오른쪽은 거꾸로 쌓임)
    left_stack = list(initial_str)
    right_stack = []
    
    for _ in range(m):
        command = input().split()
        op = command[0]
        
        if op == 'L':
            # 커서를 왼쪽으로: 왼쪽 스택의 문자를 오른쪽 스택으로 이동
            if left_stack:
                right_stack.append(left_stack.pop())
                
        elif op == 'D':
            # 커서를 오른쪽으로: 오른쪽 스택의 문자를 왼쪽 스택으로 이동
            if right_stack:
                left_stack.append(right_stack.pop())
                
        elif op == 'B':
            # 커서 왼쪽 문자 삭제: 왼쪽 스택에서 pop
            if left_stack:
                left_stack.pop()
                
        elif op == 'P':
            # 커서 왼쪽에 문자 추가: 왼쪽 스택에 push
            char_to_add = command[1]
            left_stack.append(char_to_add)
            
    # 최종 결과 출력
    # right_stack은 스택 구조상 문자열 순서가 반대이므로 뒤집어서 출력
    print("".join(left_stack + right_stack[::-1]))

if __name__ == "__main__":
    solve()
