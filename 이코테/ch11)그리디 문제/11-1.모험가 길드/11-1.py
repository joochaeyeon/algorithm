n = int(input()) 
n_list = list(map(int,input().split()))
n_list.sort()


#마지막에 남은거는 합치기 전략 사용 -> 이미 묶여진 그룹에 합친다는 의미
total = 0 #총 팀 개수
cnt = 0 #현재 구하는 팀의 구성원 수

for i in n_list:
    cnt += 1 # 현재 기준이 되는 팀원 cnt에 포함시킴
    if cnt >= i:
        total +=1
        cnt = 0
print(total)