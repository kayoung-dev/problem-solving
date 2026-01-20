import os
import random
import string

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "Easy", "P14")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
md_content = f"""# 소연의 암호 토큰 복원 (Token Restore)

## 문제 설명
보안 담당 소연은 출입 시스템 로그에서 암호 토큰을 복원하고 있습니다.
로그에는 같은 문자들이 반복해서 섞여 들어가는데, 소연이 필요한 토큰은 다음 규칙으로 복원됩니다.

문자열이 주어질 때,
중복된 문자를 제거하고 각 문자가 처음 등장한 순서대로 한 번씩만 남깁니다.

주어진 문자열을 위 규칙대로 변환하여 출력하는 프로그램을 작성하세요.

---

## 입력 형식 (Input Format)
- 한 줄에 문자열 S가 주어집니다.
- 문자열 길이는 1 이상 100 이하입니다.
- 문자열은 알파벳 대소문자와 숫자로만 이루어져 있습니다.

## 출력 형식 (Output Format)
- 중복 문자를 제거한 결과 문자열을 출력합니다.
- 문자의 순서는 처음 등장한 순서를 유지해야 합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1

Input:
{TICK}
ABBCDAA
{TICK}

Output:
{TICK}
ABCD
{TICK}

---

### 예시 2

Input:
{TICK}
a1a1B2B2
{TICK}

Output:
{TICK}
a1B2
{TICK}
"""

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py)
# ---------------------------------------------------------
py_solution = """def main():
    try:
        s = input().rstrip("\\n")
        if not s:
            return

        out = []
        for ch in s:
            found = False
            for x in out:
                if x == ch:
                    found = True
                    break
            if not found:
                out.append(ch)

        print("".join(out))

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
fixed_cases = [
    "ABBCDAA",          # ABCD
    "a1a1B2B2",         # a1B2
    "aaaaa",            # a
    "ABCDE",            # ABCDE
    "112233",           # 123
    "AAbbCCaa",         # AbCa (주의: 대소문자 구분됨 -> A b? actually string: A A b b C C a a => "AbCa")
    "Z9Z9Z9",           # Z9
    "0123401234",       # 01234
    "xXxXxX",           # xX
    "Hello123Hello",    # Helo123 (대소문자 구분: H e l l o 1 2 3 H e l l o -> H e l o 1 2 3)
]

def unique_chars_keep_order(s: str) -> str:
    out = []
    for ch in s:
        if ch not in out:
            out.append(ch)
    return "".join(out)

def random_token(min_len=1, max_len=30):
    alphabet = string.ascii_letters + string.digits
    length = random.randint(min_len, max_len)
    return "".join(random.choice(alphabet) for _ in range(length))

for i in range(1, 21):
    if i <= len(fixed_cases):
        input_str = fixed_cases[i - 1]
    else:
        # 중복이 잘 나오도록 일부러 짧은 토큰을 여러 번 섞기
        base = random_token(3, 10)
        # base를 섞어서 반복
        pieces = []
        for _ in range(random.randint(2, 6)):
            # base 일부를 랜덤으로 잘라 붙임
            a = random.randint(0, len(base) - 1)
            b = random.randint(a + 1, len(base))
            pieces.append(base[a:b])
        input_str = "".join(pieces)

    output_str = unique_chars_keep_order(input_str)

    save_file(os.path.join(test_dir, f"input_{i:02d}.in"), input_str)
    save_file(os.path.join(test_dir, f"output_{i:02d}.out"), output_str)

print("✅ 'Easy/P14' 생성이 완료되었습니다.")
