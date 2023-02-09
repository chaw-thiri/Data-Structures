def shiftedBinarySearch(array, target):
    left = 0
    right = len(array)-1
    
    while left <= right:
        mid = (left + right)// 2
        if target == array[mid]:
            return mid
        elif array[mid] > array[left]: # sorted side
            if target > array[mid] or target < array[left]:
                left = mid + 1 
            else:
                right = mid -1 
        else: # not sorted side
            if target < array[mid] or target > array[right]:
                right = mid -1
            else: 
                left = mid + 1

    return -1






array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
print(shiftedBinarySearch(array,target))