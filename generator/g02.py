import os
import random

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P02")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 편의점 알바생 단비의 유통기한 점검 (Expiration Check)

## 문제 설명
편의점 아르바이트생 **'단비'** 는 유통기한이 얼마 남지 않은 간식들을 점검하려고 합니다. 편의점에는 총 $N$개의 진열대가 있고, 각 진열대에는 여러 개의 간식이 놓여 있습니다.

**'단비'** 는 다음 규칙에 따라 **'집중 점검'** 이 필요한 진열대를 찾아내려 합니다.

1. 각 진열대에서 유통기한이 **3일 이하** 로 남은 간식들만 골라냅니다.
2. 골라낸 간식들의 **남은 일수의 합** 이 해당 진열대의 **위험 기준치 $M$** 이하이면, 유통기한이 매우 임박한 상품이 많다는 뜻이므로 해당 진열대를 **'집중 점검'** 대상으로 분류합니다.
3. 전체 진열대 중 **'집중 점검'** 대상으로 분류된 진열대는 총 몇 개인지 구하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 진열대의 개수 $N$이 주어집니다.
* 두 번째 줄부터 각 진열대의 정보가 한 줄씩 주어집니다.
* 형식: $M$ $C$ $D_1$ $D_2$ ... $D_C$

## 출력 형식 (Output Format)
* **'단비'** 가 찾아낸 **'집중 점검'** 진열대의 개수를 정수로 출력합니다.

---

## 입출력 예시 (Sample I/O)
### 예시 1
**Input:**
{TICK}
2
5 3 2 3 10
4 4 1 2 5 1
{TICK}
**Output:**
{TICK}
2
{TICK}

### 예시 2
**Input:**
{TICK}
1
3 3 2 2 1
{TICK}
**Output:**
{TICK}
0
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - 주석 오류 완벽 수정
# ---------------------------------------------------------
# solution.py 부분만 이렇게 교체해 보세요
py_solution = """import sys

def main():
    # 첫 번째 줄(N) 읽기
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    
    target_count = 0
    
    # N번만큼 반복하며 각 줄의 데이터를 읽음
    for _ in range(n):
        line = sys.stdin.readline()
        if not line:
            break
            
        data = list(map(int, line.split()))
        m = data[0]      # 위험 기준치
        c = data[1]      # 간식 개수
        days = data[2:]  # 유통기한 데이터
        
        urgent_items = [d for d in days if d <= 3]
        urgent_sum = sum(urgent_items)
        
        if urgent_items and urgent_sum <= m:
            target_count += 1
            
    print(target_count)

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
    n = random.randint(1, 15)
    test_input = [str(n)]
    ans = 0
    
    for _ in range(n):
        m = random.randint(3, 10)
        c = random.randint(3, 8)
        days = [random.randint(1, 10) for _ in range(c)]
        test_input.append(f"{m} {c} " + " ".join(map(str, days)))
        
        urgent_items = [d for d in days if d <= 3]
        if urgent_items and sum(urgent_items) <= m:
            ans += 1
            
    # input 파일에 실제 줄바꿈(\n)이 들어가도록 저장합니다.
    save_file(os.path.join(base_dir, f"input_{i:02d}.txt"), "\n".join(test_input))
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), str(ans))

print(f"✅ 'Easy/P02' 파일 생성이 완료되었습니다.")