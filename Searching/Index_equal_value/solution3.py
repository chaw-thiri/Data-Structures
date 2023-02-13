def indexEqualsValue(array):
    l = 0
    r = len(array) - 1
    while l<=r:
        mid = (l + r) //2
        if array[mid] == mid and ((mid == 0) or array[mid-1]<mid-1):
            return mid
        elif array[mid] < mid:
            l = mid + 1
        else:
            r = mid - 1
    return -1


array = [-5, -3, 0, 3, 4, 5, 9]
print(indexEqualsValue(array))