import sys

def solve():
    lines = sys.stdin.read().splitlines()
    pc = 0
    stack = []
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        opcode = parts[0]
        
        if opcode == 'CALL':
            target_addr = int(parts[1])
            # 복귀 주소 (PC + 1) 저장
            stack.append(pc + 1)
            pc = target_addr
            print(pc)
        elif opcode == 'RET':
            if not stack:
                print("STACK_ERROR")
                break
            # 스택에서 주소 복구
            pc = stack.pop()
            print(pc)

if __name__ == "__main__":
    solve()
