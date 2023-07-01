class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left 

# time = O(n) , space = O(h)
# iterative solution
def repairBst(tree):
    nodeOne = nodeTwo = prevNode = None

    stack = []
    currNode = tree
    while currNode is not None or len(stack) > 0:
        while currNode is not None:
            stack.append(currNode)
            currNode = currNode.left
        currNode = stack.pop()

        if prevNode is not None and prevNode.value > currNode.value:
            if nodeOne is None:
                nodeOne = prevNode
            nodeTwo = currNode
        
        prevNode = currNode
        currNode = currNode.right

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree