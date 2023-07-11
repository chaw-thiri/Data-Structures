# iterative solution
# t = O(n)
# s = O(n) , in perfect binary tree will come nearly to n 

def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None: # skip the null nodes
            # swap if there is a check of a single child
            # ask interviewer for that 
            continue
        swap(current)
        queue.append(current.left)
        queue.append(current.right)
def swap(tree):
    tree.left, tree.right = tree.right,tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
