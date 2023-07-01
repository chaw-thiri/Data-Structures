
# recursive sol:
class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space 
# n = no of nodes in the tree
# h = height of the tree
def repairBst(tree):
    nodeOne = nodeTwo = prevNode = None

    # nested fun
    def inOrderTraversal(node):
        nonlocal nodeOne, nodeTwo, prevNode    # local<nonLocal < global
        if node is None: # base case
            return
        
        inOrderTraversal(node.left)

        if prevNode is not None and prevNode.value > node.value: # wrong location
            if nodeOne is None:
                nodeOne = prevNode
            nodeTwo = node
        prevNode = node
        inOrderTraversal(node.right)

    inOrderTraversal(tree)

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree