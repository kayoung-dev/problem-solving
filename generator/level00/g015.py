import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P015")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "센서 데이터 요약"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Condition"]
---

## description
어떤 장비는 여러 개의 센서를 통해 데이터를 순서대로 수집합니다.<br/>
장비는 기록을 요약하기 위해, 모든 값을 단순히 더하지 않고 아래 규칙에 따라 점수를 계산합니다.<br/>
센서 데이터가 한 줄로 주어질 때, 다음 규칙으로 점수를 계산하세요.<br/>
- 데이터의 위치는 1번째부터 시작합니다.<br/>
- 짝수 번째 위치의 값만 사용합니다. (2, 4, 6, ...)<br/>
- 사용한 값 중에서 0 이하(0 또는 음수)는 제외합니다.<br/>
- 남은 값들은 모두 더한 뒤, 결과를 출력합니다.<br/>
규칙에 따라 계산한 점수를 출력하는 프로그램을 작성하세요.

## input_description
- 한 줄에 센서 데이터 값들이 공백으로 구분되어 주어집니다.
- 각 값은 정수이며, 최소 1개 이상 주어집니다.
- 각 값의 범위는 -1,000,000 이상 1,000,000 이하입니다.

## output_description
- 규칙에 따라 선택된 값들의 합을 출력합니다.
- 선택된 값이 하나도 없다면 0을 출력합니다.

# samples

### input 1
{TICK}
10 -2 30 0 50 60
{TICK}

### output 1
{TICK}
60
{TICK}


### input 2
{TICK}
-1 5 -3 7 -9
{TICK}

### output 2
{TICK}
12
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        data = list(map(int, input().split()))
        total = 0

        # 짝수 번째 위치(1-based) -> index 1, 3, 5 ...
        for i in range(1, len(data), 2):
            if data[i] > 0:
                total += data[i]

        print(total)

    except EOFError:
        pass

if __name__ == "__main__":
    main()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 테스트 케이스 생성 (20개)
fixed_cases = [
    [10, -2, 30, 0, 50, 60],            # even pos: -2,0,60 -> only >0 => 60
    [-1, 5, -3, 7, -9],                 # even pos: 5,7 -> 12
    [100],                               # even pos 없음 -> 0
    [1, 2],                              # even pos: 2 -> 2
    [1, -2],                             # even pos: -2 -> 0
    [0, 0, 0, 0],                        # even pos: 0,0 -> 0
    [5, 1, 5, 1, 5, 1],                  # even pos: 1,1,1 -> 3
    [-10, -20, -30, -40, -50, -60],      # even pos: -20,-40,-60 -> 0
    [9, 8, 7, 6, 5, 4, 3, 2, 1],         # even pos: 8,6,4,2 -> 20
    [10, 0, 10, 0, 10, 0, 10],           # even pos: 0,0,0 -> 0
]

def score(arr):
    s = 0
    for i in range(1, len(arr), 2):
        if arr[i] > 0:
            s += arr[i]
    return s

for i in range(1, 21):
    if i <= len(fixed_cases):
        arr = fixed_cases[i - 1]
    else:
        length = random.randint(1, 30)
        arr = [random.randint(-1000000, 1000000) for _ in range(length)]

    input_str = " ".join(map(str, arr))
    output_str = str(score(arr))

    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)

print("✅ 'Level00/P015' 생성이 완료되었습니다.")
