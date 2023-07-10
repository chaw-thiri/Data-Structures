# time = O(n)
# space = O(d) , call stack = depth of the tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# -1 L + R
# -2 L - R
# -3 L // R
# -4 L * R

def evaluateExpressionTree(tree):
    # base case => reach the leaves, no operation can be done
    if (tree.value >= 0):
        return tree.value
    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)
    if tree.value == -1:
        return leftValue + rightValue
    elif tree.value == -2:
        return leftValue - rightValue
    elif tree.value == -3:
        return int(leftValue / rightValue) ## round to zero
    else:
        return leftValue* rightValue
    
