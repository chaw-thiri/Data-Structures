""" binary tree topolgy = unique binary combination of 
n node without caring about the node value """
# solution 1 
# time = O((n*(2n)!)/(n!(n+1)!))
# space = O(n)
def numberOfBinaryTreeTopologies(n):
    if n == 0 :
        return 1

    numOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n-1-leftTreeSize
        numOfLeftTree = numberOfBinaryTreeTopologies(leftTreeSize)
        numOfRightTree = numberOfBinaryTreeTopologies(rightTreeSize)
        numOfTrees += numOfLeftTree * numOfRightTree
    return numOfTrees