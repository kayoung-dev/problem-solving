import sys

def solve():
    expression = sys.stdin.read().strip()
    if not expression:
        return
        
    # 연산자별 우선순위 설정
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1}
    stack = []
    result = []
    
    for char in expression:
        # 피연산자(알파벳)는 바로 결과에 추가
        if char.isalpha():
            result.append(char)
        else:
            # 스택에 있는 연산자가 현재 연산자보다 우선순위가 높거나 같다면 pop하여 결과에 추가
            while stack and precedence[stack[-1]] >= precedence[char]:
                result.append(stack.pop())
            # 현재 연산자를 스택에 push
            stack.append(char)
            
    # 스택에 남은 모든 연산자를 결과에 추가
    while stack:
        result.append(stack.pop())
        
    print("".join(result))

if __name__ == "__main__":
    solve()
