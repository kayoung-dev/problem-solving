import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P04 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P04")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 올바른 괄호 (Valid Parentheses)

## 문제 설명
괄호가 바르게 짝지어졌다는 것은 `'('` 문자로 열렸으면 반드시 짝지어서 `')'` 문자로 닫혀야 한다는 뜻입니다.

예를 들어:
* `()()` 또는 `(())()` 는 올바른 괄호입니다.
* `)()` 또는 `(()(` 는 올바르지 않은 괄호입니다.

소괄호 `'('`와 `')'`로만 이루어진 문자열 `S`가 주어졌을 때, 이 문자열이 올바른 괄호 문자열인지 판단하는 프로그램을 작성하세요.
스택(Stack)을 활용하여 **열린 괄호는 쌓고, 닫힌 괄호는 짝을 맞춰 제거**하는 아이디어를 사용해 보세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 테스트 케이스의 개수 $T$가 주어집니다. ($1 \le T \le 100$)
* 두 번째 줄부터 $T$개의 줄에 걸쳐 괄호 문자열 $S$가 주어집니다.
    * 문자열 $S$의 길이는 2 이상 100,000 이하입니다.

## 출력 형식 (Output Format)
* 각 테스트 케이스마다 올바른 괄호 문자열이면 `YES`, 아니면 `NO`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
()()
(())()
)()(
{TICK}
**Output:**
{TICK}
YES
YES
NO
{TICK}

### 예시 2
**Input:**
{TICK}
2
(()(
((()))
{TICK}
**Output:**
{TICK}
NO
YES
{TICK}
* 첫 번째 케이스는 마지막에 괄호가 닫히지 않고 열린 채 끝났으므로 `NO`입니다.
* 두 번째 케이스는 3쌍의 괄호가 완벽하게 중첩되어 있으므로 `YES`입니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def is_valid_parenthesis(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else: # char == ')'
            if not stack:
                return False
            stack.pop()
    
    # 순회가 끝났을 때 스택이 비어있어야 올바른 괄호
    return len(stack) == 0

def main():
    input = sys.stdin.readline
    
    try:
        t_str = input().strip()
        if not t_str:
            return
        t = int(t_str)
    except ValueError:
        return

    for _ in range(t):
        s = input().strip()
        if is_valid_parenthesis(s):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 내부 정답 로직 (테스트케이스 생성용)
def solve_internal(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

# 랜덤 괄호 생성 함수
def generate_random_parentheses(length, balanced_probability=0.5):
    # 50% 확률로 의도적인 정답(Balanced) 생성
    if random.random() < balanced_probability:
        if length % 2 != 0: length += 1 # 짝수 길이 보장
        
        # 셔플 방식으로는 올바른 괄호 만들기 어려움 -> 생성 로직
        # 간단하게: 랜덤한 위치에 삽입하거나 감싸기 (재귀적 or 반복적)
        # 여기서는 단순하게: 올바른 괄호 리스트를 만들고 합치는 방식 등을 섞음
        temp_stack = []
        result = []
        # 절반은 열고 절반은 닫으면 될 것 같지만 순서가 중요함
        # 가장 쉬운 방법: 카탈란 수 생성기 대신, 유효한 괄호 생성 알고리즘 사용
        
        # 검증된 생성법:
        # 열린 괄호 남은 개수(open_rem), 닫힌 괄호 남은 개수(close_rem) 추적
        def generate(p, left, right, parens=[]):
            if left: generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right: parens.append(p)
            return parens
        
        # 길이가 길면 위 재귀는 비효율적 -> 랜덤 워크 방식
        # 0부터 시작, +1('('), -1(')'), 음수 안됨, 마지막에 0
        current_balance = 0
        s_list = []
        # 절반은 '(', 절반은 ')'
        half = length // 2
        opens = half
        closes = half
        
        while opens > 0 or closes > 0:
            # 닫을 수 있는 상황: balance > 0
            can_close = (current_balance > 0) and (closes > 0)
            # 열 수 있는 상황: opens > 0. 단, 남은 공간이 최소 닫을 횟수보다 많아야 함(안전하게)
            # 여기선 간단히 opens가 있으면 열 수 있다고 가정하되, 마지막에 0이 되도록 유도
            
            # 랜덤 선택 (열기 vs 닫기)
            # 닫아야만 하는 상황: 남은 칸 == 현재 밸런스 (모두 닫아야 0됨)
            if (opens + closes) == current_balance:
                s_list.append(')')
                closes -= 1
                current_balance -= 1
            elif opens == 0:
                s_list.append(')')
                closes -= 1
                current_balance -= 1
            elif not can_close:
                s_list.append('(')
                opens -= 1
                current_balance += 1
            else:
                if random.random() < 0.5:
                    s_list.append('(')
                    opens -= 1
                    current_balance += 1
                else:
                    s_list.append(')')
                    closes -= 1
                    current_balance -= 1
        return "".join(s_list)
        
    else:
        # 무작위 생성 (오답일 확률 높음)
        s_list = [random.choice(['(', ')']) for _ in range(length)]
        return "".join(s_list)

# 테스트 케이스 20개 생성
for i in range(1, 21):
    t = random.randint(5, 15) # 한 파일당 테스트 케이스 수
    inputs = []
    outputs = []
    
    inputs.append(str(t))
    
    for _ in range(t):
        length = random.randint(2, 50) * 2 # 짝수로 길이 설정 (4 ~ 100)
        s = generate_random_parentheses(length, balanced_probability=0.5)
        inputs.append(s)
        outputs.append(solve_internal(s))
    
    input_str = "\n".join(inputs)
    output_str = "\n".join(outputs)
    
    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print(f"✅ 'Level01/P04' 생성이 완료되었습니다.")