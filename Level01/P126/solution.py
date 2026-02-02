import sys

def time_to_seconds(t_str):
    h, m, s = map(int, t_str.split(':'))
    return h * 3600 + m * 60 + s

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start_time = input_data[0]
    end_time = input_data[1]
    k_str = input_data[2]
    
    start_sec = time_to_seconds(start_time)
    end_sec = time_to_seconds(end_time)
    
    count = 0
    # 시작 초부터 종료 초까지 1초씩 증가하며 확인
    for current_total_sec in range(start_sec, end_sec + 1):
        h = current_total_sec // 3600
        m = (current_total_sec % 3600) // 60
        s = current_total_sec % 60
        
        # HH:MM:SS 형식의 문자열로 변환하여 K가 있는지 확인
        time_str = f"{h:02d}:{m:02d}:{s:02d}"
        if k_str in time_str:
            count += 1
            
    print(count)

if __name__ == "__main__":
    solve()
