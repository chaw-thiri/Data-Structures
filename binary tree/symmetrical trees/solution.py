# time = O(n), n = number of nodes
# space = O(h), h = height of the binary tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    if tree is None:
        return True  # An empty tree is considered symmetrical

    return isSymmetrical(tree.left, tree.right)


def isSymmetrical(left, right):
    if left is None and right is None:
        return True  # If both subtrees are empty, they are symmetrical

    if left is None or right is None or left.value != right.value:
        return False  # If only one subtree is empty or the values differ, they are not symmetrical

    return (
        isSymmetrical(left.left, right.right) and
        isSymmetrical(left.right, right.left)
    )  # Recursively check if the mirrored subtrees are symmetrical
