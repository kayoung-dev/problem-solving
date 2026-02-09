import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level02", "P001")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "연료 전지 충전소"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
우주선 엔진에 에너지를 공급하는 연료 전지 보관함은 입구와 출구가 하나인 수직 원통형 구조로 되어 있습니다. 이 구조의 특성상 가장 나중에 넣은 연료 캡슐을 가장 먼저 꺼내어 사용해야 합니다.

당신은 우주선의 연료 관리 시스템을 구축해야 합니다. 시스템은 다음과 같은 두 가지 명령을 처리합니다. <br />

1. **Push (1 $X$):** 에너지 수치가 $X$인 연료 캡슐 하나를 보관함에 넣습니다.
2. **Pop (2):** 보관함의 가장 위에 있는 연료 캡슐을 꺼내어 에너지를 엔진에 공급합니다. 이때 꺼낸 캡슐의 에너지 수치를 출력합니다. 만약 보관함이 비어있다면 -1을 출력합니다.

명령의 개수 $Q$와 $Q$개의 명령이 주어졌을 때, 각 Pop 명령에 대한 결과를 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 명령의 개수 $Q$가 주어집니다. 
- $1 \\le Q \\le 1,000$
- 두 번째 줄부터 $Q$개의 줄에 걸쳐 명령이 주어집니다.
- 1 $X$ : 보관함에 에너지 수치 $X$를 넣습니다. 
- $1 \\le X \\le 10,000$
- 2 : 가장 위의 캡슐을 꺼내고 그 수치를 출력합니다.

## output_description
- 2번 명령(Pop)이 주어질 때마다 한 줄에 하나씩 결과를 출력합니다.

# samples

### input 1
{TICK}
5
1 10
1 20
2
1 30
2
{TICK}

### output 1
{TICK}
20
30
{TICK}


### input 2
{TICK}
4
2
1 500
1 600
2
{TICK}

### output 2
{TICK}
-1
600
{TICK}

"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    stack = []
    results = []
    
    idx = 1
    for _ in range(q):
        op = int(input_data[idx])
        if op == 1:
            x = int(input_data[idx+1])
            stack.append(x)
            idx += 2
        else:
            if not stack:
                results.append("-1")
            else:
                results.append(str(stack.pop()))
            idx += 1
            
    if results:
        print("\\n".join(results))

if __name__ == "__main__":
    main()
"""

def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# ---------------------------------------------------------
# 4. 임의의 테스트 케이스 생성
# ---------------------------------------------------------
for i in range(1, 21):
    q = random.randint(10, 50)
    stack = []
    ops = []
    outputs = []
    
    for _ in range(q):
        if not stack or random.random() > 0.4:  
            val = random.randint(1, 1000)
            ops.append(f"1 {val}")
            stack.append(val)
        else:
            ops.append("2")
            if not stack:
                outputs.append("-1")
            else:
                outputs.append(str(stack.pop()))
                
    if not outputs:
        ops.append("2")
        outputs.append("-1")
        q = len(ops)

    input_str = f"{len(ops)}\\n" + "\\n".join(ops)
    ans_str = "\\n".join(outputs)
    

    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), ans_str)

print(f"✅ 'Level02/P001' 생성이 완료되었습니다.")