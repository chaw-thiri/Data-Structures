# T= O(n) ,
# S = O(n) max
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    arraySum = []
    brunchSumHelper(root,0, arraySum)
    return arraySum

def brunchSumHelper(currNode,currSum, arraySum):
    if currNode is None:
        return 
    newSum = currSum + currNode.value
    if currNode.left is None and currNode.right is None:
        arraySum.append(newSum)
        return 
    brunchSumHelper(currNode.left, newSum, arraySum)
    brunchSumHelper(currNode.right, newSum, arraySum)
        
    
