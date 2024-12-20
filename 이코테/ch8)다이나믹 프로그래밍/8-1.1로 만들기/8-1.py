x = int(input())

table = [0]*30001 #DP테이블 초기화 1<=x<=30000이기에

for i in range(2,x+1):

    table[i] = table[i-1] + 1
    
    if i%2==0:
        table[i] = min(table[i], table[i//2] + 1)
    if i%3==0:
        table[i] = min(table[i], table[i//3] + 1)
    if i%5==0:
        table[i] = min(table[i], table[i//5] + 1)

print(table[x])
    


# #1차 시도 실패 코드
# #큰 수로 먼저 나눈다해서 무조건 최소 횟수가 되진 않는다...!!!
#cnt =0
# while n != 1:
#     if n % 5 == 0: 
#         n //= 5
#         cnt += 1
#     elif n % 3 == 0: 
#         n //= 3
#         cnt += 1
#     elif n % 2 == 0: 
#         n //= 2
#         cnt += 1
#     else:  
#         n -= 1
#         cnt += 1 

# print(cnt)
