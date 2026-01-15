import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    # 기온 리스트 생성
    temps = list(map(int, line.split()))
    
    max_gap = 0
    
    # 인접한 두 요소를 비교 (i와 i+1)
    # len(temps) - 1 까지만 반복해야 인덱스 에러가 나지 않습니다.
    for i in range(len(temps) - 1):
        # abs() 함수로 차이의 절댓값을 구합니다.
        gap = abs(temps[i] - temps[i+1])
        if gap > max_gap:
            max_gap = gap
            
    print(max_gap)

if __name__ == "__main__":
    main()
