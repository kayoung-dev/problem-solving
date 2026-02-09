import os
import random

# ---------------------------------------------------------
# 1. 경로 설정
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level01", "P001")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "배고픈 모험가의 사과 수확"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Array"]
---

## description
모험가 **'로이'** 는 숲을 지나가다 사과나무 한 그루를 발견했습니다. 이 나무에는 $N$개의 사과가 열려 있으며, 각 사과마다 **무게** $W_i$가 다릅니다.

**'로이'** 는 배가 많이 고프지만, 너무 작은 사과는 맛이 없어서 무게가 **$K$ 미만** 인 사과는 먹지 않기로 했습니다. 

**'로이'** 가 수확한 사과의 **개수**와 수확한 모든 사과의 **총 무게**를 구하는 프로그램을 작성하세요.



## input_description
- 모든 데이터는 **한 줄**에 공백으로 구분되어 주어집니다.
- $N$ $K$ $W_1$ $W_2$ ... $W_N$
- (1 ≤ $N$ ≤ 100, 1 ≤ $K, W_i$ ≤ 1,000)

## output_description
- 수확한 사과의 **개수**와 **총 무게**를 공백으로 구분하여 출력합니다.

# samples

### input 1
{TICK}
5 150 100 200 150 80 300
{TICK}

### output 1
{TICK}
3 650
{TICK}

### input 2
{TICK}
3 500 100 200 300
{TICK}

### output 2
{TICK}
0 0
{TICK}
"""



# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
py_solution = """import sys

def main():
    # input()은 한 줄을 읽은 뒤 엔터가 입력되면 즉시 다음 코드로 진행합니다.
    try:
        line = input()
        if not line:
            return

        # 데이터를 공백 기준으로 나누어 정수로 변환
        data = list(map(int, line.split()))
        
        if len(data) < 2:
            return

        n = data[0]
        k = data[1]
        weights = data[2:2+n]
        
        # 무게가 K 이상인 사과만 필터링
        picked = [w for w in weights if w >= k]
        
        if not picked:
            print("0 0")
        else:
            # 개수와 총 무게 출력 후 프로그램 종료
            print(f"{len(picked)} {sum(picked)}")
            
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

# 임의의 테스트 케이스 생성
for i in range(1, 21):
    n = random.randint(5, 15)
    k = random.randint(100, 500)
    weights = [random.randint(50, 600) for _ in range(n)]
    
    input_str = f"{n} {k} " + " ".join(map(str, weights))
    picked = [w for w in weights if w >= k]
    ans_str = f"{len(picked)} {sum(picked)}" if picked else "0 0"
    
    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), ans_str)

print(f"✅ 'Level01/P001' 생성이 완료되었습니다.")

