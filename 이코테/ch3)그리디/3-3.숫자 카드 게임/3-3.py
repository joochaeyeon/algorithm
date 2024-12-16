n, m  =map(int,input().split()) #행,열
result = 0

# 데이터 전체로 받기
# 데이터 받을때 가장 작은 값 저장해서 가지고 있기 -> 행별 작은 수를 저장하는 것
for i in range(n):
    data = list(map(int,input().split()))
    if result < min(data): # 가장 작은 수 중 큰 값을 저장하는 것!
        result = min(data)

print(result)

