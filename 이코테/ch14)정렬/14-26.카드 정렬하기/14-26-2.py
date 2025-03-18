# https://www.acmicpc.net/problem/1715
# ⭐⭐⭐
# 알고리즘을 생각해 내지 못함....!
# -> 내가 보기엔 작은 순서대로 앞에서 부터 합치는 것이 답일듯!!
# 앞에 두개 합친걸 다시 넣어서 다른 숫자와 더해야함 -> 큐 사용

import heapq

n = int(input())
heap = []

for i in range(n):
    a = int(input())
    heapq.heappush(heap, a)

result = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    mid_result = a+b
    result +=mid_result
    heapq.heappush(heap, mid_result) #결과 값 다시 큐에다 넣어야함


