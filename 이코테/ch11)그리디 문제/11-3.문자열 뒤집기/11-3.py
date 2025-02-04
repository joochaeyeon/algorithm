data = input() #문자열을 입력받음
 
result = 0 #최종 행동 횟수
# 0과 1은 서로 바뀌는 그 순간 카운트 들어감
cnt_0 = 0 
cnt_1 = 0 

for i in range(1,len(data)):
    if data[i] == '0' and data[i-1] == '1':
        cnt_0 +=1
    elif data[i] == '1' and data[i-1] == '0':
        cnt_1 +=1

result = min(cnt_0, cnt_1)

print(result)