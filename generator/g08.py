import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P08")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 루나의 드론 점검 (Drone Check)

## 문제 설명
탐험가 루나는 탐험용 드론을 점검하고 있습니다.
드론들은 상태 코드로 관리되며,

- 1 : 정상 작동
- 0 : 고장

을 의미합니다.

드론 상태 정보가 주어질 때, 정상적으로 작동 중인 드론의 개수를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 드론의 개수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수(0 또는 1)가 공백으로 구분되어 주어집니다.

## 출력 형식 (Output Format)
- 정상 작동 중인 드론의 개수를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
Input:
{TICK}
6
1 0 1 1 0 1
{TICK}

Output:
{TICK}
4
{TICK}

### 예시 2
Input:
{TICK}
4
0 0 0 0
{TICK}

Output:
{TICK}
0
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        n_line = input().strip()
        if not n_line:
            return
        n = int(n_line)

        states_line = input().strip()
        if not states_line:
            print(0)
            return

        states = list(map(int, states_line.split()))

        ok = 0
        for s in states[:n]:
            if s == 1:
                ok += 1

        print(ok)

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

# 테스트 케이스 생성 (20개)
fixed_cases = [
    (6, [1, 0, 1, 1, 0, 1]),
    (4, [0, 0, 0, 0]),
    (1, [1]),
    (1, [0]),
    (8, [1, 1, 1, 0, 0, 1, 0, 1]),
    (10, [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),
    (5, [1, 1, 1, 1, 1]),
    (7, [0, 0, 1, 0, 1, 0, 1]),
    (9, [1, 0, 0, 1, 1, 0, 1, 0, 1]),
    (3, [0, 1, 0]),
]

for i in range(1, 21):
    if i <= len(fixed_cases):
        n, arr = fixed_cases[i - 1]
    else:
        n = random.randint(1, 100)
        arr = [random.randint(0, 1) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, arr))
    output_str = str(sum(arr))

    save_file(os.path.join(base_dir, f"input_{i:02d}.txt"), input_str)
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), output_str)

print("✅ 'Easy/P08' 생성이 완료되었습니다.")
