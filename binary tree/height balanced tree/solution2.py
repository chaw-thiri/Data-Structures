# sol from algoexpert 
# Time = O(n)
# Space = O(h)
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeClass:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced
    
def getTreeInfo(node):
    if node is None:
        return TreeClass(True,-1)
    
    leftSubtreeInfo = getTreeInfo(node.left)
    rightTreeInfo = getTreeInfo(node.right)
    
    isBalanced = (
        leftSubtreeInfo.isBalanced and 
        rightTreeInfo.isBalanced and 
        abs(leftSubtreeInfo.height-rightTreeInfo.height) <= 1
    )
    height = max(leftSubtreeInfo.height,rightTreeInfo.height) + 1
    return TreeClass(isBalanced,height)