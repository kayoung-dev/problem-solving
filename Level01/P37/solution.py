import sys

def solve():
    lines = sys.stdin.read().splitlines()
    
    undo_stack = []
    redo_stack = []
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        cmd = parts[0]
        
        if cmd == 'TYPE':
            word = parts[1]
            undo_stack.append(word)
            # 새로운 입력 발생 시 Redo 이력은 삭제됨
            redo_stack = []
            
        elif cmd == 'UNDO':
            if undo_stack:
                popped = undo_stack.pop()
                redo_stack.append(popped)
                
        elif cmd == 'REDO':
            if redo_stack:
                popped = redo_stack.pop()
                undo_stack.append(popped)
                
    # 최종 결과는 Undo 스택에 남아있는 문자열들을 순서대로 합친 것
    print("".join(undo_stack))

if __name__ == "__main__":
    solve()
