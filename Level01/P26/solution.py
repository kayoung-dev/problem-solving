import sys

def solve():
    # 문자열만 바로 읽어옴
    code = sys.stdin.read().strip()
    if not code:
        return
    
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in code:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                print("FAIL")
                return
            stack.pop()
            
    if not stack:
        print("PASS")
    else:
        print("FAIL")

if __name__ == "__main__":
    solve()
