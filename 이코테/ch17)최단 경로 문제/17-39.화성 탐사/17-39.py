# ⭐⭐⭐⭐
# 어려운 문제!!
# 다익스트라 최단 경로 알고리즘 사용
# 한지점에서 목표 지점까지의 최단 거리만 알면 되는 문제이기에

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 상하좌우 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input()) 
for _ in range(T): 
    n = int(input())  # 노드 개수

    graph = [list(map(int, input().split())) for _ in range(n)]

    distance = [[INF] * n for _ in range(n)] #테스트 케이스별 distance 초기화

    x, y = 0, 0
    q = [(graph[x][y], x, y)] # (distance,x좌표,y좌표) 순서대로 q에 들어간다.
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))


    print(distance[n-1][n-1])
