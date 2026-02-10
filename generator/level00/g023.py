import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P023")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "바둑이의 간식 점수"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Implementation", "Math"]
---

## description
강아지 '바둑이'는 간식을 먹을 때마다 정해진 점수를 얻습니다.<br/>
간식은 3일을 주기로 반복되며, 날짜별 점수는 다음과 같습니다.<br/>
- **1일째: 껌 (10점)**
- **2일째: 사료 (20점)**
- **3일째: 뼈다귀 (30점)**
4일째부터는 다시 **껌(10점)**으로 돌아가 이 패턴이 반복됩니다.<br/>
바둑이가 **오늘(1일째)**부터 시작하여 총 **N일 동안** 매일 간식을 먹었을 때, 얻은 **전체 점수의 합계**를 구하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 간식을 먹은 총 일수 N이 주어집니다. ($1 \\le N \\le 10,000$)

## output_description
- N일 동안 얻은 전체 점수의 합계를 정수로 출력합니다.

# samples

### input 1
{TICK}
4
{TICK}

### output 1
{TICK}
70
{TICK}


### input 2
{TICK}
10
{TICK}

### output 2
{TICK}
190
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
        
        # 방법 1: 반복문 활용
        # total = 0
        # for i in range(1, n + 1):
        #     if i % 3 == 1: total += 10
        #     elif i % 3 == 2: total += 20
        #     else: total += 30
        # print(total)

        # 방법 2: 수식 활용 (더 효율적임)
        sets = n // 3        # 3일 세트가 몇 번 반복되는지
        remainder = n % 3    # 세트 이후 남은 날짜
        
        # 한 세트(10+20+30)는 60점
        total = sets * 60
        
        if remainder == 1:
            total += 10
        elif remainder == 2:
            total += 30  # 10 + 20
            
        print(total)
            
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

for i in range(1, 21):
    n = random.randint(1, 1000)
    
    # 정답 계산
    sets = n // 3
    rem = n % 3
    score = sets * 60
    if rem == 1: score += 10
    elif rem == 2: score += 30
    
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(str(n))
        
    save_file(os.path.join(test_dir, f"{i}.out"), str(score))

print(f"✅ 'Level00/P023' 생성이 완료되었습니다.")