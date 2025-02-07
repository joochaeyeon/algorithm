# ⭐⭐⭐⭐
# 어려운 문제
# 뱀의 머리가 동,서,남,북에 위치할 수 있음을 고려하기❗

from collections import deque

n = int(input())
k = int(input()) #사과 개수
data = [[0]*(n+1) for _ in range(n+1)] 


#사과 위치 입력 받기
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1

l = int(input())
turn = {} #딕셔너리 형태로 입력받기 {초 : 방향} ⭐

for _ in range(l):
    time, direction = input().split()
    turn[int(time)] = direction 

# 방향 정보 (우,하,좌,상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution():
    time = 0 #현재 시간
    direction = 0 #뱀 머리 방향
    snake = deque([(1, 1)]) #뱀 위치
    data[1][1] = 2  #뱀이 있는 위치는 2로 표시

    while True:
        time+=1
        head_x, head_y = snake[-1] #머리 위치
        new_x = head_x + dx[direction]
        new_y = head_y + dy[direction]

        if new_x < 1 or new_x > n or new_y < 1 or new_y > n or data[new_x][new_y] == 2:
            return time
        
        snake.append((new_x, new_y))

        if data[new_x][new_y] == 1:  # 사과가 있다면
            data[new_x][new_y] = 2  # 사과를 먹고 길이 유지
        else:  # 사과가 없다면
            tail_x, tail_y = snake.popleft()  # 꼬리 제거
            data[tail_x][tail_y] = 0  # 보드에서 꼬리 제거
            data[new_x][new_y] = 2  # 새로운 머리 위치 추가 -> 뱀이니까 2로 채움

            if time in turn :
                if turn[time] == 'L':
                    direction = (direction - 1) % 4
                else:
                    direction = (direction + 1) % 4
print(solution())


