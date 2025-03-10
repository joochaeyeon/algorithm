from collections import deque

n,m,k,x = map(int,input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distatnce = [-1]*(n+1) #거리 초기화
distatnce[x] = 0 #출발도시

q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distatnce[next] == -1:
            distatnce[next] = distatnce[now] +1
            q.append(distatnce[next])

#전체적으로 길이가 K인걸 다 출력하는 것이니 
#bfs를 통해 길이를 구하고 k에 해당하는 노드를 출력!
check = False
for i in range(1,n+1):
    if distatnce[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)