import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    
    prefix = line1[0]
    min_len = int(line1[1])
    
    # 파일명 리스트 입력
    files = sys.stdin.readline().split()
    
    # 로직: 조건 필터링 및 대문자 변환
    # 1. startswith(prefix): 접두사 확인
    # 2. len(s) > min_len: 길이 확인
    # 3. upper(): 대문자 변환
    
    result = []
    for f in files:
        if f.startswith(prefix) and len(f) > min_len:
            result.append(f.upper())
            
    # 예외 처리 및 정렬
    if not result:
        print("-1")
    else:
        result.sort()
        print(*result)

if __name__ == "__main__": main()
