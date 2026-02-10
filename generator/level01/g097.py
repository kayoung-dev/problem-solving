import os
import random
import string

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P097 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P097")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""# 발표 순서 자동 배정

## 문제 설명
학회 운영자 **지수**는 발표 순서를 빠르게 정리해야 합니다.
각 발표자는 다음 정보를 가집니다.
- 발표자 이름(공백 없는 문자열)
- 발표 시간(분)
- 등록 번호(정수)

지수는 아래 규칙으로 발표 순서를 정합니다.

1. **발표 시간이 짧은 발표자부터** 먼저 배치한다.
2. 발표 시간이 같다면 **등록 번호가 작은 발표자부터** 먼저 배치한다.

정렬된 발표자 이름을 순서대로 출력하세요.

---

## 입력 형식 (Input Format)
- 첫번째 줄에 발표자 수 N이 주어집니다.  
- 그 다음 N줄에 걸쳐 `이름 시간 등록번호`가 공백으로 구분되어 주어집니다.

---

## 출력 형식 (Output Format)
- 정렬된 발표자 이름을 한 줄에 하나씩 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
MINA 12 104
JUN 8 120
SORA 12 101
HYUN 5 300
DAON 8 110
{TICK}
**Output:**
{TICK}
HYUN
DAON
JUN
SORA
MINA
{TICK}
- 시간 5분인 HYUN이 가장 먼저 배치됩니다.
- 8분인 DAON(등록 110)이 JUN(등록 120)보다 먼저 배치됩니다.
- 12분인 SORA(등록 101)이 MINA(등록 104)보다 먼저 배치됩니다.

### 예시 2
**Input:**
{TICK}
3
ALEX 10 2
BORA 10 1
CHRIS 7 9
{TICK}
**Output:**
{TICK}
CHRIS
BORA
ALEX
{TICK}
- 7분인 CHRIS가 먼저 배치됩니다.
- 10분끼리는 등록 번호가 작은 BORA가 ALEX보다 먼저 배치됩니다.

### 예시 3
**Input:**
{TICK}
1
KIM 15 77
{TICK}
**Output:**
{TICK}
KIM
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)

    people = []
    for _ in range(n):
        name, t, reg = input().split()
        t = int(t)
        reg = int(reg)
        people.append((t, reg, name))

    people.sort()  # (time asc, reg asc, name) - name은 동률 깨기용(문제에 영향 없음)
    for _, __, name in people:
        print(name)

if __name__ == "__main__":
    solve()
