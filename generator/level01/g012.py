import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P12 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P012")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = f"""---
title: "애니팡팡 버그 수정"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
게임 개발자 **민수**는 새로운 퍼즐 게임 '애니팡팡'을 개발 중입니다.<br/>
이 게임에는 알파벳 소문자가 적힌 블록들이 일렬로 내려오는 스테이지가 있습니다.<br/>
게임의 핵심 로직은 다음과 같습니다.
1. 같은 알파벳이 적힌 블록 두 개가 연속해서 붙어 있게 되면, 두 블록은 팡! 소리를 내며 사라집니다.
2. 블록이 사라진 후, 떨어진 빈자리를 메우기 위해 나머지 블록들이 다시 붙게 됩니다.
3. 이때 다시 붙은 블록끼리 또 같은 알파벳이라면 연쇄적으로 사라집니다.
민수는 모든 블록을 성공적으로 제거할 수 있는지 확인하는 테스트 프로그램을 만들려고 합니다. 문자열 $S$가 주어졌을 때, 모든 블록을 제거할 수 있다면 $1$을, 남는 블록이 있다면 $0$을 반환하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 알파벳 소문자로만 구성된 문자열 $S$가 주어집니다.
- 문자열 $S$의 길이는 $1$ 이상 $1,000,000$ 이하입니다.

## output_description
- 모든 블록을 제거할 수 있으면 $1$, 아니면 $0$을 출력합니다.

# samples

### input 1
{TICK}
baabaa
{TICK}

### output 1
{TICK}
1
{TICK}


### input 2
{TICK}
cdcd
{TICK}

### output 2
{TICK}
0
{TICK}
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_code = """import sys

def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(1)
    else:
        print(solution(input_data))
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_code)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성 (총 20개)
# ---------------------------------------------------------

def solve(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return 1 if not stack else 0

def generate_valid_case(target_length):
    """모든 문자가 짝지어 제거되는 문자열 생성"""
    stack = []
    res = []
    for _ in range(target_length // 2):
        c = random.choice("abcdefghijklmnopqrstuvwxyz")
        res.append(c)
        res.append(c)
    random.shuffle(res)
    # 셔플만 하면 안 되고, 스택 구조를 유지하며 무작위 삽입 필요
    # 간단하게 구현하기 위해: 괄호 생성 원리와 유사하게 처리
    s = []
    for _ in range(target_length // 2):
        char = random.choice("abcde")
        insert_pos = random.randint(0, len(s))
        s.insert(insert_pos, char)
        s.insert(insert_pos, char)
    return "".join(s)

manual_cases = [
    ("baabaa", 1),
    ("cdcd", 0),
    ("abccba", 1),
    ("aa", 1),
    ("ab", 0),
    ("aaa", 0),
    ("aaaa", 1),
    ("aabbccddeeff", 1)
]

test_cases = manual_cases[:]

# 9~20번: 랜덤 및 대규모 케이스 생성
while len(test_cases) < 20:
    case_type = len(test_cases) % 2
    if case_type == 0:
        # 성공 케이스 (짝수 길이)
        length = random.randint(10, 100)
        inp = generate_valid_case(length if length % 2 == 0 else length + 1)
    else:
        # 실패 가능성이 높은 무작위 케이스
        length = random.randint(10, 100)
        inp = "".join(random.choice("abc") for _ in range(length))
    
    out = solve(inp)
    if (inp, out) not in test_cases:
        test_cases.append((inp, out))

# 파일 쓰기
for i, (inp, out) in enumerate(test_cases, 1):
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(inp)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(str(out)) # int/bool을 문자열로 변환

print(f"✅ 'Level01/P012' 문제 생성이 완료되었습니다.")