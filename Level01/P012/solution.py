import sys

def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(1)
    else:
        print(solution(input_data))
