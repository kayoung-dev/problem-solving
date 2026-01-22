import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P28 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P28")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 심해 탐사선의 신호 차단 분석

## 문제 설명
심해 탐사선 **울릉1호**는 해저 지형을 조사하기 위해 오른쪽 방향으로 연속해서 음파 신호를 쏩니다. 각 신호는 고유한 세기(Intensity)를 가지고 있으며, 발사된 신호는 장애물을 만나기 전까지 오른쪽으로 계속 나아갑니다.

이때, 어떤 신호의 진행을 막는 **장애물**이란, 그 신호보다 **세기가 더 강한(값이 큰) 신호**를 의미합니다. 모든 신호는 발사된 직후 오른쪽으로 날아가다가, 자신보다 강한 신호를 처음 만나는 순간 그 신호에 부딪혀 소멸합니다.

예를 들어, 발사된 신호들의 세기가 `[10, 3, 7, 12]` 라면:
1. **1번 신호 (10)**: 오른쪽으로 날아가다 2번 (3), 3번 (7)은 가뿐히 지나치지만, 자신보다 강한 **4번 신호 (12)** 를 만나면 부딪혀 소멸합니다.
2. **2번 신호 (3)**: 오른쪽으로 가자마자 자신보다 강한 **3번 신호 (7)** 를 만나서 곧바로 소멸합니다.
3. **3번 신호 (7)**: 오른쪽으로 가다가 자신보다 강한 **4번 신호 (12)** 를 만나 소멸합니다.
4. **4번 신호 (12)**: 오른쪽을 봐도 자신보다 강한 신호가 없으므로, 아무것도 부딪히지 않고 끝까지 나아갑니다.

각 신호가 발사되었을 때, 이 신호의 진행을 막아 소멸시키는 **첫 번째 신호의 번호** 가 무엇인지 구하는 프로그램을 작성하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
10 3 7 12
{TICK}

**Output:**
{TICK}
4 3 4 0
{TICK}

* 1번 (10)은 4번 (12)에 막힙니다. $\\rightarrow$ **4**
* 2번 (3)은 3번 (7)에 막힙니다. $\\rightarrow$ **3**
* 3번 (7)은 4번 (12)에 막힙니다. $\\rightarrow$ **4**
* 4번 (12)은 막는 신호가 없습니다. $\\rightarrow$ **0**


### 예시 2
**Input:**
{TICK}
20 15 10 5
{TICK}

**Output:**
{TICK}
0 0 0 0
{TICK}

* 모든 신호가 오른쪽으로 갈수록 약해집니다. 즉, 뒤에 오는 어떤 신호도 앞선 신호보다 강하지 않으므로 아무도 가로막히지 않습니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    # 문자열을 읽어 정수 리스트로 변환
    data = sys.stdin.read().split()
    if not data:
        return
    
    intensities = list(map(int, data))
    n = len(intensities)
    result = [0] * n
    stack = [] # 아직 자신을 막을 장벽을 찾지 못한 신호들의 인덱스

    for i in range(n):
        # 현재 신호(i)가 스택에 대기 중인 신호들보다 강하다면, 
        # 현재 신호가 그들의 진행을 가로막는 '첫 번째 장벽'이 됨
        while stack and intensities[stack[-1]] < intensities[i]:
            target_idx = stack.pop()
            result[target_idx] = i + 1 # 신호 번호는 1부터 시작
        
        # 현재 신호도 누군가에게 막힐 때까지 대기하기 위해 스택에 추가
        stack.append(i)
    
    print(*(result))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 및 파일 저장
# ---------------------------------------------------------
def generate_test_cases():
    cases = []
    # 1-4: 고정 예제 및 엣지 케이스
    cases.append(("10 3 7 12", "4 3 4 0"))
    cases.append(("20 15 10 5", "0 0 0 0"))
    cases.append(("5 10 15 20", "2 3 4 0"))
    cases.append(("100", "0"))
    
    # 5-20: 다양한 패턴의 랜덤 케이스
    for i in range(5, 21):
        size = i * 200 # 데이터 크기 점진적 증가
        # 일부러 오름차순, 내림차순, 지그재그 섞어서 생성
        pattern_type = i % 3
        if pattern_type == 0: # 오름차순 경향
            nums = sorted([random.randint(1, 10**6) for _ in range(size)])
        elif pattern_type == 1: # 내림차순 경향
            nums = sorted([random.randint(1, 10**6) for _ in range(size)], reverse=True)
        else: # 완전 랜덤
            nums = [random.randint(1, 10**6) for _ in range(size)]
        
        # 정답 계산 (O(N) 모노토닉 스택)
        ans = [0] * size
        stk = []
        for curr in range(size):
            while stk and nums[stk[-1]] < nums[curr]:
                prev = stk.pop()
                ans[prev] = curr + 1
            stk.append(curr)
        
        cases.append((" ".join(map(str, nums)), " ".join(map(str, ans))))
    return cases

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    in_file = os.path.join(test_dir, f"input_{i:02d}.in")
    out_file = os.path.join(test_dir, f"output_{i:02d}.out")
    with open(in_file, "w", encoding="utf-8") as f:
        f.write(inp)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P28' 문제 생성이 완료되었습니다.")