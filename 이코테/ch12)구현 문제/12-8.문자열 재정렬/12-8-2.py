s = input()
alpa = []
isNum = []

for i in range(len(s)):
    if ord(s[i]) >= 65:  # 아스키 코드로 비교
        alpa.append(s[i])
    else:
        isNum.append(s[i])

alpa.sort()
result_num = sum(int(x) for x in isNum)  # 숫자 리스트 합계 수정
print(f"{''.join(alpa)}{result_num}")