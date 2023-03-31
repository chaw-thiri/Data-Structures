# time = O(n)
# space = O(n)
def largestRange(array):
    bestRange = []
    longestLenght = 0
    nums = {}
    # set all the num to True
    for num in array:
        nums[num] = True
    
    
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num-1
        right = num+1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLenght:
            longestLenght = currentLength
            bestRange =[left+1, right-1]
    return bestRange