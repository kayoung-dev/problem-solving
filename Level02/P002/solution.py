import sys

def main():
    # 입력을 빠르게 받기 위해 sys.stdin 사용
    input = sys.stdin.readline
    
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 방문 기록을 저장할 스택
    history = []

    for _ in range(n):
        command_line = input().split()
        if not command_line:
            break
        
        cmd = command_line[0]

        if cmd == "visit":
            url = command_line[1]
            history.append(url)
            print(f"[V] {url}")

        elif cmd == "back":
            if history:
                history.pop() # 현재 페이지 삭제 (pop)
                if history:
                    # 이전 페이지가 남아있음
                    print(f"[B] {history[-1]}")
                else:
                    # 스택이 비었으므로 HOME
                    print("[B] HOME")
            else:
                # 이미 비어있음
                print("[B] IGNORED")

        elif cmd == "current":
            if history:
                print(history[-1])
            else:
                print("HOME")

if __name__ == "__main__":
    main()
