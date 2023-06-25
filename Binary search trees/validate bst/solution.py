
# time = O(n)
# space = O (d ) d = depth of the tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float("-inf"),float("inf"))
# for left nodes: parent(curr node) is the max value possible
# for right nodes : parent(curr node) is the min value possible
def validateBstHelper(tree, minValue, maxValue):
    if tree is None: # left node
        return True
    if tree.value < minValue or tree.value >= maxValue:# *** right side can be greater or equal but left must be strictly less
        return False
    leftIsValid = validateBstHelper(tree.left,minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
