import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P38 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P38")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 첸의 대칭 구문 검사기

## 문제 설명
중국의 열정적인 언어학자 **첸**은 고대 문서에 기록된 문장들이 특별한 대칭 구조를 이루고 있는지 연구하고 있습니다. 첸이 찾는 대칭 구조란, 문장을 앞에서부터 읽으나 뒤에서부터 읽으나 똑같이 읽히는 **회문(Palindrome)** 구조를 말합니다. 

첸은 이 대칭성을 확인하기 위해 **스택(Stack)** 자료구조를 활용하기로 했습니다. 문장의 절반을 스택에 차례대로 넣었다가 하나씩 꺼내면서 나머지 절반과 비교하면, 스택의 '나중에 들어간 것이 먼저 나오는' 성질 덕분에 자연스럽게 역순으로 비교가 가능하기 때문입니다.

알파벳 소문자로만 구성된 문장이 주어질 때, 이 문장이 완벽한 대칭을 이루는지 판별하는 프로그램을 작성하세요. 예를 들어 `level`이나 `racecar`는 대칭이지만, `hello`는 대칭이 아닙니다.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 알파벳 소문자로만 구성된 문자열 $S$가 주어집니다.
* 문자열의 길이는 $1$ 이상 $100,000$ 이하입니다.

## 출력 형식 (Output Format)
* 주어진 문자열이 대칭(회문)이면 `YES`, 아니면 `NO`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
racecar
{TICK}

**Output:**
{TICK}
YES
{TICK}

* 앞에서부터 읽으나 뒤에서부터 읽으나 `racecar`로 동일합니다.

### 예시 2
**Input:**
{TICK}
banana
{TICK}

**Output:**
{TICK}
NO
{TICK}

* 뒤집으면 `ananab`가 되어 원래 문장과 다릅니다.

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
    # 문자열의 모든 문자를 스택에 푸시
    for char in s:
        stack.append(char)
        
    # 스택에서 하나씩 꺼내면(Pop) 문자열이 역순으로 나옴
    is_palindrome = True
    for char in s:
        if char != stack.pop():
            is_palindrome = False
            break
            
    if is_palindrome:
        print("YES")
    else:
        print("NO")

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
    # 샘플 및 기본 케이스
    cases.append(("racecar", "YES"))
    cases.append(("banana", "NO"))
    cases.append(("level", "YES"))
    cases.append(("a", "YES"))
    cases.append(("aa", "YES"))
    cases.append(("ab", "NO"))
    
    # 랜덤 케이스 생성
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(cases) + 1, 21):
        length = i * 500
        is_pal = random.choice([True, False])
        
        if is_pal:
            half = "".join(random.choices(letters, k=length))
            # 홀수/짝수 길이 랜덤 생성
            if random.random() > 0.5:
                inp = half + random.choice(letters) + half[::-1]
            else:
                inp = half + half[::-1]
            ans = "YES"
        else:
            inp = "".join(random.choices(letters, k=length * 2))
            # 운 좋게 YES가 나올 경우를 대비해 정답 시뮬레이션
            ans = "YES" if inp == inp[::-1] else "NO"
            
        cases.append((inp, ans))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P38' 문제 생성이 완료되었습니다.")