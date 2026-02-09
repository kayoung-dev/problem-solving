import os
import random
from typing import List, Tuple

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P116 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P116")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 준호의 영수증 번호 정리

## 문제 설명
회계 담당자 **준호**는 하루 동안 모인 영수증 번호를 정리하려고 합니다.  
영수증 번호는 **숫자로만 이루어진 문자열**이며, 길이가 서로 다를 수 있습니다.

준호는 영수증을 다음 규칙으로 정렬해 출력해야 합니다.

- **우선순위 1:** 숫자 크기가 작은 영수증 번호가 먼저 온다.
- **우선순위 2:** 숫자 크기가 같다면(문자열이 완전히 같다면) 입력에서 먼저 나온 것이 먼저 온다.

단, 영수증 번호는 매우 길 수 있어, 정수로 변환해서 비교할 수 없습니다.  
따라서 문자열로 주어진 번호를 **자리수 단위로 처리**하거나, **앞의 0을 적절히 다루는 방식**으로 빠르게 정렬할 수 있어야 합니다.

또한 숫자의 크기 비교는 다음과 같이 정의합니다.

- 문자열 앞의 `0`은 숫자 크기에 영향을 주지 않습니다.  
  예를 들어 `"0012"`와 `"12"`는 둘 다 숫자 12를 의미합니다.
- 모든 문자가 `0`인 경우(예: `"0"`, `"0000"`)는 숫자 0을 의미합니다.

---
## 입력 형식 (Input Format)
- 첫째 줄에 영수증 개수 $N$이 주어집니다.
- $1 \\le N \\le 200000$
- 다음 $N$줄에 영수증 번호 문자열 $S_i$가 한 줄에 하나씩 주어집니다.
- 각 $S_i$는 숫자(`0`~`9`)로만 이루어진 문자열입니다. 
- $1 \\le |S_i| \\le 1000$

## 출력 형식 (Output Format)
- 정렬된 영수증 번호를 한 줄에 하나씩 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6
12
0012
9
000
10
2
{TICK}
**Output:**
{TICK}
000
2
9
10
12
0012
{TICK}

- `"000"`은 숫자 0이므로 가장 먼저 옵니다.
- `"12"`와 `"0012"`는 숫자 크기가 같고, 입력에서 `"12"`가 먼저 나왔으므로 `"12"`가 먼저 출력됩니다.

### 예시 2
**Input:**
{TICK}
5
100
99
000099
000100
0
{TICK}
**Output:**
{TICK}
0
99
000099
100
000100
{TICK}

- `"0"`은 숫자 0이므로 가장 먼저 옵니다.
- `"99"`와 `"000099"`는 둘 다 숫자 99를 의미합니다.
  - 같은 수라면 입력에서 먼저 나온 `"99"`가 먼저 출력됩니다.
- `"100"`과 `"000100"`도 둘 다 숫자 100을 의미합니다.
  - 같은 수라면 입력에서 먼저 나온 `"100"`이 먼저 출력됩니다.
- 따라서 정렬 결과는 `0 → 99 → 000099 → 100 → 000100` 순서입니다.

### 예시 3
**Input:**
{TICK}
4
5
05
005
0005
{TICK}
**Output:**
{TICK}
5
05
005
0005
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = r"""import sys

def normalize(s: str) -> str:
    # 앞의 0 제거, 전부 0이면 "0"
    t = s.lstrip('0')
    return t if t else "0"

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = []
    for idx in range(n):
        s = input().strip()
        ns = normalize(s)
        arr.append((len(ns), ns, idx, s))  # (정규화 길이, 정규화 값, 입력순서, 원본)

    # 숫자 크기 비교: (정규화 길이, 정규화 문자열)로 정렬하면 됨
    # 안정성(동일 값이면 입력순서 유지)을 위해 idx 포함
    arr.sort(key=lambda x: (x[0], x[1], x[2]))

    out = []
    for _, __, ___, orig in arr:
        out.append(orig)
    sys.stdout.write("\n".join([x[3] for x in arr]) + "\n")

if __name__ == "__main__":
    main()
"""

def solve_internal(nums: List[str]) -> str:
    def normalize(s: str) -> str:
        t = s.lstrip('0')
        return t if t else "0"

    arr = []
    for idx, s in enumerate(nums):
        ns = normalize(s)
        arr.append((len(ns), ns, idx, s))
    arr.sort(key=lambda x: (x[0], x[1], x[2]))
    return "\n".join([x[3] for x in arr]) + "\n"

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
rng = random.Random(116_2026)

def rand_num_str(max_len: int, heavy_leading_zeros: bool) -> str:
    L = rng.randint(1, max_len)
    if heavy_leading_zeros and rng.random() < 0.7:
        # 앞에 0 많이 붙이기
        core_len = rng.randint(1, max(1, L // 3))
        core = str(rng.randint(0, 10**core_len - 1)).zfill(core_len)
        zeros = "0" * (L - len(core))
        return zeros + core
    # 일반 랜덤
    return "".join(str(rng.randint(0, 9)) for _ in range(L))

test_data: List[List[str]] = []

# 예시 1~3 고정 포함
test_data.append(["12", "0012", "9", "000", "10", "2"])
test_data.append(["100", "99", "000099", "000100", "0"])
test_data.append(["5", "05", "005", "0005"])

# 나머지 17개 생성 (중복/동일값/선행0 많이 포함)
while len(test_data) < 20:
    case_type = len(test_data) % 4
    if case_type == 0:
        n = rng.randint(1, 20)
        nums = [rand_num_str(10, True) for _ in range(n)]
    elif case_type == 1:
        n = rng.randint(50, 200)
        nums = [rand_num_str(30, True) for _ in range(n)]
    elif case_type == 2:
        n = rng.randint(500, 2000)
        nums = [rand_num_str(80, True) for _ in range(n)]
    else:
        # 동일 숫자값을 다양한 0패딩으로 반복 (안정성 체크)
        base = str(rng.randint(0, 99999))
        n = rng.randint(30, 200)
        nums = []
        for i in range(n):
            pad = rng.randint(0, 50)
            if base == "0":
                nums.append("0" * rng.randint(1, 60))
            else:
                nums.append(("0" * pad) + base)
        # 섞기
        rng.shuffle(nums)

    test_data.append(nums)

# 파일 저장
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, nums in enumerate(test_data, 1):
    input_str = str(len(nums)) + "\n" + "\n".join(nums) + "\n"
    ans = solve_internal(nums)

    with open(os.path.join(test_dir, f"input_{i:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"output_{i:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P116' 문제 생성이 완료되었습니다.")
