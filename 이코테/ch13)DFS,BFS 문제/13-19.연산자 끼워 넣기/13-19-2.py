# https://www.acmicpc.net/problem/14888

n = int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

min_result = 1e9
max_result = -1e9 

def dfs(i, now):
    global min_result, max_result, add, sub, mul, div

    if i == n:
        min_result = min(min_result, now)
        max_result = max(max_result, now)
    else:
        if add > 0:
            add-=1
            dfs(i+1, now+data[i]) 
            add+=1 #백트래킹
        if sub > 0:
            sub-=1
            dfs(i+1, now-data[i]) 
            sub+=1
        if  mul > 0:
            mul-=1
            dfs(i+1, now*data[i]) 
            mul+=1
        if div > 0:
            div -= 1
            if now < 0:
                dfs(i + 1, -(-now // data[i]))  #음수 처리!!!!-> 중요한 부분!!
            else:
                dfs(i + 1, now // data[i])  
            div += 1

dfs(1, data[0])

print(max_result)
print(min_result)