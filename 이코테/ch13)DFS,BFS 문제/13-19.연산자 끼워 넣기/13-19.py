# ⭐
# DFS이용

n = int(input())
data = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split()) # 순서대로 + - * % 개수

#min일 경우 가장 작은 값을 구하는 거니까 기본값으로 가장 큰 값을 부여
min_result = 1e9
max_result = -1e9

def dfs(i,now):
    global min_result, max_result, add, sub, mul, div

    if i == n: #모든 연산자를 다 사용할 경우 값 업데이트
        min_result = min(min_result, now)
        max_result = max(max_result, now)
    else:
        if add > 0:
            add-=1
            dfs(i+1, now+data[i]) #재귀적 수행
            add+=1 #백트래킹 -> 모든 조합을 고려해야하기에 재귀적 수행 후 백트래킹시켜 원래 상태로 복구시켜놓음
        if sub > 0:
            sub-=1
            dfs(i+1, now-data[i]) 
            sub+=1
        if mul > 0:
            mul-=1
            dfs(i+1, now*data[i]) 
            mul+=1
        if div > 0:
            div-=1
            dfs(i+1, now/data[i]) 
            div+=1

dfs(1,data[0])

print(max_result)
print(min_result)