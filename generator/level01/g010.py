import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P010")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "지우의 성적 판정기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Loop"]
---

## description
학원 조교 지우는 학생들의 점수를 입력하면 학점을 자동으로 알려주는 프로그램을 만들려고 합니다.
각 학생의 점수에 따라 학점은 아래 규칙으로 결정됩니다.

- 90 이상: A
- 80 이상: B
- 70 이상: C
- 그 외: F

학생 수와 각 학생의 점수가 주어질 때, 각 학생의 학점을 한 줄씩 출력하는 프로그램을 작성하세요.



## input_description
- 첫째 줄에 학생 수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수 점수가 공백으로 구분되어 주어집니다. (0 ≤ 점수 ≤ 100)

## output_description
- N줄에 걸쳐 각 학생의 학점을 순서대로 출력합니다.

# samples

### input 1
{TICK}
5
95 83 70 69 100
{TICK}

### output 1
{TICK}
A
B
C
F
A
{TICK}

### input 2
{TICK}
3
0 80 90
{TICK}

### output 2
{TICK}
F
B
A
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

def main():
    try:
        n_line = input().strip()
        if not n_line:
            return
        n = int(n_line)

        scores_line = input().strip()
        if not scores_line:
            return

        scores = list(map(int, scores_line.split()))

        for s in scores[:n]:
            print(grade(s))

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
    (5, [95, 83, 70, 69, 100]),
    (3, [0, 80, 90]),
    (1, [70]),
    (1, [89]),
    (4, [90, 80, 70, 60]),
    (6, [100, 99, 98, 97, 96, 95]),
    (6, [79, 78, 77, 76, 75, 74]),
    (7, [0, 1, 2, 3, 4, 5, 6]),
    (8, [85, 85, 85, 85, 85, 85, 85, 85]),
    (10, [50, 60, 70, 80, 90, 100, 69, 79, 89, 99]),
]

def expected_outputs(scores):
    out_lines = []
    for s in scores:
        if s >= 90:
            out_lines.append("A")
        elif s >= 80:
            out_lines.append("B")
        elif s >= 70:
            out_lines.append("C")
        else:
            out_lines.append("F")
    return "\n".join(out_lines)

for i in range(1, 21):
    if i <= len(fixed_cases):
        n, arr = fixed_cases[i - 1]
    else:
        n = random.randint(1, 100)
        arr = [random.randint(0, 100) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, arr))
    output_str = expected_outputs(arr)

    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)

print("✅ 'Level01/P010' 생성이 완료되었습니다.")
