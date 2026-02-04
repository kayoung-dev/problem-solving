import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P167 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P167")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "불량품 시작점 찾기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
공장 관리자 소연이는 생산 라인에서 나오는 제품들을 검사하여 기록하고 있습니다. 어느 날 기계에 결함이 발생하여 특정 시점부터 생산된 모든 제품이 '불량'으로 판정되기 시작했습니다.

검사 기록에는 정상 제품은 $0$, 불량 제품은 $1$로 기록되어 있습니다. 기록은 시간 순서대로 정렬되어 있으므로 `[0, 0, ..., 1, 1]`과 같은 형태를 가집니다. 소연이는 기계가 정확히 언제부터 고장 났는지 파악하기 위해, **처음으로 불량 제품(1)이 나타난 위치**를 찾으려고 합니다.

제품 검사 기록 리스트가 주어질 때, 첫 번째 불량 제품의 인덱스를 구하는 프로그램을 작성하세요. 위치는 $0$번부터 시작하며, 만약 모든 제품이 정상($0$)이라면 $-1$을 출력해야 합니다. 대규모 데이터를 처리해야 하므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



## input_description
- 첫 번째 줄에는 검사한 제품의 개수 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 두 번째 줄에는 $0$ 또는 $1$로 이루어진 $N$개의 검사 결과가 공백으로 구분되어 오름차순으로 주어집니다.

## output_description
- 불량 제품($1$)이 처음으로 등장하는 위치의 인덱스를 정수로 출력합니다.
- 만약 불량 제품이 하나도 없다면 $-1$을 출력합니다.

# samples

### input 1
{TICK}
6
0 0 0 1 1 1
{TICK}

### output 1
{TICK}
3
{TICK}
- 인덱스 3에서 처음으로 불량 제품인 1이 나타났으므로 3을 출력합니다.

### input 2
{TICK}
4
0 0 0 0
{TICK}

### output 2
{TICK}
-1
{TICK}
- 모든 제품이 정상(0)이므로 불량 제품의 시작점이 존재하지 않아 -1을 출력합니다.

### input 3
{TICK}
3
1 1 1
{TICK}

### output 3
{TICK}
0
{TICK}
- 첫 번째 제품부터 불량품이므로 인덱스 0을 출력합니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    records = data[1:]

    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        # 불량품(1)을 찾으면 일단 결과에 저장하고 더 앞쪽을 탐색
        if records[mid] == '1':
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    # 11~20번은 시간복잡도 검증을 위해 $N=100,000$ 수준으로 생성
    if i <= 10:
        n = random.randint(1, 100)
    else:
        n = random.randint(90000, 100000)
    
    # 케이스 유형 결정
    case_type = random.random()
    if case_type < 0.1: # 전부 0
        ans_idx = -1
        records = [0] * n
    elif case_type < 0.2: # 전부 1
        ans_idx = 0
        records = [1] * n
    else: # 중간 어딘가에서 바뀜
        ans_idx = random.randint(0, n - 1)
        records = [0] * ans_idx + [1] * (n - ans_idx)

    input_str = f"{n}\n" + " ".join(map(str, records))
    ans_str = str(ans_idx)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level01/P167' 문제 생성이 완료되었습니다. ")