import sys

def main():
    # 입력을 한 줄만 읽고 즉시 처리합니다.
    line = sys.stdin.readline().strip()
    if not line:
        return
        
    try:
        n = int(line)
        results = []
        for i in range(1, n + 1):
            s_i = str(i)
            # 숫자에 3, 6, 9가 포함되어 있는지 확인
            if any(char in s_i for char in "369"):
                results.append("clap")
            else:
                results.append(s_i)
        
        # 결과를 한 줄로 출력하고 프로그램은 종료됩니다.
        print(" ".join(results))
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
