import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P09 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P09")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 오큰수 (Next Greater Number)

## 문제 설명
크기가 $N$인 수열 $A = [A_1, A_2, ..., A_N]$이 있습니다.
각 원소 $A_i$에 대해서, 오큰수(Next Greater Number) $NGE(i)$를 구하려고 합니다.

$A_i$의 오큰수는 **오른쪽에 있으면서 $A_i$보다 큰 수 중에서 가장 왼쪽에 있는 수**를 의미합니다.
만약 그러한 수가 없다면 오큰수는 $-1$입니다.

### 예시
수열 $A = [3, 5, 2, 7]$ 인 경우:
* $3$의 오른쪽에 있으면서 $3$보다 큰 수는 $5, 7$입니다. 그중 가장 왼쪽에 있는 수는 $5$입니다.
* $5$의 오른쪽에 있으면서 $5$보다 큰 수는 $7$입니다.
* $2$의 오른쪽에 있으면서 $2$보다 큰 수는 $7$입니다.
* $7$의 오른쪽에는 더 큰 수가 없습니다. 따라서 $-1$입니다.

결과: `[5, 7, 7, -1]`

수열 $A = [9, 5, 4, 8]$ 인 경우:
* $9$보다 큰 수는 오른쪽에 없습니다. ($-1$)
* $5$보다 큰 수는 $8$입니다.
* $4$보다 큰 수는 $8$입니다.
* $8$보다 큰 수는 없습니다. ($-1$)

결과: `[-1, 8, 8, -1]`

[핵심 힌트]
* $N$의 크기가 최대 $1,000,000$입니다. 이중 반복문($O(N^2)$)을 사용하면 시간 초과가 발생합니다.
* 스택(Stack)을 사용하여 수열을 한 번만 훑어서($O(N)$) 해결해야 합니다.
* 스택에 인덱스를 저장하고, 새로 들어오는 수가 스택의 top이 가리키는 수보다 클 때를 감지해보세요.

---

## 입력 형식 (Input Format)
* 첫째 줄에 수열의 크기 $N$이 주어집니다. ($1 \\le N \\le 1,000,000$)
* 둘째 줄에 수열 $A$의 원소 $A_1, A_2, ..., A_N$이 공백으로 구분되어 주어집니다. ($1 \\le A_i \\le 1,000,000$)

## 출력 형식 (Output Format)
* 총 $N$개의 오큰수를 공백으로 구분하여 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
3 5 2 7
{TICK}
**Output:**
{TICK}
5 7 7 -1
{TICK}

### 예시 2
**Input:**
{TICK}
4
9 5 4 8
{TICK}
**Output:**
{TICK}
-1 8 8 -1
{TICK}
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

    # 수열 A 입력
    arr = list(map(int, input().split()))
    
    # 정답을 담을 배열, 기본값은 -1로 초기화
    # 오큰수가 없는 경우 그대로 -1이 출력됨
    answer = [-1] * n
    
    # 스택에는 '아직 오큰수를 찾지 못한 수의 인덱스'를 저장
    stack = []
    
    for i in range(n):
        # 스택이 비어있지 않고,
        # 현재 보고 있는 수(arr[i])가 스택의 맨 위(arr[stack[-1]])보다 크다면?
        # -> 스택에 있는 그 수의 오큰수가 바로 현재 수(arr[i])가 됨!
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            answer[idx] = arr[i]
            
        # 현재 인덱스를 스택에 넣고 다음으로 넘어감
        stack.append(i)
        
    # 출력
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

# 내부 정답 로직 (테스트케이스 생성용)
def solve_internal(arr):
    n = len(arr)
    answer = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            answer[idx] = arr[i]
        stack.append(i)
        
    return " ".join(map(str, answer))

# 테스트 케이스 20개 생성
for i in range(1, 21):
    # N의 크기 설정
    if i <= 5:
        n = random.randint(5, 50)
    elif i <= 15:
        n = random.randint(1000, 10000)
    else:
        n = random.randint(50000, 100000)
        
    # 수열 데이터 생성 (1 ~ 1,000,000)
    # 다양한 패턴 추가
    dice = random.random()
    if dice < 0.2:
        # 내림차순 (오큰수 대부분 -1)
        arr = sorted([random.randint(1, 1000000) for _ in range(n)], reverse=True)
    elif dice < 0.4:
        # 오름차순 (바로 다음 숫자가 오큰수)
        arr = sorted([random.randint(1, 1000000) for _ in range(n)])
    else:
        # 랜덤 분포
        arr = [random.randint(1, 1000000) for _ in range(n)]
        
    input_str = f"{n}\n" + " ".join(map(str, arr))
    output_str = solve_internal(arr)
    
    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print(f"✅ 'Level01/P09' 생성이 완료되었습니다.")