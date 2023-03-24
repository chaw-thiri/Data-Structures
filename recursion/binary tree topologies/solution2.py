# O(n^2) time 
#O(n) space
def numberOfBinaryTreeTopologies(n, cache={0:1}):
    if n in cache:
        return cache[n]

    numOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n-1-leftTreeSize
        numOfLeftTree = numberOfBinaryTreeTopologies(leftTreeSize, cache)
        numOfRightTree = numberOfBinaryTreeTopologies(rightTreeSize, cache)
        numOfTrees += numOfLeftTree * numOfRightTree
    cache[n]= numOfTrees
    return numOfTrees