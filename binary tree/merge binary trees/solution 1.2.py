# space = O(h), where h = height of the shorter
# time = O(n), n = no of nodes in the shorter tree
# short tree cuz the recursion will stop once one of the tree hits the none value
# and the rest will just return the longer tree 
# to eliminate unnecessary recursions
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    if tree1 is None: return tree2
    if tree2 is None: return tree1
    tree3 = BinaryTree(0)
    tree3.value = tree1.value + tree2.value
    tree3.left = mergeBinaryTrees(tree1.left,tree2.left)
    tree3.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree3
        

    
    
