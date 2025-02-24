# ⭐⭐⭐


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b] = a #작은 값이 부모가 되도록 연결!
    else:
        parent[a] = b

g = int(input())
p = int(input())
parent= [0]*(g+1)

for i in range(1, g+1):
    parent[i] = i

result = 0

for _ in range(p):
    data = find_parent(parent, int(input())) #현재 비행기의 탑승구의 루트 확인 -> 0일 시 끝 더이상 할당 못함
    if data == 0:
        break
    union_parent(parent,data,data-1) #왼쪽 집합들과 합치기!!
    result+=1
print(result)