import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P022")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "꼬미의 원형 돌기"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Math"]
---

## description
햄스터 '꼬미'가 원형으로 배치된 N개의 방을 돌며 놀고 있습니다. 각 방에는 **0번부터 N-1번까지** 번호가 붙어 있습니다.<br/>
방이 4개(N=4)라면 방 번호는 **0, 1, 2, 3**이며, 원형으로 연결되어 3번 방 다음은 다시 0번 방입니다.<br/>
꼬미는 현재 **0번 방**에 있습니다. 꼬미가 시계 방향으로 총 **K칸**을 이동했을 때, 최종적으로 멈추게 되는 방의 번호를 구하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 방의 개수 N과 이동할 칸수 K가 공백으로 구분되어 주어집니다.
- $1 \\le N \\le 100$
- $0 \\le K \\le 10,000$

## output_description
- 꼬미가 최종적으로 도착한 방의 번호를 정수로 출력합니다.

# samples

### input 1
{TICK}
4 5
{TICK}

### output 1
{TICK}
1
{TICK}


### input 2
{TICK}
10 20
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
        
    try:
        # N: 방의 개수, K: 이동 거리
        n, k = map(int, line.split())
        
        # 원형 순환의 핵심은 나머지 연산입니다.
        # 어떤 숫자든 N으로 나눈 나머지는 항상 0 ~ N-1 범위 안에 들어옵니다.
        result = k % n
        
        print(result)
            
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
    n = random.randint(2, 100)
    k = random.randint(0, 10000)
    ans = k % n
    
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(f"{n} {k}")
    save_file(os.path.join(test_dir, f"{i}.out"), str(ans))

print(f"✅ 'Level00/P022' 생성이 완료되었습니다.")