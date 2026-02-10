import os

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P47 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P047")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) 
# ---------------------------------------------------------
problem_template = r"""# 마법 구슬 공장의 원형 제거 공정

## 문제 설명
마법 구슬 공장의 공장장 **'루나'** 는 원형 컨베이어 벨트 위에 놓인 구슬들을 처리하고 있습니다. 벨트 위에는 알파벳 소문자가 적힌 구슬들이 일렬로 놓여 있으며, 벨트는 오직 한 방향으로만 움직입니다.

루나는 다음과 같은 **'큐 회전 규칙'** 에 따라 구슬을 제거합니다:
1. 벨트의 **맨 앞** 에 있는 두 개의 구슬을 확인합니다.
2. 만약 **맨 앞의 두 구슬이 서로 같은 알파벳**이라면, 두 구슬을 즉시 벨트에서 제거합니다.
3. 만약 **맨 앞의 두 구슬이 서로 다르다면**, 맨 앞에 있는 구슬 한 개를 꺼내어 벨트의 **맨 뒤** 로 보냅니다. (회전)
4. 벨트 위에 구슬이 $1$개 이하로 남거나, 더 이상 제거할 수 있는 짝이 없을 때까지 이 과정을 반복합니다.

벨트 위에 놓인 초기 구슬의 상태 $s$가 주어질 때, 최종적으로 벨트 위에 남게 되는 구슬의 개수를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
* 알파벳 소문자로만 이루어진 문자열 $s$가 주어집니다.
* 문자열 $s$의 길이는 $1$ 이상 $2,000$ 이하입니다.

## 출력 형식 (Output Format)
* 모든 공정이 끝난 후 컨베이어 벨트에 남아있는 구슬의 개수를 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
aabb
{TICK}

**Output:**
{TICK}
0
{TICK}

**설명:**
- `aa`가 맨 앞에 있으므로 제거 $\rightarrow$ `bb` 남음.
- `bb`가 맨 앞에 있으므로 제거 $\rightarrow$ 모두 제거됨. 결과는 0.

### 예시 2
**Input:**
{TICK}
abac
{TICK}

**Output:**
{TICK}
4
{TICK}

**설명:**
- `ab` 다름 $\rightarrow$ `a`를 뒤로 보냄: `baca`
- `ba` 다름 $\rightarrow$ `b`를 뒤로 보냄: `acab`
- `ac` 다름 $\rightarrow$ `a`를 뒤로 보냄: `caba`
- 한 바퀴를 돌아도 같은 짝이 맨 앞에 오지 않으므로 더 이상 제거 불가. 결과는 4.

### 예시 3
**Input:**
{TICK}
baaba
{TICK}

**Output:**
{TICK}
1
{TICK}

**설명:**
- `ba` 다름 $\rightarrow$ `b` 뒤로: `aabab`
- `aa` 같음 $\rightarrow$ 제거: `bab`
- `ba` 다름 $\rightarrow$ `b` 뒤로: `abb`
- `ab` 다름 $\rightarrow$ `a` 뒤로: `bba`
- `bb` 같음 $\rightarrow$ 제거: `a`
- 구슬이 1개 남았으므로 종료. 결과는 1.
"""

problem_md = problem_template.replace("{TICK}", TICK)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_content = """import sys
from collections import deque

def solve():
    s = sys.stdin.read().strip()
    if not s:
        print(0)
        return
    
    q = deque(list(s))
    
    # 더 이상 제거가 일어나지 않을 때까지 반복 (최대 회전 수 제한)
    changed = True
    while changed and len(q) >= 2:
        changed = False
        # 한 바퀴를 도는 동안 제거가 일어나는지 확인
        for _ in range(len(q)):
            if len(q) < 2: break
            
            if q[0] == q[1]:
                q.popleft()
                q.popleft()
                changed = True
                break # 제거되면 다시 처음부터 검사
            else:
                q.append(q.popleft()) # 회전
                
    print(len(q))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 20개 생성
# ---------------------------------------------------------
def solve_internal(s):
    from collections import deque
    q = deque(list(s))
    changed = True
    while changed and len(q) >= 2:
        changed = False
        for _ in range(len(q)):
            if len(q) < 2: break
            if q[0] == q[1]:
                q.popleft()
                q.popleft()
                changed = True
                break
            else:
                q.append(q.popleft())
    return str(len(q))

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_content)

# 20개의 테스트 데이터
test_inputs = [
    "aabb", "abac", "baaba", "abcde", "aaaa",
    "ababab", "aabccb", "abcba", "aaabbb", "abcdeedcba",
    "aabbcc", "abcdefgfedcba", "abab", "ccaa", "pqrst",
    "zzz", "aabbbbaa", "abccba", "aaaaa", "abcdef"
]

for i, s in enumerate(test_inputs, 1):
    ans = solve_internal(s)
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(s)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P047' 문제 생성이 완료되었습니다.")