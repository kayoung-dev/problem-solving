import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level02/P05 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P005")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "같은 숫자는 싫어"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
배열 `arr`가 주어집니다. 배열 `arr`의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. <br />
배열 `arr`에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. <br />
단, 제거된 후 남은 수들을 반환할 때는 배열 `arr`의 원소들의 순서를 유지해야 합니다. <br />

예를 들어:
* `arr = [1, 1, 3, 3, 0, 1, 1]` 이면 `[1, 3, 0, 1]` 을 return 합니다.
* `arr = [4, 4, 4, 3, 3]` 이면 `[4, 3]` 을 return 합니다.

스택(Stack)이나 리스트를 활용하여, **직전에 넣은 숫자와 현재 숫자가 다를 때만 저장**하는 로직을 구현해 보세요.



## input_description
- 첫 번째 줄에 배열의 크기 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 두 번째 줄에 $N$개의 정수가 공백으로 구분되어 주어집니다.

## output_description
- 연속된 중복이 제거된 숫자들을 공백으로 구분하여 출력합니다.

# samples
### input 1
{TICK}
7
1 1 3 3 0 1 1
{TICK}

### output 1
{TICK}
1 3 0 1
{TICK}

### input 2
{TICK}
5
4 4 4 3 3
{TICK}

### output 2
{TICK}
4 3
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def solve():
    input = sys.stdin.readline
    
    # N 입력 (사실 Python에서는 리스트를 바로 읽으면 되므로 크게 필요 없지만 형식상 받음)
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 배열 입력
    arr_line = input().strip()
    if not arr_line:
        # 빈 배열일 경우
        print("") 
        return
        
    arr = list(map(int, arr_line.split()))
    
    stack = []
    
    for num in arr:
        # 스택이 비어있거나, 스택의 마지막 요소(직전에 넣은 값)가 현재 값과 다르면 추가
        if not stack or stack[-1] != num:
            stack.append(num)
            
    # 결과 출력 (공백으로 구분)
    print(*(stack))

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
    if not arr:
        return ""
    stack = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    # 리스트를 공백 구분 문자열로 변환
    return " ".join(map(str, stack))

# 테스트 케이스 20개 생성
for i in range(1, 21):
    # N의 크기 (랜덤)
    n = random.randint(10, 1000)
    
    # 0~9 사이의 숫자로 구성된 리스트 생성
    # 연속된 중복이 잘 발생하도록 0~5 정도로 범위를 좁히거나 choice 사용
    arr = [random.randint(0, 9) for _ in range(n)]
    
    # 입력 문자열 구성
    input_str = f"{n}\n" + " ".join(map(str, arr))
    
    # 정답 문자열 구성
    output_str = solve_internal(arr)
    
    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)

print(f"✅ 'Level01/P005' 생성이 완료되었습니다.")