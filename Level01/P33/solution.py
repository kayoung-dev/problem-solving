import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
        
    stack = []
    current_num = 0
    current_str = ''
    
    for char in s:
        if char.isdigit():
            # 숫자가 여러 자릿수일 수 있으므로 누적 계산
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # 지금까지의 문자열과 반복 횟수를 스택에 저장
            stack.append(current_str)
            stack.append(current_num)
            # 새로운 구간 시작을 위해 초기화
            current_str = ''
            current_num = 0
        elif char == ']':
            # 닫는 괄호에서 직전 상태 복구
            num = stack.pop()
            prev_str = stack.pop()
            # 현재 구간을 반복 횟수만큼 곱한 뒤 이전 문자열에 병합
            current_str = prev_str + (num * current_str)
        else:
            # 일반 문자일 경우 현재 문자열에 추가
            current_str += char
            
    print(current_str)

if __name__ == "__main__":
    solve()
