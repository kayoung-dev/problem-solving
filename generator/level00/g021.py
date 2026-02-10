import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P021")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 포근이의 요일 맞추기 (Day of the Week)

## 문제 설명
강아지 '포근이'는 매주 특정 요일에 산책 나가는 것을 좋아합니다. 오늘은 **월요일**입니다.

포근이는 오늘로부터 정확히 $N$일이 지났을 때가 무슨 요일인지 궁금해졌습니다. 요일은 다음과 같은 순서로 반복됩니다:
**월요일 -> 화요일 -> 수요일 -> 목요일 -> 금요일 -> 토요일 -> 일요일** (다시 월요일...)

$N$이 주어졌을 때, 오늘(월요일)로부터 $N$일 후의 요일을 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 지날 날짜를 의미하는 정수 $N$이 주어집니다. ($0 \\le N \\le 10,000$)

## 출력 형식 (Output Format)
* $N$일 후의 요일을 한글로 출력합니다. (예: 월요일, 화요일 등)

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
{TICK}

**Output:**
{TICK}
목요일
{TICK}

* 월요일부터 1일 후는 화요일, 2일 후는 수요일, 3일 후는 **목요일**입니다.

### 예시 2
**Input:**
{TICK}
10
{TICK}

**Output:**
{TICK}
목요일
{TICK}

* 7일이 지나면 다시 월요일이 됩니다. 10을 7로 나눈 나머지는 3이므로, 월요일로부터 3일 뒤인 **목요일**이 됩니다.
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
        n = int(line)
        
        # 요일 리스트 (0: 월요일, 1: 화요일, ..., 6: 일요일)
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        
        # 7일 주기로 반복되므로 모듈러 연산 사용
        target_index = n % 7
        
        print(days[target_index])
            
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

# 요일 리스트 정의
days_list = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

for i in range(1, 21):
    # 테스트 케이스 생성 (0부터 10000까지 다양하게)
    if i <= 7:
        n = i - 1  # 0~6일 테스트
    else:
        n = random.randint(7, 10000)
    
    # 정답 계산
    ans = days_list[n % 7]
    
    # 입력 파일 저장
    input_path = os.path.join(test_dir, f"input_{i:02d}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(str(n))
        
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), ans)

print(f"✅ 'Level00/P021' 생성이 완료되었습니다.")