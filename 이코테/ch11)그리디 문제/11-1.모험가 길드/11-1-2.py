n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #그룹 최댓값
cnt = 0 # 그룹에 들어갈 인원 세는 것

for i in data: # 1 2 2 2 3
    cnt+=1
    if i > cnt:
        continue
    if i == cnt:
        result+=1
        cnt = 0

print(result)
