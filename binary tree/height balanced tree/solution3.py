# not complete yet
# 12/ 14 test case 
# test 2 and test 10 fail
# This is an input class. Do not edit.
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
    if tree.left is not None and tree.right is not None:
        return heightBalancedBinaryTreeHelper(tree.left)
        return heightBalancedBinaryTreeHelper(tree.right)
    # tree.left has one extra node now
    # if there is just one more extra node, the tree would not balanced
    elif tree.left is not None and tree.right is None:
        return (tree.left.left is None and tree.left.right is None)
    elif tree.right is not None and tree.left is None:
        return (tree.right.left is None and tree.right.right is None)
    return True

