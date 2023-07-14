# using stack
# space = O(h), where h = height of the shorter
# time = O(n), n = no of nodes in the shorter tree
class BinaryTree:
    def __init__(self,value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right
        
def mergeBinaryTrees(tree1,tree2):
    if tree1 is None:
        return tree2
    tree1Stack =[tree1]
    tree2Stack = [tree2]
    # stack = Last In First Out
    while len(tree1Stack) > 0:
        tree1Node = tree1Stack.pop()
        tree2Node = tree2Stack.pop()
        
        if tree2Node is None: continue
        
        tree1Node.value += tree2Node.value
        if tree1Node.left is None:
            tree1Node.left = tree2Node.left
        else:
            tree1Stack.append(tree1Node.left)
            tree2Stack.append(tree2Node.left)
            
        if tree1Node.right is None:
            tree1Node.right = tree2Node.right
        else:
            tree1Stack.append(tree1Node.right)
            tree2Stack.append(tree2Node.right)
    return tree1