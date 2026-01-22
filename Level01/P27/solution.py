import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    stack = []
    
    for token in tokens:
        if token in ('+', '-', '*'):
            # 연산자를 만나면 스택에서 두 개 추출
            op2 = stack.pop()
            op1 = stack.pop()
            
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
        else:
            # 숫자인 경우 정수로 변환하여 스택에 추가
            stack.append(int(token))
            
    print(stack[0])

if __name__ == "__main__":
    solve()
