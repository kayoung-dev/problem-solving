import sys

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
