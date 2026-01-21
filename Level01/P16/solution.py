import sys

def solution():
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        weights = list(map(int, line))
    except EOFError:
        return

    stack = []
    for w in weights:
        # 새로운 상자(w)가 스택 맨 위 상자보다 무거우면 찌그러뜨림
        while stack and stack[-1] < w:
            stack.pop()
        stack.append(w)
    
    print(*(stack))

if __name__ == "__main__":
    solution()
