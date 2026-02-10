import sys

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

def solution(s):
    n = len(s)
    count = 0
    if n % 2 != 0: return 0
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
    else:
        print(solution(input_data))
