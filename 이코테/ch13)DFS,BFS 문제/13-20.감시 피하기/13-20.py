# ⭐⭐⭐⭐
# 모든 경우의 수 고려 
# => 완전 탐색 사용

from itertools import combinations

n = int(input()) 
graph = []
teachers = [] 
spaces = [] #빈공간 위치 정보

for i in range(n):
    row = list(input().split())
    graph.append(row)
    for j in range(n):
        if row[j] == 'T':  
            teachers.append((i, j)) 
        elif row[j] == 'X':  
            spaces.append((i, j))

#감시 방향(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#감시 여부 함수
def watch(x, y, dir):
    while 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 'O':  #장애물이 있으면 감시 불가능
            return False
        if graph[x][y] == 'S':  #학생을 발견하면 감시 가능
            return True
        x += dx[dir]
        y += dy[dir]
    return False

#현재 장애물 배치에서 감시를 피할 수 있는지 확인하는 함수
def is_safe():
    for x, y in teachers:  #모든 선생님에 대해 감시 진행
        for i in range(4):  #4가지 방향으로 감시
            if watch(x, y, i):  #감시 가능여부
                return False
    return True 

#장애물 3개 배치하는 모든 조합 확인
for walls in combinations(spaces, 3):
    #장애물 설치
    for x, y in walls:
        graph[x][y] = 'O'

    if is_safe():
        print("YES")
        exit(0)

    #장애물 제거 (백트래킹) -> 모든 경우의 수를 확인해야하기에
    for x, y in walls:
        graph[x][y] = 'X'

print("NO")
