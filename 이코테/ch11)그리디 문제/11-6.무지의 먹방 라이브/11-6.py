import heapq #우선순위 큐 사용 -> 최소힙 제공 라이브러리로 음식 시간이 적은 순서대로 정렬 가능!

def solution(food_times, k):
    #더 섭취할 음식이 없다면 -1 반환
    if sum(food_times) <= k:
        return -1

    #우선순위 큐 사용
    q=[]
    for i in range(len(food_times)):
        #(음식 시간, 음식 번호) 형태로 큐에 삽입
        #우선순위 큐이기에 음식 시간이 작은 것부터 자동 정렬됨
        heapq.heappush(q, (food_times[i], i+1))
    
    total_eaten  = 0 #총 먹는 시간
    previous = 0 #직전 음식 시간
    remaining = len(food_times) #남은 음식 갯수 -> 0은 카운트 안함

    #while -> 가장 적은 음식부터 하나씩 제거
    while total_eaten + ((q[0][0] - previous) * remaining) <= k:
        now = heapq.heappop(q)[0] #가장 적은 음식 시간 제거
        total_eaten += (now - previous) * remaining #먹은 시간 누적
        remaining -= 1 
        previous = now 

    #남은 음식 중에 몇 번째 음식인지 확인
    answer = sorted(q, key=lambda x : x[1]) #음식의 번호 기준으로 정렬
    return answer[(k - total_eaten ) % remaining][1]


print(solution([3,1,2], 5))


# 오류 1
# 1. 음식이 모두 소진될 경우 고려 못함
# 2. 이중 for문인데 이것 자체에 오류가 존재 한다. 이중 for문 사용하면 안된다. 
# 3. 시간 초과 발생
# def solution(food_times, k):
#     answer = 0 # 이 값을 업데이트하자
#     for i in range(k): #1,2,3,4,5 -> 5일때 answer값을 return
#         for j in range(len(food_times)):
#             if food_times[j] != 0 :
#                 food_times[j]-=1
#                 answer = j+1 #해당 배열값으로 업데이트  
#     return answer


# 오류 2 
# 코드상 오류는 없음
# 시간초과가 발생하는 문제 발생
# 해결방법 -> 우선순위 큐 사용..! & 문제를 작게 만들 생각을 하자!
# def solution(food_times, k):
#     #더 섭취할 음식이 없다면 -1 반환
#     if sum(food_times) <= k:
#         return -1

#     answer = 0 #현재 위치
#     n = len(food_times)
    
#     for _ in range(k):
#         while food_times[answer] == 0:
#             answer = (answer + 1) % n
#         food_times[answer] -=1
#         answer = (answer+1)%n
    
#     while food_times[answer] == 0:
#         answer = (answer+1) % n

#     return answer + 1 