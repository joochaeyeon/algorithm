n,k = map(int, input().split())

#1)N에서 1을 뺴라 2) N을 K로 나눠라
cnt = 0 #최소 횟수로 1,2를 반복해라 1이 될때까지

#TIP) 최대한 많이 나눠라 
while True:
    if n == 1: #조건을 만족하니까 빠져나가기
        break

    if n%k ==0: #n이 k로 안나눠진다면 -1 하면 되니까 if-else로 처리
        n//=k
    else:
        n-=1
    cnt+=1

print(cnt)