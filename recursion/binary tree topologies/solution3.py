# O(n^2) time 
#O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n+1):
        numOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m-1-leftTreeSize
            numOfLeftTree = cache[leftTreeSize]
            numOfRightTree = cache[rightTreeSize]
            numOfTrees += numOfLeftTree * numOfRightTree
        cache.append(numOfTrees)
    return cache[n]