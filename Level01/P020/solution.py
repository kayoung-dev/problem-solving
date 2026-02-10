import sys

def solution():
    expression = sys.stdin.readline().strip()
    stack = []
    
    for char in expression:
        if char == ')':
            top = stack.pop()
            
            # 괄호 안에 내용물이 없거나, 바로 여는 괄호가 나온 경우
            # 일반적인 수식에서는 연산자나 피연산자가 있어야 함
            # 여기서는 '((...))' 형태를 잡기 위해, 
            # 닫는 괄호를 만났을 때 스택 top이 바로 '('라면 
            # 이는 '()' (빈 괄호) 이거나 '((...))' (내용물이 이미 pop된 상태)를 의미함
            if top == '(':
                print("YES")
                return
            
            # '('를 만날 때까지 계속 pop (내용물 제거)
            while top != '(':
                top = stack.pop()
        else:
            stack.append(char)
            
    print("NO")

if __name__ == "__main__":
    solution()
