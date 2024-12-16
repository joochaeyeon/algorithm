n, m = map(int,input().split())

#유저가 방문한 위치를 저장하기 위한 맵 생성
data = [[0] * m for _ in range(n)]
x,y,dir = map(int,input().split())
data[x][y] = 1 #현재 위치는 방문한 걸로 변경!

#전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0] #북,동,남,서 방향 정의 -> 90도로 왼쪽 회전이기에 북->동->남->서
dy = [0,1,0,-1]

#왼쪽으로 회전 (90도로 회전)
def turn_left():
    global dir #전역변수로 정의
    dir -=1
    if dir == -1:
        dir = 3 #방향은 0,1,2,3 이렇게 존재하기에 dir==-1일 경우 3으로 초기화 시켜줌


#시뮬레이션 시작
cnt = 1 #현재 위치에 대해 cnt를 +1해준 것
turn_time = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if data[nx][ny] == 0 and array[nx][ny] == 0:
        data[nx][ny] = 1
        x = nx
        y = ny
        cnt+=1
        turn_time=0
        continue
    else:
        turn_time+=1
        if turn_time == 4:
            nx = x - dx[dir]
            ny = y - dy[dir]

            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

print(cnt)

