data = input()

result = 1

for i in range(len(data)):
    if data[i] == '0': #주의) 문자열이기에 '0'으로 해서 비교해야한다!
        continue #어차피 0은 더하나 마나니까
    else:
        result *= int(data[i])

print(result)

