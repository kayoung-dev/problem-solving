import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
        
    try:
        n = int(line)
        
        # 방법 1: 반복문 활용
        # total = 0
        # for i in range(1, n + 1):
        #     if i % 3 == 1: total += 10
        #     elif i % 3 == 2: total += 20
        #     else: total += 30
        # print(total)

        # 방법 2: 수식 활용 (더 효율적임)
        sets = n // 3        # 3일 세트가 몇 번 반복되는지
        remainder = n % 3    # 세트 이후 남은 날짜
        
        # 한 세트(10+20+30)는 60점
        total = sets * 60
        
        if remainder == 1:
            total += 10
        elif remainder == 2:
            total += 30  # 10 + 20
            
        print(total)
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
