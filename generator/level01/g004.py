import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P004")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "하늘이의 최고의 가수 선발"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Array"]
---

## description
오디션 프로그램의 진행자 **'하늘이'** 는 공정한 심사를 위해 가수들의 점수를 계산하는 프로그램을 만들려고 합니다.

한 명의 가수는 총 $N$명의 심사위원에게 점수를 받습니다. **'하늘이'** 는 점수의 편차를 줄이기 위해 다음 규칙을 적용합니다.

1. 전체 점수 중 **가장 높은 점수** 하나와 **가장 낮은 점수** 하나를 제외합니다.
2. 제외하고 남은 점수들의 **평균**을 구합니다.

가수가 받은 점수들이 주어질 때, **'하늘이'** 의 규칙에 따라 계산된 최종 평균 점수를 출력하는 프로그램을 작성하세요.



## input_description
- 첫 번째 줄에 심사위원의 수 $N$이 주어집니다. ($3 \le N \le 20$)
- 두 번째 줄에 $N$개의 점수가 공백으로 구분되어 주어집니다. (점수는 1 이상 100 이하의 정수)

## output_description
- 최댓값과 최솟값을 하나씩 제외한 나머지 점수들의 평균을 **소수점 둘째 자리**까지 출력합니다.

# samples

### input 1
{TICK}
5
10 20 30 40 50
{TICK}

### output 1
{TICK}
30.00
{TICK}

### input 2
{TICK}
4
85 90 95 80
{TICK}

### output 2
{TICK}
87.50
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    try:
        # 첫 번째 줄 N 입력
        line1 = input()
        if not line1: return
        n = int(line1.strip())
        
        # 두 번째 줄 점수 리스트 입력
        line2 = input()
        if not line2: return
        scores = list(map(int, line2.split()))
        
        # 최댓값과 최솟값 찾기
        max_val = max(scores)
        min_val = min(scores)
        
        # 전체 합에서 최댓값과 최솟값을 한 번씩 뺌
        total_sum = sum(scores) - max_val - min_val
        
        # 평균 계산 (N-2개로 나눔)
        avg = total_sum / (n - 2)
        
        # 소수점 둘째 자리까지 출력
        print(f"{avg:.2f}")
            
    except (EOFError, ValueError, ZeroDivisionError):
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
    n = random.randint(3, 10)
    scores = [random.randint(10, 100) for _ in range(n)]
    
    # 정답 계산
    max_s = max(scores)
    min_s = min(scores)
    avg = (sum(scores) - max_s - min_s) / (n - 2)
    ans_str = f"{avg:.2f}"
    
    # 실제 줄바꿈을 사용하여 파일 저장
    file_path = os.path.join(test_dir, f"{i}.in")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{n}\n")  # 여기서 실제 엔터 처리가 됩니다.
        f.write(" ".join(map(str, scores)))
        
    save_file(os.path.join(test_dir, f"{i}.out"), ans_str)

print(f"✅ 'Level01/P004' 생성이 완료되었습니다.")