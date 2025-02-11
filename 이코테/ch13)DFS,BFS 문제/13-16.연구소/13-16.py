# ⭐⭐⭐⭐
# 어려운 문제
# DFS사용

n,m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)] #벽을 설치한 후의 맵

for _ in range(n):
    data.append(list(map(int,input().split())))


dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

#바이러스 퍼뜨리는 함수
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx,ny) #재귀함수

#안전지대 계산 함수
def get_score():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt +=1
    return cnt

#울타리 설치 함수
def dfs(fence):
    global result
    if fence == 3: #울타리3개 설치
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j) #바이러스 퍼뜨리기
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                fence+=1
                dfs(fence) #다음 벽을 세우기 위해 재귀호출
                data[i][j] =0 #백트래킹 (벽 원상복구) -> 다른 경우의 수도 보기 위해서 백트래킹하는 것
                fence-=1

dfs(0)
print(result)