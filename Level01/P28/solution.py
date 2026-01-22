import sys

def solve():
    # 문자열을 읽어 정수 리스트로 변환
    data = sys.stdin.read().split()
    if not data:
        return
    
    intensities = list(map(int, data))
    n = len(intensities)
    result = [0] * n
    stack = [] # 아직 자신을 막을 장벽을 찾지 못한 신호들의 인덱스

    for i in range(n):
        # 현재 신호(i)가 스택에 대기 중인 신호들보다 강하다면, 
        # 현재 신호가 그들의 진행을 가로막는 '첫 번째 장벽'이 됨
        while stack and intensities[stack[-1]] < intensities[i]:
            target_idx = stack.pop()
            result[target_idx] = i + 1 # 신호 번호는 1부터 시작
        
        # 현재 신호도 누군가에게 막힐 때까지 대기하기 위해 스택에 추가
        stack.append(i)
    
    print(*(result))

if __name__ == "__main__":
    solve()
