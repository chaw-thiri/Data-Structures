# sol from algoexpert
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# time = O(n)
# space = O(h)

def symmetricalTree(tree):
   return treesAreMirrored(tree.left, tree.right)
def treesAreMirrored(left,right):
    if (left is not None
    and right is not None
    and left.value==right.value):
        return (treesAreMirrored(left.left, right.right ) 
                and treesAreMirrored(left.right, right.left))
    return left == right
    
