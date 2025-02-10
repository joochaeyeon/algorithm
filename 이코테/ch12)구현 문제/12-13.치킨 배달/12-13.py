# ⭐⭐⭐⭐
# 어려운 문제
# 최대 13개에서 M개를 선택하는 문제로 조합이용❗

from itertools import combinations

n,m = map(int, input().split())
chicken, house = [],[]

for r in range(n): #행
    data = list(map(int, input().split()))
    for c in range(n): #열
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

#모든 치킨 집 중 m개의 치킨집을 뽑는 조합 계산
all_result = list(combinations(chicken,m))

def get_sum(all_result):
    result = 0
    for hx, hy in house:
        temp = 1e9 #무한으로 설정정
        for cx, cy in all_result:
            temp = min(temp, abs(hx-cx) + abs(hy - cy)) #abs()는 절댓값
        result += temp
    return result

result = 1e9
for i in all_result:
    result = min(result, get_sum(i))
print(result)