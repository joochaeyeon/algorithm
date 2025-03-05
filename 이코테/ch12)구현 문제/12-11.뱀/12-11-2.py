# ⭐⭐⭐⭐
# 어려운 문제!!

from collections import deque

def solution(n, apples, directions):
    board = [[0] * n for _ in range(n)]  
    
    for x, y in apples:
        board[x-1][y-1] = 1
    
    directions = deque(directions)  
    
    dx = [0, 1, 0, -1]  # 우,하,좌,상 (->시계방향)
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0  
    board[x][y] = 2 
    snake = deque([(x, y)]) 
    direction = 0  
    time = 0  
    
    while True:
        time += 1
        nx, ny = x + dx[direction], y + dy[direction]  
        
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            return time  
        
        if board[nx][ny] == 1:  
            board[nx][ny] = 2 
            snake.append((nx, ny))
        else:  
            board[nx][ny] = 2
            snake.append((nx, ny))
            tx, ty = snake.popleft() 
            board[tx][ty] = 0
        
        x, y = nx, ny  
        
        if directions and time == directions[0][0]:  
            _, turn = directions.popleft()
            if turn == 'L':
                direction = (direction - 1) % 4  
            else:
                direction = (direction + 1) % 4  


n = int(input()) 
k = int(input())  
apples = [tuple(map(int, input().split())) for _ in range(k)]

l = int(input())  
directions = [tuple(input().split()) for _ in range(l)]
directions = [(int(t), d) for t, d in directions]  

print(solution(n, apples, directions))