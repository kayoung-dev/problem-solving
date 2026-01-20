import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 및 기본 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
# 실제 사용 시 경로 구조에 맞춰 수정 가능
easy_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "Easy")) 

base_dir = os.path.join(easy_dir, "P26")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (Markdown)
# ---------------------------------------------------------
md_content = f"""# 우주 정거장의 신호 해독

## 문제 설명
우주 정거장의 통신 장교 '리나'는 지구로부터 수신된 암호화된 신호 배열을 분석하고 있습니다. 
우주 방사선으로 인해 신호 배열에는 의미 없는 노이즈(숫자)들이 섞여 있습니다.

보안 본부에서는 진짜 정보를 해독하기 위한 보안 키 `divisor`를 보내왔습니다. 
리나는 다음 규칙에 따라 진짜 신호만을 걸러내야 합니다.

1. 수신된 신호 배열 `arr`의 각 숫자 중, 보안 키 `divisor`로 **나누어 떨어지는 수**만 유효한 신호입니다.
2. 해독의 정확성을 위해 유효한 신호들은 **오름차순**으로 정렬되어야 합니다.
3. 만약 유효한 신호가 하나도 없다면, 이는 통신 오류이므로 **-1**을 반환해야 합니다.

신호 배열과 보안 키가 주어졌을 때, 해독된 신호 목록을 출력하는 프로그램을 작성하세요.

---

## 입력 형식
* 첫 번째 줄에 신호 배열의 크기 $N$과 보안 키 $divisor$가 공백으로 구분되어 주어집니다. ($1 \\le N \\le 100$, $1 \\le divisor \\le 100$)
* 두 번째 줄에 $N$개의 신호 데이터(자연수)가 공백으로 구분되어 주어집니다.

## 출력 형식
* 유효한 신호를 오름차순으로 정렬하여 공백으로 구분해 출력합니다.
* 유효한 신호가 없다면 -1을 출력합니다.

---

## 입출력 예시

### 예시 1
**Input:**
{TICK}
5 5
5 9 7 10 3
{TICK}

**Output:**
{TICK}
5 10
{TICK}

* 5로 나누어 떨어지는 신호는 5와 10입니다. 이를 오름차순으로 정렬하면 5 10이 됩니다.

### 예시 2
**Input:**
{TICK}
3 11
2 4 8
{TICK}

**Output:**
{TICK}
-1
{TICK}

* 11로 나누어 떨어지는 신호가 없습니다. 따라서 -1을 출력합니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (Python Solution)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 입력 처리
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    divisor = int(line1[1])
    
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: divisor로 나누어 떨어지는 값 필터링
    filtered = [num for num in arr if num % divisor == 0]
    
    # 예외 처리 및 정렬
    if not filtered:
        print("-1")
    else:
        filtered.sort()
        # 언패킹(*)을 사용하여 공백 구분 출력
        print(*filtered)

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
    n = random.randint(1, 100)
    divisor = random.randint(1, 20)
    arr = [random.randint(1, 1000) for _ in range(n)]
    
    # Input 파일 작성
    input_content = f"{n} {divisor}\n" + " ".join(map(str, arr))
    input_path = os.path.join(test_dir, f"input_{i:02d}.in")
    save_file(input_path, input_content)
    
    # Output 계산
    filtered = [x for x in arr if x % divisor == 0]
    filtered.sort()
    
    if not filtered:
        output_content = "-1"
    else:
        output_content = " ".join(map(str, filtered))
        
    output_path = os.path.join(test_dir, f"output_{i:02d}.out")
    save_file(output_path, output_content)

print(f"✅ 'Easy/P26' 생성이 완료되었습니다.")