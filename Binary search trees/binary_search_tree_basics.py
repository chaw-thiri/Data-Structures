class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

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
            else: 
                return self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
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
