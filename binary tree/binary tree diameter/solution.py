# T = O(n) , n - no of nodes
# S = O(h) , h = height of the tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# 
class TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height

def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:# base case
        return TreeInfo(0,0)

    leftTreeInfo= getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)
    # ???
    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameter = max(leftTreeInfo.diameter , rightTreeInfo.diameter)
    currDiameter = max(longestPathThroughRoot, maxDiameter)
    currHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currDiameter, currHeight)

