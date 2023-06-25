# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # avg O(log n) T , O(1) S
    # worst  O(n) T, O(1) S
    def insert(self, value):
        curr_node = self
        while True:
            if value< curr_node.value:
                if curr_node.left is None: 
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left # go left 
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else: 
                    curr_node = curr_node.right # go right
        return self

    #  O(log n ) time , O(1) space
    # O(n) time , O(1) space
    def contains(self, value):
        curr_node = self 
        while curr_node is not None:
            if value < curr_node.value:
                parentNode = curr_node
                curr_node = curr_node.left 
            elif value > curr_node.value:
                parentNode = curr_node
                curr_node = curr_node.right
            else: return True
        return False
        
                


    def remove(self, value, parentNode = None):
        currentN = self
        while currentN is not None: # None when deleted 
            # left or right , find the node
            if value < currentN.value:
                parentNode = currentN
                currentN = currentN.left 
            elif value > currentN.value:
                parentNode = currentN
                currentN = currentN.right

            # found the node
            else:
                # case 1 : two children
                if currentN.left is not None and currentN.right is not None: 
                    currentN.value = currentN.right.getMinValue() # smallest of the right tree
                    currentN.right.remove(currentN.value, currentN) # currentN.value is the copied vlaue, so delete the duplicates
                # currentN is  the parent of the copied value 

                # case 2 : node to be deleted is the root node with one child case || single node tree
                # 2 children will be handle by case 1 
                elif parentNode is None: 
                    if currentN.left is not None:
                        currentN.value = currentN.left.value
                        currentN.right = currentN.left.right
                        currentN.left = currentN.left.left
                     
                    elif currentN.right is not None:
                        currentN.value = currentN.right.value
                        currentN.left = currentN.right.left
                        currentN.right = currentN.right.right
                        
                    else: # no parent node, no child node, so the tree has only one level, 
                        # in question , it is told to do nth in case of a single level tree so pass
                        pass
                # case 3 :  child  1 case or no child  
                elif parentNode.left  == currentN:
                    if currentN.left is not None: 
                        parentNode.left =currentN.left
                    else: 
                        parentNode.left = currentN.right
                elif parentNode.right == currentN:
                    if currentN.left is not None:
                        parentNode.right = currentN.left 
                    else:
                        parentNode.right = currentN.right
                break
        return self

    def getMinValue(self): # smallest of the right tree= leftest of the right tree
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left 
        return curr_node.value
