INF = int(1e9)

n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신은 거리 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b]=0

# 각 간선에 대한 정보를 받아 그 정보로 업데이트
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)