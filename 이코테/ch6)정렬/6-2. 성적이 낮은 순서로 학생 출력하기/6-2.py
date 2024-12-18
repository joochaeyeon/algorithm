n = int(input())

array = []

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1]))) #튜플을 리스트에 추가하기 위해 괄호 두번 쳐주는 것!

array = sorted(array, key = lambda x : x[1]) #점수를 기준으로 sort하는 것!!

for i in array:
    print(i[0], end =' ')