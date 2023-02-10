# modification of quicksort 
# 1. position
# 2. looping 
# 3. time complexity = O (n) or O (n*2)
# 4. space complexity = O(1)
def quickselect(array, k):
    position = k -1
    return quickselectHelper(array, position, 0, len(array)-1)
    

def quickselectHelper(array, position, start, end):
    while True:
        if start > end:
            raise Exception('Your algorithm has error at some point.')
        pivot = start
        left = start + 1 
        right = end
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left,right,array)
            if array[left] <= array[pivot]:
                left += 1 
            if array[right] >= array[pivot]:
                right -= 1
        swap(pivot, right, array)
        if position == right:
            return array[right]
        elif position > right:
            start = right + 1 
        else:
            end = right - 1

def swap(i,j,array):
    array[i], array[j]= array[j],array[i]

print(quickselect([2,5,7,8,4,3,6,56],2))