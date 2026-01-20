import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P24")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

md_content = f"""# 스마트 물류 센터의 로봇 위치

## 문제 설명
최첨단 스마트 물류 센터에는 $N \\times N$ 크기의 거대한 격자형 보관 구역이 있습니다. 이 구역의 각 칸은 행과 열 좌표로 관리되지만, 바닥에는 0번부터 $N^2 - 1$번까지의 일련번호가 순서대로 적혀 있습니다.

번호는 왼쪽 위 (0, 0) 칸인 0번부터 시작하여 오른쪽으로 한 칸씩 이동하며 붙여집니다. 한 줄이 끝나면 다음 줄의 왼쪽 끝에서 번호가 이어집니다.

물류 로봇이 현재 바닥 번호 $idx$ 위에 멈춰 서 있습니다. 이 로봇이 현재 몇 번째 행과 열에 있는지 계산하는 프로그램을 작성하세요.

---

## 입력 형식
* 첫 번째 줄에 구역의 크기 $N$과 로봇이 서 있는 바닥 번호 $idx$가 공백으로 구분되어 주어집니다.
* $1 \\le N \\le 10,000$
* $0 \\le idx < N^2$

## 출력 형식
* 로봇의 현재 위치인 행과 열 번호를 공백으로 구분하여 출력합니다. (인덱스는 0부터 시작합니다.)

---

## 입출력 예시

### 예시 1
**Input:**
{TICK}
3 4
{TICK}

**Output:**
{TICK}
1 1
{TICK}

* $3 \\times 3$ 구역에서 4번은 두 번째 줄(행 1)의 두 번째 칸(열 1)에 위치합니다.
* 4를 3으로 나눈 몫은 1(행), 나머지는 1(열)입니다.

### 예시 2
**Input:**
{TICK}
10 25
{TICK}

**Output:**
{TICK}
2 5
{TICK}

* $10 \\times 10$ 구역에서 25번은 세 번째 줄(행 2)의 여섯 번째 칸(열 5)에 위치합니다.
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
    input_path = os.path.join(test_dir, f"input_{i:02d}.in")
    with open(input_path, "w", encoding="utf-8") as f: f.write(f"{n} {idx}")
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), f"{idx // n} {idx % n}")

print(f"✅ 'Easy/P24' 생성이 완료되었습니다.")