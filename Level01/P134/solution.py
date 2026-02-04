import sys

def solve():
    # 대용량 입력 처리를 위해 표준 입력 전체를 읽음
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    parts = list(map(int, input_data[1:]))
    
    # 오른쪽 그룹(2번 검수원)의 초기 상태 설정
    right_freq = {}
    for p in parts:
        right_freq[p] = right_freq.get(p, 0) + 1
    
    right_types = len(right_freq)
    left_freq = {}
    left_types = 0
    answer = 0
    
    # 벨트를 1번째 부품 뒤부터 N-1번째 부품 뒤까지 하나씩 잘라봄
    for i in range(n - 1):
        p = parts[i]
        
        # 왼쪽 그룹에 부품 추가
        if left_freq.get(p, 0) == 0:
            left_types += 1
        left_freq[p] = left_freq.get(p, 0) + 1
        
        # 오른쪽 그룹에서 부품 제거
        right_freq[p] -= 1
        if right_freq[p] == 0:
            right_types -= 1
            
        # 두 그룹의 고유 모델 종류 수 비교
        if left_types == right_types:
            answer += 1
            
    sys.stdout.write(str(answer) + '\n')

if __name__ == "__main__":
    solve()
