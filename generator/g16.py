import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P16")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 엘리베이터 층 이동 로그

## 문제 설명
아파트 엘리베이터가 **현재 1층**에 있습니다.  
관리실은 엘리베이터가 움직인 기록을 보고 최종 도착 층을 확인하려고 합니다.

한 줄에 이동 기록이 공백으로 주어집니다.

- `Uk` : 엘리베이터가 **k층 위로** 올라갑니다. (Up)
- `Dk` : 엘리베이터가 **k층 아래로** 내려갑니다. (Down)

규칙은 다음과 같습니다.

- 시작 층은 **1층**입니다.
- 건물의 층 범위는 **1층 ~ 50층**입니다.
- 이동을 적용한 결과가
  - 1층 미만이면 **1층으로 고정**
  - 50층 초과이면 **50층으로 고정**
- 모든 기록을 처리한 뒤 **최종 층**을 출력하세요.

---

## 입력 형식 (Input Format)
- 한 줄에 기록들이 공백으로 구분되어 주어집니다.
- 기록의 개수는 1개 이상입니다.
- 각 기록은 `Uk` 또는 `Dk` 형태입니다.
  - k는 0 이상 50 이하의 정수입니다.

## 출력 형식 (Output Format)
- 최종 층(정수)을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
Input:
{TICK}
U3 U10 D4 U100
{TICK}

Output:
{TICK}
50
{TICK}

- 1 → 4 → 14 → 10 → 110 (50으로 고정)

### 예시 2
Input:
{TICK}
D5 U2 D10
{TICK}

Output:
{TICK}
1
{TICK}

- 1 → -4(1로 고정) → 3 → -7 (1로 고정)
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        logs = input().split()
        floor = 1

        for log in logs:
            action = log[0]
            value = int(log[1:]) if len(log) > 1 else 0

            if action == 'U':
                floor += value
            elif action == 'D':
                floor -= value

            if floor < 1:
                floor = 1
            elif floor > 50:
                floor = 50

        print(floor)

    except EOFError:
        pass

if __name__ == "__main__":
    main()
"""

# ---------------------------------------------------------
# 4. 파일 저장 함수
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# ---------------------------------------------------------
# 5. 테스트 케이스 생성
# ---------------------------------------------------------
def simulate(logs):
    floor = 1
    for log in logs:
        action = log[0]
        value = int(log[1:]) if len(log) > 1 else 0

        if action == "U":
            floor += value
        elif action == "D":
            floor -= value

        floor = max(1, min(50, floor))
    return floor

fixed_cases = [
    ["U3", "U10", "D4", "U100"],          # 50
    ["D5", "U2", "D10"],                  # 1
    ["U49"],                              # 50 (1->50)
    ["D1"],                               # 1
    ["U0", "D0", "U0"],                   # 1
    ["U10", "U10", "U10"],                # 31
    ["D50", "U1"],                        # 2 (1->1->2)
    ["U20", "D5", "D30", "U7"],           # 1->21->16->1->8 => 8
    ["U1000"],                            # 50
    ["U5", "D3", "U4", "D10", "U2"],      # 1->6->3->7->1->3 => 3
]

for i in range(1, 21):
    if i <= len(fixed_cases):
        logs = fixed_cases[i - 1]
    else:
        length = random.randint(1, 30)
        logs = []
        for _ in range(length):
            action = random.choice(["U", "D"])
            value = random.randint(0, 50)
            logs.append(f"{action}{value}")

    input_str = " ".join(logs)
    output_str = str(simulate(logs))

    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print("✅ 'Easy/P16' 생성이 완료되었습니다.")
