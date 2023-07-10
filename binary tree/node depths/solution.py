# recursive solution
# T = O(n) , n = total num of nodes
# S = O(d) , d = depth of the tree
# the max num of call stack wil be d 
def nodeDepths(root):
    
    return nodeDepthsFinder(root,0)
    

def nodeDepthsFinder(currNode, depth):
    if currNode is None:
        return 0
    return depth+nodeDepthsFinder(currNode.left, depth+1)+nodeDepthsFinder(currNode.right, depth+1)
    # why ??? 
    # with depth, the ans will always be ZERO
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
