import os
import random
import string
from functools import cmp_to_key

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P096 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P096")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 가장 작은 안내 코드 만들기

## 문제 설명
시설 관리자 **유나**는 방문객에게 제공할 **안내 코드**를 생성하고 있습니다.

안내 코드는 여러 개의 **토큰(문자열)** 을 한 줄로 **이어 붙인 문자열**로 만들어집니다.  
유나는 코드가 가능한 한 짧고 깔끔하게 보이도록, 이어 붙인 결과가 **사전식으로 가장 작은 문자열**이 되도록 안내코드를 정하려고 합니다.

토큰 배열이 주어질 때, 모든 토큰을 이어 붙여 만들 수 있는 결과 중  
**사전식으로 가장 작은 문자열**을 출력하세요.

- ["A3", "A30", "B"] → "A30A3B" 가 더 작습니다. <br/>( "A30A3B" < "A3A30B" )

 결과는 매우 길어질 수 있으므로 그대로 문자열로 출력하세요. 모든 토큰이 숫자 '0'만으로 이루어진 경우(예: "0", "00") 결과는 "0"을 출력합니다.

---

## 입력 형식 (Input Format)
- 첫째 줄에 토큰 개수가 정수 N으로 주어진다.
- 둘째 줄 N개의 토큰이 문자열로 주어진다.
- 각 토큰은 길이 1 이상 10 이하
- 각 토큰은 영문 대문자(A~Z)와 숫자(0~9)로만 구성

---

## 출력 형식 (Output Format)
- 만들 수 있는 가장 작은 문자열을 출력한다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
A3 A30 B
{TICK}
**Output:**
{TICK}
A30A3B
{TICK}
- "A30"과 "A3"은 "A30A3"와 "A3A30" 중 더 작은 쪽이 앞에 오도록 정렬합니다.

### 예시 2
**Input:**
{TICK}
4
Z9 A1 A10 B2
{TICK}
**Output:**
{TICK}
A10A1B2Z9
{TICK}
- 토큰을 이어 붙인 문자열이 사전식으로 가장 작아지도록 배치합니다.

### 예시 3
**Input:**
{TICK}
3
0 00 000
{TICK}
**Output:**
{TICK}
0
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
#    - 비교 기준: a+b vs b+a (오름차순)
# ---------------------------------------------------------
solution_py = """import sys
from functools import cmp_to_key

def cmp(a: str, b: str) -> int:
    if a + b < b + a:
        return -1
    if a + b > b + a:
        return 1
    return 0

def is_all_zero_tokens(tokens):
    # 모든 토큰이 '0'만으로 구성되면 True
    for t in tokens:
        if any(ch != '0' for ch in t):
            return False
    return True

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    tokens = input().split()
    tokens = tokens[:n]

    tokens.sort(key=cmp_to_key(cmp))
    if is_all_zero_tokens(tokens):
        print("0")
    else:
        print("".join(tokens))

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def cmp_internal(a: str, b: str) -> int:
    if a + b < b + a:
        return -1
    if a + b > b + a:
        return 1
    return 0

def is_all_zero_tokens_internal(tokens):
    for t in tokens:
        for ch in t:
            if ch != "0":
                return False
    return True

def solve_internal(tokens):
    tokens = sorted(tokens, key=cmp_to_key(cmp_internal))
    if is_all_zero_tokens_internal(tokens):
        return "0"
    return "".join(tokens)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(96)
test_data = []

# 예시 3개
test_data.append(["A3", "A30", "B"])
test_data.append(["Z9", "A1", "A10", "B2"])
test_data.append(["0", "00", "000"])

def rand_token():
    # 영문+숫자 혼합 토큰 생성 (길이 1~10)
    L = random.randint(1, 10)
    chars = []
    for _ in range(L):
        chars.append(random.choice(string.ascii_uppercase + "0123456789"))
    return "".join(chars)

for _ in range(17):
    n = random.randint(1, 200)
    mode = random.randint(1, 7)

    if mode == 1:
        tokens = [rand_token() for _ in range(n)]

    elif mode == 2:
        # 접두어가 비슷한 토큰 (정렬 비교가 중요한 케이스)
        base = random.choice(["A", "B", "Z", "K"])
        tokens = []
        for _ in range(n):
            tail_len = random.randint(0, 4)
            tail = "".join(random.choice("0123456789") for _ in range(tail_len))
            tokens.append(base + tail if tail else base)

    elif mode == 3:
        # 숫자 토큰 위주
        tokens = []
        for _ in range(n):
            L = random.randint(1, 10)
            tokens.append("".join(random.choice("0123456789") for _ in range(L)))

    elif mode == 4:
        # 모두 0 토큰 섞기 (정답이 0이 나오도록)
        tokens = []
        for _ in range(n):
            L = random.randint(1, 10)
            tokens.append("0" * L)

    elif mode == 5:
        # 한 글자 토큰만 (정렬 직관 확인)
        tokens = [random.choice(string.ascii_uppercase + "0123456789") for _ in range(n)]

    elif mode == 6:
        # 대문자 1개 + 숫자 여러 개 (코드 느낌)
        tokens = []
        for _ in range(n):
            head = random.choice(string.ascii_uppercase)
            dlen = random.randint(0, 6)
            tail = "".join(random.choice("0123456789") for _ in range(dlen))
            tokens.append(head + tail)

    else:
        # 중복 많음
        pool = [rand_token() for _ in range(random.randint(1, 6))]
        tokens = [random.choice(pool) for _ in range(n)]

    test_data.append(tokens)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, tokens in enumerate(test_data, 1):
    n = len(tokens)
    input_str = f"{n}\n" + " ".join(tokens) + "\n"
    ans = solve_internal(tokens)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P096' 문제 생성이 완료되었습니다. ")
