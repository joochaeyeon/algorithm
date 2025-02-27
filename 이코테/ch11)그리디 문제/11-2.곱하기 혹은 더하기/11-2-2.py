s = input()
result = 1  #최종 값 -> 곱셈할때 문제가 발생하니 1로 초기화

for i in s:
    if int(i) == 0:
        continue #어차피 0을 더해도 0이니
    else:
        result*=int(i)
print(result)