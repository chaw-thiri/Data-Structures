# time O(n)
# space O(k)
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    count = 0
    array = []
    reverseOrderTraverse(tree, array, k, count)
    print("final array >>>")
    print(array)
    if len(array) >= k:
        return array[k-1]
    return -1

def reverseOrderTraverse(tree, array, k, count):
    if len(array) <=k:
        if tree is not None:
            print("addition by right")
            reverseOrderTraverse(tree.right, array, k, count)
            print(array)
            print("appending")
            array.append(tree.value)
            print(array)
            print("left")
            reverseOrderTraverse(tree.left, array, k, count)
            print(array)
    else:
        return


