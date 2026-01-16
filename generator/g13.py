import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P13")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 현우의 방문 기록 정리 (Visit Log Cleanup)

## 문제 설명
도서관에서 근무하는 현우는 하루 동안 방문한 사람들의 출입 기록을 정리하고 있습니다.
출입 시스템의 특성상, 같은 사람이 하루에 여러 번 출입하면 동일한 번호가 여러 번 기록됩니다.

현우는 하루 동안 어떤 사람들이 도서관을 방문했는지를 한 번씩만 확인하고 싶어합니다.
그래서 방문 기록에서 중복된 번호를 제거하고,
각 번호가 처음 등장한 순서대로 하나씩만 남기려고 합니다.

정수로 이루어진 방문 기록이 주어질 때,
중복을 제거한 결과를 처음 등장한 순서대로 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 방문 기록의 개수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수(방문자 번호)가 공백으로 구분되어 주어집니다. (-1000 ≤ 번호 ≤ 1000)

## 출력 형식 (Output Format)
- 중복을 제거한 방문자 번호들을 공백으로 구분하여 한 줄에 출력합니다.
- 모든 번호가 중복되어 있더라도, 처음 등장한 번호는 반드시 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1

입력
{TICK}
8
1 2 2 3 1 4 4 5
{TICK}

출력
{TICK}
1 2 3 4 5
{TICK}

---

### 예시 2

입력
{TICK}
6
7 7 7 7 7 7
{TICK}

출력
{TICK}
7
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        n = int(input().strip())
        records = list(map(int, input().split()))

        unique = []
        for x in records[:n]:
            duplicated = False
            for y in unique:
                if y == x:
                    duplicated = True
                    break
            if not duplicated:
                unique.append(x)

        print(" ".join(map(str, unique)))

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
    (8, [1, 2, 2, 3, 1, 4, 4, 5]),
    (6, [7, 7, 7, 7, 7, 7]),
    (5, [1, 2, 3, 4, 5]),
    (10, [0, 0, 1, 1, 0, 2, 2, 3, 3, 2]),
    (7, [-1, -1, -2, -2, -1, 0, 0]),
    (9, [5, 4, 5, 4, 5, 4, 3, 3, 2]),
    (1, [42]),
    (8, [1, 1, 2, 2, 3, 3, 4, 4]),
    (8, [2, 1, 2, 1, 2, 1, 2, 1]),
    (12, [3, 3, 3, 2, 2, 1, 1, 0, 0, -1, -1, -1]),
]

def unique_keep_order(arr):
    out = []
    for x in arr:
        if x not in out:
            out.append(x)
    return out

for i in range(1, 21):
    if i <= len(fixed_cases):
        n, arr = fixed_cases[i - 1]
    else:
        n = random.randint(1, 100)
        arr = [random.randint(-10, 10) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, arr))
    output_arr = unique_keep_order(arr)
    output_str = " ".join(map(str, output_arr))

    save_file(os.path.join(base_dir, f"input_{i:02d}.txt"), input_str)
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), output_str)

print("✅ 'Easy/P13' 생성이 완료되었습니다.")

