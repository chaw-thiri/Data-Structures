# time = O(k^n), space O(n)
def staircaseTraversal(height,maxSteps):
    return numberofWaysToTop(height,maxSteps)
def numberofWaysToTop(height,maxSteps):
    if height <= 1:
        return 1 
    numberOfWays =0
    for step in range(1, min(maxSteps, height)+1):
        numberOfWays += numberofWaysToTop(height-step,maxSteps)
    return numberOfWays