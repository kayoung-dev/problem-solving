import os
import random
from collections import deque

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P75 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P75")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_template = r"""# 동아리방 점유권 끝장 토론

## 문제 설명
캠퍼스에 새로 지어진 아주 멋진 동아리방이 하나 있습니다. 이 방을 차지하기 위해 **'푸른 파도'** 동아리와 **'붉은 열정'** 동아리가 끝장 토론을 벌이기로 했습니다. 

두 동아리의 부원들이 일렬로 서서 순서대로 발언권을 얻으며, 토론은 다음과 같은 규칙으로 진행됩니다.

1. **상대방 설득** 
    - 자신의 차례가 된 부원은 상대 동아리 부원 중 한 명을 지목하여 토론장에서 퇴장시킬 수 있습니다. 퇴장당한 부원은 이번 토론은 물론, 앞으로의 모든 토론 순서에서 제외됩니다.
2. **다음 라운드 진출** 
    - 상대방을 퇴장시킨 부원은 이번 차례를 마치고 다시 자신의 동아리 줄 맨 뒤로 가서 다음 발언 기회를 기다립니다.
3. **승리 선언** 
    - 자신의 차례에 토론장에 남은 사람들이 모두 자신의 동아리 부원들뿐이라면, 즉시 토론을 종료하고 동아리방 점유권을 획득합니다.

모든 부원은 자기 동아리의 승리를 위해 가장 전략적으로 행동합니다. 즉, 자신의 차례가 오면 아직 퇴장당하지 않은 상대 동아리 부원 중 **가장 먼저 발언권이 돌아올 사람**을 지목하여 퇴장시킵니다.

부원들이 줄을 서 있는 초기 순서가 주어질 때, 최종적으로 어느 동아리가 동아리방을 차지하게 될지 예측하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 토론에 참여하는 총 부원 수 $N$이 주어집니다. ($1 \le N \le 10,000$)
- 두 번째 줄에 부원들의 소속을 나타내는 길이 $N$의 문자열이 주어집니다.
    - `B`: 푸른 파도 (Blue Wave) 소속 부원
    - `R`: 붉은 열정 (Red Passion) 소속 부원

## 출력 형식 (Output Format)
- 최종 승리한 동아리의 이름을 출력합니다. 
    - 푸른 파도가 승리하면 `Blue Wave`
    - 붉은 열정이 승리하면 `Red Passion`

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
BBRRR
{TICK}

**Output:**
{TICK}
Blue Wave
{TICK}

- 초기 순서: $[B_1, B_2, R_1, R_2, R_3]$ 
- **$B_1$의 차례** 
  - 가장 먼저 발언할 상대인 $R_1$을 퇴장시킵니다. 
  - $B_1$은 줄 맨 뒤로 갑니다.
  - 남은 인원: $B_2, R_2, R_3, B_1$
- **$B_2$의 차례** 
  - 다음 상대인 $R_2$를 퇴장시킵니다. $B_2$는 줄 맨 뒤로 갑니다.
  - 남은 인원: $R_3, B_1, B_2$
- **$R_3$의 차례** 
  - 현재 남은 상대 중 가장 순서가 빠른 $B_1$을 퇴장시킵니다. 
  - $R_3$은 줄 맨 뒤로 갑니다. 
  - 남은 인원: $B_2, R_3$
- **$B_2$의 차례** 
  - 유일하게 남은 상대인 $R_3$을 퇴장시킵니다.
  - 남은 인원: $B_2$
- **결과:** 푸른 파도 부원만 남았으므로 `Blue Wave`가 승리합니다.

### 예시 2
**Input:**
{TICK}
3
BRR
{TICK}

**Output:**
{TICK}
Red Passion
{TICK}

- 첫 번째 B 부원이 두 번째 R 부원을 퇴장시킵니다. 그리고 줄 맨 뒤로 갑니다. 
    - 남은 인원: R, B
- 세 번째 R 부원의 차례가 옵니다. 이 부원은 첫 번째 B 부원을 퇴장시킵니다.
- 결국 붉은 열정 부원만 남게 되어 승리합니다.

### 예시 3
**Input:**
{TICK}
6
BBRRRB
{TICK}

**Output:**
{TICK}
Blue Wave
{TICK}

"""

problem_md = problem_template.replace("{TICK}", TICK)
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - sys.stdin.readline 적용
# ---------------------------------------------------------
solution_py = """import sys
from collections import deque

# 입력 방식 최적화
input = sys.stdin.readline

def solve():
    # 1. N 읽기
    line_n = input().strip()
    if not line_n: return
    n = int(line_n)
    
    # 2. 동아리 소속 데이터 읽기
    senate = input().strip()
    if not senate: return

    # 각 동아리 부원들의 초기 인덱스를 보관
    blue = deque()
    red = deque()
    
    for i, s in enumerate(senate):
        if s == 'B':
            blue.append(i)
        else:
            red.append(i)
            
    # 3. 토론 시뮬레이션
    while blue and red:
        b_idx = blue.popleft()
        r_idx = red.popleft()
        
        # 더 앞 순서인 부원이 상대방을 퇴장시키고 뒤로 가서 줄을 섬
        # 다음 라운드(인덱스 + N)로 위치를 갱신
        if b_idx < r_idx:
            blue.append(b_idx + n)
        else:
            red.append(r_idx + n)
            
    # 4. 결과 출력
    if blue:
        print("Blue Wave")
    else:
        print("Red Passion")

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(senate):
    n = len(senate)
    blue = deque([i for i, s in enumerate(senate) if s == 'B'])
    red = deque([i for i, s in enumerate(senate) if s == 'R'])
    while blue and red:
        b = blue.popleft()
        r = red.popleft()
        if b < r: blue.append(b + n)
        else: red.append(r + n)
    return "Blue Wave" if blue else "Red Passion"

test_data = [
    (2, "BR"),
    (3, "BRR"),
    (6, "BBRRRB")
]

for _ in range(17):
    tn = random.randint(10, 100)
    tsenate = "".join(random.choice(['B', 'R']) for _ in range(tn))
    test_data.append((tn, tsenate))

for i, (n, senate) in enumerate(test_data, 1):
    input_str = f"{n}\n{senate}"
    ans = solve_internal(senate)
    
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str.strip())
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P75' 문제 생성이 완료되었습니다.")