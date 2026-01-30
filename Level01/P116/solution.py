import sys

def normalize(s: str) -> str:
    # 앞의 0 제거, 전부 0이면 "0"
    t = s.lstrip('0')
    return t if t else "0"

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = []
    for idx in range(n):
        s = input().strip()
        ns = normalize(s)
        arr.append((len(ns), ns, idx, s))  # (정규화 길이, 정규화 값, 입력순서, 원본)

    # 숫자 크기 비교: (정규화 길이, 정규화 문자열)로 정렬하면 됨
    # 안정성(동일 값이면 입력순서 유지)을 위해 idx 포함
    arr.sort(key=lambda x: (x[0], x[1], x[2]))

    out = []
    for _, __, ___, orig in arr:
        out.append(orig)
    sys.stdout.write("\n".join([x[3] for x in arr]) + "\n")

if __name__ == "__main__":
    main()
