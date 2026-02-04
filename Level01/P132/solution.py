import sys

def solve():
    # 대량 데이터 처리를 위한 최적화된 입력 방식
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # ID 범위가 10,000 이하이므로 배열을 사용하여 속도 향상
    data = list(map(int, input_data[1:]))
    
    # 오른쪽 구간 빈도 측정
    right_freq = [0] * 10001
    right_unique_count = 0
    for x in data:
        right_freq[x] += 1
    
    # 초기에 오른쪽 구간에서 유일(빈도가 정확히 1)한 ID 개수 계산
    for f in right_freq:
        if f == 1:
            right_unique_count += 1
            
    left_freq = [0] * 10001
    left_unique_count = 0
    answer = 0
    
    # 슬라이딩 윈도우 방식으로 경계면 이동
    for i in range(n - 1):
        val = data[i]
        
        # 1. 왼쪽으로 데이터 추가
        old_l_f = left_freq[val]
        left_freq[val] += 1
        if left_freq[val] == 1: # 0에서 1이 되면 유일 ID 증가
            left_unique_count += 1
        elif old_l_f == 1: # 1에서 2가 되면 더 이상 유일하지 않음
            left_unique_count -= 1
            
        # 2. 오른쪽에서 데이터 제거
        old_r_f = right_freq[val]
        right_freq[val] -= 1
        if right_freq[val] == 1: # 2에서 1이 되면 유일 ID로 부활
            right_unique_count += 1
        elif old_r_f == 1: # 1에서 0이 되면 유일 ID 소멸
            right_unique_count -= 1
            
        # 3. 조건 비교
        if left_unique_count == right_unique_count:
            answer += 1
            
    sys.stdout.write(str(answer) + '\n')

if __name__ == "__main__":
    solve()
