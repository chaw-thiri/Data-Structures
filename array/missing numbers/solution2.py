# O(n) time
# O(1) space 

def missingNumbers(nums):
    total = sum(range(1,len(nums)+3))

    for num in nums: # get the sum of missing numbers
        total -= num 
    averageMissingValue = total //2

    foundFirstHalf, foundSecondHalf = 0,0
    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageMissingValue + 1))
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums)+3))

    return [expectedFirstHalf- foundFirstHalf, expectedSecondHalf- foundSecondHalf]