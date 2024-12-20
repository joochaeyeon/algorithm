n=  int(input()) #가로:n / 세로:2

table = [0]*1001

table[1] = 1
table[2] = 3

for i in range(3,n+1):
    table[i] = (table[i-1] +2 *table[i-2]) %796796

print(table[n])

