# time = avg O(log n) , worst O(n)
# space = avg O(log n) , worst O(n)
def findClosestValueInBst(tree, target):
        return findHelper(target, tree, float('inf'))
    

def findHelper(target, tree, closest):
    if tree == None:
        return closest # end the recursion
    else:
        if abs(closest -target) > abs(tree.value - target):
            closest = tree.value 
        if target > tree.value:
            return findHelper(target, tree.right, closest)
        elif target < tree.value:
            return findHelper(target, tree.left, closest)
        elif target == tree.value:
            return closest 

    
        


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value    # node value
        self.left = None #left child
        self.right = None #right child



