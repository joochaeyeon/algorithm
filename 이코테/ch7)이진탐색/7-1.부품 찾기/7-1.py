#가게
n = int(input())
nList = list(map(int, input().split()))

#손님
m = int(input())
mList = list(map(int, input().split()))

for i in mList:
    if i in nList:
        print("yes", end = " ")
    else:
        print("no", end = " ")