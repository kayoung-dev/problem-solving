import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    
    if k <= 2:
        print(1)
        return
    
    # 중복 계산을 피하기 위해 각 층의 결과를 순차적으로 저장
    floor_info = [0] * (k + 1)
    floor_info[1] = 1
    floor_info[2] = 1
    
    for i in range(3, k + 1):
        # 이전 두 층의 정보를 합산하여 현재 층의 정보 생성
        floor_info[i] = floor_info[i-1] + floor_info[i-2]
        
    print(floor_info[k])

if __name__ == "__main__":
    solve()
