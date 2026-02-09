import os
import random
import string

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P003")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "별이의 비밀 편지 해독"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
모험가 **'별이'** 는 숲속 도서관에서 오래된 종이 한 장을 발견했습니다. 이 종이에는 알 수 없는 문자들이 적혀 있었는데, 자세히 보니 모든 문장이 **거꾸로** 적혀 있다는 것을 알아냈습니다.

**'별이'** 가 비밀 편지의 내용을 올바르게 읽을 수 있도록, 입력받은 문자열을 뒤집어서 출력하는 프로그램을 작성하세요.



## input_description
- 해독해야 할 문자열 $S$가 한 줄에 주어집니다.
- 문자열의 길이는 1 이상 100 이하입니다.
- 문자열은 알파벳 대소문자, 숫자, 그리고 공백으로 이루어져 있습니다.

## output_description
- 입력받은 문자열을 거꾸로 뒤집은 결과를 출력합니다.

# samples

### input 1
{TICK}
olleh
{TICK}

### output 1
{TICK}
hello
{TICK}

### input 2
{TICK}
I love Python
{TICK}

### output 2
{TICK}
nohtyP evol I
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # input()을 사용하여 엔터가 입력되는 즉시 한 줄을 읽습니다.
    try:
        line = input()
        if not line:
            return
            
        # 파이썬의 슬라이싱 기능을 사용하여 문자열을 뒤집습니다.
        reversed_str = line[::-1]
        
        # 결과 출력 후 즉시 종료
        print(reversed_str)
            
    except EOFError:
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

# 테스트 케이스 생성 (20개)
test_data = [
    "hello", "I love Python", "12345", "Racecar", "A man a plan a canal Panama",
    "OpenAI", "Data Structure", "Algorithm", "Byeol-i", "Secret Letter",
    "Python is fun", "Level", "Madam", "1004", "Happy New Year",
    "Step on no pets", "Was it a car or a cat I saw", "Never odd or even",
    "Apple", "Banana"
]

for i in range(1, 21):
    if i <= len(test_data):
        input_str = test_data[i-1]
    else:
        # 무작위 문자열 생성
        input_str = ''.join(random.choices(string.ascii_letters + " ", k=20)).strip()
    
    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), input_str[::-1])

print(f"✅ 'Level01/P003' 생성이 완료되었습니다.")