# ⭐⭐⭐⭐
# 어려운 문제
# BFS사용

from collections import deque

n,k = map(int,input().split())
graph=[]
virus=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j)) #(바이러스 종류, 시간, x, y)

virus.sort()
q = deque(virus)

target_s, target_x, target_y = map(int,input().split()) 

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny]=virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])