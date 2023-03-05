# time = O (n*2)\ space = O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    triplet = []
    for i in range(len(array)-2): # want to stop when no more 3 numbers are left
        left = i+1 # right side of i
        right= len(array)-1 # end of the array
        while left < right: 
            currentSum = array[i]+ array[left]+ array[right]
            if currentSum == targetSum:
                triplet.append([array[i],array[left], array[right]])
                left += 1
                right -= 1 # move both pointers at the same time
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplet