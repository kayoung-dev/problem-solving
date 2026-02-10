import os
import random
from typing import List, Tuple

import os
import random

# ---------------------------------------------------------
# 1. 경로 설정 (Level01/P115 폴더 생성)
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
base_dir = os.path.join(root_dir, "Level01", "P115")
test_dir = os.path.join(base_dir, "test")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

TICK = "`" * 3

# ---------------------------------------------------------
# 2. 문제 설명 (problem.md)
# ---------------------------------------------------------
problem_md = rf"""# 이 정원사의 호스 연결 최적화

## 문제 설명
정원사 이 씨는 넓은 평지에 총 $V$개의 꽃밭을 가꾸고 있습니다. 최근 가뭄이 심해져 모든 꽃밭에 물을 공급하기 위해 수로 시스템을 구축하려고 합니다.

이 씨는 모든 꽃밭이 서로 연결되어 어느 한 곳에서 물을 틀면 모든 꽃밭에 물이 전달되기를 원합니다. 꽃밭 사이에는 미리 조사해둔 $E$개의 연결 가능한 경로들이 있으며, 각 경로마다 필요한 호스의 길이 $L$이 다릅니다. 

모든 꽃밭을 하나의 연결망으로 묶되, 호스를 구입하는 비용을 아끼기 위해 **사용되는 호스의 총 길이 합을 최소화**하는 경로들을 선택해야 합니다. 정렬된 정보를 바탕으로 이 씨를 도와 최소한의 호스 길이를 구하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에는 꽃밭의 개수 $V$가 주어집니다. 
- $1 \le V \le 100$
- 두 번째 줄에는 연결 가능한 경로의 개수 $E$가 주어집니다. 
- $1 \le E \le 1,000$
- 세 번째 줄부터 $E$개의 줄에 걸쳐 각 경로의 정보가 $A, B, L$ 형태로 주어집니다. 
- 이는 $A$번 꽃밭과 $B$번 꽃밭을 연결하는 호스의 길이가 $L$임을 의미합니다. 
- $1 \le L \le 10,000$

## 출력 형식 (Output Format)
모든 꽃밭을 연결하는 데 필요한 호스의 최소 총 길이를 정수로 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
{TICK}
3
3
1 2 10
2 3 5
1 3 2
{TICK}
**Output:**
{TICK}
7
{TICK}

- 경로를 길이순으로 정렬하면 (1, 3) 2m, (2, 3) 5m, (1, 2) 10m입니다.
- 가장 짧은 2m와 5m를 선택하면 모든 꽃밭(1, 2, 3)이 연결되며 총 길이는 $2 + 5 = 7$입니다.

### 예시 2
**Input:**
{TICK}
4
5
1 2 1
2 3 2
3 4 3
4 1 4
1 3 5
{TICK}
**Output:**
{TICK}
6
{TICK}

- 길이가 짧은 순서대로 (1, 2) 1m, (2, 3) 2m, (3, 4) 3m를 선택하면 총 6m로 모든 꽃밭이 연결됩니다. 
- (4, 1)이나 (1, 3)은 이미 연결된 상태이므로 추가할 필요가 없습니다.

### 예시 3
**Input:**
{TICK}
5
7
1 2 5
1 3 3
2 3 2
2 4 8
3 4 10
3 5 4
4 5 6
{TICK}
**Output:**
{TICK}
15
{TICK}
- 호스 길이를 짧은 순으로 정렬합니다: (2, 3) 2m, (1, 3) 3m, (3, 5) 4m, (1, 2) 5m, (4, 5) 6m, (2, 4) 8m, (3, 4) 10m.
- 가장 짧은 **(2, 3) 2m**를 선택합니다.
- 다음으로 짧은 **(1, 3) 3m**를 선택합니다. (1, 2, 3번 연결됨)
- 다음으로 짧은 **(3, 5) 4m**를 선택합니다. (1, 2, 3, 5번 연결됨)
- 다음인 (1, 2) 5m는 이미 1-3-2 경로로 연결되어 있으므로 건너뜁니다.
- 다음인 **(4, 5) 6m**를 선택합니다. (모든 꽃밭 연결 완료)
- 총합: $2 + 3 + 4 + 6 = 15$

---
## 힌트 (Note)
- 모든 장소를 연결하면서 비용을 최소로 하려면, **가장 저렴한(짧은) 경로**부터 차례대로 살펴보는 것이 유리합니다. 
- 다만, 이미 다른 길을 통해 서로 갈 수 있는 상태라면 굳이 호스를 추가로 연결할 필요가 없다는 점에 유의하세요!
"""

