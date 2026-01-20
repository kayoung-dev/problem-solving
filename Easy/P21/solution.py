import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    try:
        n = int(line)
        
        # 요일 리스트 (0: 월요일, 1: 화요일, ..., 6: 일요일)
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        
        # 7일 주기로 반복되므로 모듈러 연산 사용
        target_index = n % 7
        
        print(days[target_index])
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
