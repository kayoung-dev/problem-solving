import os
import random
import bisect

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P174 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P174")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "열차 관제사 유진의 승강장 배정"
level: "1"
time_limit: 1000
memory_limit: 131072
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Binary Search"]
---

## description
고속열차 관제사 유진이는 1번 승강장의 열차 진입 스케줄을 관리합니다. 모든 열차는 $[s, e)$ 형태의 시간 동안 승강장을 점유합니다. ($s$시 정각 진입, $e$시 정각 직전 출발)

새로운 열차가 진입을 요청할 때, 기존에 확정된 열차 스케줄과 **단 1초라도 겹친다면** 안전을 위해 진입을 거절(`DENY`)해야 합니다. 겹치지 않는다면 진입을 승인(`ALLOW`)하고 스케줄에 추가합니다.

정렬 상태를 유지하며 이웃한 예약만 확인하는 $O(N \log N)$ 알고리즘을 구현하세요.



## input_description
- 첫 번째 줄에 열차 진입 요청 횟수 $N$가 주어집니다. 
- $1 \le N \le 100,000$
- 이후 $Q$개의 줄에 걸쳐 각 열차의 진입 시각 $s$와 출발 시각 $e$가 공백으로 구분되어 주어집니다. 
- $0 \le s < e \le 10^9$

## output_description
- 각 요청에 대해 승인되면 `ALLOW`, 거절되면 `DENY`를 한 줄에 하나씩 출력합니다.
- 입력이 들어오는 즉시 결과를 출력해야 합니다.

# samples

### input 1
{TICK}
3
10 20
15 25
20 30
{TICK}

### output 1
{TICK}
ALLOW
DENY
ALLOW
{TICK}


### input 2
{TICK}
3
50 100
0 30
20 60
{TICK}

### output 2
{TICK}
ALLOW
ALLOW
DENY
{TICK}


### input 3
{TICK}
4
10 50
60 100
110 150
55 58
{TICK}

### output 3
{TICK}
ALLOW
ALLOW
ALLOW
ALLOW
{TICK}

""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys
import bisect

def solve():
    input = sys.stdin.readline
    line = input().strip()
    if not line: return
    q = int(line)
    
    schedule = [] # (start, end)
    
    for _ in range(q):
        req = input().split()
        if not req: break
        s, e = map(int, req)
        
        # 시작 시간 기준으로 위치 찾기 (O(log N))
        idx = bisect.bisect_left(schedule, (s, e))
        
        can_assign = True
        # 뒷집 확인
        if idx < len(schedule) and e > schedule[idx][0]:
            can_assign = False
        # 앞집 확인
        if can_assign and idx > 0 and s < schedule[idx-1][1]:
            can_assign = False
            
        if can_assign:
            schedule.insert(idx, (s, e))
            sys.stdout.write("ALLOW\n")
        else:
            sys.stdout.write("DENY\n")

if __name__ == "__main__":
    solve()
"""
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성
# ---------------------------------------------------------
def get_p174_ans(requests):
    sched = []
    results = []
    for s, e in requests:
        idx = bisect.bisect_left(sched, (s, e))
        conflict = False
        if idx < len(sched) and e > sched[idx][0]: conflict = True
        if not conflict and idx > 0 and s < sched[idx-1][1]: conflict = True
        if not conflict:
            sched.insert(idx, (s, e))
            results.append("ALLOW")
        else:
            results.append("DENY")
    return results

for i in range(1, 21):
    if i <= 5: # 소규모 랜덤
        q = random.randint(1, 100)
        reqs = [(s := random.randint(0, 1000), s + random.randint(1, 100)) for _ in range(q)]
    elif i <= 10: # 중규모
        q = 5000
        reqs = [(s := random.randint(0, 10**8), s + random.randint(1, 10**5)) for _ in range(q)]
    else: # [저격용 최악의 케이스] Q = 100,000
        # 선형 탐색은 매번 끝까지 검사하게 되며 O(Q^2) 발생
        q = 100000
        reqs = [(i * 20, i * 20 + 10) for i in range(q)] # 0-10, 20-30, ... (모두 ALLOW 되는 케이스)
    
    ans = get_p174_ans(reqs)
    with open(os.path.join(test_dir, f"{i}.in"), "w") as f:
        f.write(f"{q}\n")
        for s, e in reqs: f.write(f"{s} {e}\n")
    with open(os.path.join(test_dir, f"{i}.out"), "w") as f:
        f.write("\n".join(ans) + "\n")

print(f"✅ 'Level01/P174' 문제 생성이 완료되었습니다. ")