# ⭐⭐⭐⭐

n = int(input())
time = [] #각 상담을 완료하는데 걸리는 시간
price = [] # 각 상담을 완료했을때 받을 수 있는 금액
dp = [0] * (n+1)
max_result = 0

for _ in range(n):
    x,y = map(int, input().split())
    time.append(x)
    price.append(y)

#bottom-up 방식을 이용
for i in range(n-1, -1, -1): 
    t = time[i] + i

    if t <= n: #상담이 기간 안에 끝나는 경우
        dp[i] = max(price[i] + dp[t], max_result)
        max_result = dp[i]
    else: #상담이 기간 안에 안끝날 경우
        dp[i] = max_result

print(max_result)