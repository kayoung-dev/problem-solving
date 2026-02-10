import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 및 기본 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P028")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "과자 공장의 포장 기계"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Math"]
---

## description
과자 공장의 신입 사원 '민수'는 쿠키를 포장하는 업무를 맡았습니다.<br/>
포장 기계는 한 상자에 정확히 **box_size**개의 쿠키를 담을 수 있습니다.<br/>
컨베이어 벨트를 통해 여러 묶음의 쿠키들이 도착합니다. 기계는 다음 규칙에 따라 작동합니다.
1. 쿠키 묶음 개수가 **box_size**로 **남김없이 나누어 떨어질 때만** 포장을 진행합니다.
2. 포장이 가능한 경우, 해당 묶음으로 **몇 개의 상자**를 만들 수 있는지(몫)를 계산합니다.
3. 만들어진 상자 개수들을 **오름차순**으로 정렬하여 기록합니다.
4. 포장할 수 있는 쿠키 묶음이 하나도 없다면 **-1**을 기록합니다.
쿠키 묶음 배열과 상자 용량 box_size가 주어질 때, 기록해야 할 상자 개수 목록을 구하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 쿠키 묶음의 수 $N$과 상자 용량 box_size가 공백으로 구분되어 주어집니다. ($1 \\le N \\le 100$, $1 \\le$ box_size $\\le 100$)
- 두 번째 줄에 $N$개의 쿠키 묶음 데이터(자연수)가 공백으로 구분되어 주어집니다.

## output_description
- 만들어진 상자의 개수(몫)를 오름차순으로 정렬하여 공백으로 구분해 출력합니다.
- 포장 가능한 묶음이 없다면 -1을 출력합니다.

# samples

### input 1
{TICK}
5 4
4 12 7 8 3
{TICK}

### output 1
{TICK}
1 2 3
{TICK}


### input 2
{TICK}
3 5
2 4 9
{TICK}

### output 2
{TICK}
-1
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (Python Solution)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    box_size = int(line1[1])
    
    # 쿠키 묶음 배열
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: 나누어 떨어지는 경우, 몫(num // box_size)을 저장
    results = []
    for num in arr:
        if num % box_size == 0:
            results.append(num // box_size)
    
    # 예외 처리 및 정렬
    if not results:
        print("-1")
    else:
        results.sort()
        print(*results)

if __name__ == "__main__": main()
"""

# ---------------------------------------------------------
# 4. 파일 생성 및 테스트 케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 메인 문제 파일 및 솔루션 저장
save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 테스트 케이스 20개 생성
for i in range(1, 21):
    # 랜덤 데이터 생성
    n = random.randint(1, 100)
    box_size = random.randint(1, 20)
    # 최소한 box_size보다는 큰 값들이 섞이도록 범위 설정
    arr = [random.randint(1, 100 * box_size) for _ in range(n)]
    
    # Input 파일 작성
    input_content = f"{n} {box_size}\n" + " ".join(map(str, arr))
    input_path = os.path.join(test_dir, f"{i}.in")
    save_file(input_path, input_content)
    
    # Output 계산: 몫을 리스트에 담음
    quotients = [x // box_size for x in arr if x % box_size == 0]
    quotients.sort()
    
    if not quotients:
        output_content = "-1"
    else:
        output_content = " ".join(map(str, quotients))
        
    output_path = os.path.join(test_dir, f"{i}.out")
    save_file(output_path, output_content)

print(f"✅ 'Level00/P028' 생성이 완료되었습니다.")