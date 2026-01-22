import sys

def solution():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 3:
        return

    n = int(lines[0])
    wait_days = int(lines[1]) # D
    life_days = int(lines[2]) # F
    
    # dp[i] = i번째 날에 '새로 태어난' 아메바 수
    dp = [0] * (n + 1)
    
    # 1일 차에 최초 1마리
    dp[1] = 1
    
    # 현재 번식 가능한(다 자란) 아메바 수
    active_parents = 0
    
    for i in range(2, n + 1):
        # 1. 성장 기간(Wait)이 지나 번식 가능해진 그룹 추가
        if i - wait_days >= 1:
            active_parents += dp[i - wait_days]
            
        # 2. 수명(Life)이 다해 사라지는 그룹 제거
        # (i - life_days)일에 태어난 애들은 오늘 사라짐 (번식 능력 상실)
        if i - life_days >= 1:
            active_parents -= dp[i - life_days]
        
        # 오늘 새로 태어난 수 = 현재 번식 가능한 부모 수 * 1
        dp[i] = active_parents
        
    # N일 차에 살아있는 수 구하기
    # = (N - life_days + 1)일부터 N일까지 태어난 아메바들의 합
    total_alive = 0
    start_day = max(1, n - life_days + 1)
    
    for i in range(start_day, n + 1):
        total_alive += dp[i]
        
    print(total_alive)

if __name__ == "__main__":
    solution()
