import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    steps = 0
    total_zeros = 0
    
    # 종료 조건 "11"을 만족할 때까지 루프
    while s != "11":
        steps += 1
        
        ones_count = s.count('1')
        zeros_count = s.count('0')
        total_zeros += zeros_count
        
        # 새로운 신호 = (L + 2)의 이진법 변환
        s = bin(ones_count + 2)[2:]
        
    print(f"{steps} {total_zeros}")

if __name__ == "__main__":
    solve()
