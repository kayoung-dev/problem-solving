import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level00", "P020")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "구름이의 평균 미달 책장"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Math"]
---

## description
도서관 사서 '구름이'는 책장에 꽂힌 책들의 두께(페이지 수)를 조사했습니다.<br/>
구름이는 책들의 **평균 페이지 수**를 구한 뒤, 평균보다 **엄격히 적은(미만)** 페이지를 가진 책이 총 몇 권인지 알고 싶어 합니다.<br/>
책들의 페이지 수가 리스트로 주어질 때, 평균보다 적은 페이지의 책 권수를 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 책들의 페이지 수가 공백으로 구분되어 한 줄에 주어집니다.
- 각 페이지 수는 1 이상 1,000 이하의 정수입니다.
- 책은 최소 1권 이상 100권 이하로 주어집니다.

## output_description
- 평균 페이지 수보다 적은 책의 권수를 정수로 출력합니다.

# samples

### input 1
{TICK}
100 200 300 400 500
{TICK}

### output 1
{TICK}
2
{TICK}


### input 2
{TICK}
10 20 15
{TICK}

### output 2
{TICK}
1
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 입력을 한 줄 읽어 처리
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    try:
        pages = list(map(int, line.split()))
        if not pages:
            print(0)
            return
            
        # 1. 평균 구하기
        avg = sum(pages) / len(pages)
        
        # 2. 평균보다 작은 값 세기
        count = 0
        for p in pages:
            if p < avg:
                count += 1
                
        print(count)
            
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
    n = random.randint(3, 20)
    pages = [random.randint(10, 500) for _ in range(n)]
    
    # 정답 계산
    avg = sum(pages) / len(pages)
    ans = len([p for p in pages if p < avg])
            
    # 입력 파일 저장
    input_path = os.path.join(test_dir, f"{i}.in")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, pages)))
        
    save_file(os.path.join(test_dir, f"{i}.out"), str(ans))

print(f"✅ 'Level00/P020' 생성이 완료되었습니다.")