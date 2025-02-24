# ⭐⭐⭐⭐

n,m = map(int, input().split())
parent = [0] *(n+1)

edges =[]
result = 0

for i in range(1,n+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    x,y,z = map(int, input().split())
    edges.append((z,x,y))

edges.sort()
total = 0 #전체 가로등 비용

for edge in edges:
    cost,a,b = edge
    total+=cost
    #사이클이 발생하지 않는 경우에만 집합에 포함시킴!!
    # -> 부모가 같지 않으면 사이클이 발생 안하거다.
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(total - result) #total-result는 꺼야 하는 가로등의 총 비용을 의미!!