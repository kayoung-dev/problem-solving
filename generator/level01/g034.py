import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P34 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P34")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3
# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 우주 정거장 파일 경로 정제

## 문제 설명
스페인의 우주 비행사 **소피아**는 국제 우주 정거장(ISS)의 메인 컴퓨터 시스템을 점검하고 있습니다. 이 시스템은 파일 경로가 매우 복잡하게 꼬여 있어 관리하기가 어렵습니다.

소피아는 복잡하게 표시된 '절대 경로'를 가장 단순한 형태인 '정규 경로(Canonical Path)'로 변환하려고 합니다. 정규 경로는 다음과 같은 규칙을 따릅니다:

1.  경로는 항상 슬래시(`/`)로 시작합니다.
2.  두 개 이상의 연속된 슬래시는 하나로 취급합니다. (예: `//` $\\rightarrow$ `/`)
3.  `.`은 현재 디렉토리를 의미하므로 경로에서 무시합니다.
4.  `..`은 상위 디렉토리로 이동함을 의미합니다. 만약 상위 디렉토리가 없다면 루트(`/`)에 머뭅니다.
5.  경로의 맨 마지막에는 슬래시가 포함되지 않습니다. (단, 루트 경로인 경우는 `/`로 표시합니다.)

소피아를 도와 복잡한 입력 경로를 깔끔한 정규 경로로 정리하는 프로그램을 작성하세요.



---
## 입력 형식 (Input Format)
* 첫 번째 줄에 정제되지 않은 절대 경로 문자열이 주어집니다.
* 문자열의 길이는 $1$ 이상 $3,000$ 이하입니다.
* 문자열은 영문 소문자, 숫자, 슬래시(`/`), 점(`.`)으로만 구성됩니다.

## 출력 형식 (Output Format)
* 정제된 정규 경로를 한 줄로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
/home//foo/
{TICK}

**Output:**
{TICK}
/home/foo
{TICK}

* 연속된 슬래시와 마지막 슬래시가 제거되어 `/home/foo`가 됩니다.

### 예시 2
**Input:**
{TICK}
/a/./b/../../c/
{TICK}

**Output:**
{TICK}
/c
{TICK}

* `/a/` 이동 $\\rightarrow$ `/a/./` (현재 위치 유지)
* `/a/b/` 이동 $\\rightarrow$ `/a/b/../` (상위인 `/a`로 이동)
* `/a/../` (상위인 `/`로 이동) $\\rightarrow$ `/c/` 이동
* 최종 결과는 **/c**입니다.

---
## 힌트
이 문제는 슬래시(`/`)를 기준으로 문자열을 분리한 뒤, 각 단어를 차례대로 처리하며 **스택(Stack)** 에 담는 것이 핵심입니다. 일반적인 폴더 이름은 스택에 넣고, `..`이 나오면 스택에서 가장 최근에 넣은 폴더를 꺼내는(`pop`) 논리를 적용해 보세요.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    path = sys.stdin.read().strip()
    if not path:
        return
        
    # 슬래시를 기준으로 경로 성분을 나눔
    parts = path.split('/')
    stack = []
    
    for part in parts:
        # 빈 문자열(연속 슬래시)이나 '.'은 무시
        if part == '' or part == '.':
            continue
        # '..'인 경우 상위 디렉토리로 이동 (스택에서 제거)
        elif part == '..':
            if stack:
                stack.pop()
        # 일반 폴더 이름인 경우 스택에 추가
        else:
            stack.append(part)
            
    # 정규 경로 형식으로 조립
    print("/" + "/".join(stack))

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
    cases.append(("/home//foo/", "/home/foo"))
    cases.append(("/a/./b/../../c/", "/c"))
    cases.append(("/../", "/"))
    cases.append(("/home/../../..", "/"))
    
    # 랜덤 케이스
    folders = ["usr", "bin", "etc", "var", "tmp", "local", "lib"]
    for i in range(len(cases) + 1, 21):
        depth = random.randint(3, 8)
        path_list = [""]
        sim_stack = []
        
        for _ in range(depth):
            r = random.random()
            if r < 0.2: # ..
                path_list.append("..")
                if sim_stack: sim_stack.pop()
            elif r < 0.3: # .
                path_list.append(".")
            elif r < 0.4: # empty (double slash)
                path_list.append("")
            else: # folder
                f = random.choice(folders) + str(random.randint(1, 9))
                path_list.append(f)
                sim_stack.append(f)
        
        inp = "/".join(path_list)
        if not inp.startswith("/"): inp = "/" + inp
        ans = "/" + "/".join(sim_stack)
        cases.append((inp, ans))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P34' 문제 생성이 완료되었습니다.")