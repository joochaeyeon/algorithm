# ⭐
# BFS사용

from collections import deque

#n:정점, m:간선, k:최단거리, x:출발도시
n, m, k, x = map(int, input().split())

graph=[[] for _ in range (n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0 #출발 지점

#BFS 수행
q = deque([x])
while q:
    now =q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        if distance[next_node] == -1: 
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1) 
