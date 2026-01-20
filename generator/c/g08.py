import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (C/P08 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "C", "P08")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 따뜻한 날 기다리기 (Daily Temperatures)

## 문제 설명
매일매일의 기온이 리스트 형태인 `temperatures`로 주어집니다.
당신은 각 날짜별로, '더 따뜻한 날씨를 보려면 며칠을 기다려야 하는지' 알고 싶습니다.

만약 더 따뜻해지는 날이 앞으로 영영 없다면 `0`을 기록하면 됩니다.

### 예시 상황
기온이 `[10, 11, 9, 13]` 이라고 가정해 봅시다.

1. 첫째 날(10도): 바로 다음 날(11도)이 더 따뜻합니다. -> 1일 기다림
2. 둘째 날(11도): 셋째 날(9도)은 춥습니다. 넷째 날(13도)이 되어야 더 따뜻해집니다. -> 2일 기다림
3. 셋째 날(9도): 넷째 날(13도)이 더 따뜻합니다. -> 1일 기다림
4. 넷째 날(13도): 뒤에 날짜가 없습니다. -> 0일

따라서 정답은 `[1, 2, 1, 0]` 입니다.

[핵심 힌트]
* 이중 반복문($O(N^2)$)을 쓰면 시간 초과가 발생할 수 있습니다.
* 스택(Stack)을 사용하여 한 번만 훑어서($O(N)$) 해결할 수 있습니다.
* 스택에는 기온 그 자체가 아니라, '그 기온이 발생한 날짜(인덱스)'를 넣어야 날짜 차이를 계산할 수 있습니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 날짜의 수 $N$이 주어집니다. ($1 \le N \le 100,000$)
* 두 번째 줄에 $N$일 동안의 기온이 공백으로 구분되어 주어집니다. (기온은 -100 ~ 100 사이 정수)

## 출력 형식 (Output Format)
* 각 날짜별로 더 따뜻한 날까지 며칠이 걸리는지 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
8
13 14 15 11 10 12 16 14
{TICK}
**Output:**
{TICK}
1 1 4 2 1 1 0 0
{TICK}
* **3번째 날(15도):** 4, 5, 6번째 날은 다 15도보다 낮거나 같습니다. 7번째 날(16도)이 되어야 따뜻해집니다. (7 - 3 = 4일 뒤)
* **7번째 날(16도):** 남은 날 중에 16도보다 높은 날이 없습니다. (0)

### 예시 2
**Input:**
{TICK}
5
20 19 18 17 16
{TICK}
**Output:**
{TICK}
0 0 0 0 0
{TICK}
* 날이 갈수록 추워지기만 합니다. 더 따뜻해지는 날은 오지 않습니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except ValueError:
        return

    # 기온 리스트 입력
    temps = list(map(int, input().split()))
    
    # 정답 배열 (기본값 0으로 초기화)
    answer = [0] * n
    
    # 스택: "아직 더 따뜻한 날을 찾지 못한 날짜들의 인덱스"를 모아둡니다.
    stack = []
    
    for i in range(n):
        # 스택이 비어있지 않고, 
        # 현재 기온(temps[i])이 스택의 가장 최근 날짜(stack[-1])의 기온보다 높다면?
        # -> 드디어 더 따뜻한 날을 만난 것입니다!
        while stack and temps[stack[-1]] < temps[i]:
            past_day = stack.pop()
            # 기다린 날짜 = 현재 날짜(i) - 과거 날짜(past_day)
            answer[past_day] = i - past_day
            
        # 현재 날짜도 아직 더 따뜻한 날을 못 만났으므로 스택에 넣고 다음으로 넘어갑니다.
        stack.append(i)
        
    print(*(answer))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 내부 정답 로직 (검증용)
def solve_internal(temps):
    n = len(temps)
    answer = [0] * n
    stack = [] # 인덱스 저장
    
    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)
        
    return " ".join(map(str, answer))

# 테스트 케이스 20개 생성
for i in range(1, 21):
    # N의 크기
    if i <= 5:
        n = random.randint(5, 20)
    elif i <= 15:
        n = random.randint(1000, 5000)
    else:
        n = random.randint(50000, 100000)
        
    # 기온 데이터 생성 (-10 ~ 35도)
    dice = random.random()
    if dice < 0.2:
        # 계속 추워짐 (내림차순) -> 답이 모두 0
        temps = sorted([random.randint(0, 30) for _ in range(n)], reverse=True)
    elif dice < 0.4:
        # 계속 따뜻해짐 (오름차순) -> 답이 모두 1 (마지막 제외)
        temps = sorted([random.randint(0, 30) for _ in range(n)])
    else:
        # 랜덤
        temps = [random.randint(-10, 35) for _ in range(n)]
        
    input_str = f"{n}\n" + " ".join(map(str, temps))
    output_str = solve_internal(temps)
    
    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print(f"✅ 'C/P08' 생성이 완료되었습니다.")