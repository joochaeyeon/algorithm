# ⭐
# 파이썬에는 이진 탐색 라이브러리인 bisect 모듈이 존재 
# bisect_left(a, x)	x가 들어갈 왼쪽 인덱스 찾기
# bisect_right(a, x) x가 들어갈 오른쪽 인덱스 찾기
# insort_left(a, x)	x를 정렬된 위치에 왼쪽 기준 삽입
# insort_right(a, x) x를 정렬된 위치에 오른쪽 기준 삽입

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int,input().split()))

#left_value와 right_value인 데이터의 개수 반환 함수
def cnt_value (array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

result = cnt_value(data, x, x)

if result == 0:
    print(-1)
else:
    print(result)