import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    lengths = list(map(int, input_data[1:]))
    
    # 이중 반복문을 통해 모든 가능한 두 막대의 조합(Pair)을 전수 조사
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            if lengths[i] + lengths[j] == 100:
                found = True
                break
        if found:
            break
            
    if found:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
