
my_array= [3,7,5,6,3]
# important concepts
# two kinds of swaps, rt and lt--> when crossover  , rt and pivot --> end
# start, end, left, right ******
# sort the shorter side first will shorten space complexity
# time complexity = O(nlog n ) or O(n*2)
# space complexity = O (log n)

def quickSort(array):
    quickSorthelper(array, 0, len(array)-1)
    return array
def quickSorthelper(array, start, end):
    left = start + 1
    right = end
    pivot = start
    if start >= end: # = when len(array) == 1
        return array
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    array[right],array[pivot] = array[pivot],array[right]
    Short_left_side = (right-1)-start > end-(right+1)
    if Short_left_side:
        quickSorthelper(array, right+1, end)
        quickSorthelper(array, start, right-1)
    else:
        quickSorthelper(array, start, right-1)
        quickSorthelper(array, right+1, end)

print(quickSort(my_array))