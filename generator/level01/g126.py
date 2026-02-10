import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P126 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P126")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 시스템 로그 이상 징후 탐색

## 문제 설명
공장의 중앙 관제 시스템은 모든 설비의 작동 기록을 `시:분:초` 형태의 타임스탬프로 남깁니다. 엔지니어인 당신은 특정 시간대 사이에 발생한 시스템 오류를 분석해야 합니다.

경험적으로 시스템 오류는 타임스탬프 숫자에 특정 '에러 번호'인 $K$가 포함되어 있을 때 빈번하게 발생한다는 것을 알아냈습니다. 예를 들어 에러 번호 $K=3$이라면, `03:00:15`나 `12:35:20`과 같이 시, 분, 초 중 어느 곳이라도 숫자 $3$이 포함된 순간들을 모두 조사해야 합니다.

조사해야 할 **시작 시각**과 **종료 시각**, 그리고 **에러 번호 $K$** 가 주어질 때, 해당 범위(시작 시각과 종료 시각 포함) 내에서 에러 번호 $K$가 포함된 타임스탬프가 총 몇 번 나타나는지 계산하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 시작 시각과 종료 시각이 `HH:MM:SS` 형식으로 공백을 사이에 두고 주어집니다.
- 두 번째 줄에 에러 번호인 한 자리 숫자 $K$가 주어집니다
- $0 \le K \le 9$
- 시각은 $00:00:00$부터 $23:59:59$ 사이이며, 시작 시각은 항상 종료 시각보다 빠르거나 같습니다.

## 출력 형식 (Output Format)
- 해당 시간 범위 내에서 숫자 $K$가 포함된 타임스탬프의 총 횟수(초)를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
00:00:00 00:00:10
3
{TICK}
**Output:**
{TICK}
1
{TICK}
- 00:00:00부터 00:00:10 사이에서 숫자 3이 포함된 시각은 00:00:03 단 하나입니다.

### 예시 2
**Input:**
{TICK}
12:00:00 12:59:59
5
{TICK}
**Output:**
{TICK}
1575
{TICK}
- 12시 00분부터 59분까지 중 '분'에 $5$가 포함된 분은 총 15개($05, 15, 25, 35, 45, 50\dots59$분)입니다. 
  - 이 15분 동안은 모든 초($60$초)가 조건을 만족하므로 $15 \times 60 = 900$초입니다.
- 나머지 45분 동안은 '분'에 $5$가 없으므로 '초'에 $5$가 포함되어야 합니다. 
  - 매분 '초'에 $5$가 포함된 순간은 15번이므로 $45 \times 15 = 675$초입니다.
- 따라서 총합은 $900 + 675 = 1575$입니다.

### 예시 3
**Input:**
{TICK}
08:30:00 09:00:00
7
{TICK}
**Output:**
{TICK}
342
{TICK}
- `08:30:00`부터 `08:59:59`까지의 30분 중 '분'에 $7$이 들어간 분은 37분, 47분, 57분으로 총 3개입니다. 
  - $3 \times 60 = 180$ 개
- '분'에 $7$이 들어가지 않은 나머지 27분 동안은 '초'에 $7$이 들어간 경우($07, 17, 27, 37, 47, 57$초)인 6번씩을 셉니다. 
  - $27 \times 6 = 162$ 개
- 마지막 시각인 `09:00:00`에는 $7$이 없으므로, 총합은 $180 + 162 = 342$입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def time_to_seconds(t_str):
    h, m, s = map(int, t_str.split(':'))
    return h * 3600 + m * 60 + s

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start_time = input_data[0]
    end_time = input_data[1]
    k_str = input_data[2]
    
    start_sec = time_to_seconds(start_time)
    end_sec = time_to_seconds(end_time)
    
    count = 0
    # 시작 초부터 종료 초까지 1초씩 증가하며 확인
    for current_total_sec in range(start_sec, end_sec + 1):
        h = current_total_sec // 3600
        m = (current_total_sec % 3600) // 60
        s = current_total_sec % 60
        
        # HH:MM:SS 형식의 문자열로 변환하여 K가 있는지 확인
        time_str = f"{h:02d}:{m:02d}:{s:02d}"
        if k_str in time_str:
            count += 1
            
    print(count)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(start_sec, end_sec, k):
    k_str = str(k)
    count = 0
    for t in range(start_sec, end_sec + 1):
        h = t // 3600
        m = (t % 3600) // 60
        s = t % 60
        if k_str in f"{h:02d}:{m:02d}:{s:02d}":
            count += 1
    return str(count)

for i in range(1, 21):
    # 다양한 시간대 생성
    s1 = random.randint(0, 86399)
    s2 = random.randint(s1, 86399)
    k_val = random.randint(0, 9)
    
    def to_format(s):
        h = s // 3600
        m = (s % 3600) // 60
        sec = s % 60
        return f"{h:02d}:{m:02d}:{sec:02d}"
    
    input_str = f"{to_format(s1)} {to_format(s2)}\n{k_val}"
    ans = solve_internal(s1, s2, k_val)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P126' 문제 생성이 완료되었습니다. ")