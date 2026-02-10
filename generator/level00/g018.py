import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P018")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "두리의 징검다리"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Condition"]
---

## description
강을 건너려는 강아지 '두리' 앞에 숫자가 적힌 징검다리들이 놓여 있습니다.<br/>
'두리'는 다음과 같은 규칙으로 점수를 계산하며 강을 건너려고 합니다.<br/>
1. 첫 번째, 세 번째, 다섯 번째... 처럼 **홀수 번째** 다리를 밟으면 그 숫자를 더합니다.<br/>
2. 두 번째, 네 번째, 여섯 번째... 처럼 **짝수 번째** 다리를 밟으면 그 숫자를 뺍니다.<br/>
징검다리에 적힌 숫자 리스트가 주어질 때, '두리'가 모든 다리를 건넌 후의 최종 점수를 구하는 프로그램을 작성하세요. (점수는 0점에서 시작합니다.)

## input_description
- 첫 번째 줄에 징검다리에 적힌 정수들이 공백으로 구분되어 한 줄에 주어집니다.
- 다리의 개수는 1개 이상 100개 이하입니다.

## output_description
- 계산된 최종 점수를 정수로 출력합니다.

# samples

### input 1
{TICK}
10 5 20 7
{TICK}

### output 1
{TICK}
18
{TICK}


### input 2
{TICK}
100 50 10
{TICK}

### output 2
{TICK}
60
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 한 줄의 데이터를 읽어옵니다.
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    # 공백으로 나누어 리스트로 변환
    stones = list(map(int, line.split()))
    
    total_score = 0
    for i in range(len(stones)):
        # i가 0, 2, 4... 일 때가 실제로는 1, 3, 5... 번째 다리입니다.
        if (i + 1) % 2 != 0:
            total_score += stones[i]
        else:
            total_score -= stones[i]
            
    print(total_score)

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
    n = random.randint(5, 25)
    stones = [random.randint(1, 100) for _ in range(n)]
    
    # 정답 계산
    score = 0
    for idx, val in enumerate(stones):
        if (idx + 1) % 2 != 0:
            score += val
        else:
            score -= val
            
    # 입력 파일 저장 (숫자 리스트만 한 줄로 저장)
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, stones)))
        
    save_file(os.path.join(test_dir, f"{i}.out"), str(score))

print(f"✅ 'Level00/P018' 생성이 완료되었습니다.")