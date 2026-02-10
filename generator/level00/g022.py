import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P022")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 보강된 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 꼬미의 원형 돌기 (Circular Move)

## 문제 설명
햄스터 '꼬미'가 원형으로 배치된 N개의 방을 돌며 놀고 있습니다. 각 방에는 **0번부터 N-1번까지** 번호가 붙어 있습니다.

예를 들어, 방이 4개(N=4)라면 방 번호는 **0, 1, 2, 3**이 됩니다. 이 방들은 원형으로 연결되어 있어서, 마지막 번호인 3번 방에서 시계 방향으로 한 칸을 더 가면 다시 0번 방으로 돌아오게 됩니다.

꼬미는 현재 **0번 방**에 있습니다. 꼬미가 시계 방향으로 총 **K칸**을 이동했을 때, 최종적으로 멈추게 되는 방의 번호를 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 방의 개수 N과 이동할 칸수 K가 공백으로 구분되어 주어집니다.
* 1 <= N <= 100
* 0 <= K <= 10,000

## 출력 형식 (Output Format)
* 꼬미가 최종적으로 도착한 방의 번호를 정수로 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
4 5
{TICK}

**Output:**
{TICK}
1
{TICK}

- 방의 개수가 4개이므로 번호는 [0, 1, 2, 3]입니다.
- 0번에서 시작하여 5칸을 이동합니다.
- 1칸 이동: 1번 방
- 2칸 이동: 2번 방
- 3칸 이동: 3번 방
- 4칸 이동: 0번 방 (한 바퀴 돌았음)
- 5칸 이동: **1번 방** (최종 도착)
- **계산식:** 5 % 4 = 1

### 예시 2
**Input:**
{TICK}
10 20
{TICK}

**Output:**
{TICK}
0
{TICK}

- 방이 10개일 때 20칸 이동하면, 정확히 두 바퀴(10칸 + 10칸)를 돌고 다시 처음 위치인 **0**번 방에 멈춥니다.
- **계산식:** 20 % 10 = 0
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
        
    try:
        # N: 방의 개수, K: 이동 거리
        n, k = map(int, line.split())
        
        # 원형 순환의 핵심은 나머지 연산입니다.
        # 어떤 숫자든 N으로 나눈 나머지는 항상 0 ~ N-1 범위 안에 들어옵니다.
        result = k % n
        
        print(result)
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

for i in range(1, 21):
    n = random.randint(2, 100)
    k = random.randint(0, 10000)
    ans = k % n
    
    input_path = os.path.join(test_dir, f"input_{i:02d}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(f"{n} {k}")
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), str(ans))

print(f"✅ 'Level00/P022' 생성이 완료되었습니다.")