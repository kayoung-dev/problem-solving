def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    # 출력할 때도 str()로 변환하여 출력하는 것이 안전함
    print(solution(input_data))
