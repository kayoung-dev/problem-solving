import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 식 입력
    expression = input().split()
    stack = []

    for token in expression:
        if token not in ["+", "-", "*", "/"]:
            # 숫자일 경우 push
            stack.append(int(token))
        else:
            # 연산자일 경우 pop 2번
            val2 = stack.pop()
            val1 = stack.pop()
            
            if token == '+':
                res = val1 + val2
            elif token == '-':
                res = val1 - val2
            elif token == '*':
                res = val1 * val2
            elif token == '/':
                # C/Java 스타일의 정수 나눗셈 (0을 향해 버림)
                # Python의 //는 내림(floor)이므로 음수 계산시 차이가 있음
                # 문제 의도에 맞게 int(val1 / val2) 사용
                res = int(val1 / val2)
                
            stack.append(res)
            
    # 최종 결과 출력
    print(stack[0])

if __name__ == "__main__":
    solve()
