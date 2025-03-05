# ⭐⭐
# 어려운 문제!!

def can_build(answer):
    for x, y, structure in answer:
        if structure == 0:  # 기둥
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, structure, operation in build_frame:
        if operation == 1:  #설치
            answer.append([x, y, structure])
            if not can_build(answer):
                answer.remove([x, y, structure])
        else:  #삭제
            answer.remove([x, y, structure])
            if not can_build(answer):
                answer.append([x, y, structure])
    return sorted(answer)



# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))