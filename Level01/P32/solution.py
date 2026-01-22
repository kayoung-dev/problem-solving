import sys

def solve():
    lines = sys.stdin.read().splitlines()
    
    stack = []      # 실제 데이터를 담는 메인 스택
    min_stack = []  # 각 시점의 최솟값을 관리하는 보조 스택
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        cmd = parts[0]
        
        if cmd == 'PUSH':
            val = int(parts[1])
            stack.append(val)
            # 보조 스택이 비어있거나, 현재 값이 최솟값보다 작거나 같으면 추가
            if not min_stack or val <= min_stack[-1]:
                min_stack.append(val)
        
        elif cmd == 'POP':
            if stack:
                popped = stack.pop()
                # 제거된 값이 현재 최솟값이었다면 보조 스택에서도 제거
                if popped == min_stack[-1]:
                    min_stack.pop()
        
        elif cmd == 'TOP':
            print(stack[-1] if stack else "-1")
        
        elif cmd == 'MIN':
            print(min_stack[-1] if min_stack else "-1")

if __name__ == "__main__":
    solve()
