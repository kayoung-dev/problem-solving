import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P085 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P085")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = """# 두 팀 키 매칭

## 문제 설명
감독 **유진**은 두 팀의 선수들을 한 줄로 세워 연습 경기를 준비합니다.  
각 팀에는 선수 $N$명이 있고, 각 선수는 **키**를 가지고 있습니다.

유진은 아래 방식으로 매칭을 정했습니다.

1. A팀 선수들의 키 배열 $A$를 오름차순으로 정렬한다.
2. B팀 선수들의 키 배열 $B$를 오름차순으로 정렬한다.
3. 정렬된 상태에서 같은 인덱스끼리 매칭한다.

매칭이 끝난 뒤, 각 매칭 쌍의 **키 차이의 합**을 계산하려고 합니다.

|A_1 - B_1| + |A_2 - B_2| + ... + |A_N - B_N|


위 값을 출력하세요.

---

## 입력 형식 (Input Format)
- 첫째 줄에 정수 $N$이 주어집니다. $(1 \\le N \\le 200)$
- 둘째 줄에 $N$개의 정수 $A_1, A_2, \\dots, A_N$이 공백으로 구분되어 주어집니다.
- 셋째 줄에 $N$개의 정수 $B_1, B_2, \\dots, B_N$이 공백으로 구분되어 주어집니다.
- 모든 키는 $(1 \\le A_i, B_i \\le 300)$ 입니다.

## 출력 형식 (Output Format)
- 정렬 후 같은 인덱스끼리 매칭했을 때의 키 차이의 합을 출력하세요.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4
150 160 170 180
155 165 175 185
{TICK}
**Output:**
{TICK}
20
{TICK}

### 예시 2
**Input:**
{TICK}
5
170 150 160 160 180
165 155 190 150 160
{TICK}
**Output:**
{TICK}
20
{TICK}
- 두 배열을 각각 오름차순으로 정렬한다.
- [ 150, 160, 160, 170, 180 ]
- [ 150, 155, 160, 165, 190 ]
- 같은 인덱스끼리 매칭하여 키 차이의 절댓값을 더한다.
- 차이의 합은 `0 + 5 + 0 + 5 + 10 = 20` 


### 예시 3
**Input:**
{TICK}
1
200
180
{TICK}
**Output:**
{TICK}
20
{TICK}
""".format(TICK=TICK)


# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
solution_py = """import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    total = 0
    for i in range(n):
        total += abs(a[i] - b[i])

    print(total)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 테스트케이스 생성 로직
# ---------------------------------------------------------
def solve_internal(a, b):
    a = sorted(a)
    b = sorted(b)
    return str(sum(abs(a[i] - b[i]) for i in range(len(a))))

random.seed(85)

test_data = []

# 샘플 3개
test_data.append(([150, 160, 170, 180], [155, 165, 175, 185]))
test_data.append(([170, 150, 160, 160, 180], [165, 155, 190, 150, 160]))
test_data.append(([200], [180]))

# 랜덤 17개
for _ in range(17):
    n = random.randint(1, 200)
    a = [random.randint(1, 300) for _ in range(n)]
    b = [random.randint(1, 300) for _ in range(n)]
    test_data.append((a, b))

# ---------------------------------------------------------
# 5. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

for i, (a, b) in enumerate(test_data, 1):
    n = len(a)
    input_str = f"{n}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)) + "\n"
    ans = solve_internal(a, b)

    with open(os.path.join(test_dir, f"{i}.in"), "w") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w") as f:
        f.write(ans + "\n")

print(f"✅ 'Level01/P085' 문제 생성이 완료되었습니다. ")
