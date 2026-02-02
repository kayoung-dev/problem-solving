import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2:
            return
        heights = list(map(int, line2.split()))
        
        max_height = -1
        answer_pos = 0
        
        # 모든 학생을 한 명씩 확인하며 가장 큰 키를 찾음
        for i in range(n):
            if heights[i] > max_height:
                max_height = heights[i]
                answer_pos = i + 1  # 1번째부터 시작하므로 +1
                
        print(answer_pos)
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
