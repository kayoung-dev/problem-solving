import sys
from collections import deque

# 입력 최적화
input = sys.stdin.readline

def solve():
    # 1. 초기 설정 읽기
    line1 = input().strip()
    if not line1: return
    limit = int(line1)
    
    line2 = input().strip()
    if not line2: return
    q_count = int(line2)
    
    # 2. 시스템 데이터 구조
    queue = deque() # FIFO 저장소
    lookup_set = set() # 중복 체크용 (car_id, lot_id, ts)
    
    results = []
    
    # 3. 명령 처리
    for _ in range(q_count):
        cmd = input().strip().split()
        if not cmd: continue
        
        type = cmd[0]
        
        if type == "ADD":
            car_id, lot_id, ts = int(cmd[1]), int(cmd[2]), int(cmd[3])
            item = (car_id, lot_id, ts)
            
            if item in lookup_set:
                results.append("false")
            else:
                # 용량 초과 시 오래된 데이터 삭제
                if len(queue) >= limit:
                    oldest = queue.popleft()
                    lookup_set.remove(oldest)
                
                queue.append(item)
                lookup_set.add(item)
                results.append("true")
                
        elif type == "PROCESS":
            if not queue:
                results.append("EMPTY")
            else:
                item = queue.popleft()
                lookup_set.remove(item)
                results.append(f"[{item[0]}, {item[1]}, {item[2]}]")
                
        elif type == "COUNT":
            target_lot = int(cmd[1])
            start_t, end_t = int(cmd[2]), int(cmd[3])
            
            count = 0
            # 현재 저장된 모든 차량 전수 조사
            for car, lot, ts in queue:
                if lot == target_lot and start_t <= ts <= end_t:
                    count += 1
            results.append(str(count))
            
    # 4. 일괄 출력
    print("\n".join(results))

if __name__ == "__main__":
    solve()
