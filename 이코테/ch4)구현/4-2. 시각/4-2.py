n = int(input())
cnt = 0

#00시00분00초
for i in range(n+1):
    for j in range(60): 
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1

print(cnt)