def indexEqualsValue(array):
    return indexEqualsValueHelper(array, 0, len(array)-1)
def indexEqualsValueHelper(array, l, r):
    if l > r:
        return -1
    mid = (l + r) //2
    if array[mid] == mid and ((mid == 0) or array[mid-1]<mid-1):
        return mid
    elif array[mid] < mid:
        return indexEqualsValueHelper(array, mid+1, r)
    else:
        return indexEqualsValueHelper(array, l, mid-1)

array = [-5, -3, 0, 3, 4, 5, 9]
print(indexEqualsValue(array))