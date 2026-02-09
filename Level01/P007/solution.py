import sys

def main():
    try:
        # 1. 찾을 문자 입력 (엔터 포함 문자열 처리)
        line1 = input()
        if not line1: return
        target_char = line1.strip()
        
        # 2. 전체 문장 입력
        sentence = input()
        
        # 3. 개수 세기
        count = sentence.count(target_char)
        
        print(count)
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()
