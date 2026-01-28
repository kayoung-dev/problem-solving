import os
import random
import re

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P100 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P100")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 파일 정렬 기준 맞추기

## 문제 설명
개발자 **민재**는 프로젝트 폴더 안의 파일들을 보기 쉽게 정리하려고 합니다.

각 파일 이름은 다음과 같은 형태로 이루어져 있습니다.

- 알파벳으로 이루어진 **이름 부분**
- 숫자로 이루어진 **번호 부분**

예를 들어, 파일 이름은 다음과 같이 주어질 수 있습니다.

{TICK}
img12
img2
test10
test1
{TICK}

민재는 파일을 다음 기준에 따라 정렬합니다.

1. 이름 부분을 **대소문자 구분 없이 사전순**으로 정렬한다.
2. 이름 부분이 같다면, **번호 부분을 숫자 크기 기준**으로 정렬한다.

정렬된 파일 이름을 한 줄에 하나씩 출력하세요.

---

## 입력 형식 (Input Format)
첫 줄에 파일의 개수 N이 주어집니다.  
다음 N줄에 걸쳐 파일 이름이 한 줄에 하나씩 주어집니다.

---

## 출력 형식 (Output Format)
정렬된 파일 이름을 한 줄에 하나씩 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
img12
img2
test10
test1
{TICK}
**Output:**
{TICK}
img2
img12
test1
test10
{TICK}
- 이름 부분 기준으로 먼저 정렬합니다.
- 같은 이름에서는 번호를 숫자로 비교합니다.

### 예시 2
**Input:**
{TICK}
3
File9
file10
file2
{TICK}
**Output:**
{TICK}
file2
File9
file10
{TICK}
- 대소문자는 구분하지 않습니다.

### 예시 3
**Input:**
{TICK}
2
data100
data20
{TICK}
**Output:**
{TICK}
data20
data100
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
import re

def split_file(name: str):
    # 이름(알파벳)+번호(숫자) 형태를 가정
    m = re.match(r"([a-zA-Z]+)(\\d+)$", name)
    head = m.group(1).lower()
    num = int(m.group(2))
    return head, num

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    files = [input().strip() for _ in range(n)]

    files.sort(key=split_file)

    for f in files:
        print(f)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def split_internal(name: str):
    m = re.match(r"([a-zA-Z]+)(\d+)$", name)  # ✅ 여기서 \d+ 로 써야 함
    return m.group(1).lower(), int(m.group(2))

def solve_internal(arr):
    arr2 = sorted(arr, key=lambda x: split_internal(x))
    return "\n".join(arr2)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(100)
test_data = []

# 예시 3개
test_data.append(["img12", "img2", "test10", "test1"])
test_data.append(["File9", "file10", "file2"])
test_data.append(["data100", "data20"])

HEAD_POOL = ["img", "test", "file", "data", "log", "temp", "doc"]

for _ in range(17):
    n = random.randint(1, 200)
    arr = []
    for _ in range(n):
        head = random.choice(HEAD_POOL)
        # 대소문자 섞기
        if random.randint(0, 1) == 1:
            head = head.upper()
        num = random.randint(0, 1000)
        arr.append(f"{head}{num}")
    test_data.append(arr)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, arr in enumerate(test_data, 1):
    input_str = f"{len(arr)}\n" + "\n".join(arr) + "\n"
    ans = solve_internal(arr)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P100' 문제 생성이 완료되었습니다.")
