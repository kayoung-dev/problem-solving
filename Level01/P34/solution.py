import sys

def solve():
    path = sys.stdin.read().strip()
    if not path:
        return
        
    # 슬래시를 기준으로 경로 성분을 나눔
    parts = path.split('/')
    stack = []
    
    for part in parts:
        # 빈 문자열(연속 슬래시)이나 '.'은 무시
        if part == '' or part == '.':
            continue
        # '..'인 경우 상위 디렉토리로 이동 (스택에서 제거)
        elif part == '..':
            if stack:
                stack.pop()
        # 일반 폴더 이름인 경우 스택에 추가
        else:
            stack.append(part)
            
    # 정규 경로 형식으로 조립
    print("/" + "/".join(stack))

if __name__ == "__main__":
    solve()
