n,m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# POINT
# a 배열의 가장 작은 수 <-> b배열의 가장 큰 수 
# 이래야지 a배열 합이 가장 크게 나온다.
a.sort()
b.sort(reverse=True)

for i in range(m):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))