# ⭐⭐⭐
# bottom - up방식으로 삼각형의 맨 아래에서부터 위로 올라오면서 가장 큰 경로 값을 갱신하는 방식으로 구현되어진다!!

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
        for j in range(i+1):
            # 1. 왼쪽 위에서 내려오는 경우
            if j ==0:
                up_left = 0
            else:
                up_left = dp[i-1][j-1]
            # 2. 바로 위에서 내려오는 경우
            if j == i:
                up = 0
            else:
                up = dp[i-1][j]
                
            dp[i][j] = dp[i][j] + max(up_left, up)
            
print(max(dp[n-1]))