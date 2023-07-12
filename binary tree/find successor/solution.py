# T = O(n)
# S = O(n), n = number of nodes in the tree
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def inOrderTraversal(tree,array=[]):
    if tree is  not None:
        inOrderTraversal(tree.left, array)
        array.append(tree)   # tree.value is appended here, find successor function cannot compare curr_node with node.
        inOrderTraversal(tree.right, array)
    return array
        
    

def findSuccessor(tree, node):
    # Write your code here.
    array = inOrderTraversal(tree)
   
    for idx,curr_node in enumerate(array):
        if curr_node != node:
            continue
        if idx == len(array)-1:
            return None
        
        return array[idx+1]
       

            
  

        
        
