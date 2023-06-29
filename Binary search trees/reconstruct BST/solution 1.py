# T = O(n^2) 
#   looping through the array n, calling it n time, so n * n ---> n square
# S = O(h) , h = height of the BST: no of call stack on recursion
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues)==0:
        return None
    # root node will always be index 0
    currentValue=preOrderTraversalValues[0]
    rightSubtreeRootIdx=len(preOrderTraversalValues)


    # to get right tree index
    for idx in range(1,len(preOrderTraversalValues)):
        value=preOrderTraversalValues[idx]
        if value>=currentValue:
            rightSubtreeRootIdx=idx
            break

    leftSubtree=reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
    rightSubtree=reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
    return BST(currentValue,leftSubtree,rightSubtree) # leftSubtree is a left child and right subtree is a right child