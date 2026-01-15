import sys

def main():
    try:
        # 첫 번째 줄 N 입력
        line1 = input()
        if not line1: return
        n = int(line1.strip())
        
        # 두 번째 줄 점수 리스트 입력
        line2 = input()
        if not line2: return
        scores = list(map(int, line2.split()))
        
        # 최댓값과 최솟값 찾기
        max_val = max(scores)
        min_val = min(scores)
        
        # 전체 합에서 최댓값과 최솟값을 한 번씩 뺌
        total_sum = sum(scores) - max_val - min_val
        
        # 평균 계산 (N-2개로 나눔)
        avg = total_sum / (n - 2)
        
        # 소수점 둘째 자리까지 출력
        print(f"{avg:.2f}")
            
    except (EOFError, ValueError, ZeroDivisionError):
        pass

if __name__ == "__main__":
    main()
