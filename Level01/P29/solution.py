import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    stack = []
    for val in map(int, data):
        if val == 0:
            if stack:
                stack.pop()
        else:
            stack.append(val)
            
    print(sum(stack))

if __name__ == "__main__":
    solve()
