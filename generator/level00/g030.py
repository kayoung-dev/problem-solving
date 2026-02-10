import os
import random
import string

# ---------------------------------------------------------
# 1. 경로 설정 및 기본 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P030")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "오염된 데이터 복구"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
서버실의 정전 사고로 인해 데이터베이스의 파일명들이 손상되었습니다.<br/>
시스템 관리자 '현우'는 백업 시스템에서 파일 리스트를 복구했지만, 불필요한 임시 파일들이 섞여 있습니다.<br/>
현우는 다음 규칙을 적용하여 중요한 파일만 필터링하고 표준 형식으로 변환하려 합니다.
1. **검색 조건 1:** 파일명이 특정 접두사 **prefix**로 시작해야 합니다.
2. **검색 조건 2:** 파일명의 길이가 **min_len**보다 **커야(초과)** 합니다. (같으면 안 됩니다.)
3. **변환 규칙:** 위 두 조건을 만족하는 파일명은 모두 **대문자**로 변환합니다.
4. **정렬:** 변환된 파일명 목록은 **사전 순(오름차순)**으로 정렬합니다.
5. **예외 처리:** 조건을 만족하는 파일이 하나도 없다면 **-1**을 출력합니다.
파일 리스트와 검색 조건이 주어졌을 때, 복구된 파일 목록을 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 검색할 접두사 prefix와 기준 길이 min_len이 공백으로 구분되어 주어집니다.
  - prefix는 영문 소문자로 구성됩니다.
  - min_len은 1 이상 50 이하의 자연수입니다.
- 두 번째 줄에 공백으로 구분된 $N$개의 파일명(문자열)들이 주어집니다. ($1 \\le N \\le 100$)

## output_description
- 조건을 만족하는 파일명을 대문자로 변환하여 오름차순으로 정렬한 뒤 공백으로 구분해 출력합니다.
- 만족하는 파일이 없다면 -1을 출력합니다.

# samples

### input 1
{TICK}
sys 5
system sysfile autoexec sys config systematic
{TICK}

### output 1
{TICK}
SYSTEM SYSTEMATIC SYSFILE
{TICK}


### input 2
{TICK}
temp 10
tempfile template temporary
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
    
    prefix = line1[0]
    min_len = int(line1[1])
    
    # 파일명 리스트 입력
    files = sys.stdin.readline().split()
    
    # 로직: 조건 필터링 및 대문자 변환
    # 1. startswith(prefix): 접두사 확인
    # 2. len(s) > min_len: 길이 확인
    # 3. upper(): 대문자 변환
    
    result = []
    for f in files:
        if f.startswith(prefix) and len(f) > min_len:
            result.append(f.upper())
            
    # 예외 처리 및 정렬
    if not result:
        print("-1")
    else:
        result.sort()
        print(*result)

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

# 랜덤 단어 생성 함수
def generate_random_word(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# 테스트 케이스 20개 생성
for i in range(1, 21):
    # 랜덤 파라미터 생성
    prefix_len = random.randint(2, 4)
    prefix = generate_random_word(prefix_len)
    min_len = random.randint(3, 10)
    
    n = random.randint(5, 50)
    
    # 데이터셋 생성 전략:
    # 1. 완전 랜덤 단어
    # 2. prefix는 맞지만 길이가 짧은 단어 (실패 케이스)
    # 3. prefix도 맞고 길이도 긴 단어 (정답 후보)
    
    arr = []
    for _ in range(n):
        case_type = random.random()
        
        # 1. 정답 후보 (조건 만족)
        if case_type < 0.3:
            word_len = random.randint(min_len + 1, min_len + 8)
            suffix = generate_random_word(word_len - len(prefix))
            arr.append(prefix + suffix)
            
        # 2. prefix는 맞지만 길이가 짧거나 같은 경우 (실패 케이스)
        elif case_type < 0.6:
            # [수정된 부분] prefix 길이가 min_len보다 크면, "길이가 짧은 실패 케이스"를 만들 수 없음
            # 따라서 이 경우에는 그냥 랜덤 단어를 생성하거나, 로직을 건너뜀
            if len(prefix) > min_len:
                # 불가능하므로 그냥 아무 랜덤 단어(실패) 생성
                arr.append(generate_random_word(random.randint(3, 10)))
            else:
                # 정상적인 범위(prefix 길이 ~ min_len) 내에서 생성
                word_len = random.randint(len(prefix), min_len)
                suffix = generate_random_word(word_len - len(prefix))
                arr.append(prefix + suffix)
                
        # 3. 아예 다른 단어 (실패 케이스)
        else:
            word_len = random.randint(3, 15)
            arr.append(generate_random_word(word_len))
            
    # 섞기
    random.shuffle(arr)
    
    # Input 파일 작성
    input_content = f"{prefix} {min_len}\n" + " ".join(arr)
    input_path = os.path.join(test_dir, f"{i}.in")
    save_file(input_path, input_content)
    
    # Output 계산
    result = []
    for f in arr:
        if f.startswith(prefix) and len(f) > min_len:
            result.append(f.upper())
    result.sort()
    
    if not result:
        output_content = "-1"
    else:
        output_content = " ".join(result)
        
    output_path = os.path.join(test_dir, f"{i}.out")
    save_file(output_path, output_content)
print(f"✅ 'Level00/P030' 생성이 완료되었습니다.")