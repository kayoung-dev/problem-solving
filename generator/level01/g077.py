import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P077 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P077")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 그래픽 보드 픽셀 패턴 복원

## 문제 설명
디자인 동아리의 **정호**는 $M$ 길이의 '패턴 스탬프'를 사용해 $N$ 길이의 '목표 픽셀 배열'을 완성했습니다. 

처음에 도화지는 모든 칸이 비어 있는 상태($?$)였습니다. 정호는 스탬프를 도화지의 특정 위치에 찍어 무늬를 만들어 나갔습니다. 스탬프를 찍으면 해당 구간의 기존 내용은 스탬프의 무늬로 완전히 덮어씌워집니다. 스탬프는 반드시 도화지의 경계 안($0 \le i \le N-M$)에 완전히 들어오게 찍어야 합니다.

목표 배열을 만들기 위해 정호가 스탬프를 찍었던 **위치(인덱스)들의 순서**를 찾아내는 프로그램을 작성하세요. 단, 여러 가지 방법이 있다면 **가장 적은 횟수로 스탬프를 찍는 순서**를 출력해야 합니다. 만약 최소 횟수가 같은 방법이 여러 개라면 그중 아무거나 하나를 출력합니다.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 패턴 스탬프 문자열 $S$가 주어집니다. 
- $2 \le |S| \le 5$
- 두 번째 줄에 목표 픽셀 배열 문자열 $T$가 주어집니다. 
- $|S| \le |T| \le 15$
- 모든 문자열은 영문 소문자로만 구성됩니다.

## 출력 형식 (Output Format)
- 스탬프를 찍은 **최소 횟수**의 위치들을 **첫 번째 작업부터 마지막 작업까지** 순서대로 공백으로 구분하여 한 줄에 출력합니다.
- 만약 어떤 방법으로도 목표 배열을 만들 수 없다면 `FAILED`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
abc
ababc
{TICK}

**Output:**
{TICK}
0 2
{TICK}

- 초기 상태: `?????`
- **방법 A (2회)** 
  - `0`번 위치에 찍기(`abc??`)
  - `2`번 위치에 찍기(`ababc`). **성공!**
- **방법 B (3회)** 
  - `1`번 위치(`?abc?`)
  - `0`번 위치(`abcbc`)
  - `2`번 위치(`ababc`). **성공!**
- 2회가 최소 횟수이므로 `0 2`만 정답으로 인정됩니다.

### 예시 2 
**Input:**
{TICK}
aba
ababa
{TICK}

**Output:**
{TICK}
0 2
{TICK}

- **목표 상태:** `ababa` (길이 5), **스탬프:** `aba` (길이 3)
- **방법 A ($0 \to 2$ 순서):**
    - $0$번 위치에 찍기: `aba??` (인덱스 0, 1, 2가 `a, b, a`가 됨)
    - $2$번 위치에 찍기: `ababa` (인덱스 2, 3, 4가 `a, b, a`로 덮어씌워짐. 인덱스 2는 원래 `a`였으므로 결과 유지)
- **방법 B ($2 \to 0$ 순서):**
    - $2$번 위치에 찍기: `??aba` (인덱스 2, 3, 4가 `a, b, a`가 됨)
    - $0$번 위치에 찍기: `ababa` (인덱스 0, 1, 2가 `a, b, a`로 덮어씌워짐. 인덱스 2는 원래 `a`였으므로 결과 유지)
- 두 방법 모두 **최소 횟수 2회**를 만족하며 최종 결과가 동일하므로, `0 2` 또는 `2 0` 중 어떤 것을 출력해도 정답입니다.

### 예시 3
**Input:**
{TICK}
abc
abac
{TICK}

**Output:**
{TICK}
FAILED
{TICK}
"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys
from collections import deque

input = sys.stdin.readline

def solve():
    stamp = input().strip()
    target = input().strip()
    if not stamp or not target: return
    
    m, n = len(stamp), len(target)
    goal = "?" * n
    
    # 목표에서 시작하여 초기상태로 가는 최단 경로 탐색
    queue = deque([(target, [])])
    visited = {target}
    
    while queue:
        curr, path = queue.popleft()
        
        if curr == goal:
            # 역순 탐색이므로 결과를 뒤집어서 출력
            print(*(path[::-1]))
            return
            
        for i in range(n - m + 1):
            match = True
            has_val = False
            temp = list(curr)
            
            for j in range(m):
                if curr[i+j] == '?': continue
                if curr[i+j] == stamp[j]:
                    has_val = True
                    temp[i+j] = '?'
                else:
                    match = False
                    break
            
            if match and has_val:
                nxt = "".join(temp)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [i]))
                    
    print("FAILED")

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (모든 정답 기록)
# ---------------------------------------------------------
def get_all_solutions(stamp, target):
    m, n = len(stamp), len(target)
    goal = "?" * n
    queue = deque([(target, [])])
    visited = {target: 0}
    min_dist = float('inf')
    all_paths = []
    
    while queue:
        curr, path = queue.popleft()
        if len(path) > min_dist: break
        
        if curr == goal:
            min_dist = len(path)
            all_paths.append(" ".join(map(str, path[::-1])))
            continue
            
        for i in range(n - m + 1):
            match, has_val = True, False
            temp = list(curr)
            for j in range(m):
                if curr[i+j] == '?': continue
                if curr[i+j] == stamp[j]:
                    has_val, temp[i+j] = True, '?'
                else:
                    match = False
                    break
            if match and has_val:
                nxt = "".join(temp)
                if nxt not in visited or visited[nxt] == len(path) + 1:
                    visited[nxt] = len(path) + 1
                    queue.append((nxt, path + [i]))
    
    if not all_paths: return ["FAILED"]
    return sorted(list(set(all_paths)))

test_data = [
    ("abc", "ababc"),
    ("aba", "ababa"),
    ("abc", "abac")
]

for _ in range(17):
    m_len, n_len = random.randint(2, 3), random.randint(5, 12)
    s = "".join(random.choice("abc") for _ in range(m_len))
    base = ["?"] * n_len
    for _ in range(random.randint(3, 5)):
        idx = random.randint(0, n_len - m_len)
        for j in range(m_len): base[idx+j] = s[j]
    t = "".join(base).replace("?", random.choice("abc"))
    test_data.append((s, t))

for i, (s, t) in enumerate(test_data, 1):
    input_str = f"{s}\n{t}"
    ans_list = get_all_solutions(s, t)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        # 모든 가능한 최단 경로 정답을 여러 줄에 걸쳐 저장
        f.write("\n".join(ans_list))

print(f"✅ 'Level01/P077' 문제 생성이 완료되었습니다. ")