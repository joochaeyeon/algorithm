#https://school.programmers.co.kr/learn/courses/30/lessons/60058

#균형 잡힌 괄호 문자열의 인덱스를 반환!
def balance_index(p):
    cnt = 0 #왼쪽 괄호 갯수

    for i in range(len(p)):
        if p[i] == "(": #인덱스를 반환하는 것이기에 p[i]를 활용
            cnt+=1
        else:
            cnt-=1
        if cnt == 0:
            return i
        
        
# 올바른 괄호 문자열인지 판단
def check(p): 
    cnt = 0 #왼쪽 괄호 갯수
    for i in p:
        if i == "(":
            cnt+=1
        else:
            if cnt == 0: #쌍이 맞지 않은 경우
                return False
            cnt-=1
    return True


def solution(p):
    answer = ""
    if p == "":
        return answer #빈문자열일 경우 빈문자열 반환
    
    index = balance_index(p)
    u = p[:index+1] #왼쪽
    v = p[index+1:] #오른쪽
    
    if check(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1]) # 첫번째와 마지막번째 문자를 제거!!!
        for i in range(len(u)):
            if u[i] == "(": #-> 새로운 문자열 만들기!
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)

    return answer


# p="(()())()"
p=")("
print(solution(p))