n,m,k =  map(int, input().split())
data = list(map(int, input().split())) #N개의 자연수 입력
final =0

#1. data를 가장 큰 수 기준으로 정렬
#POINT) 가장 큰수와 두번째 큰 수만을 사용한다!
data.sort(reverse=True)
first = data[0]
second = data[1]

while True:
    for i in range(k): #중복 k와 관련한 것 / k번 반복하고 if로 내려감 -> second를 더함
        if m == 0:
            break
        final += first
        m-=1
    if m == 0:
        break
    final+=second
    m-=1



print(final)