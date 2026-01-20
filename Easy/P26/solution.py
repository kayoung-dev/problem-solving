import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    divisor = int(line1[1])
    
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: divisor로 나누어 떨어지는 값 필터링
    filtered = [num for num in arr if num % divisor == 0]
    
    # 예외 처리 및 정렬
    if not filtered:
        print("-1")
    else:
        filtered.sort()
        # 언패킹(*)을 사용하여 공백 구분 출력
        print(*filtered)

if __name__ == "__main__": main()
