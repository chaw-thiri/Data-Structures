class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class binary_search_tree: 
    def __init__(self):
        self.root = None 

    def insert(self, value):
        if self.root == None: 
            self.root = node(value)
        else: 
            self._insert(value,self.root)
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else: 
                return self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                return self._insert(value,cur_node.right_child)
        else : 
            print ("Value already in the tree! ")
    

    def print(self):
        if self.root != None:
            self._print_tree(self.root)
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None: 
            self._height(self.root, 0)
        else: 
            return 0
    def _height(self, cur_node, curr_height):
        if cur_node == None:
            return curr_height
        left_height = self._height(cur_node.left_child, curr_height+1)
        right_height = self._height(cur_node.right_child, curr_height+1)
        return max(left_height,right_height)
    

    def search(self,value):
        if self.root!= None:
            return self._search(value, self.root)
        else: return False #BST is empty
    def _search(self, value, cur_node):
        if value == cur_node.value: return True
        elif value < cur_node.value and cur_node.left_child!= None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child!= None:
            return self._search(value, cur_node.right_child)
        else: #no value in the whole BST
            return False
        
    def find(self,value):
        if self.root!= None:
            return self._find(value, self.root)
        else: return None #BST is empty
    def _find(self, value, cur_node):
        if value == cur_node.value: return cur_node
        elif value < cur_node.value and cur_node.left_child!= None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child!= None:
            return self._find(value, cur_node.right_child)
        else: #no value in the whole BST
            return None
        

    def delete_value(self, value):
        return self.delete_node(self.find(value))
    def delete_node(self,node):
        
        def no_of_child(self,   curr_node):
            n = 0
            if curr_node.left_child != None:
                n += 1
            elif curr_node.right_child != None:
                n += 1
            return n 
        
        
        def min_node_value(self,cur_node):
            current = cur_node
            while current.left_child != None:
                current = current.left_child
            return current 


        node_child = no_of_child(node)
        node_parent = node.parent
        # case 1 : no child
        if node_child == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None
            
        # case 2 : one child
        elif node_child == 1:
            #find if the child is left or right 
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child
            
            #replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            child.parent = node_parent

        # case 3 : two children
        elif node_child == 2:
            successor = min_node_value(node.right_child) # to get the leftest child of the right child
            node.value = successor.node # node to be deleted is replaced with successor
            self.delete_node(successor) # successor is deleted to avoid duplication 

        




tree = binary_search_tree()
tree.insert(0)
tree.insert(1)
tree.insert(4)
tree.insert(9)
tree.insert(5)
tree.insert(89)
tree.insert(23)
tree.insert(5)
tree.print()
print(tree.search(24))


print("Deleting nodes ....")
tree.delete_value(1)
print("finding 5")
print("\n")
tree.print()
