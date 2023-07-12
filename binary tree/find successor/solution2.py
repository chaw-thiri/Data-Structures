# time = O(h), h = height of the tree
# space O(1)
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree,node):
    if node.right is not None:
        return getLeftmostChild(node.right)
    return getRightmostParent(node)
    
def getLeftmostChild(node):
    currNode = node
    while currNode.left is not None:
        currNode = currNode.left
        
    return currNode

def getRightmostParent(node):
    currNode = node
    while currNode.parent is not None and currNode.parent.right == currNode:
        currNode = currNode.parent
    return currNode.parent