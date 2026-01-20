import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 및 기본 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
# 실제 사용 시 경로 구조에 맞춰 수정 가능
easy_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "Easy")) 

base_dir = os.path.join(easy_dir, "P27")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (Markdown)
# ---------------------------------------------------------
md_content = f"""# 숲속 다람쥐의 빈 주머니

## 문제 설명
가을을 맞아 숲속 다람쥐 '토토'는 겨울잠을 대비해 도토리를 모으고 있습니다.
토토는 맛있는 도토리를 구별하는 특별한 기준인 **`divisor`** 를 가지고 있습니다.

토토가 주운 도토리들의 무게가 담긴 배열 `arr`가 주어졌을 때, 토토는 다음 규칙에 따라 도토리를 주머니에 담으려 합니다.

1. 도토리의 무게가 **`divisor`** 로 **나누어 떨어지는 것**만 주머니에 담습니다.
2. 주머니 안에서 정리가 잘 되도록, 담은 도토리들은 무게가 가벼운 순서인 **오름차순** 으로 정렬해야 합니다.
3. 만약 규칙에 맞는 도토리가 하나도 없다면, 토토는 빈손으로 돌아가야 합니다. 이때는 빈 주머니를 의미하는 숫자 **-1** 을 반환해야 합니다.

토토가 최종적으로 주머니에 담게 될 도토리의 무게 목록을 구하는 프로그램을 작성하세요.

---

## 입력 형식
* 첫 번째 줄에 도토리의 개수 $N$과 기준 무게 `divisor`가 공백으로 구분되어 주어집니다. ($1 \\le N \\le 100$, $1 \\le divisor \\le 100$)
* 두 번째 줄에 $N$개의 도토리 무게(자연수)가 공백으로 구분되어 주어집니다.

## 출력 형식
* 선택된 도토리의 무게를 오름차순으로 정렬하여 공백으로 구분해 출력합니다.
* 만약 선택된 도토리가 없다면 **-1** 을 출력합니다.

---

## 입출력 예시

### 예시 1
**Input:**
{TICK}
4 10
5 20 10 3
{TICK}

**Output:**
{TICK}
10 20
{TICK}

* 10으로 나누어 떨어지는 무게는 10과 20입니다. 오름차순으로 정렬하면 10 20이 됩니다.

### 예시 2
**Input:**
{TICK}
3 7
2 8 5
{TICK}

**Output:**
{TICK}
-1
{TICK}

* 7로 나누어 떨어지는 무게가 하나도 없습니다. 따라서 **-1** 을 출력합니다.
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
    
    # 도토리 무게 배열
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 로직: divisor로 나누어 떨어지는 무게 필터링
    filtered = [w for w in arr if w % divisor == 0]
    
    # 예외 처리: 빈 배열일 경우 -1 출력
    if not filtered:
        print("-1")
    else:
        # 오름차순 정렬
        filtered.sort()
        # 결과 출력
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

print(f"✅ 'Easy/P27' 생성이 완료되었습니다.")