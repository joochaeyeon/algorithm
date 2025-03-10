# ⭐⭐⭐⭐
# 어려운 문제!!
# DFS사용
# 0:빈칸, 1:벽, 2:바이러스
# https://www.acmicpc.net/problem/14502

n,m = map(int,input().split())
data =[]
temp = [[0] * m for _ in range(n)] #벽을 설치한 뒤의 map

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 0

#dfs를 통해 바이러스가 사방에 퍼지도록 하는 함수
def virus(x,y):
    for i in range(4): #한점에 대해 상,하,좌,우로 바이러스 퍼트림
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx <n and ny >=0 and ny < m :
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 #바이러스 전염
                virus(nx,ny)

#현재 맵에서 안전한 영역의 크기 계산하는 함수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score+=1
    return score

#울타리 설치 후 매번 안전 영역 크기 계산
def dfs(cnt): # cnt:울타리 갯수
    global result

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return #return 값 없이 그냥 함수를 종료시킴
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] =1
                cnt+=1
                dfs(cnt)
                data[i][j] =0 #백트래킹을 위해 -> 벽을 설치한 상태가 유지되므로 잘못된 경우의 수를 탐색하게 되기에
                cnt-=1

dfs(0)
print(result)   
