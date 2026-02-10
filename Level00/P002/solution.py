import sys

def main():
    # 첫 번째 줄(N) 읽기
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    
    target_count = 0
    
    # N번만큼 반복하며 각 줄의 데이터를 읽음
    for _ in range(n):
        line = sys.stdin.readline()
        if not line:
            break
            
        data = list(map(int, line.split()))
        m = data[0]      # 위험 기준치
        c = data[1]      # 간식 개수
        days = data[2:]  # 유통기한 데이터
        
        urgent_items = [d for d in days if d <= 3]
        urgent_sum = sum(urgent_items)
        
        if urgent_items and urgent_sum <= m:
            target_count += 1
            
    print(target_count)

if __name__ == "__main__":
    main()
