def find_start(arr,target):
    if arr[0] == target:
        return 0
    left ,right = 0,len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid+1

        else:
            left = mid -1
    return -1

def first_and_last(arr,target):
    if len(arr) == 0:
        return [-1,-1]
    start = find_start(arr,target)
    if start == -1:
        return [-1,-1]
    end = start
    while end + 1 < len(arr) and arr[end + 1] == target:
        end +=1
    return [start,end]

def find_end(arr,target):
    if arr[-1] == target:
        return len(arr) -1
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid +1
    return -1



