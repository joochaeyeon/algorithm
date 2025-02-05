s = input()
result = []
isNum = 0

for x in s:
    if x.isalpha():
        result.append(x)
    else:
        isNum+=int(x)

result.sort()

if isNum != 0:
    result.append(str(isNum))

print("".join(result))
