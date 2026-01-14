import os
import random

# 1. 디렉토리 설정
base_dir = "P01"
if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 생성 (problem_01.md)
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

**Example 1**
Input: {TICK}6 150 120 200 150 80 170 145{TICK}
Output: {TICK}3 520{TICK}

**Example 2**
Input: {TICK}3 500 100 200 300{TICK}
Output: {TICK}0 0{TICK}
"""

# ---------------------------------------------------------
# 3. 테스트케이스 데이터 생성 (20개)
# ---------------------------------------------------------
test_cases = [
    [6, 150, 120, 200, 150, 80, 170, 145],  # 1: 기본 예제 1
    [3, 500, 100, 200, 300],                # 2: 기본 예제 2
    [1, 100, 100],                          # 3: N=1, 무게가 딱 K인 경우
    [1, 100, 99],                           # 4: N=1, 무게가 K 미만
    [5, 1, 1, 1, 1, 1, 1],                  # 5: K=1 (모두 수확)
    [5, 1000, 999, 999, 999, 999, 999],     # 6: K가 매우 커서 아무도 못 먹는 경우
    [10, 50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], # 7: 절반 수확
    [100, 500] + [499]*100,                 # 8: N=100 (최대), 전부 미달
    [100, 500] + [500]*100,                 # 9: N=100 (최대), 전부 통과
    [100, 1] + [random.randint(1, 1000) for _ in range(100)], # 10: 랜덤 데이터 1
    [50, 300] + [random.randint(100, 500) for _ in range(50)], # 11: 랜덤 데이터 2
    [5, 200, 200, 200, 200, 200, 200],      # 12: 모든 값이 K와 동일
    [10, 100, 0, 0, 0, 0, 0, 100, 101, 102, 103, 104], # 13: 0 점수 포함 (경계)
    [4, 250, 249, 251, 249, 251],           # 14: K 근처 값들
    [8, 777, 776, 777, 778, 1, 1000, 500, 777, 800], # 15: 행운의 숫자 경계
    [2, 1000, 1000, 1000],                  # 16: N=2, 둘 다 합격
    [2, 1000, 999, 999],                    # 17: N=2, 둘 다 불합격
    [20, 10, 5, 15, 5, 15, 5, 15, 5, 15, 5, 15, 5, 15, 5, 15, 5, 15, 5, 15, 5, 15], # 18: 반복 패턴
    [15, 333] + [i*10 for i in range(1, 16)], # 19: 수열 형태
    [30, 800] + [random.randint(750, 850) for _ in range(30)] # 20: 랜덤 밀집 영역
]

# ---------------------------------------------------------
# 4. 파일 저장 및 실행
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# MD 및 정답 코드 저장
save_file(os.path.join(base_dir, "problem.md"), md_content)

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
save_file(os.path.join(base_dir, "solution_01.py"), py_solution)

# 테스트케이스 파일 생성
for i, case in enumerate(test_cases, 1):
    n, k = case[0], case[1]
    weights = case[2:2+n]
    
    # 입력 파일 저장
    input_str = " ".join(map(str, case[:2+n]))
    save_file(os.path.join(base_dir, f"input_{i}.txt"), input_str)
    
    # 출력 파일 저장 (로직 계산)
    picked = [w for w in weights if w >= k]
    if not picked:
        output_str = "0 0"
    else:
        output_str = f"{len(picked)} {sum(picked)}"
    save_file(os.path.join(base_dir, f"output_{i}.txt"), output_str)

print(f"✅ 'P01' 디렉토리에 20개의 테스트케이스와 수정된 마크다운 생성이 완료되었습니다.")