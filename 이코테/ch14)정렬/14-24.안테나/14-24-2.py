# https://www.acmicpc.net/problem/18310

n = int(input())
data = list(map(int,input().split()))

data.sort()

result = data[(n-1) // 2] 
print(result)