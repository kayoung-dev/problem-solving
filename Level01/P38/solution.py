import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
        
    stack = []
    # 문자열의 모든 문자를 스택에 푸시
    for char in s:
        stack.append(char)
        
    # 스택에서 하나씩 꺼내면(Pop) 문자열이 역순으로 나옴
    is_palindrome = True
    for char in s:
        if char != stack.pop():
            is_palindrome = False
            break
            
    if is_palindrome:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
