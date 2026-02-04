import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    steps = 0
    while len(s) > 1:
        steps += 1
        current_sum = 0
        
        # 현재 문자열에서 숫자만 골라내어 짝수인지 확인
        for char in s:
            if char.isdigit():
                digit = int(char)
                if digit % 2 != 0: # 홀수인 경우만 합산
                    current_sum += digit
        
        # 합계를 16진법 대문자로 변환 (hex()는 '0x'를 붙이고 소문자임)
        s = hex(current_sum)[2:].upper()
        
    print(f"{steps} {s}")

if __name__ == "__main__":
    solve()
