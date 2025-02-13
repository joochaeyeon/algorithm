import sys

n = int(sys.stdin.readline().strip())
house = list(map(int, sys.stdin.readline().split()))

house.sort()
result = house[(n-1) // 2] #홀수 -> 가운데, 짝수 -> 가운데 두 개 중 작은 값 선택택
print(result)