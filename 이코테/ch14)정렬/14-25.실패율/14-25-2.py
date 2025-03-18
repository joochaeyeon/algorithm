# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # 실패율을 계산 -> (스테이지 번호, 실패율)
    failure_rates = []
    

    for i in range(1, N+1):
        total_people = len([stage for stage in stages if stage >= i])
        failed_people = len([stage for stage in stages if stage == i])
        
        # 실패율 계산: 실패한 사람 수 / 도달한 사람 수
        if total_people == 0:
            failure_rate = 0  
        else:
            failure_rate = failed_people / total_people
        
        failure_rates.append((i, failure_rate))
    
    # 실패율을 기준으로 내림차순 정렬, 실패율이 동일하면 스테이지 번호 순으로 정렬
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 스테이지 번호만 반환
    answer = [stage[0] for stage in failure_rates]
    
    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4,4,4,4,4]	

stages.sort()
print(solution(N, stages))