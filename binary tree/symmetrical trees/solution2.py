# sol from algoexpert
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# The function checks if the given binary tree is symmetrical
def symmetricalTree(tree):
    return treesAreMirrored(tree.left, tree.right)

# The helper function checks if two subtrees are mirrored
def treesAreMirrored(left, right):
    # Base cases:
    # If both subtrees are not None and have equal values
    if left is not None and right is not None and left.value == right.value:
        # Recursively check if the mirrored subtrees are symmetrical
        return (
            treesAreMirrored(left.left, right.right) and
            treesAreMirrored(left.right, right.left)
        )
    # If at least one subtree is None or the values differ, they are not symmetrical
    return left == right

    
