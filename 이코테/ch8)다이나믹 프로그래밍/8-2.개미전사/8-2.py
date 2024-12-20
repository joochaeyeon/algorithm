n = int(input())
k = list(map(int, input().split()))

table = [0] * 100

table[0] = k[0]
table[1] = max(k[0], k[1])

for i in range(2,n):
    table[i] = max(table[i-1], table[i-2] + k[i])

print(table[n-1])