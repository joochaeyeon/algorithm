# ⭐⭐⭐⭐
# BFS 이용

from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]
    total_population = board[x][y]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(board[cx][cy] - board[nx][ny]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    total_population += board[nx][ny]
    
    if len(union) > 1:
        new_population = total_population // len(union)

        for ux, uy in union:
            board[ux][uy] = new_population
        return True
    return False

days = 0

while True:
    visited = [[False] * n for _ in range(n)]
    moved = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True
    if not moved:
        break

    days += 1

print(days)
