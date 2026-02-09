import os
import random
import string

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P007")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "초코의 특정 문자 세기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
호기심 많은 강아지 **'초코'** 는 문장 속에 숨어 있는 특정 알파벳을 찾는 놀이를 좋아합니다.

**'초코'** 가 찾으려고 하는 **알파벳 한 개**와 **긴 문장**이 주어졌을 때, 그 문장 안에 해당 알파벳이 총 몇 번 등장하는지 세어보는 프로그램을 작성하세요.

(단, 대문자와 소문자는 서로 다른 문자로 취급합니다.)



## input_description
- 첫 번째 줄에 찾으려는 **알파벳 한 글자** $C$가 주어집니다.
- 두 번째 줄에 검색 대상이 되는 **문장** $S$가 주어집니다. (길이는 1000 이하, 공백 포함)

## output_description
- 문장 $S$ 안에 알파벳 $C$가 몇 번 포함되어 있는지 정수로 출력합니다.

# samples

### input 1
{TICK}
a
Banana and Apple
{TICK}

### output 1
{TICK}
4
{TICK}

### input 2
{TICK}
P
pineapple
{TICK}

### output 2
{TICK}
0
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    try:
        # 1. 찾을 문자 입력 (엔터 포함 문자열 처리)
        line1 = input()
        if not line1: return
        target_char = line1.strip()
        
        # 2. 전체 문장 입력
        sentence = input()
        
        # 3. 개수 세기
        count = sentence.count(target_char)
        
        print(count)
            
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

# 테스트 데이터 생성 (다양한 빈도수 유도)
for i in range(1, 21):
    target = random.choice(string.ascii_letters)
    
    # 0~100 사이의 난수로 케이스 유형 결정
    chance = random.randint(1, 100)
    
    if chance <= 20: 
        # [Case 1: 0개] 타겟 문자가 아예 없는 경우
        pool = string.ascii_letters.replace(target, "") + " "
        sentence_chars = random.choices(pool, k=random.randint(20, 50))
        
    elif chance <= 60:
        # [Case 2: 적당히 많음] 2~10개 정도 강제 주입
        pool = string.ascii_letters + " "
        base_len = random.randint(30, 80)
        sentence_chars = random.choices(pool, k=base_len)
        
        inject_count = random.randint(2, 10)
        for _ in range(inject_count):
            pos = random.randint(0, len(sentence_chars) - 1)
            sentence_chars[pos] = target
            
    else:
        # [Case 3: 매우 많음] 타겟 문자를 20% 확률로 도배
        length = random.randint(50, 200)
        sentence_chars = []
        for _ in range(length):
            if random.random() < 0.3: # 30% 확률로 타겟 문자
                sentence_chars.append(target)
            else:
                sentence_chars.append(random.choice(string.ascii_letters + " "))
    
    sentence = "".join(sentence_chars)
    
    # 정답 계산
    ans = sentence.count(target)
    
    # 파일 저장
    input_file = os.path.join(test_dir, f"{i}.in")
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(f"{target}\n")
        f.write(f"{sentence}")
        
    save_file(os.path.join(test_dir, f"{i}.out"), str(ans))

print(f"✅ 'Level01/P007' 생성이 완료되었습니다.")