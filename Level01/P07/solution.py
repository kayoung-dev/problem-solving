import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 재료 리스트 입력
    ingredients = list(map(int, input().split()))
    
    stack = []
    count = 0
    
    # 햄버거 레시피: 1 (빵) -> 2 (야채) -> 3 (고기) -> 1 (빵)
    # 스택에 쌓을 때는 [1, 2, 3, 1] 패턴을 찾아야 함
    
    for ingredient in ingredients:
        stack.append(ingredient)
        
        # 스택에 재료가 4개 이상 모였을 때 패턴 확인
        if len(stack) >= 4:
            # 스택의 끝 4개가 [1, 2, 3, 1] 인지 확인
            # (슬라이싱을 사용하면 코드가 간결해짐)
            if stack[-4:] == [1, 2, 3, 1]:
                count += 1
                # 4개 제거 (pop 4번)
                for _ in range(4):
                    stack.pop()
                
                # [최적화 팁]
                # Python에서는 del stack[-4:] 가 pop() 루프보다 조금 더 빠를 수 있음
                
    print(count)

if __name__ == "__main__":
    solve()
