import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
        
    try:
        # N: 방의 개수, K: 이동 거리
        n, k = map(int, line.split())
        
        # 원형 순환의 핵심은 나머지 연산입니다.
        # 어떤 숫자든 N으로 나눈 나머지는 항상 0 ~ N-1 범위 안에 들어옵니다.
        result = k % n
        
        print(result)
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
