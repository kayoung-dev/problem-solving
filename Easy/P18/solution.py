import sys

def main():
    # 한 줄의 데이터를 읽어옵니다.
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    # 공백으로 나누어 리스트로 변환
    stones = list(map(int, line.split()))
    
    total_score = 0
    for i in range(len(stones)):
        # i가 0, 2, 4... 일 때가 실제로는 1, 3, 5... 번째 다리입니다.
        if (i + 1) % 2 != 0:
            total_score += stones[i]
        else:
            total_score -= stones[i]
            
    print(total_score)

if __name__ == "__main__":
    main()
