import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P108 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P108")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 무빙워크 도착 그룹

## 문제 설명
공항 직원 **지훈**은 무빙워크(움직이는 보도)를 이용하는 사람들의 흐름을 관찰하고 있습니다.

무빙워크의 끝 지점까지의 거리 \(L\) (단위: m)가 주어집니다.  
각 $i$번째 사람은 다음 정보를 가집니다. 

- 현재 위치 $p_i$ (시작점으로부터 떨어진 거리, $0 \le p_i < L$)
- 걷는 속도 $v_i$ (m/min, $v_i > 0$)

모든 사람은 무빙워크 위에서 끝 지점 \(L\)을 향해 같은 방향으로 이동합니다.

사람들은 앞사람을 추월할 수 없습니다.
하지만 뒤에 있는 사람이 더 빠르게 걸어서 앞사람을 따라잡으면, 그 순간부터는
앞사람 옆에서 **같은 속도(앞사람 속도)** 로 함께 이동합니다.

이렇게 함께 이동하는 사람들의 묶음을 **도착 그룹**이라고 합니다.

- 도착 그룹은 한 명일 수도 있고, 여러 명이 붙어 이동하는 상태일 수도 있습니다.
- 어떤 사람이 **끝 지점 \(L\)에서** 다른 그룹을 따라잡는 경우도 같은 그룹으로 봅니다.

끝 지점에 도착하는 **도착 그룹의 개수**를 출력하세요.

---

## 입력 형식
- 첫 줄에 무빙워크 길이 \(L\)과 사람 수 \(N\)이 공백으로 주어집니다.
- 다음 \(N\)줄에 각 사람의 `위치 속도`가 주어집니다.

---

## 출력 형식
- 끝 지점에 도착하는 도착 그룹의 개수를 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
12 5
10 2
8 4
0 1
5 1
3 3
{TICK}

**Output:**
{TICK}
3
{TICK}
- 각 사람의 도착 시간은 $\\frac{{L - p_i}}{{v_i}}$ 입니다. 
  - (10,2) → 1
  - (8,4) → 1
  - (5,1) → 7
  - (3,3) → 3
  - (0,1) → 12
- 끝 지점에 가까운 순서로 보면,
  - (10,2)와 (8,4)는 도착 시간이 같아 끝 지점에서 만나므로 같은 그룹입니다.
  - (5,1)은 더 늦게 도착하므로 새로운 그룹입니다.
  - (3,3)은 (5,1)을 따라잡아 같은 그룹이 됩니다.
  - (0,1)은 앞 그룹들을 따라잡지 못해 새로운 그룹입니다.

### 예시 2
**Input:**
{TICK}
20 6
18 1
12 2
6 4
4 1
3 6
1 1
{TICK}

**Output:**
{TICK}
4
{TICK}
- 각 사람의 도착 시간은 $\\frac{{L - p_i}}{{v_i}}$ 로 계산합니다.
  - (18, 1) → (20−18)/1 = 2
  - (12, 2) → (20−12)/2 = 4
  - (6, 4) → (20−6)/4 = 3.5
  - (4, 1) → (20−4)/1 = 16
  - (3, 6) → (20−3)/6 ≈ 2.83
  - (1, 1) → (20−1)/1 = 19
- 끝 지점에 가까운 사람부터(위치가 큰 순서) 확인합니다.
  - (18, 1)은 가장 앞에 있으며 도착 시간이 2입니다. (새로운 그룹 생성)
  - (12, 2)는 도착 시간이 4로 더 늦기 때문에, 앞 그룹을 따라잡지 못합니다. (새로운 그룹 생성)
  - (6, 4)는 도착 시간이 3.5로, 바로 앞 그룹(12, 2)의 도착 시간 4보다 빠르므로 따라잡아 같은 그룹이 됩니다.
  - (4, 1)은 도착 시간이 16으로 매우 늦어 앞 그룹들을 따라잡지 못합니다. (새로운 그룹 생성)
  - (3, 6)은 도착 시간이 약 2.83으로, 앞에 있는 (4, 1)을 따라잡아 같은 그룹이 됩니다.
  - (1, 1)은 도착 시간이 19로 가장 늦어, 앞 그룹들을 따라잡지 못하고 (새로운 그룹 생성)

### 예시 3
**Input:**
{TICK}
10 3
2 2
4 1
6 1
{TICK}

**Output:**
{TICK}
2
{TICK}
- 각 사람의 도착 시간
  - (6, 1) → (10−6)/1 = 4
  - (4, 1) → (10−4)/1 = 6
  - (2, 2) → (10−2)/2 = 4

