# ⭐
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data= list(map(int,input().split()))

def cnt(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

result = cnt(data, x, x)

if result == 0:
    print(-1)
else:
    print(result)