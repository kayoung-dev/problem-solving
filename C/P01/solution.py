import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    stack = []
    results = []
    
    idx = 1
    for _ in range(q):
        op = int(input_data[idx])
        if op == 1:
            x = int(input_data[idx+1])
            stack.append(x)
            idx += 2
        else:
            if not stack:
                results.append("-1")
            else:
                results.append(str(stack.pop()))
            idx += 1
            
    if results:
        print("\n".join(results))

if __name__ == "__main__":
    main()