- 끝 지점에 가까운 사람부터(위치가 큰 순서) 확인합니다.
  - (6, 1)은 가장 앞에 있으며 도착 시간이 4입니다. (새로운 그룹 생성)
  - (4, 1)은 도착 시간이 6으로 더 늦기 때문에, 앞 그룹을 따라잡지 못합니다. (새로운 그룹 생성)
  - (2, 2)는 도착 시간이 4로, 앞에 있는 (4, 1)의 도착 시간 6보다 빠르므로 따라잡아 같은 그룹이 됩니다.

- 결과적으로 목적지에 도착하는 그룹은 총 2개입니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    L, N = map(int, input().split())
    people = []
    for _ in range(N):
        p, v = map(int, input().split())
        people.append((p, v))

    # 끝 지점에 가까운 순(위치 내림차순) 정렬
    people.sort(key=lambda x: x[0], reverse=True)

    groups = 0
    max_time = -1.0

    for p, v in people:
        t = (L - p) / v
        # 뒤 사람이 도착 시간이 더 늦으면(큰 값이면) 앞 그룹을 따라잡지 못해 새 그룹
        if t > max_time:
            groups += 1
            max_time = t
        # t <= max_time 이면 앞 그룹을 따라잡아 합쳐짐

    print(groups)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(L, people):
    people = sorted(people, key=lambda x: x[0], reverse=True)

    groups = 0
    max_num = -1
    max_den = 1

    for p, v in people:
        num = L - p
        den = v
        if max_num < 0 or num * max_den > max_num * den:
            groups += 1
            max_num, max_den = num, den

    return f"{groups}\n"

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개) 
# ---------------------------------------------------------
random.seed(108)
test_cases = []

# (A) 예시 3개 (problem.md와 일치)
test_cases.append((12, [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]))  # 3
test_cases.append((20, [(18, 1), (12, 2), (6, 4), (4, 1), (3, 6), (1, 1)]))  # 4
test_cases.append((10, [(2, 2), (4, 1), (6, 1)]))  # 2

# (B) 목적지에서 "딱 합류"하는 케이스 (도착 시간 동일)
# L=10, (8,1)->2, (6,2)->2 : 끝에서 만나도 같은 그룹
test_cases.append((10, [(8, 1), (6, 2), (1, 1)]))  # 앞 둘 합류, (1,1)은 별도 -> 2

# (C) 이미 앞사람이 느려서 뒤가 연쇄적으로 합류하는 케이스
test_cases.append((30, [(29, 1), (20, 10), (10, 10), (0, 10)]))  # (20,10)->1, (29,1)->1 합류, 나머지도 합류 -> 1

# (D) 아무도 합류 못 하는 케이스 (앞으로 갈수록 더 빨리 도착)
# 위치가 앞일수록 더 빨라서 뒤는 더 늦게 도착 -> 모두 분리
test_cases.append((50, [(45, 1), (30, 1), (10, 1), (0, 1)]))  # 모두 같은 속도 -> 4

# (E) 같은 도착시간이 여러 개 섞인 케이스 (동시간 다발)
# L=60: (50,5)->2, (40,10)->2, (30,15)->2, (10,5)->10
test_cases.append((60, [(50, 5), (40, 10), (30, 15), (10, 5)]))  # 앞 3 합류 1그룹 + 1개 -> 2

# (F) 랜덤 케이스 13개: 합류/비합류가 섞이도록 생성
def gen_case():
    L = random.randint(20, 300)
    N = random.randint(5, min(120, L))  # 위치 중복 방지 위해 L 제한 고려
    positions = random.sample(range(0, L), N)

    people = []
    for p in positions:
        # 속도 분포를 넓게: 합류/비합류 섞이게
        v = random.randint(1, 50)
        people.append((p, v))
    return (L, people)

for _ in range(13):
    test_cases.append(gen_case())

assert len(test_cases) == 20

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성 
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, (L, people) in enumerate(test_cases, 1):
    # input 파일: 실제 개행
    input_lines = [f"{L} {len(people)}"]
    for p, v in people:
        input_lines.append(f"{p} {v}")
    input_str = "\n".join(input_lines) + "\n"

    with open(os.path.join(test_dir, f"input_{idx:02d}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)

    # output 파일: solve_internal이 끝 개행 포함 
    ans = solve_internal(L, people)
    with open(os.path.join(test_dir, f"output_{idx:02d}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print("✅ 'Level01/P108' 문제 생성이 완료되었습니다.")