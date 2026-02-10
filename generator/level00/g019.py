import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P019")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "나비의 기온 차이"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Condition"]
---

## description
나비는 매일 정해진 시간의 기온을 기록하고 있습니다.<br/>
나비는 문득 **어제와 오늘 사이의 기온 변화**가 얼마나 큰지 궁금해졌습니다.
기온 기록 리스트가 주어질 때, 인접한 두 기온의 차이(절댓값) 중 **가장 큰 값**을 구하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 여러 날의 기온이 공백으로 구분되어 한 줄에 주어집니다.
- 기온은 정수로 주어지며, 최소 2개 이상의 기온이 입력됩니다.

## output_description
- 인접한 두 기온 차이의 최댓값을 정수로 출력합니다.

# samples

### input 1
{TICK}
10 12 15 11 18
{TICK}

### output 1
{TICK}
7
{TICK}


### input 2
{TICK}
20 20 20
{TICK}

### output 2
{TICK}
0
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    # 기온 리스트 생성
    temps = list(map(int, line.split()))
    
    max_gap = 0
    
    # 인접한 두 요소를 비교 (i와 i+1)
    # len(temps) - 1 까지만 반복해야 인덱스 에러가 나지 않습니다.
    for i in range(len(temps) - 1):
        # abs() 함수로 차이의 절댓값을 구합니다.
        gap = abs(temps[i] - temps[i+1])
        if gap > max_gap:
            max_gap = gap
            
    print(max_gap)

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

for i in range(1, 21):
    n = random.randint(3, 15)
    temps = [random.randint(-10, 35) for _ in range(n)]
    
    # 정답 계산
    max_g = 0
    for idx in range(len(temps) - 1):
        g = abs(temps[idx] - temps[idx+1])
        if g > max_g:
            max_g = g
            
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, temps)))
        
    save_file(os.path.join(test_dir, f"{i}.out"), str(max_g))

print(f"✅ 'Level00/P019' 생성이 완료되었습니다.")