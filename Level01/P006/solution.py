import sys

def main():
    try:
        # 1. 책의 개수 N 입력
        line1 = input()
        if not line1: return
        n = int(line1.strip())
        
        # 2. 찾을 책 제목 입력
        target_book = input().strip()
        
        # 3. 책 리스트 입력
        line3 = input()
        if not line3: return
        books = line3.split()
        
        # 선형 탐색 (Linear Search)
        # 파이썬 리스트의 index() 메서드를 활용하거나 반복문으로 찾을 수 있습니다.
        if target_book in books:
            # index는 0부터 시작하므로 +1 해줍니다.
            print(books.index(target_book) + 1)
        else:
            print("-1")
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()
