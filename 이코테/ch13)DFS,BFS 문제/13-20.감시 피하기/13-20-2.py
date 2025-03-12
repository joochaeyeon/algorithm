# https://www.acmicpc.net/problem/18428
# ⭐⭐⭐⭐⭐
# POINT)
# 조합을 이용하여 모든 경우의 수를 확인해야만 한다.

from itertools import combinations

n = int(input())
graph = []
teachers = []
spaces= [] 

for i in range(n):
    row = list(input().split())
    graph.append(row)
    for j in range(n):
        if row[j] == "T":
            teachers.append((i,j))
        elif row[j] == "X":
            spaces.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def watch(x,y,dir):
    while 0<= x <n  and 0<=y<n:
        if graph[x][y] == "O":
            return False
        if graph[x][y] == 'S': 
            return True
        x+=dx[dir]
        y+=dy[dir]
    return False

def is_safe():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return False
    return True

for walls in combinations(spaces, 3):
    #장애물 설치
    for x, y in walls:
        graph[x][y] = 'O'

    if is_safe():
        print("YES")
        exit(0)

    #장애물 제거 (백트래킹)
        graph[x][y] = 'X'

print("NO")
