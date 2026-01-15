import sys

def main():
    # 입력을 한 줄 읽어 처리
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    try:
        pages = list(map(int, line.split()))
        if not pages:
            print(0)
            return
            
        # 1. 평균 구하기
        avg = sum(pages) / len(pages)
        
        # 2. 평균보다 작은 값 세기
        count = 0
        for p in pages:
            if p < avg:
                count += 1
                
        print(count)
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
