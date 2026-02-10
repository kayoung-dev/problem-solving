import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 및 기본 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P025")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (Markdown)
# ---------------------------------------------------------
md_content = f"""# 마법 학교의 물약 정리

## 문제 설명
마법 학교의 신입생 '에릭'은 방학을 맞아 연금술 창고 정리를 돕게 되었습니다.
창고에는 다양한 마력 지수를 가진 물약들이 무작위로 놓여 있습니다.

창고 관리인 선생님은 에릭에게 다음과 같은 규칙으로 물약을 정리해달라고 부탁했습니다.

1. 오늘의 기준 마력인 **`divisor`** 로 **나누어 떨어지는 마력 지수**를 가진 물약만 골라냅니다.
2. 골라낸 물약들은 마력 지수가 **작은 순서대로(오름차순)** 진열장에 배치합니다.
3. 만약 `divisor`로 나누어 떨어지는 물약이 하나도 없다면, 창고 정리가 불가능하다는 표시로 **-1**을 보고해야 합니다.

물약들의 마력 지수가 담긴 배열 `arr`와 기준 마력 `divisor`가 주어질 때, 에릭이 진열장에 배치해야 할 물약 목록을 구하는 프로그램을 작성하세요.

---

## 입력 형식
* 첫 번째 줄에 물약 배열의 크기 $N$과 기준 마력 `divisor`가 공백으로 구분되어 주어집니다. ($1 \\le N \\le 100$, $1 \\le divisor \\le 100$)
* 두 번째 줄에 $N$개의 물약 마력 지수가 공백으로 구분되어 주어집니다. (각 마력 지수는 1 이상 1,000 이하의 자연수)

## 출력 형식
* 조건을 만족하는 수를 오름차순으로 정렬하여 공백으로 구분해 출력합니다.
* 만약 나누어 떨어지는 수가 하나도 없다면 -1을 출력합니다.

---

## 입출력 예시

### 예시 1
**Input:**
{TICK}
4 5
5 9 7 10
{TICK}

**Output:**
{TICK}
5 10
{TICK}

* 5로 나누어 떨어지는 수는 5와 10입니다. 이를 오름차순으로 정렬하면 [5, 10]이 됩니다.

### 예시 2
**Input:**
{TICK}
3 10
3 2 6
{TICK}

**Output:**
{TICK}
-1
{TICK}

* 10으로 나누어 떨어지는 수가 하나도 없으므로 -1을 출력합니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (Python Solution)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 첫 번째 줄: 배열 크기 N, 나누는 수 divisor
    first_line = sys.stdin.readline().split()
    if not first_line: return
    n = int(first_line[0])
    divisor = int(first_line[1])
    
    # 두 번째 줄: 배열 요소
    arr = list(map(int, sys.stdin.readline().split()))
    
    # divisor로 나누어 떨어지는 수 필터링
    result = [num for num in arr if num % divisor == 0]
    
    # 결과가 비어있으면 -1, 아니면 오름차순 정렬 후 출력
    if not result:
        print("-1")
    else:
        result.sort()
        # 리스트 요소들을 공백으로 구분하여 출력
        print(*(result))

if __name__ == "__main__": main()
"""

# ---------------------------------------------------------
# 4. 파일 생성 및 테스트 케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 메인 문제 파일 및 솔루션 저장
save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 테스트 케이스 20개 생성
for i in range(1, 21):
    # 랜덤 데이터 생성
    n = random.randint(1, 100)           # 배열 크기
    divisor = random.randint(1, 20)      # 나누는 수
    arr = [random.randint(1, 1000) for _ in range(n)] # 물약 마력 지수 배열
    
    # Input 파일 내용 작성
    input_content = f"{n} {divisor}\n" + " ".join(map(str, arr))
    input_path = os.path.join(test_dir, f"input_{i:02d}.in")
    save_file(input_path, input_content)
    
    # Output 계산 (Python 로직 그대로 구현)
    filtered = [x for x in arr if x % divisor == 0]
    filtered.sort()
    
    if not filtered:
        output_content = "-1"
    else:
        output_content = " ".join(map(str, filtered))
        
    output_path = os.path.join(test_dir, f"output_{i:02d}.out")
    save_file(output_path, output_content)

print(f"✅ 'Level00/P025' 생성이 완료되었습니다.")