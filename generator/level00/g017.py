import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P017")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md) - 예시 2개 포함
# ---------------------------------------------------------
md_content = f"""# 미미의 369 게임 (369 Game)

## 문제 설명
친구들과 369 게임을 하던 '미미'는 숫자가 커질수록 박수를 쳐야 할지 말지 헷갈리기 시작했습니다.

369 게임의 규칙은 다음과 같습니다.
1. 1부터 입력받은 숫자 N까지 차례대로 말합니다.
2. 숫자에 3, 6, 9가 하나라도 포함되어 있다면 숫자 대신 clap을 출력합니다.
3. 그 외의 경우에는 숫자를 그대로 출력합니다.

'미미'를 도와 1부터 N까지 규칙에 맞게 결과를 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 마지막 숫자 N이 주어집니다. (1 <= N <= 100)

## 출력 형식 (Output Format)
* 1부터 N까지의 결과를 공백으로 구분하여 한 줄에 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
10
{TICK}

**Output:**
{TICK}
1 2 clap 4 5 clap 7 8 clap 10
{TICK}

### 예시 2
**Input:**
{TICK}
16
{TICK}

**Output:**
{TICK}
1 2 clap 4 5 clap 7 8 clap 10 11 12 clap 14 15 clap
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) - 한 줄 입력 후 즉시 종료
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 입력을 한 줄만 읽고 즉시 처리합니다.
    line = sys.stdin.readline().strip()
    if not line:
        return
        
    try:
        n = int(line)
        results = []
        for i in range(1, n + 1):
            s_i = str(i)
            # 숫자에 3, 6, 9가 포함되어 있는지 확인
            if any(char in s_i for char in "369"):
                results.append("clap")
            else:
                results.append(s_i)
        
        # 결과를 한 줄로 출력하고 프로그램은 종료됩니다.
        print(" ".join(results))
            
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
    n = random.randint(1, 100)
    
    # 정답 생성
    ans_list = [("clap" if any(c in str(num) for c in "369") else str(num)) for num in range(1, n + 1)]
    ans_str = " ".join(ans_list)
    
    # 입력 파일 저장: 불필요한 문자 없이 숫자와 실제 줄바꿈만 저장
    input_path = os.path.join(test_dir, f"input_{i:02d}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(str(n)) # 숫자만 쓰고 줄바꿈은 넣지 않거나 시스템 표준만 사용
        
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), ans_str)

print(f"✅ 'Level00/P017' 생성이 완료되었습니다.")