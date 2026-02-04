import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    steps = 0
    total_zeros = 0
    
    # 신호가 "10"이 될 때까지 반복
    while s != "10":
        steps += 1
        
        # 현재 문자열에서 1의 개수(L)와 0의 개수 파악
        ones_count = s.count('1')
        zeros_count = s.count('0')
        
        total_zeros += zeros_count
        
        # L * 2를 이진법으로 변환
        # bin(n)은 '0b...' 형태이므로 [2:]로 슬라이싱
        s = bin(ones_count * 2)[2:]
        
    print(f"{steps} {total_zeros}")

if __name__ == "__main__":
    solve()
