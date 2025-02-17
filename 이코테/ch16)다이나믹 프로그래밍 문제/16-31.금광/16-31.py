# ⭐⭐⭐
# 어려운 문제

t = int(input())
results = [] 

for _ in range(t):
    n, m = map(int, input().split())  # (n, m) -> 최대(행, 열)
    data = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(data[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 1. 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 2. 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 3. 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)  # 세 가지 경우 중 가장 큰 값 선택

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    results.append(result) 

for res in results:
    print(res)
