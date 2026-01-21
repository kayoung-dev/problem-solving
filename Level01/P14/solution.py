import sys

def solution(s):
    stack = []
    current_str = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char
            
    return current_str

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    print(solution(input_data))
