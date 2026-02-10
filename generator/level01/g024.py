import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P24 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P24")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 스카이라인과 레이더

## 문제 설명
미래 도시 **네오-서울**에는 일직선상에 다양한 높이의 빌딩들이 $N$개 서 있습니다.
각 빌딩의 옥상에는 **레이더 송신기**가 설치되어 있습니다. 이 레이더는 **왼쪽 방향**으로 수평 신호를 발사하여 데이터를 전송합니다.

레이더 신호는 수평으로 이동하다가, **발신한 빌딩보다 높이가 높은 첫 번째 빌딩**에 부딪히면 수신됩니다. 만약 신호가 도시 끝까지 이동하는 동안 더 높은 빌딩을 만나지 못하면, 그 신호는 수신되지 않고 사라집니다.

모든 빌딩이 동시에 왼쪽으로 신호를 발사할 때, 각 빌딩의 신호를 수신하는 빌딩의 번호를 구하는 프로그램을 작성하세요.

### 규칙
1. 빌딩의 높이는 모두 정수입니다.
2. 모든 빌딩은 왼쪽으로만 신호를 보냅니다.
3. 신호는 **발신한 빌딩보다 높이가 '높은'** 건물에만 수신됩니다. (높이가 같거나 낮은 건물은 통과합니다.)
4. 빌딩의 번호는 왼쪽부터 1번, 2번, ..., $N$번입니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 빌딩의 개수 $N$이 주어집니다. ($1 \\le N \\le 100,000$)
* 두 번째 줄에 각 빌딩의 높이를 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. (높이는 $1$ 이상 $100,000,000$ 이하)

## 출력 형식 (Output Format)
* 1번 빌딩부터 $N$번 빌딩까지 순서대로, 해당 빌딩의 신호를 수신하는 **빌딩의 번호**를 공백으로 구분하여 출력합니다.
* 수신하는 빌딩이 없다면 `0`을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
6 9 5 7 4
{TICK}

**Output:**
{TICK}
0 0 2 2 4
{TICK}

* **1번 빌딩(6):** 왼쪽에 건물이 없음 $\\rightarrow$ `0`
* **2번 빌딩(9):** 왼쪽의 1번(6)은 9보다 낮음 $\\rightarrow$ 수신 불가 $\\rightarrow$ `0`
* **3번 빌딩(5):** 왼쪽의 2번(9)이 5보다 높음 $\\rightarrow$ **2번 수신** $\\rightarrow$ `2`
* **4번 빌딩(7):** 왼쪽의 3번(5) 통과, 2번(9)이 7보다 높음 $\\rightarrow$ **2번 수신** $\\rightarrow$ `2`
* **5번 빌딩(4):** 왼쪽의 4번(7)이 4보다 높음 $\\rightarrow$ **4번 수신** $\\rightarrow$ `4`

### 예시 2
**Input:**
{TICK}
4
1 2 3 4
{TICK}

**Output:**
{TICK}
0 0 0 0
{TICK}
* 모든 빌딩이 자신보다 왼쪽 빌딩들보다 높기 때문에, 아무도 신호를 수신하지 못합니다. (오름차순)

"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    input = sys.stdin.readline
    
    # 입력 처리
    try:
        n_str = input().strip()
        if not n_str: return
        n = int(n_str)
        heights = list(map(int, input().split()))
    except ValueError:
        return

    stack = [] # (index, height) 튜플 저장
    result = []
    
    # 각 빌딩을 순서대로 확인 (1-based index 사용을 위해 i+1 저장)
    for i in range(n):
        current_height = heights[i]
        
        # 스택의 top이 현재 건물보다 낮거나 같으면 pop
        # (왜냐하면 현재 건물이 그들보다 오른쪽에서 가로막고 있으므로, 
        # 이후의 건물들은 pop되는 건물들을 볼 수 없음 + 현재 건물보다 낮아서 수신도 못함)
        while stack and stack[-1][1] <= current_height:
            stack.pop()
            
        if stack:
            # 스택에 남은 것이 있다면, 그것이 나보다 높은 가장 가까운 건물
            result.append(str(stack[-1][0]))
        else:
            # 스택이 비었다면 왼쪽에 나보다 높은 건물이 없음
            result.append("0")
            
        # 현재 건물을 스택에 추가
        stack.append((i + 1, current_height))

    print(" ".join(result))

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve_internal(n, heights):
    stack = []
    result = []
    for i in range(n):
        h = heights[i]
        while stack and stack[-1][1] <= h:
            stack.pop()
        
        if stack:
            result.append(str(stack[-1][0]))
        else:
            result.append("0")
        
        stack.append((i + 1, h))
    return " ".join(result)

# 수동 케이스
manual_cases = [
    ([6, 9, 5, 7, 4], "0 0 2 2 4"),
    ([1, 2, 3, 4, 5], "0 0 0 0 0"),
    ([5, 4, 3, 2, 1], "0 1 2 3 4"),
    ([10, 10, 10, 10], "0 0 0 0"), # 높이가 같은 경우 수신 불가
    ([3, 9, 9, 3, 5, 7], "0 0 0 3 3 3"), # 예외 케이스
    ([1, 5, 3, 6, 7, 6, 5], "0 0 2 0 0 5 6")
]

test_cases = []
for h_list, ans in manual_cases:
    inp = f"{len(h_list)}\n" + " ".join(map(str, h_list))
    test_cases.append((inp, ans))

# 랜덤 케이스 생성
for _ in range(14):
    n = random.randint(10, 1000) # 테스트용이라 N을 적당히 조절 (실제 문제는 10만)
    heights = [random.randint(1, 100000) for _ in range(n)]
    
    ans = solve_internal(n, heights)
    inp = f"{n}\n" + " ".join(map(str, heights))
    
    test_cases.append((inp, ans))

# 파일 저장
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P24' 문제 생성이 완료되었습니다.")