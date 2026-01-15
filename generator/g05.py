import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P05")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 태양이의 보물 지도 탐험 (Treasure Map)

## 문제 설명
꼬마 탐험가 **'태양이'** 는 오래된 보물 지도를 발견했습니다. 지도에는 보물이 숨겨진 장소로 가기 위한 이동 명령들이 적혀 있습니다.

**'태양이'** 는 현재 좌표 $(0, 0)$에 서 있으며, 지도에 적힌 명령에 따라 다음과 같이 이동합니다.

* **U (Up)**: 위로 이동 ($y$ 좌표 $+1$)
* **D (Down)**: 아래로 이동 ($y$ 좌표 $-1$)
* **L (Left)**: 왼쪽으로 이동 ($x$ 좌표 $-1$)
* **R (Right)**: 오른쪽으로 이동 ($x$ 좌표 $+1$)

명령어들이 나열된 문자열이 주어질 때, 모든 이동을 마친 후 **'태양이'** 가 도착하게 될 최종 좌표 $(x, y)$를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 이동 명령어가 공백으로 구분된 하나의 문자열 $S$가 한 줄에 주어집니다.
* 명령어의 개수는 1개 이상 100개 이하입니다.

## 출력 형식 (Output Format)
* 최종 위치의 $x$ 좌표와 $y$ 좌표를 공백으로 구분하여 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
U R U R
{TICK}

**Output:**
{TICK}
2 2
{TICK}

> **설명:** 위로 1칸, 오른쪽으로 1칸, 위로 1칸, 오른쪽으로 1칸 이동하여 최종 위치는 (2, 2)가 됩니다.

### 예시 2
**Input:**
{TICK}
R R L D U U
{TICK}

**Output:**
{TICK}
1 1
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - 엔터 즉시 종료 버전
# ---------------------------------------------------------
py_solution = """import sys

def main():
    try:
        # 한 줄의 명령어를 입력받습니다.
        line = input()
        if not line:
            return
            
        commands = line.split()
        x, y = 0, 0
        
        for cmd in commands:
            if cmd == 'U':
                y += 1
            elif cmd == 'D':
                y -= 1
            elif cmd == 'L':
                x -= 1
            elif cmd == 'R':
                x += 1
        
        # 최종 좌표 출력
        print(f"{x} {y}")
            
    except EOFError:
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

# 테스트 케이스 생성
for i in range(1, 21):
    count = random.randint(5, 30)
    cmds = [random.choice(['U', 'D', 'L', 'R']) for _ in range(count)]
    input_str = " ".join(cmds)
    
    # 정답 계산
    x, y = 0, 0
    for c in cmds:
        if c == 'U': y += 1
        elif c == 'D': y -= 1
        elif c == 'L': x -= 1
        elif c == 'R': x += 1
    
    # input_str 끝에 개행 문자를 붙여 실제 줄바꿈이 포함되게 저장
    save_file(os.path.join(base_dir, f"input_{i:02d}.txt"), input_str + "\n")
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), f"{x} {y}")

print(f"✅ 'Easy/P05' 생성이 완료되었습니다. (2차원 좌표 이동 문제)")