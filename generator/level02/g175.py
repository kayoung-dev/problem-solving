import os
import random
import bisect

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P175 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P175")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""---
title: "프로듀서 디소울의 녹음 부스 예약"
level: "1"
time_limit: 1000
memory_limit: 131072
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Binary Search"]
---

## description
힙합 프로듀서 디소울은 자신의 개인 녹음 부스 예약 시스템을 관리합니다. 보컬 녹음은 아주 미세한 소음에도 결과물이 망가질 수 있기 때문에, 두 가수의 녹음 시간이 단 1초라도 겹치는 것을 절대 허용하지 않습니다.

모든 예약은 $[s, e)$ 형태의 반개구간으로 관리됩니다. ($s$시 정각 시작, $e$시 정각 직전 종료)

새로운 예약 신청이 들어올 때, 기존에 확정된 예약들과 **시간이 겹친다면** `CONFLICT`를 출력하고 예약을 거절합니다. 만약 겹치는 시간이 전혀 없다면 `BOOKED`를 출력하고 해당 예약을 확정 목록에 추가합니다.

예약 요청 횟수 $N$이 최대 $100,000$회에 달하므로, 효율적인 이진 탐색 알고리즘을 사용하여 시스템의 응답 속도를 유지하세요.



## input_description
- 첫 번째 줄에 예약 신청 횟수 $N$이 주어집니다. 
- $1 \le N \le 100,000$
- 이후 $N$개의 줄에 걸쳐 각 예약의 시작 시각 $s$와 종료 시각 $e$가 공백으로 구분되어 주어집니다. 
- $0 \le s < e \le 10^9$

## output_description
- 각 요청에 대해 예약이 성공하면 `BOOKED`, 중복으로 인해 실패하면 `CONFLICT`를 한 줄에 하나씩 출력합니다.
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
BOOKED
CONFLICT
BOOKED
{TICK}
- [10, 20) 예약 성공.
- [15, 25)는 기존 예약 [10, 20)과 15~20분 구간이 겹치므로 실패.
- [20, 30)은 기존 예약이 끝남과 동시에 시작하므로 성공.

### input 2
{TICK}
4
100 200
50 60
70 110
10 40
{TICK}

### output 2
{TICK}
BOOKED
BOOKED
CONFLICT
BOOKED
{TICK}

### input 3
{TICK}
3
0 1000
500 600
1000 2000
{TICK}

### output 3
{TICK}
BOOKED
CONFLICT
BOOKED
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
    n = int(line)
    
    # 시작 시간 기준으로 정렬된 상태를 유지할 리스트
    sessions = [] # (start, end)
    
    for _ in range(n):
        req = input().split()
        if not req: break
        s, e = map(int, req)
        
        # 이진 탐색으로 현재 시작 시간이 들어갈 위치 탐색 (O(log N))
        idx = bisect.bisect_left(sessions, (s, e))
        
        is_conflict = False
        # 1. 뒷집 확인 (내 종료 시간이 뒤 세션의 시작 시간보다 늦으면 충돌)
        if idx < len(sessions) and e > sessions[idx][0]:
            is_conflict = True
        
        # 2. 앞집 확인 (내 시작 시간이 앞 세션의 종료 시간보다 빠르면 충돌)
        if not is_conflict and idx > 0 and s < sessions[idx-1][1]:
            is_conflict = True
            
        if not is_conflict:
            sessions.insert(idx, (s, e))
            sys.stdout.write("BOOKED\n")
        else:
            sys.stdout.write("CONFLICT\n")

if __name__ == "__main__":
    solve()
"""
with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 테스트케이스 생성
# ---------------------------------------------------------
def get_p175_ans(requests):
    sched = []
    results = []
    for s, e in requests:
        idx = bisect.bisect_left(sched, (s, e))
        conflict = False
        if idx < len(sched) and e > sched[idx][0]: conflict = True
        if not conflict and idx > 0 and s < sched[idx-1][1]: conflict = True
        if not conflict:
            sched.insert(idx, (s, e))
            results.append("BOOKED")
        else:
            results.append("CONFLICT")
    return results

for i in range(1, 21):
    if i <= 5: # 소규모 랜덤
        n = random.randint(1, 100)
        reqs = [(s := random.randint(0, 1000), s + random.randint(1, 100)) for _ in range(n)]
    elif i <= 10: # 중규모
        n = 5000
        reqs = [(s := random.randint(0, 10**8), s + random.randint(1, 10**5)) for _ in range(n)]
    else: # [저격용 최악의 케이스] N = 100,000
        # 선형 탐색 사용 시 100억 번의 연산이 필요하도록 설계
        n = 100000
        # 0-10, 20-30, 40-50... 식으로 절대 겹치지 않게 10만 개 삽입
        reqs = [(j * 20, j * 20 + 10) for j in range(n)]
    
    ans = get_p175_ans(reqs)
    with open(os.path.join(test_dir, f"{i}.in"), "w") as f:
        f.write(f"{n}\n")
        for s, e in reqs: f.write(f"{s} {e}\n")
    with open(os.path.join(test_dir, f"{i}.out"), "w") as f:
        f.write("\n".join(ans) + "\n")

print(f"✅ 'Level01/P175' 문제 생성이 완료되었습니다.")