n =int(input())
data = list(map(int, input().split()))
data.sort()

def binary_search(arr, start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid: #왼쪽 탐색
        return binary_search(arr, start, mid -1)
    else:
        return binary_search(arr,mid+1,end) #오른쪽 탐색

result = binary_search(data, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)