import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P37 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P037")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 라르스의 버전 관리 언두 시스템

## 문제 설명
스웨덴의 소프트웨어 엔지니어 **라르스**는 텍스트 편집기의 핵심 기능인 '작업 취소(Undo)'와 '다시 실행(Redo)' 시스템을 개발하고 있습니다. 라르스는 이 기능을 구현하기 위해 두 개의 스택을 사용하는 아키텍처를 설계했습니다.

작동 규칙은 다음과 같습니다:
1.  **`TYPE X`**: 문서의 맨 뒤에 문자열 **X**를 추가합니다. 이 작업은 **Undo 스택**에 저장되며, 새로운 글자를 타이핑했으므로 **Redo 스택은 즉시 모두 비워집니다.**
2.  **`UNDO`**: 가장 최근에 추가한 문자열 작업을 취소합니다. 취소된 문자열은 **Undo 스택**에서 꺼내 **Redo 스택**으로 옮깁니다. 만약 Undo 스택이 비어 있다면 아무 일도 일어나지 않습니다.
3.  **`REDO`**: 가장 최근에 취소했던 작업을 다시 복구합니다. 문자열을 **Redo 스택**에서 꺼내 다시 **Undo 스택**으로 옮깁니다. 만약 Redo 스택이 비어 있다면 아무 일도 일어나지 않습니다.



소프트웨어 아키텍처에 관심이 많은 케이트를 도와, 모든 편집 명령이 끝난 후 최종적으로 문서에 남아있는 문자열이 무엇인지 출력하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄부터 편집 명령어가 한 줄에 하나씩 주어집니다.
* 명령어의 총 개수 $N$은 $1$ 이상 $100,000$ 이하입니다.
* `TYPE X`에서 **X**는 공백이 없는 알파벳 소문자 문자열(길이 $1$~$10$)입니다.

## 출력 형식 (Output Format)
* 모든 명령을 수행한 후, 최종적으로 완성된 문서의 전체 내용을 한 줄로 출력합니다.
* 만약 문서가 완전히 비어 있다면 빈 줄을 출력하거나 아무것도 출력하지 않습니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
TYPE apple
TYPE banana
UNDO
REDO
TYPE cherry
{TICK}

**Output:**
{TICK}
applebananacherry
{TICK}

* `TYPE apple`, `TYPE banana`: 문서 상태는 `applebanana`입니다.
* `UNDO`: `banana`를 취소하여 `apple`이 됩니다. (Redo 스택에 `banana` 보관)
* `REDO`: 취소했던 `banana`를 복구하여 다시 `applebanana`가 됩니다.
* `TYPE cherry`: 새로운 입력을 하면 Redo 스택이 비워지고 `applebananacherry`가 됩니다.

### 예시 2
**Input:**
{TICK}
TYPE code
UNDO
UNDO
REDO
{TICK}

**Output:**
{TICK}
code
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    lines = sys.stdin.read().splitlines()
    
    undo_stack = []
    redo_stack = []
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        cmd = parts[0]
        
        if cmd == 'TYPE':
            word = parts[1]
            undo_stack.append(word)
            # 새로운 입력 발생 시 Redo 이력은 삭제됨
            redo_stack = []
            
        elif cmd == 'UNDO':
            if undo_stack:
                popped = undo_stack.pop()
                redo_stack.append(popped)
                
        elif cmd == 'REDO':
            if redo_stack:
                popped = redo_stack.pop()
                undo_stack.append(popped)
                
    # 최종 결과는 Undo 스택에 남아있는 문자열들을 순서대로 합친 것
    print("".join(undo_stack))

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
    cases.append(("TYPE apple\\nTYPE banana\\nUNDO\\nREDO\\nTYPE cherry", "applebananacherry"))
    cases.append(("TYPE code\\nUNDO\\nUNDO\\nREDO", "code"))
    
    # 랜덤 케이스
    words = ["hi", "dev", "stack", "data", "link", "node", "cpu"]
    for i in range(len(cases) + 1, 21):
        num_cmds = i * 500
        cmds = []
        u_sim = []
        r_sim = []
        
        for _ in range(num_cmds):
            rand = random.random()
            if rand < 0.6: # TYPE
                w = random.choice(words)
                cmds.append(f"TYPE {{w}}")
                u_sim.append(w)
                r_sim = []
            elif rand < 0.8: # UNDO
                cmds.append("UNDO")
                if u_sim:
                    r_sim.append(u_sim.pop())
            else: # REDO
                cmds.append("REDO")
                if r_sim:
                    u_sim.append(r_sim.pop())
                    
        cases.append(("\\n".join(cmds), "".join(u_sim)))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    real_inp = inp.replace("\\\\n", "\\n").replace("\\n", "\n")
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(real_inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P037' 문제 생성이 완료되었습니다.")