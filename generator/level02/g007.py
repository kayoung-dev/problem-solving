import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level02/P07 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..")) 
base_dir = os.path.join(root_dir, "Level02", "P007")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""---
title: "햄버거 만들기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack"]
---

## description
당신은 햄버거 가게에서 아르바이트를 하고 있습니다.<br />
이 가게만의 특별한 햄버거 레시피는 재료를 반드시 **[빵 - 야채 - 고기 - 빵]** 순서로 쌓아야만 햄버거 하나가 완성된다는 것입니다. <br />

재료는 조리된 순서대로 컨베이어 벨트를 타고 하나씩 당신에게 도착합니다. 당신은 도착한 재료를 순서대로 쌓아 올리다가, **[빵, 야채, 고기, 빵]** 순서가 완성되는 즉시 햄버거를 포장해야 합니다. 포장된 햄버거는 쌓아둔 재료 더미에서 사라집니다.

재료는 다음과 같이 숫자로 표기됩니다:
* 1: 빵 (Bread)
* 2: 야채 (Vegetable)
* 3: 고기 (Meat)

예를 들어, 재료가 `[2, 1, 1, 2, 3, 1, 2, 3, 1]` 순서로 들어온다고 가정해 봅시다. <br />

1. `2(야채)`: 쌓음
2. `1(빵)`: 쌓음
3. `1(빵)`: 쌓음
4. `2(야채)`: 쌓음
5. `3(고기)`: 쌓음
6. `1(빵)`: 쌓음 -> 현재 스택의 윗부분이 `1, 2, 3, 1` (빵, 야채, 고기, 빵)이 되었습니다!
7. **포장!**: 스택에서 `1, 2, 3, 1`을 제거합니다. (남은 스택: `[2, 1]`)
8. `2(야채)`: 쌓음
9. `3(고기)`: 쌓음 (현재 스택: `[2, 1, 2, 3]`)
10. `1(빵)`: 쌓음 -> 현재 스택의 윗부분이 `1, 2, 3, 1`이 되었습니다!
11. **포장!**: 제거합니다.

총 2개의 햄버거를 만들 수 있습니다.
주어진 재료 리스트를 보고 만들 수 있는 햄버거의 총개수를 구하세요.

## input_description
- 첫 번째 줄에 재료의 개수 $N$이 주어집니다. ($1 \le N \le 1,000,000$)
- 두 번째 줄에 $N$개의 재료 숫자가 공백으로 구분되어 주어집니다. (1, 2, 3 중 하나)

## output_description
- 만들 수 있는 햄버거의 개수를 출력합니다.

# samples

### input 1
{TICK}
9
2 1 1 2 3 1 2 3 1
{TICK}

### output 1
{TICK}
2
{TICK}

### input 2
{TICK}
9
1 3 2 3 2 1 1 2 3
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

def solve():
    input = sys.stdin.readline
    
    # N 입력
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # 재료 리스트 입력
    ingredients = list(map(int, input().split()))
    
    stack = []
    count = 0
    
    # 햄버거 레시피: 1 (빵) -> 2 (야채) -> 3 (고기) -> 1 (빵)
    # 스택에 쌓을 때는 [1, 2, 3, 1] 패턴을 찾아야 함
    
    for ingredient in ingredients:
        stack.append(ingredient)
        
        # 스택에 재료가 4개 이상 모였을 때 패턴 확인
        if len(stack) >= 4:
            # 스택의 끝 4개가 [1, 2, 3, 1] 인지 확인
            # (슬라이싱을 사용하면 코드가 간결해짐)
            if stack[-4:] == [1, 2, 3, 1]:
                count += 1
                # 4개 제거 (pop 4번)
                for _ in range(4):
                    stack.pop()
                
                # [최적화 팁]
                # Python에서는 del stack[-4:] 가 pop() 루프보다 조금 더 빠를 수 있음
                
    print(count)

if __name__ == "__main__":
    solve()
"""

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def save_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

save_file(os.path.join(base_dir, "problem.md"), md_content)
save_file(os.path.join(base_dir, "solution.py"), py_solution)

# 내부 정답 로직 (테스트케이스 생성용)
def solve_internal(ingredients):
    stack = []
    count = 0
    for x in ingredients:
        stack.append(x)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            count += 1
            del stack[-4:]
    return str(count)

# 테스트 케이스 생성 로직
def generate_burger_case():
    # 랜덤한 재료 생성 (1, 2, 3)
    length = random.randint(20, 100)
    base_ingredients = [random.choice([1, 2, 3]) for _ in range(length)]
    
    # 햄버거 패턴 [1, 2, 3, 1] 을 랜덤 위치에 강제로 주입
    # 주입 시, 기존 재료 사이에 끼워 넣어서 연쇄 작용(pop 후 합쳐짐)이 일어나도록 유도
    # 예: 1 2 (1 2 3 1) 3 1 -> 괄호 부분 빠지면 1 2 3 1 됨
    
    # 햄버거 주입 횟수
    num_burgers = random.randint(5, 20)
    
    for _ in range(num_burgers):
        # 현재 리스트의 랜덤 위치에 [1, 2, 3, 1] 삽입
        insert_idx = random.randint(0, len(base_ingredients))
        # 리스트 슬라이스 끼워넣기
        base_ingredients[insert_idx:insert_idx] = [1, 2, 3, 1]
        
    return base_ingredients

# 테스트 케이스 20개 생성
for i in range(1, 21):
    ingredients = generate_burger_case()
    
    input_str = f"{len(ingredients)}\n" + " ".join(map(str, ingredients))
    output_str = solve_internal(ingredients)
    
    save_file(os.path.join(test_dir, f"{i}.in"), input_str)
    save_file(os.path.join(test_dir, f"{i}.out"), output_str)

print(f"✅ 'Level02/P007' 생성이 완료되었습니다.")