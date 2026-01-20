import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    divisor = int(line1[1])
    
    # 도토리 무게 배열
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: divisor로 나누어 떨어지는 무게 필터링
    filtered = [w for w in arr if w % divisor == 0]
    
    # 예외 처리: 빈 배열일 경우 -1 출력
    if not filtered:
        print("-1")
    else:
        # 오름차순 정렬
        filtered.sort()
        # 결과 출력
        print(*filtered)

if __name__ == "__main__": main()
