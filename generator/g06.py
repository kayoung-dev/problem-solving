import os
import random
import string

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P06")

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 구름이의 책 찾기 (Book Search)

## 문제 설명
도서관 사서 **'구름이'** 는 엉망진창으로 섞여 있는 책장 정리를 맡게 되었습니다. 책장에는 $N$권의 책이 무작위로 꽂혀 있습니다.

**'구름이'** 가 찾고자 하는 특정 책의 제목이 주어졌을 때, 그 책이 **왼쪽에서 몇 번째** 위치에 꽂혀 있는지 찾아내는 프로그램을 작성하세요.

* 만약 책이 존재하면 그 위치(1부터 시작)를 출력합니다.
* 만약 찾는 책이 책장에 없다면 `-1`을 출력합니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 책의 총 개수 $N$이 주어집니다. ($1 \le N \le 100$)
* 두 번째 줄에 찾고자 하는 **목표 책 제목**이 주어집니다.
* 세 번째 줄에 책장에 꽂힌 $N$권의 책 제목들이 공백으로 구분되어 주어집니다.
* 책 제목은 영문 대소문자로만 구성됩니다.

## 출력 형식 (Output Format)
* 찾는 책의 위치(1부터 시작하는 순서)를 정수로 출력합니다.
* 책이 없다면 `-1`을 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
5
Python
Java C++ Python Ruby Go
{TICK}

**Output:**
{TICK}
3
{TICK}

* 'Python'은 [Java, C++, Python, Ruby, Go] 중에서 **3번째**에 위치해 있습니다.

### 예시 2
**Input:**
{TICK}
3
HTML
CSS JavaScript React
{TICK}

**Output:**
{TICK}
-1
{TICK}

* 책장에 'HTML'이라는 책은 없습니다.
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """import sys

def main():
    try:
        # 1. 책의 개수 N 입력
        line1 = input()
        if not line1: return
        n = int(line1.strip())
        
        # 2. 찾을 책 제목 입력
        target_book = input().strip()
        
        # 3. 책 리스트 입력
        line3 = input()
        if not line3: return
        books = line3.split()
        
        # 선형 탐색 (Linear Search)
        # 파이썬 리스트의 index() 메서드를 활용하거나 반복문으로 찾을 수 있습니다.
        if target_book in books:
            # index는 0부터 시작하므로 +1 해줍니다.
            print(books.index(target_book) + 1)
        else:
            print("-1")
            
    except (EOFError, ValueError):
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

# 테스트용 단어 풀
word_pool = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape",
    "Python", "Java", "C++", "Rust", "Go", "Swift", "Kotlin",
    "Red", "Green", "Blue", "Yellow", "Black", "White"
]

for i in range(1, 21):
    n = random.randint(5, 20)
    
    # 책장 구성 (중복 없이 선택)
    books = random.sample(word_pool, k=min(n, len(word_pool)))
    
    # 타겟 설정 (80% 확률로 존재하는 책, 20% 확률로 없는 책)
    if random.random() < 0.8:
        target = random.choice(books)
        ans = books.index(target) + 1
    else:
        target = "MissingBook"
        ans = -1
        
    # 파일 저장 (실제 줄바꿈 적용)
    input_filepath = os.path.join(base_dir, f"input_{i:02d}.txt")
    with open(input_filepath, "w", encoding="utf-8") as f:
        f.write(f"{len(books)}\n")
        f.write(f"{target}\n")
        f.write(" ".join(books))
        
    save_file(os.path.join(base_dir, f"output_{i:02d}.txt"), str(ans))

print(f"✅ 'Easy/P06' 생성이 완료되었습니다.")