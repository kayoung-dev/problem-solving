import os
import random
import sys

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P25)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P025")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "신비한 구슬 호리병"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
마법사 멀린은 입구가 좁고 긴 '신비한 호리병'을 가지고 있습니다.<br/>
이 호리병에는 신기한 마법이 걸려 있어서, **같은 색깔의 구슬 두 개가 서로 맞닿으면 두 구슬이 모두 펑! 하고 사라집니다.**
당신은 일렬로 놓인 구슬들을 순서대로 이 호리병 안에 넣으려고 합니다. 구슬은 한 번에 하나씩 호리병의 입구로 들어갑니다.<br/>
새로 넣으려는 구슬의 색깔이 호리병 속 "가장 위(Top)"에 있는 구슬과 같다면, 둘 다 사라집니다. 색깔이 다르다면 위에 쌓이게 됩니다.
모든 구슬을 처리한 후, 호리병 안에 남아있는 구슬들을 바닥부터 순서대로 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 구슬들의 색깔을 나타내는 문자열 $S$가 주어집니다.
- 문자열의 길이는 1 이상 100,000 이하이며, 알파벳 소문자로만 구성됩니다.

## output_description
- 모든 과정을 마친 후 호리병에 남아있는 구슬들의 문자열을 출력합니다. 호리병이 비어있다면 `empty`를 출력합니다.

# samples

### input 1
{TICK}
aaabba
{TICK}

### output 1
{TICK}
empty
{TICK}


### input 2
{TICK}
abccbd
{TICK}

### output 2
{TICK}
ad
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution():
    # 문자열 입력
    s = sys.stdin.readline().strip()
    if not s:
        return

    stack = []
    
    for char in s:
        # 스택이 비어있지 않고, 맨 위의 구슬과 현재 구슬이 같다면?
        if stack and stack[-1] == char:
            stack.pop() # 펑! (맨 위 제거, 현재 구슬도 넣지 않음)
        else:
            stack.append(char) # 다르다면 쌓기
            
    if stack:
        print("".join(stack))
    else:
        print("empty")

if __name__ == "__main__":
    solution()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------

def solve_internal(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack) if stack else "empty"

# 수동 케이스
manual_cases = [
    ("aaabba", "empty"), # 연쇄 폭발 예시
    ("abccbd", "ad"),    # 중간 폭발 예시
    ("apple", "ale"),    # 일반 단어
    ("aaaa", "empty"),   # 짝수개 연속
    ("aaaaa", "a"),      # 홀수개 연속
    ("abcde", "abcde"),  # 폭발 없음
    ("abba", "empty"),   # 대칭형
    ("aca", "aca")       # 떨어져 있는 같은 글자는 폭발 안 함
]

test_cases = []
for inp, out in manual_cases:
    test_cases.append((inp, out))

# 랜덤 케이스 생성
# 폭발이 자주 일어나도록 하기 위해 문자 종류를 제한하거나 의도적으로 짝을 만듦
chars_pool = "abcdefgh" # 문자 종류를 적게 해서 충돌 확률 높임

for _ in range(12): # 총 20개 채우기
    length = random.randint(10, 1000)
    
    # 랜덤 문자열 생성
    s_list = []
    for _ in range(length):
        # 30% 확률로 바로 직전 문자와 같은 문자 추가 (연속 폭발 유도)
        if s_list and random.random() < 0.3:
            s_list.append(s_list[-1])
        else:
            s_list.append(random.choice(chars_pool))
            
    s = "".join(s_list)
    ans = solve_internal(s)
    
    test_cases.append((s, ans))

# 파일 저장
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(out)

print(f"✅ 'Level01/P025' 문제 생성이 완료되었습니다.")