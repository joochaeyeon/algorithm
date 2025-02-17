n = int(input())
data = list(map(int, input().split()))

# bottom-up 방식으로 하는게 좋을듯
# 그 다음꺼와 비교했을때 뒤의 숫자가 앞에 숫자보다 크면 열외 
dp = [1] * n

for i in range(1, n): 
    for j in range(0, i):
        if data[j] > data[i]:  
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))



# # 문제 발생 1) 
# # 단순히 연속된 두 개의 수를 비교하는 것이 아니라 전체 수열을 고려해야만 한다.
# cnt = 0

# for i in range(n-2, 0, -1):
#     if data[i] > data[i-1]:
#         cnt+=1
# print(cnt)