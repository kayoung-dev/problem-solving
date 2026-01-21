import sys

def solution():
    # 입력을 공백 기준으로 분리하여 리스트로 만듦
    tokens = sys.stdin.readline().strip().split()
    stack = []
    
    for token in tokens:
        if token == 'Z':
            # Z가 나오면 스택에서 가장 최근 숫자를 제거
            if stack:
                stack.pop()
        else:
            # 숫자가 나오면 스택에 추가 (정수로 변환)
            stack.append(int(token))
            
    # 스택에 남은 숫자들의 합 출력
    print(sum(stack))

if __name__ == "__main__":
    solution()
