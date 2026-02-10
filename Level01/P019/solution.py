import sys

def solution():
    s = sys.stdin.readline().strip()
    stack = []
    temp = 1
    result = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            temp *= 2
        elif s[i] == '[':
            stack.append(s[i])
            temp *= 3
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                print(0)
                return
            if s[i-1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        elif s[i] == ']':
            if not stack or stack[-1] == '(':
                print(0)
                return
            if s[i-1] == '[':
                result += temp
            stack.pop()
            temp //= 3
            
    if stack:
        print(0)
    else:
        print(result)

if __name__ == "__main__":
    solution()
