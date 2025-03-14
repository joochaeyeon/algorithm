# https://www.acmicpc.net/problem/10825

import sys

n = int(sys.stdin.readline().strip())
data = []

for i in range(n):
    name, korean, english, math =sys.stdin.readline().split()
    data.append((name, int(korean), int(english), int(math)))

data.sort(key = lambda x: (-x[1],x[2],-x[3],x[0])) #-x[1] : - 는 내림차순으로 정렬!

for i in data:
    print(i[0])