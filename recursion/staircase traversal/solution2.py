# time = O(k*n), space O(n)
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})
def numberOfWaysToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]
    numberOfWays = 0
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps, memoize)
    memoize[height] = numberOfWays
    return numberOfWays