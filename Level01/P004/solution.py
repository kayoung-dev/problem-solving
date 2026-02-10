import sys

def is_valid_parenthesis(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else: # char == ')'
            if not stack:
                return False
            stack.pop()
    
    # 순회가 끝났을 때 스택이 비어있어야 올바른 괄호
    return len(stack) == 0

def main():
    input = sys.stdin.readline
    
    try:
        t_str = input().strip()
        if not t_str:
            return
        t = int(t_str)
    except ValueError:
        return

    for _ in range(t):
        s = input().strip()
        if is_valid_parenthesis(s):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
