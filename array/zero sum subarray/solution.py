def zeroSumSubarray(nums):
    sums = set([0])
    # checking the sum linearly will cost excessive time, in that case set is use. 
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        # sums += currentSum       cannot use + for set stupid
        # sums.append(currentSum)   set does not have append
        sums.add(currentSum)
    return False
