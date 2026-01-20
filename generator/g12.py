import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P12")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 유진의 최고 기온 찾기 (Max Temperature)

## 문제 설명
기상 관측을 맡은 유진은 오늘 기록된 기온들 중 가장 높은 값을 빠르게 확인하려고 합니다.
여러 개의 기온 값이 주어질 때, 가장 높은 기온을 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수(기온)가 공백으로 구분되어 주어집니다. (-50 ≤ 기온 ≤ 50)

## 출력 형식 (Output Format)
- 가장 높은 기온을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1

Input:
{TICK}
5
3 -2 5 1 0
{TICK}

Output:
{TICK}
5
{TICK}

---

### 예시 2

Input:
{TICK}
4
-10 -3 -7 -50
{TICK}

Output:
{TICK}
-3
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

        arr_line = input().strip()
        if not arr_line:
            return
        arr = list(map(int, arr_line.split()))

        max_val = arr[0]
        for x in arr[:n]:
            if x > max_val:
                max_val = x

        print(max_val)

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
    (5, [3, -2, 5, 1, 0]),
    (4, [-10, -3, -7, -50]),
    (1, [0]),
    (1, [-50]),
    (6, [1, 1, 1, 1, 1, 1]),
    (6, [-1, -1, -1, -1, -1, -1]),
    (7, [-50, -20, 0, 10, 20, 30, 50]),
    (7, [50, 30, 20, 10, 0, -20, -50]),
    (8, [2, 2, 2, 3, 2, 2, 2, 2]),
    (10, [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]),
]

for i in range(1, 21):
    if i <= len(fixed_cases):
        n, arr = fixed_cases[i - 1]
    else:
        n = random.randint(1, 100)
        arr = [random.randint(-50, 50) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, arr))
    output_str = str(max(arr))

    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print("✅ 'Easy/P12' 생성이 완료되었습니다.")
