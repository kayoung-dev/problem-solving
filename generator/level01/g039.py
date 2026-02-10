import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P39 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P039")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 파티마의 문서 태그 유효성 검사

## 문제 설명
모로코의 유능한 웹 요원 **파티마**는 네트워크를 통해 전송되는 수많은 문서 데이터의 무결성을 검사하는 임무를 맡고 있습니다. 파티마가 다루는 데이터는 HTML이나 XML과 유사하게 `<태그이름>`과 `</태그이름>`이 쌍을 이루어 정보를 감싸는 구조로 되어 있습니다. 

네트워크 소켓 프로그래밍을 공부 중인 케이트는 파티마를 도와 전송받은 문서의 태그들이 올바르게 중첩되고 닫혔는지 확인하는 프로그램을 작성하려고 합니다. 유효한 문서는 다음 규칙을 반드시 지켜야 합니다:

1.  모든 여는 태그(`<tag>`)는 반드시 그에 대응하는 닫는 태그(`</tag>`)와 짝을 이루어야 합니다.
2.  나중에 열린 태그가 먼저 닫혀야 하는 **스택(Stack)** 의 원칙($LIFO$)을 따라야 합니다. 즉, 태그의 중첩 순서가 올바라야 합니다. <br/>(예: `<a><b></b></a>`는 유효하지만, `<a><b></a></b>`는 유효하지 않습니다.)
3.  태그 내부의 문자열을 제외한 일반 텍스트는 태그의 유효성에 영향을 주지 않습니다.

주어진 문서 문자열에서 태그들의 쌍이 완벽하게 맞는지 판별하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 태그와 텍스트가 포함된 문자열 $S$가 주어집니다.
* 문자열의 길이는 $1$ 이상 $100,000$ 이하입니다.
* 태그는 알파벳 소문자로만 구성되며, `<`로 시작하여 `>`로 끝납니다. 닫는 태그는 `</`로 시작합니다.

## 출력 형식 (Output Format)
* 태그의 중첩과 짝이 올바르면 `VALID`, 그렇지 않으면 `INVALID`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
<p>Hello <b>World</b></p>
{TICK}

**Output:**
{TICK}
VALID
{TICK}

* `<p>`가 먼저 열리고 `<b>`가 열린 뒤, `</b>`가 먼저 닫히고 마지막에 `</p>`가 닫혔으므로 유효합니다.

### 예시 2
**Input:**
{TICK}
<div><span>Error</div></span>
{TICK}

**Output:**
{TICK}
INVALID
{TICK}

* `<span>`이 나중에 열렸으므로 `<div>`보다 먼저 닫혀야 하지만, `</div>`가 먼저 나타나 규칙을 위반했습니다.

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("VALID")
        return
        
    stack = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == '<':
            j = i
            while j < n and s[j] != '>':
                j += 1
            if j == n: # 닫히지 않은 태그
                print("INVALID")
                return
            
            tag_content = s[i+1:j]
            i = j + 1
            
            if tag_content.startswith('/'):
                # 닫는 태그인 경우
                tag_name = tag_content[1:]
                if not stack or stack[-1] != tag_name:
                    print("INVALID")
                    return
                stack.pop()
            else:
                # 여는 태그인 경우
                stack.append(tag_content)
        else:
            i += 1
            
    if not stack:
        print("VALID")
    else:
        print("INVALID")

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
    cases.append(("<p>Hello <b>World</b></p>", "VALID"))
    cases.append(("<div><span>Error</div></span>", "INVALID"))
    cases.append(("<root><item></item><item></item></root>", "VALID"))
    cases.append(("<tag>unclosed", "INVALID"))
    cases.append(("</no_opening>", "INVALID"))
    
    # 랜덤 케이스 생성
    tag_names = ["div", "span", "p", "a", "b", "i", "ul", "li"]
    for i in range(len(cases) + 1, 21):
        depth = random.randint(2, 5)
        stk = []
        path = []
        
        is_valid = random.choice([True, False])
        
        if is_valid:
            def build_valid(d):
                if d == 0: return ""
                t = random.choice(tag_names)
                return f"<{t}>" + build_valid(d-1) + f"</{t}>"
            inp = build_valid(depth)
            ans = "VALID"
        else:
            # 의도적 오류 생성
            t1 = random.choice(tag_names)
            t2 = random.choice([x for x in tag_names if x != t1])
            inp = f"<{t1}><{t2}></{t1}></{t2}>"
            ans = "INVALID"
            
        cases.append((inp, ans))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P039' 문제 생성이 완료되었습니다.")