import sys

def main():
    try:
        # 한 줄의 명령어를 입력받습니다.
        line = input()
        if not line:
            return
            
        commands = line.split()
        x, y = 0, 0
        
        for cmd in commands:
            if cmd == 'U':
                y += 1
            elif cmd == 'D':
                y -= 1
            elif cmd == 'L':
                x -= 1
            elif cmd == 'R':
                x += 1
        
        # 최종 좌표 출력
        print(f"{x} {y}")
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()
