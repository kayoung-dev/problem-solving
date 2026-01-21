import sys

def get_priority(op):
    if op == '(' or op == ')': return 0
    if op == '+' or op == '-': return 1
    if op == '*' or op == '/': return 2
    return -1

def solution(s):
    stack = []
    result = ""
    
    for char in s:
        if char.isalpha():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and get_priority(stack[-1]) >= get_priority(char):
                result += stack.pop()
            stack.append(char)
            
    while stack:
        result += stack.pop()
        
    return result

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    print(solution(input_data))
