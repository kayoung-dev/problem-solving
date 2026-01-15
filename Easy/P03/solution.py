import sys

def main():
    # input()을 사용하여 엔터가 입력되는 즉시 한 줄을 읽습니다.
    try:
        line = input()
        if not line:
            return
            
        # 파이썬의 슬라이싱 기능을 사용하여 문자열을 뒤집습니다.
        reversed_str = line[::-1]
        
        # 결과 출력 후 즉시 종료
        print(reversed_str)
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()
