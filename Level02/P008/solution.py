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

    # 기온 리스트 입력
    temps = list(map(int, input().split()))
    
    # 정답 배열 (기본값 0으로 초기화)
    answer = [0] * n
    
    # 스택: "아직 더 따뜻한 날을 찾지 못한 날짜들의 인덱스"를 모아둡니다.
    stack = []
    
    for i in range(n):
        # 스택이 비어있지 않고, 
        # 현재 기온(temps[i])이 스택의 가장 최근 날짜(stack[-1])의 기온보다 높다면?
        # -> 드디어 더 따뜻한 날을 만난 것입니다!
        while stack and temps[stack[-1]] < temps[i]:
            past_day = stack.pop()
            # 기다린 날짜 = 현재 날짜(i) - 과거 날짜(past_day)
            answer[past_day] = i - past_day
            
        # 현재 날짜도 아직 더 따뜻한 날을 못 만났으므로 스택에 넣고 다음으로 넘어갑니다.
        stack.append(i)
        
    print(*(answer))

if __name__ == "__main__":
    solve()
