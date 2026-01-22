import sys

def solve():
    # 입력을 읽어 정수로 변환
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    n = int(input_data)
    
    # 0인 경우 예외 처리
    if n == 0:
        print("0")
        return
        
    stack = []
    
    # 2로 나누며 나머지를 스택에 저장
    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n //= 2
        
    # 스택에서 하나씩 꺼내어 문자열로 합침 (역순 출력)
    result = ""
    while stack:
        result += str(stack.pop())
        
    print(result)

if __name__ == "__main__":
    solve()
