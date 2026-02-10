import sys

def solution():
    keylog = sys.stdin.read().strip()
    
    left_stack = []
    right_stack = []
    
    for char in keylog:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
    
    # 왼쪽 스택은 그대로, 오른쪽 스택은 거꾸로 출력해야 함
    print("".join(left_stack) + "".join(reversed(right_stack)))

if __name__ == "__main__":
    solution()
