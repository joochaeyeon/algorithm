# ⭐⭐⭐⭐
# 문제 이해가 필요한 문제!!
# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

#상하좌우 움직임 -> bfs 이용!!
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

#BFS로 연합 찾기
def process(x, y, index):
    united = [(x, y)]  # 현재 연합을 저장하는 리스트
    q = deque([(x, y)])
    union[x][y] = index  # 현재 연합의 번호 할당
    summary = graph[x][y]  # 연합의 총 인구 수
    cnt = 1  # 현재 연합 국가 수

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    cnt += 1
                    united.append((nx, ny))

    # 연합 국가들의 인구 이동 적용
    new_population = summary // cnt
    for i, j in united:
        graph[i][j] = new_population

    return cnt

total_cnt = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0  # 연합 개수

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                if process(i, j, index) > 1:  # 연합이 형성되었을 때만 index 증가
                    index += 1

    if index == 0:  #연합이 더 이상 형성되지 않으면 종료
        break

    total_cnt += 1

print(total_cnt)
