import sys

def solution():
    # 빠른 입출력을 위해 sys.stdin 사용
    input = sys.stdin.readline
    
    initial_str = input().strip()
    try:
        m_line = input().strip()
        if not m_line:
            m = 0
        else:
            m = int(m_line)
    except ValueError:
        m = 0
        
    left_stack = list(initial_str)
    right_stack = []
    
    for _ in range(m):
        command = input().split()
        cmd_type = command[0]
        
        if cmd_type == 'L':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif cmd_type == 'D':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif cmd_type == 'B':
            if left_stack:
                left_stack.pop()
        elif cmd_type == 'P':
            left_stack.append(command[1])
            
    # 오른쪽 스택은 역순으로 출력해야 함
    print("".join(left_stack) + "".join(reversed(right_stack)))

if __name__ == "__main__":
    solution()
