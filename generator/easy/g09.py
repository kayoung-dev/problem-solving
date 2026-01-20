import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))  
# current_dir = Easy/generator/easy

easy_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "Easy"))  
# easy_dir = Easy/

base_dir = os.path.join(easy_dir, "P09")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 민준의 이동 기록 계산 (Robot Movement)

## 문제 설명
탐사 로봇을 조종하는 민준은 로봇의 이동 기록을 확인하고 있습니다.
로봇은 여러 번 이동하며, 각 이동 거리는 정수로 기록됩니다.

- 양수는 앞으로 이동한 거리
- 음수는 뒤로 이동한 거리

모든 이동 기록이 주어질 때, 로봇의 최종 위치를 계산하는 프로그램을 작성하세요.
로봇의 시작 위치는 0입니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 이동 횟수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수가 공백으로 구분되어 주어집니다.

## 출력 형식 (Output Format)
- 로봇의 최종 위치를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
Input:
{TICK}
5
3 -2 4 -1 2
{TICK}

Output:
{TICK}
6
{TICK}

### 예시 2
Input:
{TICK}
4
-5 2 1 -3
{TICK}

Output:
{TICK}
-5
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        n = int(input().strip())
        moves = list(map(int, input().split()))

        position = 0
        for m in moves[:n]:
            position += m

        print(position)

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
    (5, [3, -2, 4, -1, 2]),
    (4, [-5, 2, 1, -3]),
    (1, [10]),
    (1, [-7]),
    (6, [1, 1, 1, 1, 1, 1]),
    (6, [-1, -1, -1, -1, -1, -1]),
    (8, [2, -1, 2, -1, 2, -1, 2, -1]),
    (5, [0, 0, 0, 0, 0]),
    (7, [5, -3, -2, 4, -1, 1, -4]),
    (3, [100, -50, -25]),
]

for i in range(1, 21):
    if i <= len(fixed_cases):
        n, arr = fixed_cases[i - 1]
    else:
        n = random.randint(1, 100)
        arr = [random.randint(-20, 20) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, arr))
    output_str = str(sum(arr))

    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print("✅ 'Easy/P09' 생성이 완료되었습니다.")
