# ⭐⭐⭐⭐⭐⭐
# 어려운 문제
# 완전 탐색 이용❗= 모든 경우의 수를 확인
# 순열 이용❗

from itertools import permutations

def solution(n, weak, dist):
    #원형을 일자 형태로 변경
    length = len(weak)

    for i in range(length):
        weak.append(weak[i]+n)
        
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist,len(dist))):
            cnt = 1
            position = weak[start] + friends[cnt-1]
            for index in range(start, start+length):
                if position < weak[index]:
                    cnt+=1
                    if cnt > len(dist):
                        break
                    position = weak[index] + friends[cnt-1]
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer

# n = 12
# weak = [1,5,6,10]
# dist = [1,2,3,4]
n = 12
weak = [1,3,4,9,10]
dist = [3,5,7]

print(solution(n, weak, dist))