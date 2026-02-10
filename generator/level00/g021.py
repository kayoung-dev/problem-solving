import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P021")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "포근이의 요일 맞추기"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Math"]
---

## description
강아지 '포근이'는 매주 특정 요일에 산책 나가는 것을 좋아합니다. 오늘은 **월요일**입니다.<br/>
포근이는 오늘로부터 정확히 $N$일이 지났을 때가 무슨 요일인지 궁금해졌습니다.<br/>
요일은 **월요일 → 화요일 → 수요일 → 목요일 → 금요일 → 토요일 → 일요일** 순서로 반복됩니다.<br/>
$N$이 주어졌을 때, 오늘(월요일)로부터 $N$일 후의 요일을 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 지날 날짜를 의미하는 정수 $N$이 주어집니다. ($0 \\le N \\le 10,000$)

## output_description
- $N$일 후의 요일을 한글로 출력합니다. (예: 월요일, 화요일 등)

# samples

### input 1
{TICK}
3
{TICK}

### output 1
{TICK}
목요일
{TICK}


### input 2
{TICK}
10
{TICK}

### output 2
{TICK}
목요일
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
    
    try:
        n = int(line)
        
        # 요일 리스트 (0: 월요일, 1: 화요일, ..., 6: 일요일)
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        
        # 7일 주기로 반복되므로 모듈러 연산 사용
        target_index = n % 7
        
        print(days[target_index])
            
    except ValueError:
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

# 요일 리스트 정의
days_list = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

for i in range(1, 21):
    # 테스트 케이스 생성 (0부터 10000까지 다양하게)
    if i <= 7:
        n = i - 1  # 0~6일 테스트
    else:
        n = random.randint(7, 10000)
    
    # 정답 계산
    ans = days_list[n % 7]
    
    # 입력 파일 저장
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(str(n))
        
    save_file(os.path.join(test_dir, f"{i}.out"), ans)

print(f"✅ 'Level00/P021' 생성이 완료되었습니다.")