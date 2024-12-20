n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

table = [10001] * (m + 1)
table[0] = 0  # 0원을 만들기 위해 필요한 동전 개수는 0

for coin in array:
    for j in range(coin, m + 1):
        if table[j - coin] != 10001:  # 동전을 사용할 수 있는 경우
            table[j] = min(table[j], table[j - coin] + 1)


if table[m] == 10001: 
    print(-1)
else:
    print(table[m])
