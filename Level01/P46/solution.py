import sys
from collections import deque

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return not stack

def solve():
    s = sys.stdin.read().strip()
    if not s: return
    
    n = len(s)
    count = 0
    q = deque(s)
    
    for _ in range(n):
        if is_valid(list(q)):
            count += 1
        q.append(q.popleft())
    print(count)

if __name__ == "__main__":
    solve()
