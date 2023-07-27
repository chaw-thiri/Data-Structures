# two pointers method

# time = O(n)
# space = O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slowNode = linkedList
    fastNode = linkedList
    while fastNode != None and fastNode.next != None: #  put fastNode at the front
        #cuz Nonetype erro can arise if fastNode.next is checked first
       slowNode = slowNode.next
       fastNode = fastNode.next.next
    return slowNode