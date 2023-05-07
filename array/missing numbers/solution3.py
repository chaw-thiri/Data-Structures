def missingNumbers(nums):
    solutionXOR = 0
    for i in range(0,len(nums)+3):
        solutionXOR ^= i
        if i < len(nums):
            solutionXOR ^= nums[i]
        
    solution = [0,0]
    setBit = solutionXOR & -solutionXOR
    for i in range(0, len(nums) + 3):
        if i & setBit ==0:
            solution[0] ^= i
        else:
            solution[1] ^= i

        if i < len(nums):
            if nums[i] & setBit == 0:
                solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]
    
    return sorted(solution)