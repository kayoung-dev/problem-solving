import sys

def main():
    # input()은 한 줄을 읽은 뒤 엔터가 입력되면 즉시 다음 코드로 진행합니다.
    try:
        line = input()
        if not line:
            return

        # 데이터를 공백 기준으로 나누어 정수로 변환
        data = list(map(int, line.split()))
        
        if len(data) < 2:
            return

        n = data[0]
        k = data[1]
        weights = data[2:2+n]
        
        # 무게가 K 이상인 사과만 필터링
        picked = [w for w in weights if w >= k]
        
        if not picked:
            print("0 0")
        else:
            # 개수와 총 무게 출력 후 프로그램 종료
            print(f"{len(picked)} {sum(picked)}")
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()
