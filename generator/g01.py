import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P01")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (입출력 예시 추가)
# ---------------------------------------------------------
md_content = f"""# 배고픈 모험가의 사과 수확 (Apple Harvest)

## 문제 설명
모험가 '**로이**'는 숲을 지나가다 사과나무 한 그루를 발견했습니다. 이 나무에는 $N$개의 사과가 열려 있으며, 각 사과마다 **무게** $W_i$가 다릅니다.

'**로이**'는 배가 많이 고프지만, 너무 작은 사과는 맛이 없어서 무게가 **$K$ 미만**인 사과는 먹지 않기로 했습니다. 

'**로이**'가 수확할 사과의 **개수**와 수확한 모든 사과의 **총 무게**를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 모든 입력 데이터는 **한 줄**로 주어집니다.
* 형식: $N$ $K$ $W_1$ $W_2$ ... $W_N$
* 1 ≤ $N$ ≤ 100, 1 ≤ $K, W_i$ ≤ 1,000

## 출력 형식 (Output Format)
* 첫째 줄에 수확한 사과의 **개수**와 수확한 모든 사과의 **총 무게**를 공백으로 구분하여 출력합니다.
* 수확할 수 있는 사과가 없다면 `0 0`을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
6 150 120 200 150 80 170 145
{TICK}

**Output:**
{TICK}
3 520
{TICK}

> **설명:** 기준 무게 $K=150$ 이상인 사과는 200, 150, 170으로 총 **3개**이며, 이들의 합은 **520**입니다.

### 예시 2
**Input:**
{TICK}
3 500 100 200 300
{TICK}

**Output:**
{TICK}
0 0
{TICK}

> **설명:** 모든 사과의 무게가 500 미만이므로 수확할 수 있는 사과가 없습니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 및 테스트 데이터 정의
# ---------------------------------------------------------
py_solution = """import sys
data = list(map(int, sys.stdin.read().split()))
if data:
    n, k = data[0], data[1]
    weights = data[2:2+n]
    res = [w for w in weights if w >= k]
    if not res:
        print("0 0")
    else:
        print(f"{len(res)} {sum(res)}")
"""

test_cases = [
    [6, 150, 120, 200, 150, 80, 170, 145], [3, 500, 100, 200, 300],
    [1, 100, 100], [1, 100, 99], [5, 1, 1, 1, 1, 1, 1],
    [5, 1000, 999, 999, 999, 999, 999], [10, 50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    [100, 500] + [499]*100, [100, 500] + [500]*100,
    [100, 1] + [random.randint(1, 1000) for _ in range(100)],
    [50, 300] + [random.randint(100, 500) for _ in range(50)],
    [5, 200, 200, 200, 200, 200, 200], [10, 100, 0, 0, 0, 0, 0, 100, 101, 102, 103, 104],
    [4, 250, 249, 251, 249, 251], [8, 777, 776, 777, 778, 1, 1000, 500, 777, 800],
    [2, 1000, 1000, 1000], [2, 1000, 999, 999],
    [20, 10] + [random.choice([5, 15]) for _ in range(20)],
    [15, 333] + [i*10 for i in range(1, 16)],
    [30, 800] + [random.randint(750, 850) for _ in range(30)]
]

# ---------------------------------------------------------
# 4. 파일 저장 실행
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution_01.py"), py_solution)

for i, case in enumerate(test_cases, 1):
    n, k = case[0], case[1]
    weights = case[2:2+n]
    input_str = " ".join(map(str, case[:2+n]))
    save_file(os.path.join(base_dir, f"input_{i:02d}.txt"), input_str)
    
    picked = [w for w in weights if w >= k]
    output_str = f"{len(picked)} {sum(picked)}" if picked else "0 0"
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), output_str)

print(f"✅ Easy/P01 내부에 입출력 예시가 포함된 problem.md와 테스트케이스가 생성되었습니다.")