import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P024")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "스마트 물류 센터의 로봇 위치"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Math"]
---

## description
최첨단 스마트 물류 센터에는 $N \\times N$ 크기의 거대한 격자형 보관 구역이 있습니다.<br/>
각 칸에는 0번부터 $N^2 - 1$번까지의 일련번호가 순서대로 적혀 있습니다.
번호는 왼쪽 위 (0, 0) 칸인 0번부터 오른쪽으로 한 칸씩 붙여지고, 한 줄이 끝나면 다음 줄의 왼쪽 끝에서 이어집니다.<br/>
물류 로봇이 현재 바닥 번호 $idx$ 위에 멈춰 서 있습니다. 이 로봇이 현재 몇 번째 행과 열에 있는지 계산하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 구역의 크기 $N$과 로봇이 서 있는 바닥 번호 $idx$가 공백으로 구분되어 주어집니다.
- $1 \\le N \\le 10,000$, $0 \\le idx < N^2$

## output_description
- 로봇의 현재 위치인 행과 열 번호를 공백으로 구분하여 출력합니다. (인덱스는 0부터 시작합니다.)

# samples

### input 1
{TICK}
3 4
{TICK}

### output 1
{TICK}
1 1
{TICK}


### input 2
{TICK}
10 25
{TICK}

### output 2
{TICK}
2 5
{TICK}
"""

py_solution = """import sys
def main():
    line = sys.stdin.readline().strip()
    if not line: return
    try:
        n, idx = map(int, line.split())
        print(f"{idx // n} {idx % n}")
    except: pass
if __name__ == "__main__": main()
"""

def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

for i in range(1, 21):
    n = random.randint(2, 10000)
    idx = random.randint(0, n*n - 1)
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f: f.write(f"{n} {idx}")
    save_file(os.path.join(test_dir, f"{i}.out"), f"{idx // n} {idx % n}")

print(f"✅ 'Level00/P024' 생성이 완료되었습니다.")