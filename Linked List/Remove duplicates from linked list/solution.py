# time = O(n) : traverse all the node
# space = O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList): # linked list = head node
    currentNode = linkedList
    while (currentNode != None):
        nextDiffNode = currentNode.next
        while (nextDiffNode != None  and currentNode.value == nextDiffNode.value): # skip all the duplicate values
            nextDiffNode = nextDiffNode.next
        currentNode.next = nextDiffNode
        
        # move the pointer
        currentNode = nextDiffNode
    return linkedList # return the object
