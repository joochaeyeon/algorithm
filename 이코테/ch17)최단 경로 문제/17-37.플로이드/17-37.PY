# 각 지점마다의 최단경로를 찾아내는 것, 자기 자신은 0이 된다.
# -> 플로이드 워셜 알고리즘 이용‼️

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    # 가장 짧은 간선 정보로만 저장
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print(0, end =" ")
        else:
            print(graph[a][b], end =" ")
    print() #다음줄
