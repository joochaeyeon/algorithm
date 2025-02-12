# ⭐⭐⭐⭐⭐⭐
# 어려운 문제
# 조금 어려운 BFS 문제

from collections import deque

def is_valid(x, y, n, board): #이동가능 여부
    return 0 <= x < n and 0 <= y < n and board[x][y] == 0

def bfs(board):
    n = len(board)
    queue = deque([((0, 0), (0, 1), 0)])  #((x1, y1), (x2, y2), 이동 횟수)
    visited = set([((0, 0), (0, 1))])

    #이동 방향 (상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        (x1, y1), (x2, y2), cnt = queue.popleft()

        #도착점에 도달하면 반환
        if (x1, y1) == (n-1, n-1) or (x2, y2) == (n-1, n-1):
            return cnt

        for i in range(4):
            nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
            if is_valid(nx1, ny1, n, board) and is_valid(nx2, ny2, n, board):
                if ((nx1, ny1), (nx2, ny2)) not in visited:
                    visited.add(((nx1, ny1), (nx2, ny2)))
                    queue.append(((nx1, ny1), (nx2, ny2), cnt + 1))

        #회전 (가로 <-> 세로 변경)
        if x1 == x2:  #가로로 놓여 있을 때
            for d in [-1, 1]:  # 위(-1), 아래(1) 이동 가능 여부 체크
                if is_valid(x1 + d, y1, n, board) and is_valid(x2 + d, y2, n, board):
                    if ((x1, y1), (x1 + d, y1)) not in visited:
                        visited.add(((x1, y1), (x1 + d, y1)))
                        queue.append(((x1, y1), (x1 + d, y1), cnt + 1))
                    if ((x2, y2), (x2 + d, y2)) not in visited:
                        visited.add(((x2, y2), (x2 + d, y2)))
                        queue.append(((x2, y2), (x2 + d, y2), cnt + 1))
        
        if y1 == y2:  #세로로 놓여 있을 때
            for d in [-1, 1]:  #왼쪽(-1), 오른쪽(1) 이동 가능 여부 체크
                if is_valid(x1, y1 + d, n, board) and is_valid(x2, y2 + d, n, board):
                    if ((x1, y1), (x1, y1 + d)) not in visited:
                        visited.add(((x1, y1), (x1, y1 + d)))
                        queue.append(((x1, y1), (x1, y1 + d), cnt + 1))
                    if ((x2, y2), (x2, y2 + d)) not in visited:
                        visited.add(((x2, y2), (x2, y2 + d)))
                        queue.append(((x2, y2), (x2, y2 + d), cnt + 1))

    return -1 #이동 불가능한 경우

def solution(board):
    return bfs(board)

board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
print(solution(board))