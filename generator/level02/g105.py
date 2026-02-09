import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P105 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P105")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 가격 변동 구간 정리

## 문제 설명
데이터 분석가 **도윤**은 특정 상품의 가격 변동 기록을 분석하고 있습니다.

가격이 변동된 구간들은 시간 순서와 관계없이 기록되어 있으며,  
각 기록은 가격이 변동된 **시작 시점과 종료 시점**으로 표현됩니다.

도윤은 이 변동 구간들을 정리하여,  
실제로 **연속적으로 가격 변동이 있었던 구간**만을 깔끔하게 정리하려고 합니다.

서로 겹치거나 바로 이어지는 구간은 하나의 구간으로 합칠 수 있습니다.  
단, 서로 떨어져 있는 구간은 합칠 수 없습니다.

주어진 가격 변동 구간 목록을 정리한 뒤,  
겹치거나 이어지는 구간을 모두 병합한 결과를 시간 순서대로 출력하세요.

---

## 입력 형식
- 첫 줄에 가격 변동 구간의 개수 N이 주어집니다.
- 다음 N줄에는 각 구간의 시작 시점과 종료 시점이 주어집니다.
- 각 줄은 `시작 종료` 형식이며, 두 값은 정수입니다.

---

## 출력 형식
- 병합이 완료된 구간의 개수를 첫 줄에 출력합니다.
- 다음 줄부터 병합된 구간을 시작 시점 기준 오름차순으로 출력합니다.
- 각 줄은 `시작 종료` 형식입니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
1 5
3 7
8 10
10 12
15 18
{TICK}

**Output:**
{TICK}
3
1 7
8 12
15 18
{TICK}
- (1,5)와 (3,7)은 겹치므로 (1,7)로 합쳐집니다.
- (8,10)과 (10,12)는 끝과 시작이 같아 이어지므로 (8,12)로 합쳐집니다.
- (1,7)과 (8,12)는 7 다음이 8이라 떨어져 있으므로 합치지 않습니다.

### 예시 2
**Input:**
{TICK}
4
6 8
1 3
2 4
9 11
{TICK}

**Output:**
{TICK}
3
1 4
6 8
9 11
{TICK}
- 입력은 섞여 있지만 시작 시점 기준으로 정렬하면 (1,3), (2,4), (6,8), (9,11) 순서가 됩니다.
- (1,3)과 (2,4)는 겹치므로 (1,4)로 병합됩니다.
- 나머지 구간들은 서로 떨어져 있어 그대로 유지됩니다.

### 예시 3
**Input:**
{TICK}
2
5 6
8 9
{TICK}

**Output:**
{TICK}
2
5 6
8 9
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    intervals = []

    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append((s, e))

    if not intervals:
        print(0)
        return

    # 시작 시점 기준 정렬
    intervals.sort()

    merged = []
    cur_s, cur_e = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_e:  # 겹치거나 이어지는 경우
            cur_e = max(cur_e, e)
        else:
            merged.append((cur_s, cur_e))
            cur_s, cur_e = s, e

    merged.append((cur_s, cur_e))

    print(len(merged))
    for s, e in merged:
        print(s, e)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(intervals):
    if not intervals:
        return "0\n"
    intervals = sorted(intervals)
    merged = []
    cur_s, cur_e = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_e:
            cur_e = max(cur_e, e)
        else:
            merged.append((cur_s, cur_e))
            cur_s, cur_e = s, e
    merged.append((cur_s, cur_e))

    lines = [str(len(merged))]
    for s, e in merged:
        lines.append(f"{s} {e}")
    return "\n".join(lines)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(105)
test_data = []

# 예시 3개
test_data.append([(1, 5), (3, 7), (8, 10), (10, 12), (15, 18)])
test_data.append([(6, 8), (1, 3), (2, 4), (9, 11)])
test_data.append([(5, 6), (8, 9)])

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    intervals = []
    for _ in range(n):
        s = random.randint(0, 1000)
        e = random.randint(s + 1, s + random.randint(1, 50))
        intervals.append((s, e))
    test_data.append(intervals)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, intervals in enumerate(test_data, 1):
    input_lines = [str(len(intervals))]
    for s, e in intervals:
        input_lines.append(f"{s} {e}")
    input_str = "\n".join(input_lines) + "\n"

    ans = solve_internal(intervals)

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print("✅ 'Level01/P105' 문제 생성이 완료되었습니다.")
