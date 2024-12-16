n = int(input())
data = list(map(str, input().split()))


#무조건 (1,1)에서 시작
x = 1
y = 1

for i in data:
    # 현재 위치를 임시 변수로 저장
    nx, ny = x, y  
    
    if i == 'R': 
        ny+=1
    elif i == 'L':
        ny-=1
    elif i == 'U':
        nx-=1
    elif i == 'D':
        nx+=1

    # 이동 후 위치가 범위를 벗어나면 무시 (원래 좌표 유지하겠다는 의미)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 유효한 경우에만 실제 이동
    x, y = nx, ny

print(x,y)