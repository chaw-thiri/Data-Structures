# O(n) ST 
# cons : doesn't use the given insert method

def minHeightBst(array):
    return minHeightHelper(array,None, 0, len(array)-1)
def minHeightHelper(array,curr_node, startIdx, endIdx):
    midIdx = (startIdx+endIdx)//2
    if (startIdx > endIdx): # until all the value in the array has been added
        return  
 
    newNode = BST(array[midIdx]) # =
    if curr_node is None:
        curr_node = newNode
    else: # smaller or larger
        if newNode.value < curr_node.value:
            curr_node.left = newNode
            curr_node = curr_node.left  # insertion : O(n) time complexity 
        else:
            curr_node.right = newNode
            curr_node = curr_node.right
        # cannot use while loop here cus there are two functions to return
    minHeightHelper(array,curr_node, startIdx, midIdx-1)
    minHeightHelper(array,curr_node,midIdx+1,endIdx)



    return curr_node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
