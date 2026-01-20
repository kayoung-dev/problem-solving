import sys

def main():
    # 첫 번째 줄: 배열 크기 N, 나누는 수 divisor
    first_line = sys.stdin.readline().split()
    if not first_line: return
    n = int(first_line[0])
    divisor = int(first_line[1])
    
    # 두 번째 줄: 배열 요소
    arr = list(map(int, sys.stdin.readline().split()))
    
    # divisor로 나누어 떨어지는 수 필터링
    result = [num for num in arr if num % divisor == 0]
    
    # 결과가 비어있으면 -1, 아니면 오름차순 정렬 후 출력
    if not result:
        print("-1")
    else:
        result.sort()
        # 리스트 요소들을 공백으로 구분하여 출력
        print(*(result))

if __name__ == "__main__": main()
