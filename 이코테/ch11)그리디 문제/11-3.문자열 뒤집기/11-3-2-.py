s = input()

cnt_0 = 0
cnt_1 = 0

for i in range(1,len(s)):
    if s[i] == '0' and s[i-1] == '1':
        cnt_0 +=1
    elif s[i] == '1' and s[i-1] == '0':
        cnt_1 +=1

        
print(min(cnt_0, cnt_1)) #작게 변하는 수를 뒤집으면 되는 거니까