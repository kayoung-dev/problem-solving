import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P170 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P170")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "잃어버린 보석 조각 찾기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색", "수학"]
---

## description
고고학자 지우는 유적에서 두 종류의 보석 조각들을 발견했습니다. 첫 번째 주머니에는 $N$개의 **붉은 보석**이, 두 번째 주머니에는 $M$개의 **푸른 보석**이 들어있습니다.

고대 기록에 따르면, 하나의 붉은 보석($x$)과 하나의 푸른 보석($y$)은 특별한 무게 규칙을 만족할 때만 결합되어 완벽한 보석이 됩니다. 그 규칙은 **푸른 보석의 무게($y$)가 붉은 보석의 무게($x$)를 2배한 값보다 정확히 $K$만큼 더 무거워야 한다**는 것입니다.

지우가 가진 보석 조각들 중 이 규칙을 만족하는 보석 쌍은 **항상 딱 하나만 존재함**이 보장됩니다. 결합 가능한 [붉은 보석 무게, 푸른 보석 무게]를 찾아 출력하는 프로그램을 작성하세요. 

데이터의 양이 방대하므로 반드시 $O(N \log M)$ 또는 $O(N \log N)$의 성능을 보장해야 합니다.



## input_description
- 첫 번째 줄에는 붉은 보석의 개수 $N$, 푸른 보석의 개수 $M$, 그리고 기준 수치 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N$
- $M \le 100,000$
- $-10^9 \le K \le 10^9$
- 두 번째 줄에는 붉은 보석 $N$개의 무게가 공백으로 구분되어 주어집니다.
- 세 번째 줄에는 푸른 보석 $M$개의 무게가 공백으로 구분되어 주어집니다. 모든 무게는 $1$ 이상 $10^9$ 이하의 정수입니다.

## output_description
- 조건을 만족하는 붉은 보석의 무게와 푸른 보석의 무게를 한 줄에 공백으로 구분하여 출력합니다.
- 문제의 조건상 정답은 항상 하나만 존재합니다.

# samples

### input 1
{TICK}
3 4 10
5 15 25
10 20 30 40
{TICK}

### output 1
{TICK}
5 20
{TICK}
- 붉은 보석 5의 2배(10)에 $K=10$을 더하면 20입니다. 푸른 보석 목록에 20이 있으며, 다른 조합(15, 25 등)은 규칙을 만족하지 않습니다.

### input 2
{TICK}
2 2 -5
10 20
15 25
{TICK}

### output 2
{TICK}
10 15
{TICK}
- 붉은 보석 10의 2배(20)에서 5를 빼면($-5$) 15입니다. 푸른 보석 목록에 15가 유일한 정답으로 존재합니다.

### input 3
{TICK}
3 3 100
10 20 30
110 120 150
{TICK}

### output 3
{TICK}
10 120
{TICK}
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    # 대량 데이터 처리를 위한 최적화된 입력 읽기
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, m, k = map(int, input_data[:3])
    red_gems = list(map(int, input_data[3:3+n]))
    blue_gems = list(map(int, input_data[3+n:3+n+m]))

    # 탐색 대상인 푸른 보석 리스트 정렬
    blue_gems.sort()
    
    for red in red_gems:
        # 타겟 방정식: y = 2x + k
        target = (red * 2) + k
        
        # 이진 탐색으로 유일한 해 찾기
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if blue_gems[mid] == target:
                print(f"{red} {target}")
                return
            elif blue_gems[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성 
# ---------------------------------------------------------
for i in range(1, 21):
    if i <= 10:
        # [저격용] 선형 탐색 시 100억 번 연산 유도
        n, m = 100000, 100000
        k = 100
        red_gems = list(range(1, n + 1))
        # 정답 후보(2x + 100)는 항상 짝수이므로, 홀수들만 배치하여 오답 유도
        blue_gems = [j * 2 + 1 for j in range(1, m)]
        ans_red = red_gems[-1]
        ans_blue = 2 * ans_red + k
        blue_gems.append(ans_blue) # 정답을 맨 뒤에 배치
    else:
        # [랜덤형] 유일해 보장 데이터
        n, m = random.randint(80000, 100000), random.randint(80000, 100000)
        k = random.randint(-10**5, 10**5)
        ans_red = random.randint(1, 10**8)
        ans_blue = 2 * ans_red + k
        
        red_gems = [ans_red]
        red_set = {ans_red}
        while len(red_gems) < n:
            r = random.randint(1, 10**8)
            if r not in red_set:
                red_gems.append(r)
                red_set.add(r)
        
        forbidden_blue = {2 * r + k for r in red_gems}
        blue_gems = [ans_blue]
        blue_set = {ans_blue}
        while len(blue_gems) < m:
            b = random.randint(1, 10**9)
            if b not in blue_set and b not in forbidden_blue:
                blue_gems.append(b)
                blue_set.add(b)
        
        random.shuffle(red_gems)
        random.shuffle(blue_gems)

    input_str = f"{n} {m} {k}\n" + " ".join(map(str, red_gems)) + "\n" + " ".join(map(str, blue_gems))
    ans_str = f"{ans_red} {ans_blue}"
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans_str)

print(f"✅ 'Level01/P170' 문제 생성이 완료되었습니다. ")