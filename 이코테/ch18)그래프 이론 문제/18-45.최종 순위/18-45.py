# ⭐⭐⭐⭐⭐
# 엄청 어려운 문제!!

from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0] *(n+1) #모든 진입차수를 0으로 초기화
    graph = [[False]*(n+1) for i in range(n+1)]
    data=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]] == True
            indegree[data[j]]+=1
    
    #올해 변경된 순위 입력
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] +=1
            indegree[b]-=1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -=1
            indegree[b]+=1

result = []
q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

certain = True
cycle = False

for i in range(n):
    if len(q) == 0:
        cycle = True
        break
    if len(q) >= 2:
        certain = True
        break
    now = q.popleft()
    result.append(now)
    for j in range(1, n+1):
        if graph[now][j]:
            indegree[j] -=1
            if indegree[j] == 0:
                q.append(j)

if cycle:
    print("IMPOSSIBLE")
elif not certain:
    print("?")
else:
    for i in result:
        print(i, end = " ")
        print()