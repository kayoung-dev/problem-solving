import sys
from collections import deque

def solve():
    # 데이터를 토큰 단위로 읽어오는 제너레이터
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    tokens = get_input()
    
    try:
        line = next(tokens)
        if not line: return
        n = int(line)
    except (StopIteration, ValueError):
        return

    bus = deque()

    for _ in range(n):
        try:
            cmd = next(tokens)
            if cmd == "F_IN":
                name = next(tokens)
                bus.appendleft(name)
            elif cmd == "B_IN":
                name = next(tokens)
                bus.append(name)
            elif cmd == "F_OUT":
                if bus:
                    bus.popleft()
            elif cmd == "B_OUT":
                if bus:
                    bus.pop()
        except StopIteration:
            break

    if not bus:
        print("EMPTY")
    else:
        print(" ".join(bus))

if __name__ == "__main__":
    solve()
