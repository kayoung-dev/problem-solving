import os

# 1. 디렉토리 설정
base_dir = "P01"
if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 생성 (problem_01.md)
# ---------------------------------------------------------
# '로이' 표시 방식을 바깥쪽 작은따옴표 + 안쪽 굵게 형식으로 변경하여 깨짐 방지
md_content = f"""# 문제 01. 배고픈 모험가의 사과 수확 (Apple Harvest)

## 문제 설명
모험가 '**로이**'는 숲을 지나가다 사과나무 한 그루를 발견했습니다. 이 나무에는 $N$개의 사과가 열려 있으며, 각 사과마다 **무게**가 다릅니다.

'**로이**'는 배가 많이 고프지만, 너무 작은 사과는 맛이 없어서 무게가 **$K$ 미만**인 사과는 먹지 않기로 했습니다. 

'**로이**'가 수확할 사과의 **개수**와 수확한 사과들의 **전체 무게의 합**을 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 모든 입력 데이터는 **한 줄**로 주어집니다.
* 형식: $N$ $K$ $W_1$ $W_2$ ... $W_N$
* 1 ≤ $N$ ≤ 100, 1 ≤ $K, W_i$ ≤ 1,000

## 출력 형식 (Output Format)
* 첫째 줄에 수확한 사과의 **개수**와 **총 무게**를 공백으로 구분하여 출력합니다.
* 수확할 수 있는 사과가 없다면 `0 0`을 출력합니다.

---

## 입출력 예시 (Sample I/O)

**Example 1**
Input: {TICK}6 150 120 200 150 80 170 145{TICK}
Output: {TICK}3 520{TICK}

**Example 2**
Input: {TICK}3 500 100 200 300{TICK}
Output: {TICK}0 0{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 및 테스트케이스 생성 (이전과 동일)
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# MD 파일 저장
save_file(os.path.join(base_dir, "problem_01.md"), md_content)

# (참고: 아래는 기존과 동일한 로직입니다)
py_solution = """import sys
data = list(map(int, sys.stdin.read().split()))
if data:
    n, k = data[0], data[1]
    weights = data[2:2+n]
    res = [w for w in weights if w >= k]
    print(f"{len(res)} {sum(res)}")
"""
save_file(os.path.join(base_dir, "solution_01.py"), py_solution)

test_cases = [
    [6, 150, 120, 200, 150, 80, 170, 145],
    [3, 500, 100, 200, 300],
    [5, 1, 10, 20, 30, 40, 50],
    [1, 100, 100],
    [10, 200, 150, 250, 150, 250, 150, 250, 150, 250, 150, 250]
]

for i, case in enumerate(test_cases, 1):
    save_file(os.path.join(base_dir, f"input_{i}.txt"), " ".join(map(str, case)))
    n, k = case[0], case[1]
    picked = [w for w in case[2:2+n] if w >= k]
    save_file(os.path.join(base_dir, f"output_{i}.txt"), f"{len(picked)} {sum(picked)}")

print(f"'P01' 디렉토리에 서식이 수정된 파일 생성이 완료되었습니다.")