"""


# ---------------------------------------------------------
# 4. 내부 풀이 (정답 생성용)
# ---------------------------------------------------------
def solve_internal(rows):
    people = [(t, reg, name) for (name, t, reg) in rows]
    people.sort()
    return "\n".join(name for _, __, name in people)

# ---------------------------------------------------------
# 5. 테스트케이스 생성 (20개) - "사람 이름" 사용
# ---------------------------------------------------------
random.seed(97)

# 자연스러운 이름 풀(대문자/로마자, 공백 없음)
NAME_POOL = [
    # Korean romanization style
    "JIHUN", "SEYEON", "MINJAE", "HAEUN", "DOYUN", "YUNA", "JISU", "JIMIN",
    "TAEHOON", "SUAH", "DAEUN", "SUNGHO", "YOUNGHO", "HYEJIN", "SOHYUN",
    "JUNSEO", "JIWON", "SEJIN", "HYERIN", "DONGWOO", "SEUNGMIN", "JAEYOUNG",
    "HANA", "YERIM", "SOYOUNG", "MINSEO", "DAHYUN", "GUNWOO", "YONGJUN",
    "EUNJI", "EUNSOO", "HYEONSU", "HYEONWOO", "SEUNGHOON", "YOONSEO",
    "SANGMIN", "SANGWOO", "NAYEON", "YUJIN", "YEJUN",
    # English names
    "ALEX", "CHRIS", "EMMA", "OLIVIA", "NOAH", "LIAM", "SOPHIA", "MASON",
    "ETHAN", "AVA", "MIA", "LUCAS", "JAMES", "BEN", "DANIEL", "GRACE",
    "RACHEL", "HANNAH", "AMY", "JACK", "KATE", "SARAH", "LEO", "NICK",
    "IVAN", "ERIC", "KEVIN", "RYAN", "JASON", "TOM",
    # Extra short names
    "MINA", "JUN", "SORA", "HYUN", "DAON", "BORA", "KIM"
]

def unique_names(n, rnd):
    """
    n개 이름을 중복 없이 생성.
    풀에서 뽑고 부족하면 뒤에 숫자를 붙여 유니크 보장.
    """
    names = []
    used = set()

    pool = NAME_POOL[:]
    rnd.shuffle(pool)

    idx = 0
    while len(names) < n:
        if idx < len(pool):
            base = pool[idx]
            idx += 1
        else:
            base = rnd.choice(NAME_POOL)

        name = base
        if name in used:
            # 중복이면 숫자 붙이기
            suffix = 2
            while f"{base}{suffix}" in used:
                suffix += 1
            name = f"{base}{suffix}"

        used.add(name)
        names.append(name)

    return names

def gen_case(rnd):
    n = rnd.randint(1, 200)
    mode = rnd.randint(1, 7)

    names = unique_names(n, rnd)
    regs = rnd.sample(range(1, 10**6), n)

    rows = []

    if mode == 1:
        # 완전 랜덤
        for i in range(n):
            t = rnd.randint(1, 60)
            rows.append((names[i], t, regs[i]))

    elif mode == 2:
        # 시간이 동일(등록번호로만 정렬 확인)
        fixed_t = rnd.randint(1, 60)
        for i in range(n):
            rows.append((names[i], fixed_t, regs[i]))

    elif mode == 3:
        # 시간이 좁은 범위(동률 많이)
        for i in range(n):
            t = rnd.randint(1, 5)
            rows.append((names[i], t, regs[i]))

    elif mode == 4:
        # 시간은 랜덤, 등록번호는 일부 근접(타이브레이크 확인용)
        base_reg = rnd.randint(1, 10**6 - 1000)
        close_regs = [base_reg + rnd.randint(0, 999) for _ in range(n)]
        # close_regs에도 중복 가능 → 안전하게 섞어서 사용(등록번호 중복 허용해도 문제는 됨)
        rnd.shuffle(close_regs)
        for i in range(n):
            t = rnd.randint(1, 60)
            rows.append((names[i], t, close_regs[i]))

    elif mode == 5:
        # 이미 정렬된 입력(정렬 결과 그대로인지 확인)
        for i in range(n):
            t = rnd.randint(1, 60)
            rows.append((names[i], t, regs[i]))
        rows.sort(key=lambda x: (x[1], x[2]))

    elif mode == 6:
        # 역정렬된 입력(정렬이 제대로 되는지 확인)
        for i in range(n):
            t = rnd.randint(1, 60)
            rows.append((names[i], t, regs[i]))
        rows.sort(key=lambda x: (x[1], x[2]), reverse=True)

    else:
        # 극단: 시간 1~60 다양 + 등록번호도 랜덤 (기본)
        for i in range(n):
            t = rnd.randint(1, 60)
            rows.append((names[i], t, regs[i]))

    return rows

test_data = []

# 예시 3개(문제 예시와 일치)
test_data.append([
    ("MINA", 12, 104),
    ("JUN", 8, 120),
    ("SORA", 12, 101),
    ("HYUN", 5, 300),
    ("DAON", 8, 110),
])
test_data.append([
    ("ALEX", 10, 2),
    ("BORA", 10, 1),
    ("CHRIS", 7, 9),
])
test_data.append([
    ("KIM", 15, 77),
])

# 랜덤 17개
rnd = random.Random(97)
for _ in range(17):
    test_data.append(gen_case(rnd))

# ---------------------------------------------------------
# 6. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for idx, rows in enumerate(test_data, 1):
    lines = [str(len(rows))]
    for name, t, reg in rows:
        lines.append(f"{name} {t} {reg}")
    input_str = "\n".join(lines) + "\n"
    ans = solve_internal(rows)

    with open(os.path.join(test_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P097' 문제 생성이 완료되었습니다. ")
