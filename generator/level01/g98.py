import os
import random
from collections import Counter

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P98 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P98")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 기록으로 복원한 데이터 순서

## 문제 설명
데이터 분석가 **지민**은 어떤 데이터가 저장된 **원래의 순서**를 복원하려고 합니다.

지민에게 주어진 것은 하나의 배열이 아니라, 여러 번에 걸쳐 저장된 **기록들**입니다.  
각 기록은 중괄호 {{ }}로 감싸진 숫자들의 묶음이며, 이 묶음들은 모두 **같은 데이터 순서**에서 앞부분만 선택해 만든 결과입니다.

예를 들어, 원래 데이터의 순서가 다음과 같다고 가정해봅시다.

{TICK}
[2, 1, 3, 4]
{TICK}

이 데이터는 저장 과정에서 다음과 같은 형태의 기록들로 남을 수 있습니다.

{TICK}
{{2}}
{{2,1}}
{{2,1,3}}
{{2,1,3,4}}
{TICK}

이 기록들은 순서가 섞인 상태로 하나의 문자열로 주어집니다.

지민은 이 기록들을 살펴보며 한 가지 규칙을 발견했습니다.  
**원래 순서에서 앞에 있던 숫자일수록 더 많은 기록에 등장**하고,  
뒤에 있던 숫자일수록 등장하는 횟수가 적다는 점입니다.

따라서 모든 기록에 등장하는 숫자들의 **등장 횟수**를 세고,  
그 횟수가 **많은 순서대로 정렬**하면 원래 데이터의 순서를 복원할 수 있습니다.

주어진 기록 문자열을 분석하여,  
**원래 데이터의 순서를 공백으로 구분해 출력하세요.**


---

## 입력 형식 (Input Format)
- 첫 줄에 기록 문자열 S가 주어진다.  
- S는 여러 개의 집합을 표현한 문자열이다.

---

## 출력 형식 (Output Format)
- 복원된 데이터 순서를 공백으로 구분해 출력한다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
{{{{2}},{{2,1}},{{2,1,3}},{{2,1,3,4}}}}
{TICK}
**Output:**
{TICK}
2 1 3 4
{TICK}

- 숫자 2는 모든 기록에 등장하므로 가장 앞에 위치합니다.
- 숫자 1은 세번 등장합니다.
- 숫자 3과 4는 등장 횟수가 두번 으로 같지만 낮은 숫자가 먼저 위치합니다.

### 예시 2
**Input:**
{TICK}
{{{{4}},{{4,3}},{{4,3,2}},{{4,3,2,1}},{{4,3}}}}
{TICK}
**Output:**
{TICK}
4 3 2 1
{TICK}

- 4는 모든 기록에 등장하여 가장 앞에 옵니다.
- 3은 네번 등장합니다.
- 2는 두번 등장합니다.
- 1은 한 번만 등장하므로 가장 뒤에 배치됩니다.

### 예시 3
**Input:**
{TICK}
{{{{5}},{{5,4}},{{5,4,3}},{{5,4,3,2}},{{5,4,3,2,1}}}}
{TICK}
**Output:**
{TICK}
5 4 3 2 1
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys
from collections import Counter

def solve():
    s = sys.stdin.readline().strip()

    # 중괄호 제거 및 집합 분리
    s = s[2:-2]
    parts = s.split("},{")

    counter = Counter()
    for part in parts:
        nums = map(int, part.split(","))
        for x in nums:
            counter[x] += 1

    # 등장 횟수 내림차순 정렬
    result = sorted(counter.items(), key=lambda x: -x[1])
    print(" ".join(str(x[0]) for x in result))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(s):
    s = s[2:-2]
    parts = s.split("},{")
    counter = Counter()
    for part in parts:
        for x in part.split(","):
            counter[int(x)] += 1
    result = sorted(counter.items(), key=lambda x: -x[1])
    return " ".join(str(x[0]) for x in result)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(98)
test_data = []

# 예시 3개
test_data.append("{{2},{2,1},{2,1,3},{2,1,3,4}}")
test_data.append("{{20,111},{111}}")
test_data.append("{{5},{5,4},{5,4,3},{5,4,3,2},{5,4,3,2,1}}")

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 8)
    base = list(range(1, n + 1))
    random.shuffle(base)

    sets = []
    for i in range(1, n + 1):
        subset = base[:i]
        random.shuffle(subset)
        sets.append("{" + ",".join(map(str, subset)) + "}")

    random.shuffle(sets)
    test_data.append("{" + ",".join(sets) + "}")

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, s in enumerate(test_data, 1):
    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(s + "\n")
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(solve_internal(s) + "\n")

print("✅ 'Level01/P98' 문제 생성이 완료되었습니다.")
