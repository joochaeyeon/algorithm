# ⭐⭐⭐
import sys

n, c = map(int, sys.stdin.readline().split())  
house = sorted(int(sys.stdin.readline()) for _ in range(n))  

low, high = 1, house[-1] - house[0]  
result = 0  

while low <= high:
    mid = (low + high) // 2  
    cnt = 1 
    prev = house[0]  #마지막으로 공유기가 설치된 집


    for i in range(1, n):
        if house[i] - prev >= mid:
            cnt += 1
            prev = house[i]
    
    if cnt >= c:
        result = mid  
        low = mid + 1  
    else:
        high = mid - 1 

print(result)  
