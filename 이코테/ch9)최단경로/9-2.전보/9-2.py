import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())  # 노드 개수, 간선 개수, 시작 노드
graph = [[] for _ in range(n + 1)]  # 그래프 초기화
distance = [INF] * (n + 1)  # 최단 거리 테이블 초기화

# 그래프 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())  # x에서 y로 가는 비용이 z
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:  # 인접 노드 탐색
            cost = dist + i[1]  # 현재 노드를 거쳐서 가는 거리 계산
            if cost < distance[i[0]]:  # 최단 거리 업데이트
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  # 우선순위 큐에 저장

# 다익스트라 실행
dijkstra(start)

# 결과 계산
cnt = 0  # 도달할 수 있는 도시 수
max_dist = 0  # 가장 먼 도시 거리

for d in distance:
    if d != INF:
        cnt += 1
        max_dist = max(max_dist, d)

print(cnt - 1, max_dist)  # 시작 노드는 제외해야 하므로 cnt - 1 출력
