import sys

def solution():
    # 문자열 입력
    s = sys.stdin.readline().strip()
    if not s:
        return

    stack = []
    
    for char in s:
        # 스택이 비어있지 않고, 맨 위의 구슬과 현재 구슬이 같다면?
        if stack and stack[-1] == char:
            stack.pop() # 펑! (맨 위 제거, 현재 구슬도 넣지 않음)
        else:
            stack.append(char) # 다르다면 쌓기
            
    if stack:
        print("".join(stack))
    else:
        print("empty")

if __name__ == "__main__":
    solution()
