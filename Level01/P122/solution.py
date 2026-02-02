import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    weights = list(map(int, input_data[2:]))
    
    bad_apple_count = 0
    
    # 각 사과를 하나씩 확인하며 기준 무게 K 미만인지 검사
    for w in weights:
        if w < k:
            bad_apple_count += 1
            
    print(bad_apple_count)

if __name__ == "__main__":
    solve()
