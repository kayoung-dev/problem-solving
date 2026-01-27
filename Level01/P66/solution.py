import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    
    # 데이터 파싱
    line_a = list(map(int, input_data[1:1+n]))
    line_b = list(map(int, input_data[1+n:1+2*n]))
    line_c = list(map(int, input_data[1+2*n:1+3*n]))
    
    # 이전 학생의 각 코너 완료 시각 (초기값 0)
    prev_end_a = 0
    prev_end_b = 0
    prev_end_c = 0
    
    results = []
    
    for i in range(n):
        # 1코너: 앞사람이 비워줘야 시작 (prev_end_a) + 내 소요시간
        curr_end_a = prev_end_a + line_a[i]
        
        # 2코너: 내가 1코너에서 와야 하고(curr_end_a), 앞사람이 2코너를 비워줘야 함(prev_end_b)
        curr_end_b = max(curr_end_a, prev_end_b) + line_b[i]
        
        # 3코너: 내가 2코너에서 와야 하고(curr_end_b), 앞사람이 3코너를 비워줘야 함(prev_end_c)
        curr_end_c = max(curr_end_b, prev_end_c) + line_c[i]
        
        results.append(str(curr_end_c))
        
        # 다음 학생을 위해 완료 시간 갱신
        prev_end_a = curr_end_a
        prev_end_b = curr_end_b
        prev_end_c = curr_end_c
        
    print(" ".join(results))

if __name__ == "__main__":
    solve()
