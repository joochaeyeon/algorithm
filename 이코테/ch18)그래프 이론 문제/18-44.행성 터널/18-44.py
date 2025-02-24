# ⭐⭐⭐⭐⭐

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))  


edges = []

for dim in range(3):
    planets.sort(key=lambda p: p[dim])  
    for i in range(n - 1):
        cost = abs(planets[i][dim] - planets[i + 1][dim])
        edges.append((cost, planets[i][3], planets[i + 1][3]))


edges.sort()

parent = [i for i in range(n)]
total_cost = 0

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b): 
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)
