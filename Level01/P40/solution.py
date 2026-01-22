import sys

def solve():
    # 입력을 읽어와 첫 번째 값(개수 K)을 추출
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    numbers = input_data[1:]
    
    stack = []
    
    for i in range(k):
        num = int(numbers[i])
        if num == 0:
            # 0이면 가장 최근 값을 제거
            if stack:
                stack.pop()
        else:
            # 0이 아니면 스택에 추가
            stack.append(num)
            
    # 남아있는 모든 값의 합계 출력
    print(sum(stack))

if __name__ == "__main__":
    solve()
