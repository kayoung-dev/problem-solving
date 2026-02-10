import sys

def solution():
    # 문자열 읽기
    try:
        source = sys.stdin.readline().strip()
        target = sys.stdin.readline().strip()
    except:
        return

    if not source or not target:
        return

    stack = []
    result = []
    
    source_idx = 0
    target_idx = 0
    n = len(source)
    
    # target 문자열을 하나씩 완성해 나감
    while target_idx < n:
        target_char = target[target_idx]
        
        # 1. 스택의 Top이 찾는 문자와 같다면 -> Pop (건조)
        if stack and stack[-1] == target_char:
            stack.pop()
            result.append('1')
            target_idx += 1
        
        # 2. 스택의 Top이 다르다면 -> 찾는 문자가 나올 때까지 Push (세척)
        elif source_idx < n:
            stack.append(source[source_idx])
            result.append('0')
            source_idx += 1
            
        # 3. 더 이상 Push할 것도 없고, 스택 Top도 다르다면 -> 불가능
        else:
            print("impossible")
            return
            
    print("".join(result))

if __name__ == "__main__":
    solution()
