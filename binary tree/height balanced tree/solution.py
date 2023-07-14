# time = O(n)
# space = O(h) , n = number of nodes in the tree, h = height of the tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def heightBalancedBinaryTree(tree):
    if tree is None:
        return True
    return heightBalancedBinaryTreeHelper(tree)

def heightBalancedBinaryTreeHelper(tree):
    if tree is None:
        return True

    leftHeight = getHeight(tree.left)
    rightHeight = getHeight(tree.right)

    if (
        abs(leftHeight - rightHeight) > 1 or
        not heightBalancedBinaryTreeHelper(tree.left) or
        not heightBalancedBinaryTreeHelper(tree.right)
    ):
        return False

    return True

def getHeight(tree):
    if tree is None:
        return 0
    return max(getHeight(tree.left), getHeight(tree.right)) + 1
