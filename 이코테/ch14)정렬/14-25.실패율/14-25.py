# ⭐

def solution(N, stages):
    stage_users = [0] * (N + 2) #스테이지가 1부터 N+1까지 가능

    for s in stages: #해당 스테이지 배열에 +1 시켜줌 -> 그러면 스테이지별 몇명이 실패했는지를 알 수 있다.
        stage_users[s] += 1
    
    total_players = len(stages)
    fail = []

    for i in range(1, N + 1):
        if total_players == 0:  #도달한 사람이 없으면 실패율 0
            fail.append((0, i))
        else:
            fail.append((stage_users[i] / total_players, i))
            total_players -= stage_users[i]  #다음 스테이지로 넘어감

    fail.sort(key=lambda x: (-x[0], x[1]))
    result = [stage for _, stage in fail]

    return result


N = 5
stages = [2,1,2,6,2,4,3,3]
N = 4
stages = [4,4,4,4,4]

print(solution(N, stages))