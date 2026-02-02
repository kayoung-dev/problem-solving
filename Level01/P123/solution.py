import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    grid = input_data[2:]
    
    # 2차원 격자를 순회하며 1을 찾음
    for r in range(n):
        for c in range(m):
            # 1차원 리스트로 읽어들인 grid에서 현재 위치 계산
            if int(grid[r * m + c]) == 1:
                print(f"{r + 1} {c + 1}")
                return

if __name__ == "__main__":
    solve()
