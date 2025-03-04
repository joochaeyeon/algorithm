# 어려운 문제
# 우선순위 큐 알고리즘을 생각해서 풀어야 한다.
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1 

    #시간이 작은 음식부터 빼야하기에 우선순위 큐 사용!
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) #(음식 시간, 음식 번호)형태로 큐에 삽입
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length-=1
        previous = now
    result  = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value) % length][1] 


# #시간초과 발생 코드
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1  

#     idx = 0 
#     for _ in range(k):  
#         while food_times[idx] == 0:  
#             idx = (idx + 1) % len(food_times)  
        
#         food_times[idx] -= 1  
#         idx = (idx + 1) % len(food_times)  

#     while food_times[idx] == 0:  
#         idx = (idx + 1) % len(food_times)  

#     return idx + 1  


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
