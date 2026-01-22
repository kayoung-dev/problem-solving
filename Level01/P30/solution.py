import sys

def solve():
    lines = sys.stdin.read().splitlines()
    in_stack = []
    out_stack = []
    total_weight = 0
    
    for line in lines:
        parts = line.split()
        if not parts: continue
        
        if parts[0] == 'IN':
            w = int(parts[1])
            in_stack.append(w)
            total_weight += w
        elif parts[0] == 'OUT':
            if not out_stack:
                while in_stack:
                    out_stack.append(in_stack.pop())
            
            if not out_stack:
                print("-1")
            else:
                popped = out_stack.pop()
                total_weight -= popped
                print(f"{popped} {total_weight}")

if __name__ == "__main__":
    solve()
