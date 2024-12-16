data = input()

x = int(ord(data[0])) - int(ord('a')) + 1 
y = int(data[1])
methods = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] #총 8가지 방법이 존재

cnt = 0
for i in methods:
    nx = x+i[1]
    ny = y+i[0]

    if nx >=1 and nx <= 8 and ny >= 1 and ny<=8:
        cnt+=1

print(cnt)