import sys

def solve():
    # 데이터를 모두 읽어와 공백 단위로 분리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 1차원 리스트를 2차원 서버실 격자로 변환
    grid = []
    for i in range(n):
        row = list(map(int, input_data[1 + i*n : 1 + (i+1)*n]))
        grid.append(row)
    
    max_heat_sum = 0
    
    # 냉각 장치의 왼쪽 위 시작점 (r, c)를 이동하며 모든 경우의 수 확인
    # 장치가 3x3이므로 n-2까지만 탐색 가능
    for r in range(n - 2):
        for c in range(n - 2):
            current_sum = 0
            # 시작점 (r, c)로부터 3x3 범위의 열기 합산
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    current_sum += grid[i][j]
            
            # 발견한 합계 중 최댓값 유지
            if current_sum > max_heat_sum:
                max_heat_sum = current_sum
                
    print(max_heat_sum)

if __name__ == "__main__":
    solve()
