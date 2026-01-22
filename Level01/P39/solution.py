import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("VALID")
        return
        
    stack = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == '<':
            j = i
            while j < n and s[j] != '>':
                j += 1
            if j == n: # 닫히지 않은 태그
                print("INVALID")
                return
            
            tag_content = s[i+1:j]
            i = j + 1
            
            if tag_content.startswith('/'):
                # 닫는 태그인 경우
                tag_name = tag_content[1:]
                if not stack or stack[-1] != tag_name:
                    print("INVALID")
                    return
                stack.pop()
            else:
                # 여는 태그인 경우
                stack.append(tag_content)
        else:
            i += 1
            
    if not stack:
        print("VALID")
    else:
        print("INVALID")

if __name__ == "__main__":
    solve()
