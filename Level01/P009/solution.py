import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except ValueError:
        return

    # 수열 A 입력
    arr = list(map(int, input().split()))
    
    # 정답을 담을 배열, 기본값은 -1로 초기화
    # 오큰수가 없는 경우 그대로 -1이 출력됨
    answer = [-1] * n
    
    # 스택에는 '아직 오큰수를 찾지 못한 수의 인덱스'를 저장
    stack = []
    
    for i in range(n):
        # 스택이 비어있지 않고,
        # 현재 보고 있는 수(arr[i])가 스택의 맨 위(arr[stack[-1]])보다 크다면?
        # -> 스택에 있는 그 수의 오큰수가 바로 현재 수(arr[i])가 됨!
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            answer[idx] = arr[i]
            
        # 현재 인덱스를 스택에 넣고 다음으로 넘어감
        stack.append(i)
        
    # 출력
    print(*(answer))

if __name__ == "__main__":
    solve()
