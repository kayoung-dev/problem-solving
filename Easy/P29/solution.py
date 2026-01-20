import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    key = int(line1[1])  # 'divisor' 대신 'key' 사용
    
    # 암호 숫자 배열
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: key의 배수(나누어 떨어지는 수) 필터링
    real_codes = [num for num in arr if num % key == 0]
    
    # 예외 처리: 결과가 비어있으면 -1
    if not real_codes:
        print("-1")
    else:
        # 오름차순 정렬
        real_codes.sort()
        # 공백 구분 출력
        print(*real_codes)

if __name__ == "__main__": main()