with open(os.path.join(base_dir, "problem.md"), "w", encoding="utf-8") as f:
    f.write(problem_md)

# ---------------------------------------------------------
# 3. 정답 코드 (solution.py) 
# ---------------------------------------------------------
solution_py = rf"""import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve():
    input = sys.stdin.readline
    
    line = input().strip()
    if not line: return
    v = int(line)
    
    line = input().strip()
    if not line: return
    e = int(line)
    
    edges = []
    for _ in range(e):
        edge_data = list(map(int, input().split()))
        if len(edge_data) == 3:
            edges.append(edge_data)
            
    # 핵심: 간선 비용(호스 길이)을 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    
    parent = [i for i in range(v + 1)]
    total_length = 0
    count = 0
    
    for a, b, length in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_length += length
            count += 1
            if count == v - 1:
                break
                
    print(total_length)

if __name__ == "__main__":
    solve()
"""

with open(os.path.join(base_dir, "solution.py"), "w", encoding="utf-8") as f:
    f.write(solution_py)

# ---------------------------------------------------------
# 4. 파일 저장 및 테스트케이스 생성
# ---------------------------------------------------------
def solve_internal(v, e, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(v + 1)]
    def _find(x):
        if parent[x] != x: parent[x] = _find(parent[x])
        return parent[x]
    def _union(a, b):
        rootA, rootB = _find(a), _find(b)
        if rootA < rootB: parent[rootB] = rootA
        else: parent[rootA] = rootB

    total = 0
    cnt = 0
    for a, b, l in edges:
        if _find(a) != _find(b):
            _union(a, b)
            total += l
            cnt += 1
    return str(total)

# 테스트 케이스 20개 생성
for i in range(1, 21):
    if i <= 3: # 예시 케이스 반영
        if i == 1: v, e, edges = 3, 3, [[1,2,10],[2,3,5],[1,3,2]]
        elif i == 2: v, e, edges = 4, 5, [[1,2,1],[2,3,2],[3,4,3],[4,1,4],[1,3,5]]
        else: v, e, edges = 5, 7, [[1,2,5],[1,3,3],[2,3,2],[2,4,8],[3,4,10],[3,5,4],[4,5,6]]
    else:
        v = random.randint(5, 20)
        e = random.randint(v, v * 2)
        edges = []
        # 연결성 보장을 위해 최소 트리 구성
        nodes = list(range(1, v + 1))
        random.shuffle(nodes)
        for idx in range(v - 1):
            edges.append([nodes[idx], nodes[idx+1], random.randint(1, 100)])
        # 나머지 랜덤 간선 추가
        for _ in range(e - (v - 1)):
            a, b = random.sample(range(1, v + 1), 2)
            edges.append([a, b, random.randint(1, 100)])

    input_str = f"{v}\n{e}\n" + "\n".join([f"{a} {b} {l}" for a, b, l in edges])
    ans = solve_internal(v, e, edges)
    
    with open(os.path.join(test_dir, f"{i}.in"), "w", encoding="utf-8") as f:
        f.write(input_str)
    with open(os.path.join(test_dir, f"{i}.out"), "w", encoding="utf-8") as f:
        f.write(ans)

print(f"✅ 'Level01/P115' 문제 생성이 완료되었습니다. ")
