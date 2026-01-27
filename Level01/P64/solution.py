import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    capacity = int(input_data[1])
    usage = int(input_data[2])
    
    inflows = list(map(int, input_data[3:]))
    
    current_water = 0
    total_overflow = 0
    
    for water_in in inflows:
        # 1. 아침 유입
        current_water += water_in
        
        # 2. 오버플로우 체크
        if current_water > capacity:
            overflow = current_water - capacity
            total_overflow += overflow
            current_water = capacity # 물은 가득 찬 상태로 유지
            
        # 3. 저녁 소비
        if current_water >= usage:
            current_water -= usage
        else:
            current_water = 0 # 물이 부족하면 있는 만큼만 다 씀
            
    print(total_overflow)

if __name__ == "__main__":
    solve()
