#국어 감소 -> 영어 증가 -> 수학 감소 -> 이름이 사전 순 (대문자 -> 소문자)

import sys

n = int(sys.stdin.readline().strip())
data = []

for i in range(n):
    name, korean, english, math =  sys.stdin.readline().split()
    data.append((name, int(korean), int(english), int(math)))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in data:
    print(i[0])