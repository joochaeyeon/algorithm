def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1): #길이가 같은지 보려는 거니까 최대는 문자열/2이다.
        compressed = "" #압축 결과 str
        prev = s[0:step] #step의 크기를 늘려가며 정함
        cnt = 1
        for j in range(step, len(s), step):
            if prev == s[j : j+step]:
                cnt+=1
            else:
                #cnt가 2 이상이면 "개수+문자" 형태로 추가하고, 그렇지 않으면 그냥 문자만 추가
                compressed+= str(cnt) + prev if cnt>=2 else prev
                #prev를 새로운 문자로 업데이트하고, cnt를 다시 1로 초기화
                prev = s[j:j+step]
                cnt = 1
        #반복문이 끝났을 때, 마지막까지 세었던 문자열을 compressed에 추가
        compressed+= str(cnt) + prev if cnt>=2 else prev
        answer = min(answer, len(compressed))
    return answer





# 테스트케이스
# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s="abcabcdede"
# s ="abcabcabcabcdededededede"
s = "xababcdcdababcdcd"

print(solution(s))


#아이디어 1 -> 트리 이용 
#아이디어에 오류가 존재했다. 왼쪽 자식이 ac, 오른쪽 자식이 cc일 경우 ac2c이렇게 되기에
#해결방법
#step을 이용해서 압축해 나가는 방법을 사용