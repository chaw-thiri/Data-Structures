# oridnary method : find the mid point using lenght
# time = O(n)
# space = O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    currentNode = linkedList  # linkedList = head node
    count = 0
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next
        
    middleNode = linkedList
    for _ in range(count // 2):
        middleNode = middleNode.next
        
    return middleNode
