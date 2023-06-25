# time = O(n)
# space = O(n) / O(d) = depth of BST
def inOrderTraverse(tree, array):
    # left, current, right
    if tree is not None:
        inOrderTraverse(tree.left, array)
        # all the elements on the left side has been added
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    # current, left, right
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.right, array)
        preOrderTraverse(tree.left, array)
    return array


def postOrderTraverse(tree, array):
    # left, right, current
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
