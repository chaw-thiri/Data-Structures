# recursive sol
# T = O(n)
# S = O(d) , d = depth of the tree
def invertBinaryTree(tree):
    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    

def swap(tree):
    tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
