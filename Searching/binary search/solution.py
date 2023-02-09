def shiftedBinarySearch(array, target):
    shiftedBinarySearchHelper(array,target,0,len(array)-1)

def shiftedBinarySearchHelper(array, target, left_pt, right_pt):
    midpoint = (left_pt + right_pt) //2
    if array[midpoint] != target:
        if array[left_pt] < array[midpoint]: 
            if (array[midpoint] > target 
                and array[left_pt] > target):    
                return shiftedBinarySearchHelper(array,target, midpoint+1, right_pt)
            elif (array[midpoint] > target 
                and array[left_pt] < target):
                return shiftedBinarySearchHelper(array,target, left_pt, midpoint-1)
        else:
            return shiftedBinarySearchHelper(array,target, midpoint, right_pt)
            
    else:
        return midpoint
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
print(shiftedBinarySearch(array,target))