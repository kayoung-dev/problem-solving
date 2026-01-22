import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P40 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P40")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 마크의 게임 점수 복구

## 문제 설명
미국에 사는 열정적인 게이머 **마크**는 친구들과 함께 고전 아케이드 게임 대회를 열었습니다. 마크는 각 라운드가 끝날 때마다 획득한 점수를 장부에 기록하는데, 가끔 긴장한 나머지 점수를 잘못 입력하는 실수를 하곤 합니다. 

마크는 실수를 바로잡기 위해 특별한 규칙을 정했습니다. 점수를 입력하다가 **'0'** 을 입력하면, 이는 "방금 쓴 점수는 실수니 지워줘!"라는 신호입니다. '0'이 입력될 때마다 가장 최근에 썼던 점수를 하나씩 지워나갑니다. 만약 '0'을 여러 번 입력한다면, 입력한 횟수만큼 최근 기록부터 차례대로 지워집니다.

모든 라운드가 끝나고 마크가 최종적으로 기록한 모든 점수의 합계를 구하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
* 첫 번째 줄에 마크가 입력한 숫자의 개수 $K$가 주어집니다. ($1 \\le K \\le 100,000$)
* 이후 $K$개의 줄에 정수가 한 줄에 하나씩 주어집니다.
* 입력되는 정수는 $0$ 이상 $1,000,000$ 이하입니다.
* 정수가 $0$일 경우 가장 최근에 쓴 수를 지우고, $0$이 아닐 경우 해당 수를 기록합니다.
* 데이터를 지울 수 있는 상태(기록된 점수가 있는 상태)에서만 $0$이 입력된다고 가정합니다.

## 출력 형식 (Output Format)
* 최종적으로 장부에 남은 모든 점수의 합을 출력합니다. 

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
3
0
4
0
{TICK}

**Output:**
{TICK}
0
{TICK}

* `3` 입력: [3]
* `0` 입력: 최근의 3을 지움 []
* `4` 입력: [4]
* `0` 입력: 최근의 4를 지움 []
* 최종 합계는 0입니다.

### 예시 2
**Input:**
{TICK}
10
1
3
5
4
0
0
7
0
0
6
{TICK}

**Output:**
{TICK}
7
{TICK}

* `1, 3, 5, 4` 입력 후 `0` 두 번으로 `4, 5` 제거 -> [1, 3]
* `7` 입력 후 `0` 두 번으로 `7, 3` 제거 -> [1]
* `6` 입력 -> [1, 6]
* 최종 합계는 7입니다.

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = f"""import sys

def solve():
    # 입력을 읽어와 첫 번째 값(개수 K)을 추출
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    numbers = input_data[1:]
    
    stack = []
    
    for i in range(k):
        num = int(numbers[i])
        if num == 0:
            # 0이면 가장 최근 값을 제거
            if stack:
                stack.pop()
        else:
            # 0이 아니면 스택에 추가
            stack.append(num)
            
    # 남아있는 모든 값의 합계 출력
    print(sum(stack))

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
    cases.append(("4\\n3\\n0\\n4\\n0", "0"))
    cases.append(("10\\n1\\n3\\n5\\n4\\n0\\n0\\n7\\n0\\n0\\n6", "7"))
    
    # 랜덤 대규모 케이스
    for i in range(len(cases) + 1, 21):
        k = i * 2000
        cmds = [str(k)]
        stk_sim = []
        
        for _ in range(k):
            # 스택에 값이 있을 때만 30% 확률로 0 발생
            if stk_sim and random.random() < 0.3:
                cmds.append("0")
                stk_sim.pop()
            else:
                val = random.randint(1, 100000)
                cmds.append(str(val))
                stk_sim.append(val)
        
        cases.append(("\\n".join(cmds), str(sum(stk_sim))))
    return cases

all_cases = generate_test_cases()
for i, (inp, out) in enumerate(all_cases, 1):
    real_inp = inp.replace("\\\\n", "\\n").replace("\\n", "\n")
    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(real_inp)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P40' 문제 생성이 완료되었습니다.")