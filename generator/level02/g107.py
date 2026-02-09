import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P107 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P107")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 회의 일정 우선순위 정리

## 문제 설명
팀 리더 **민수**는 하루 동안 여러 회의 일정을 관리해야 합니다.

각 회의는 `회의ID`, `시작 시각`, `종료 시각`, `중요도`로 구성됩니다.
회의 시각은 분 단위 정수로 표현되며, 하루는 0분부터 시작합니다.
기본적으로 선택된 회의들끼리는 **서로 시간이 겹치지 않아야** 합니다.

민수는 회의 일정이 서로 겹치는 경우,  
**중요도가 높은 회의를 우선적으로 유지**하고  
중요도가 같다면 **회의 시간이 더 짧은 회의**를 선택하려고 합니다.

회의를 위 기준에 따라 선택하고 정렬하세요.

---

## 입력 형식
- 첫 줄에 회의 개수 N이 주어집니다.
- 다음 N줄에 `회의ID 시작 종료 중요도` 가 주어집니다.

---

## 출력 형식
- 선택된 회의 개수를 첫 줄에 출력합니다.
- 다음 줄부터 선택된 회의를 시작 시각 기준으로 출력합니다.
- 각 줄은 `회의ID 시작 종료 중요도` 형식입니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
1 60 120 3
2 90 150 5
3 160 200 2
4 140 180 5
{TICK}

**Output:**
{TICK}
1
4 140 180 5
{TICK}
- 회의 1(60~120)과 회의 2(90~150)는 시간이 겹치며, 중요도가 더 높은 회의 2가 선택됩니다.
- 회의 2(90~150)와 회의 4(140~180)는 시간이 겹치고 중요도가 같으므로, 회의 시간이 더 짧은 회의 4가 선택됩니다.
- 회의 3(160~200)은 선택된 회의 4(140~180)와 시간이 겹치며 중요도가 더 낮아 제외됩니다.
- 최종적으로 선택된 회의는 회의 4 하나입니다.

### 예시 2
**Input:**
{TICK}
6
10 0 60 3
11 30 50 3
12 45 80 4
13 80 120 2
14 100 110 2
15 110 140 2
{TICK}

**Output:**
{TICK}
3
12 45 80 4
14 100 110 2
15 110 140 2
{TICK}
- 회의 10(0~60)과 11(30~50)은 겹칩니다. 중요도가 같으므로 더 짧은 회의 11을 선택합니다.
- 회의 11(30~50)과 12(45~80)은 겹칩니다. 12의 중요도가 더 높으므로 회의 12를 선택합니다. 
- 회의 12(45~80) 다음으로 회의 13(80~120)은 겹치지 않으므로 일단 추가합니다.
- 회의 13(80~120)과 14(100~110)은 겹칩니다. 중요도가 같으므로 더 짧은 회의 14를 선택합니다.
- 회의 15(110~140)는 앞의 회의시간과 겹치지 않으므로 추가합니다.

### 예시 3
**Input:**
{TICK}
3
20 10 20 5
19 10 20 5
21 20 30 1
{TICK}

**Output:**
{TICK}
2
19 10 20 5
21 20 30 1
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    meetings = []

    for _ in range(n):
        mid, s, e, p = map(int, input().split())
        meetings.append((mid, s, e, p))

    # 시작 시각 기준 정렬
    meetings.sort(key=lambda x: x[1])

    selected = []

    for m in meetings:
        if not selected:
            selected.append(m)
            continue

        last = selected[-1]
        # 겹치지 않으면 그대로 추가
        if m[1] >= last[2]:
            selected.append(m)
        else:
            # 겹치면 우선순위 비교
            _, s1, e1, p1 = last
            _, s2, e2, p2 = m

            dur1 = e1 - s1
            dur2 = e2 - s2

            replace = False
            if p2 > p1:
                replace = True
            elif p2 == p1:
                if dur2 < dur1:
                    replace = True
                elif dur2 == dur1:
                    if m[0] < last[0]:
                        replace = True

            if replace:
                selected[-1] = m

    # 출력은 시작 시각 기준
    selected.sort(key=lambda x: x[1])

    print(len(selected))
    for m in selected:
        print(*m)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용) 
# ---------------------------------------------------------
def solve_internal(meetings):
    meetings = sorted(meetings, key=lambda x: x[1])
    selected = []

    for m in meetings:
        if not selected:
            selected.append(m)
            continue

        last = selected[-1]
        if m[1] >= last[2]:
            selected.append(m)
        else:
            _, s1, e1, p1 = last
            _, s2, e2, p2 = m
            dur1 = e1 - s1
            dur2 = e2 - s2

            replace = False
            if p2 > p1:
                replace = True
            elif p2 == p1:
                if dur2 < dur1:
                    replace = True
                elif dur2 == dur1 and m[0] < last[0]:
                    replace = True

            if replace:
                selected[-1] = m

    selected.sort(key=lambda x: x[1])

    lines = [str(len(selected))]
    for m in selected:
        lines.append(" ".join(map(str, m)))

    # 여기서 끝 개행까지 포함해서 반환
    return "\n".join(lines) + "\n"

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개)
# ---------------------------------------------------------
random.seed(107)
test_data = []

# 예시 3개
test_data.append([
    (1, 60, 120, 3),
    (2, 90, 150, 5),
    (3, 160, 200, 2),
    (4, 140, 180, 5),
])

test_data.append([
    (10, 0, 60, 3),
    (11, 30, 50, 3),
    (12, 45, 80, 4),
    (13, 80, 120, 2),
    (14, 100, 110, 2),
    (15, 110, 140, 2),
])

test_data.append([
    (20, 10, 20, 5),
    (19, 10, 20, 5),
    (21, 20, 30, 1),
])

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 90)
    meetings = []
    used = set()
    for _ in range(n):
        while True:
            mid = random.randint(1, 500)
            if mid not in used:
                used.add(mid)
                break
        s = random.randint(0, 1200)
        e = random.randint(s + 1, s + random.randint(5, 180))
        p = random.randint(1, 5)
        meetings.append((mid, s, e, p))
    test_data.append(meetings)

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성 
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, meetings in enumerate(test_data, 1):
    # input 파일
    input_lines = [str(len(meetings))]
    for m in meetings:
        input_lines.append(" ".join(map(str, m)))
    input_str = "\n".join(input_lines) + "\n"

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    # output 파일: ans 자체에 이미 끝 개행 포함 
    ans = solve_internal(meetings)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P107' 문제 생성이 완료되었습니다.")