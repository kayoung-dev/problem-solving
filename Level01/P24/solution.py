import sys

def solution():
    input = sys.stdin.readline
    
    # 입력 처리
    try:
        n_str = input().strip()
        if not n_str: return
        n = int(n_str)
        heights = list(map(int, input().split()))
    except ValueError:
        return

    stack = [] # (index, height) 튜플 저장
    result = []
    
    # 각 빌딩을 순서대로 확인 (1-based index 사용을 위해 i+1 저장)
    for i in range(n):
        current_height = heights[i]
        
        # 스택의 top이 현재 건물보다 낮거나 같으면 pop
        # (왜냐하면 현재 건물이 그들보다 오른쪽에서 가로막고 있으므로, 
        # 이후의 건물들은 pop되는 건물들을 볼 수 없음 + 현재 건물보다 낮아서 수신도 못함)
        while stack and stack[-1][1] <= current_height:
            stack.pop()
            
        if stack:
            # 스택에 남은 것이 있다면, 그것이 나보다 높은 가장 가까운 건물
            result.append(str(stack[-1][0]))
        else:
            # 스택이 비었다면 왼쪽에 나보다 높은 건물이 없음
            result.append("0")
            
        # 현재 건물을 스택에 추가
        stack.append((i + 1, current_height))

    print(" ".join(result))

if __name__ == "__main__":
    solution()
