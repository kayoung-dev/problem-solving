import os
import random
import bisect

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P162 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P162")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

random.seed(162)  # 재현 가능하게

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) - Q 쿼리 버전
# ---------------------------------------------------------
problem_md = r"""---
title: "시험 합격자 찾기 (쿼리 버전)"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
시험 관리자 영희는 학생들의 시험 점수를 낮은 점수부터 높은 점수까지 순서대로 정렬하여 보관하고 있습니다.

이번에는 합격 기준 점수 $K$에 대한 질문이 총 $Q$번 주어집니다.
각 질문마다 장부에서 **처음으로 $K$점 이상을 받은 학생**이 몇 번째 위치(인덱스)에 있는지 찾아야 합니다.

장부의 위치는 $0$번부터 시작하며, 만약 $K$점 이상을 받은 학생이 한 명도 없다면 $-1$을 출력합니다.
데이터의 양이 방대하므로 각 질문을 반드시 $O(\log N)$에 처리해야 합니다.

---

## input_description
- 첫 번째 줄에 점수의 개수 $N$과 질문의 개수 $Q$가 주어집니다.
- $1 \le N \le 100,000$
- $1 \le Q \le 100,000$
- 두 번째 줄에 오름차순으로 정렬된 $N$개의 점수가 주어집니다.
- 각 점수는 $0$ 이상 $10^9$ 이하의 정수입니다.
- 다음 $Q$개의 줄에 기준 점수 $K$가 한 줄에 하나씩 주어집니다.
- 각 $K$는 $0$ 이상 $10^9$ 이하의 정수입니다.

---

## output_description
- 각 질문에 대해 점수가 $K$ 이상인 값이 처음으로 나타나는 위치(인덱스)를 한 줄에 하나씩 출력합니다.
- 조건을 만족하는 값이 없으면 $-1$을 출력합니다.

# samples

### input 1
{TICK}
5 3
70 75 80 85 90
80
76
95
{TICK}

### output 1
{TICK}
2
2
-1
{TICK}


### input 2
{TICK}
4 4
50 50 60 70
50
55
70
71
{TICK}

### output 2
{TICK}
0
2
3
-1
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - Q 쿼리 처리, lower_bound
# ---------------------------------------------------------
solution_py = r"""import sys
from bisect import bisect_left

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    q = int(next(it))

    scores = [int(next(it)) for _ in range(n)]

    out = []
    for _ in range(q):
        k = int(next(it))
        idx = bisect_left(scores, k)
        out.append(str(idx if idx < n else -1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성 (1.in ~ 20.in, 1.out ~ 20.out)
#    - 작은/중간/큰 섞기
#    - 마지막 2개는 "선형탐색 탐지용" 최악 케이스로 구성
# ---------------------------------------------------------
def make_scores(n: int):
    # 중복 허용, 정렬
    return sorted(random.randint(0, 10**9) for _ in range(n))

def answer_queries(scores, queries):
    n = len(scores)
    out_lines = []
    for k in queries:
        idx = bisect.bisect_left(scores, k)
        out_lines.append(str(idx if idx < n else -1))
    return "\n".join(out_lines)

for i in range(1, 21):
    # 기본 크기 결정
    if i <= 6:
        n = random.randint(1, 30)
        q = random.randint(1, 20)
    elif i <= 14:
        n = random.randint(100, 2000)
        q = random.randint(50, 500)
    elif i <= 18:
        n = random.randint(20000, 100000)
        q = random.randint(5000, 30000)
    elif i == 19:
        # 탐지용(1): 큰데 파일 사이즈 조금 절약
        n = 100000
        q = 50000
    else:
        # 탐지용(2): 최악 케이스 (linear search 거의 확정 TLE)
        n = 100000
        q = 100000

    scores = make_scores(n)
    mx = scores[-1]

    # 쿼리 구성
    queries = []

    if i == 20:
        # 최악: 항상 없음 -> 매 쿼리마다 끝까지 스캔 유도
        # (K > max(scores))
        queries = [mx + 1] * q

    elif i == 19:
        # 최악: 항상 맨 끝에서만 만족
        # (K = max(scores))
        queries = [mx] * q

    else:
        # 일반 케이스: 섞어서 정확성 확인
        # 1) 존재 안 함(큰 값) 20%
        # 2) 배열 안의 값(중복 포함) 40%
        # 3) 임의 값 40%
        for _ in range(q):
            r = random.random()
            if r < 0.2:
                queries.append(mx + random.randint(1, 1000))  # 없음
            elif r < 0.6:
                queries.append(random.choice(scores))         # 존재
            else:
                queries.append(random.randint(0, 10**9))       # 임의

    # 정답 생성
    out_str = answer_queries(scores, queries)

    # 입력 생성 (K는 Q줄)
    input_lines = []
    input_lines.append(f"{n} {q}")
    input_lines.append(" ".join(map(str, scores)))
    input_lines.extend(map(str, queries))
    input_str = "\n".join(input_lines)

    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out_str)

print("✅ 'Level01/P162' (Q-쿼리 버전) 문제 생성이 완료되었습니다.")
print("✅ 19~20번 테스트는 선형탐색(TLE) 탐지용 최악 케이스입니다.")
