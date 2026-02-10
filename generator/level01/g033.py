import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P33 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P033")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 아마라의 고대 문자열 해독

## 문제 설명
나이지리아의 유능한 고고학자 **아마라**는 고대 유적지에서 수수께끼 같은 암호가 새겨진 돌판을 발견했습니다. 이 암호는 `3[a2[c]]`와 같이 숫자와 대괄호(`[]`)가 중첩된 독특한 규칙으로 압축되어 있습니다. 

해독 규칙은 **'k[문자열]'** 형태가 보이면 괄호 안의 **문자열**을 **k번** 반복하여 이어 붙이는 것입니다. 예를 들어, `2[bc]`는 `bcbc`가 되고, `3[a2[c]]`는 먼저 안쪽의 `2[c]`를 `cc`로 해석한 뒤, 전체 `3[acc]`를 해독하여 `accaccacc`라는 문장을 만들어내는 방식입니다.

아마라를 도와 이 압축된 고대 암호를 원래의 긴 문장으로 복원하는 프로그램을 작성하세요. 괄호는 여러 번 중첩될 수 있으며, 반복 횟수를 나타내는 숫자는 한 자릿수 이상일 수 있음에 유의해야 합니다.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 압축된 형태의 문자열이 주어집니다.
* 문자열의 길이는 $1$ 이상 $10,000$ 이하입니다.
* 반복 횟수 $k$는 $1$ 이상 $300$ 이하의 정수입니다.
* 문자열은 소문자, 숫자, 그리고 대괄호(`[`, `]`)로만 구성됩니다.

## 출력 형식 (Output Format)
* 해독이 완료된 최종 문자열을 한 줄로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3[a]2[bc]
{TICK}

**Output:**
{TICK}
aaabcbc
{TICK}

* `3[a]`는 `aaa`가 되고, `2[bc]`는 `bcbc`가 되어 이들을 합친 `aaabcbc`가 결과가 됩니다.

### 예시 2
**Input:**
{TICK}
3[a2[c]]
{TICK}

**Output:**
{TICK}
accaccacc
{TICK}

* `2[c]`를 해독하면 `cc`가 됩니다.
* `3[acc]`를 해독하면 `accaccacc`가 완성됩니다.

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

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
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

def generate_test_cases():
    cases = []
    # 샘플 케이스
    cases.append(("3[a]2[bc]", "aaabcbc"))
    cases.append(("3[a2[c]]", "accaccacc"))
    cases.append(("2[abc]3[cd]ef", "abcabccdcdef"))
    
    # 랜덤 케이스 생성
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(cases) + 1, 21):
        rep1 = random.randint(1, 4)
        char1 = random.choice(letters)
        rep2 = random.randint(1, 3)
        char2 = "".join(random.choices(letters, k=2))
        
        inp = f"{{rep1}}[{{char1}}{{rep2}}[{{char2}}]]"
        ans = (char1 + (char2 * rep2)) * rep1
        cases.append((inp, ans))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P033' 문제 생성이 완료되었습니다.")