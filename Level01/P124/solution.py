import sys

def solve():
    line = sys.stdin.read().strip()
    if not line:
        return
    
    s = int(line)
    count = 0
    
    # 000부터 999까지 모든 경우를 확인
    for i in range(10):      # 첫 번째 자리
        for j in range(10):  # 두 번째 자리
            for k in range(10): # 세 번째 자리
                if i + j + k == s:
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    solve()
