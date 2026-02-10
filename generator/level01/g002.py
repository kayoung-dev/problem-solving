import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P002")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "인터넷 브라우저의 '뒤로 가기'"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
평소 인터넷 쇼핑을 즐기는 '지수'는 마음에 드는 옷을 찾기 위해 여러 페이지를 돌아다닙니다. 쇼핑몰 사이트는 복잡해서 페이지를 자주 이동하게 됩니다.<br />

브라우저의 **'뒤로 가기'** 버튼은 가장 최근에 방문한 페이지를 현재 기록에서 삭제하고, 바로 직전 페이지를 보여주는 기능을 합니다. 이는 자료구조의 **스택(Stack)** 개념인 **후입선출(LIFO)** 방식과 동일합니다.

초기 상태는 어떤 페이지도 방문하지 않은 **'HOME'** 상태입니다.
지수가 내린 명령어 리스트를 입력받아, 각 행동에 따른 결과를 출력하는 프로그램을 작성하세요.


## input_description
- 첫 번째 줄에 명령어의 개수 $N$이 주어집니다. ($1 \le N \le 100$)
- 두 번째 줄부터 $N$개의 줄에 걸쳐 명령어가 주어집니다.
    - `visit [URL]`: 해당 URL 페이지를 방문합니다. (URL은 공백 없는 문자열)
    - `back`: 현재 페이지를 닫고 이전 페이지로 돌아갑니다.
    - `current`: 현재 머물고 있는 페이지를 확인합니다.

## output_description
- `visit`: 방문 시 `[V] {{URL}}`을 출력합니다.
- `back`: 
    - 이전 페이지로 돌아갔다면 `[B] {{현재_URL}}`을 출력합니다. 
    - 돌아가서 홈 화면이 되었다면 `[B] HOME`을 출력합니다.
    - 이미 홈 화면이라서 돌아갈 곳이 없다면 `[B] IGNORED`를 출력합니다.
- `current`: 
    - 현재 페이지가 있다면 해당 URL을 출력합니다.
    - 홈 화면이라면 `HOME`을 출력합니다.

# samples

### input 1
{TICK}
5
visit naver.com
visit google.com
back
visit github.com
current
{TICK}

### output 1
{TICK}
[V] naver.com
[V] google.com
[B] naver.com
[V] github.com
github.com
{TICK}

### input 2
{TICK}
4
visit blog.me
back
back
current
{TICK}

### output 2
{TICK}
[V] blog.me
[B] HOME
[B] IGNORED
HOME
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # 입력을 빠르게 받기 위해 sys.stdin 사용
    input = sys.stdin.readline
    
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 방문 기록을 저장할 스택
    history = []

    for _ in range(n):
        command_line = input().split()
        if not command_line:
            break
        
        cmd = command_line[0]

        if cmd == "visit":
            url = command_line[1]
            history.append(url)
            print(f"[V] {url}")

        elif cmd == "back":
            if history:
                history.pop() # 현재 페이지 삭제 (pop)
                if history:
                    # 이전 페이지가 남아있음
                    print(f"[B] {history[-1]}")
                else:
                    # 스택이 비었으므로 HOME
                    print("[B] HOME")
            else:
                # 이미 비어있음
                print("[B] IGNORED")

        elif cmd == "current":
            if history:
                print(history[-1])
            else:
                print("HOME")

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

# 테스트 케이스 생성 로직
def solve_internal(commands):
    history = []
    results = []
    
    for line in commands:
        parts = line.split()
        cmd = parts[0]
        
        if cmd == "visit":
            url = parts[1]
            history.append(url)
            results.append(f"[V] {url}")
            
        elif cmd == "back":
            if history:
                history.pop()
                if history:
                    results.append(f"[B] {history[-1]}")
                else:
                    results.append("[B] HOME")
            else:
                results.append("[B] IGNORED")
                
        elif cmd == "current":
            if history:
                results.append(history[-1])
            else:
                results.append("HOME")
                
    return "\n".join(results)

# 임의의 테스트 케이스 20개 생성
urls = ["naver.com", "google.com", "daum.net", "github.com", "stackoverflow.com", "youtube.com", "notion.so"]
cmd_types = ["visit", "back", "current"]

for i in range(1, 21):
    n = random.randint(5, 20)
    commands = []
    for _ in range(n):
        c_type = random.choices(cmd_types, weights=[50, 30, 20], k=1)[0]
        if c_type == "visit":
            commands.append(f"visit {random.choice(urls)}")
        else:
            commands.append(c_type)
            
    input_str = f"{n}\n" + "\n".join(commands)
    output_str = solve_internal(commands)
    
    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)

print(f"✅ 'Level01/P002' 생성이 완료되었습니다.")