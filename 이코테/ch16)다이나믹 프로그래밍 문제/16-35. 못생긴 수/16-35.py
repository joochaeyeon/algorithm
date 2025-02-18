# ⭐
# 소인수 문제
# 오직 2,3,5를 약수로 가지는 합성수 의미 
# 즉, 2,3,5의 배수들이 오름차순으로 정렬되고 n번째를 출력하면 된다.

n = int(input()) 
dp = [0] * n
dp[0] = 1  

index2 = index3 = index5 = 0  
next2, next3, next5 = 2, 3, 5 

for i in range(1, n):

    dp[i] = min(next2, next3, next5)


    if dp[i] == next2:
        index2 += 1
        next2 = dp[index2] * 2
    if dp[i] == next3:
        index3 += 1
        next3 = dp[index3] * 3
    if dp[i] == next5:
        index5 += 1
        next5 = dp[index5] * 5

print(dp[n-1])
