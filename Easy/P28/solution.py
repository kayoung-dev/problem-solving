import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    box_size = int(line1[1])
    
    # 쿠키 묶음 배열
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: 나누어 떨어지는 경우, 몫(num // box_size)을 저장
    results = []
    for num in arr:
        if num % box_size == 0:
            results.append(num // box_size)
    
    # 예외 처리 및 정렬
    if not results:
        print("-1")
    else:
        results.sort()
        print(*results)

if __name__ == "__main__": main()
