import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P127 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P127")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = r"""# 교량 지지대 강도 설계

## 문제 설명
교량 설계 엔지니어인 소윤이는 강 위에 새로운 보도교를 건설하고 있습니다. 다리의 특정 구간을 안전하게 받치기 위해서는 반드시 **3개의 지지대**를 설치해야 합니다. 

소윤이는 창고에 보관된 $N$개의 지지대 중 3개를 골라 사용하려고 합니다. 각 지지대는 고유의 버틸 수 있는 강도(Strength)를 가지고 있습니다. 다리의 안전을 위해서는 3개 지지대의 강도 합이 높을수록 좋지만, 너무 무거운 지지대를 사용하면 다리 상판에 무리가 가기 때문에 **전체 강도의 합이 제한치 $L$을 초과해서는 안 됩니다.**

소윤이를 도와 창고에 있는 $N$개의 지지대 중 3개를 골랐을 때, **제한치 $L$을 넘지 않으면서 강도의 합이 최대가 되는 경우**를 찾아 그 합계를 출력하는 프로그램을 작성해 주세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 지지대의 개수 $N$과 강도 제한치 $L$이 공백으로 구분되어 주어집니다 
- $3 \le N \le 100$,
- $10 \le L \le 300,000$
- 두 번째 줄에 각 지지대의 강도를 나타내는 $N$개의 정수가 공백으로 구분되어 주어집니다. 
- 각 강도는 $1$ 이상 $100,000$ 이하입니다.
- 제한치 $L$을 넘지 않으면서 3개를 고를 수 있는 조합은 반드시 하나 이상 존재합니다.

## 출력 형식 (Output Format)
- 제한치 $L$ 이하이면서 3개 지지대의 강도 합이 최대가 되는 값을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5 21
5 6 7 8 9
{TICK}
**Output:**
{TICK}
21
{TICK}
- 6, 7, 8을 고르면 합이 21이 되어 제한치와 정확히 일치하며 최대가 됩니다.

### 예시 2
**Input:**
{TICK}
10 500
93 181 245 214 315 36 185 115 73 136
{TICK}
**Output:**
{TICK}
497
{TICK}

- 가능한 3개의 지지대 조합을 모두 조사합니다. (총 120가지 조합)
- 그중 합이 500 이하인 것들을 추려냅니다.
   - 예: 181 + 245 + 36 = 462
   - 예: 181 + 185 + 115 = 481
   - 예: 245 + 115 + 136 = 496
   - 예: 181 + 181 + 135 ... 
   - (중복 불가)
- 조사 결과, **$245 + 136 + 116$** 등 을 계산했을 때 497이 최대임을 확인합니다.

### 예시 3
**Input:**
{TICK}
5 10
1 2 3 4 5
{TICK}
**Output:**
{TICK}
10
{TICK}

- 세 지지대의 합이 $10$ 이하인 모든 경우를 구합니다.
   - $(1, 2, 3) \rightarrow 6$
   - $(1, 2, 4) \rightarrow 7$
   - $(1, 3, 5) \rightarrow 9$
   - $(1, 4, 5) \rightarrow 10$
   - $(2, 3, 5) \rightarrow 10$
- 결과적으로 제한치 $10$을 넘지 않는 가장 큰 합계는 $10$입니다.
""".replace("{TICK}", TICK)

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = r"""import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    limit = int(input_data[1])
    strengths = list(map(int, input_data[2:]))
    
    max_sum = 0
    
    # 3중 반복문을 이용해 서로 다른 3개의 지지대를 고르는 모든 조합을 확인
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_sum = strengths[i] + strengths[j] + strengths[k]
                
                # 제한치 이하이면서 현재까지 발견한 최대합보다 크면 갱신
                if current_sum <= limit:
                    if current_sum > max_sum:
                        max_sum = current_sum
                        
    print(max_sum)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(n, limit, strengths):
    max_s = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                s = strengths[i] + strengths[j] + strengths[k]
                if s <= limit and s > max_s:
                    max_s = s
    return str(max_s)

for i in range(1, 21):
    n = random.randint(5, 100)
    # n이 작을 때는 큰 값을, n이 클 때는 적당한 값을 섞음
    strengths = [random.randint(1, 10000) for _ in range(n)]
    
    # 임의의 3개를 골라 그 합 근처로 제한치를 설정하여 정답 유도
    sample_indices = random.sample(range(n), 3)
    sample_sum = sum(strengths[idx] for idx in sample_indices)
    limit = sample_sum + random.randint(0, 100)
    
    input_str = f"{n} {limit}\n" + " ".join(map(str, strengths))
    ans = solve_internal(n, limit, strengths)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P127' 문제 생성이 완료되었습니다.")