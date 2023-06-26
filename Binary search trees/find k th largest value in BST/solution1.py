# not the best ST
# O(n) ST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    array = []
    inOrderTraverse(tree,array)
    print(array)
    if (len(array)>= k):
        return array[len(array)-k]
    return -1

    # O(N) ST
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array