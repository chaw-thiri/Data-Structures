# O(n) time
# O(n) space
# naive solution

def missingNumbers(nums):
    includedNums = set(nums)

    solution = []
    for num in range(1,len(nums)+3):
        if not num in includedNums:
            solution.append(num)

    return solution