import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P169 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P169")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "참석자 명단 확인"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["이진탐색"]
---

## description
행사 진행자 동수는 입구에서 방문객들의 입장을 도와주고 있습니다. 동수는 사전에 신청한 사람들의 고유 번호가 적힌 참석자 명단을 가지고 있으며, 이 명단은 번호순으로 정렬되어 있습니다.

동수는 입구에 도착한 방문객의 고유 번호 $K$가 명단에 있는지 확인해야 합니다. 명단에 번호가 있다면 입장 가능($1$), 없다면 입장 불가능($0$)으로 판정합니다.

참석자 명단 리스트와 방문객 번호 $K$가 주어질 때, 입장 가능 여부를 판단하는 프로그램을 작성하세요. 데이터의 양이 매우 많으므로 반드시 $O(\log N)$의 시간 복잡도로 해결해야 합니다.



## input_description
- 첫 번째 줄에는 명단에 기록된 인원수 $N$과 확인하려는 번호 $K$가 공백으로 구분되어 주어집니다. 
- $1 \le N \le 100,000$
- $1 \le K \le 10^9$
- 두 번째 줄에는 오름차순으로 정렬된 $N$개의 고유 번호가 공백으로 구분되어 주어집니다. 
- 각 번호는 $1$ 이상 $10^9$ 이하의 정수입니다.

## output_description
- 방문객 번호 $K$가 명단에 존재하면 $1$을, 존재하지 않으면 $0$을 출력합니다.

# samples

### input 1
{TICK}
5 15
10 12 15 18 20
{TICK}

### output 1
{TICK}
1
{TICK}
- 명단 `[10, 12, 15, 18, 20]`에 방문객 번호 15가 존재하므로 1을 출력합니다.

### input 2
{TICK}
4 7
1 3 5 9
{TICK}

### output 2
{TICK}
0
{TICK}
- 명단에 7이라는 번호가 없으므로 0을 출력합니다.

### input 3
{TICK}
3 100
100 200 300
{TICK}

### output 3
{TICK}
1
{TICK}
- 명단의 가장 첫 번째 위치에 100이 존재하므로 1을 출력합니다.
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
    k = int(data[1])
    ids = list(map(int, data[2:]))

    low = 0
    high = n - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == k:
            found = True
            break
        elif ids[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    if found:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    # 11~20번은 시간 복잡도 검증을 위해 대규모 데이터 사용
    if i <= 10:
        n = random.randint(1, 100)
    else:
        n = random.randint(90000, 100000)
    
    # 중복 없는 오름차순 리스트 생성
    ids = sorted(random.sample(range(1, 10**9), n))
    
    # 50% 확률로 존재하는 값, 50% 확률로 존재하지 않는 값 설정
    if random.random() > 0.5:
        target = random.choice(ids)
        ans = "1"
    else:
        target = random.randint(1, 10**9)
        # 만약 우연히 생성한 target이 리스트에 있다면 1, 없으면 0
        import bisect
        idx = bisect.bisect_left(ids, target)
        if idx < n and ids[idx] == target:
            ans = "1"
        else:
            ans = "0"

    input_str = f"{n} {target}\n" + " ".join(map(str, ids))
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P169' 문제 생성이 완료되었습니다.")