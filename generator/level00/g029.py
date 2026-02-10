import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 및 기본 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P029")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "비밀 요원의 암호 해독"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Condition"]
---

## description
비밀 요원 '제임스'는 적의 기지에서 암호화된 숫자 배열을 입수했습니다.<br/>
본부에서는 이 암호를 풀 수 있는 **핵심 키(key)**를 전송해 주었습니다.<br/>
제임스는 다음 규칙에 따라 가짜 숫자들 속에 숨어 있는 진짜 암호를 찾아내야 합니다.
1. 수신된 숫자 배열의 값 중에서, 핵심 키 **key**의 **배수**인 숫자만 진짜 암호입니다. (key로 나누었을 때 나머지가 0인 경우)
2. 찾아낸 진짜 암호들은 **오름차순** 정렬해야 해석이 가능합니다.
3. key의 배수가 하나도 없다면 **-1**을 출력하고 철수해야 합니다.
숫자 배열과 핵심 키가 주어졌을 때, 진짜 암호(숫자)들을 찾아 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 배열의 크기 $N$과 핵심 키 key가 공백으로 구분되어 주어집니다. ($1 \\le N \\le 100$, $1 \\le$ key $\\le 100$)
- 두 번째 줄에 $N$개의 수신된 숫자(자연수)가 공백으로 구분되어 주어집니다.

## output_description
- 조건(key의 배수)을 만족하는 숫자를 오름차순으로 정렬하여 공백으로 구분해 출력합니다.
- 만족하는 숫자가 없다면 -1을 출력합니다.

# samples

### input 1
{TICK}
5 4
4 12 7 9 16
{TICK}

### output 1
{TICK}
4 12 16
{TICK}


### input 2
{TICK}
3 5
2 3 9
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
    key = int(line1[1])  # 'divisor' 대신 'key' 사용
    
    # 암호 숫자 배열
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: key의 배수(나누어 떨어지는 수) 필터링
    real_codes = [num for num in arr if num % key == 0]
    
    # 예외 처리: 결과가 비어있으면 -1
    if not real_codes:
        print("-1")
    else:
        # 오름차순 정렬
        real_codes.sort()
        # 공백 구분 출력
        print(*real_codes)

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
    key = random.randint(1, 20) # 변수명 key로 변경
    arr = [random.randint(1, 1000) for _ in range(n)]
    
    # Input 파일 작성
    input_content = f"{n} {key}\n" + " ".join(map(str, arr))
    input_path = os.path.join(test_dir, f"{i}.in")
    save_file(input_path, input_content)
    
    # Output 계산
    result = [x for x in arr if x % key == 0]
    result.sort()
    
    if not result:
        output_content = "-1"
    else:
        output_content = " ".join(map(str, result))
        
    output_path = os.path.join(test_dir, f"{i}.out")
    save_file(output_path, output_content)

print(f"✅ 'Level00/P029' 생성이 완료되었습니다.")