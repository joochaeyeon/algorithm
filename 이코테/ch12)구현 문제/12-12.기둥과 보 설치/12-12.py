# ⭐⭐
# 어려운 문제
# 전형적인 시뮬레이션 문제❗
# 시간복잡도가 충분하기에 일일히 확인하면서 설치 or 삭제를 진행할 수 있었다.
# ➡ 시간복잡도 or 공간복잡도 확인하고 코드 짜도록❗

def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0:
            if y == 0  or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1, 0] in answer:
                continue
            return False #삭제를 무시
        elif stuff == 1:
            if [x,y-1, 0] in answer or [x+1,y-1, 0] in answer or ([x-1,y, 1] in answer and [x+1,y, 1] in answer):  
                continue
            return False #설치를 무시
    return True 

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, op = frame
        if op == 0: #삭제 연산
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff]) #가능하지 않다면 삭제하지 않고 넘어간다.
        if op == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)


# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))