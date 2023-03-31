# time O(n), loop through the array only once.
# space = O(1) : constant space 
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i,num,array):
            minOutOfOrder = min(minOutOfOrder,num) # the first num i see 
            maxOutOfOrder = max(maxOutOfOrder,num)
    
    if minOutOfOrder == float("inf"):
        return [-1,-1]
    
    # find the idx from the min and max values
    subarrayLeftIdx = 0
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
        
    subarrayRightIdx = len(array)-1
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1

    return[subarrayLeftIdx,subarrayRightIdx]

def isOutOfOrder(i, num, array):
    # if the index is 0, check only right side, if index is -1, check only left 
    # else check both sides.
    if i == 0:
        return num> array[i+1]
    if i == len(array)-1:
        return num< array[i-1]
    return num > array[i+1] or num < array[i-1]
    
