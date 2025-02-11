# ⭐⭐
# 재귀함수 이용

def solution(p):
    if not p:
        return ""

    #균형잡힌 괄호 문자열 분리
    cnt, index = 0, 0
    for i, ch in enumerate(p): #enumerate() : 반복문에서 인덱스와 값을 동시에 가져올 때 사용하는 내장 함수
        cnt += 1 if ch == '(' else -1
        if cnt == 0:
            index = i
            break
    
    u, v = p[:index+1], p[index+1:]

    if u[0] == '(' and u[-1] == ')':
        return u + solution(v)

    return "(" + solution(v) + ")" + "".join(')' if ch == '(' else '(' for ch in u[1:-1])


p="(()())()"
# p=")("
print(solution(p))