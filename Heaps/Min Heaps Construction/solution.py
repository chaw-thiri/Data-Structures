# don't touch the values , just play with indice
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    
    # O(n) time, O(1) space
    def buildHeap(self, array):
        LastParentIdx = (len(array)-2)//2
        for currentIdx in reversed(range(LastParentIdx + 1)): # go from bottom to top
            self.siftDown(currentIdx, len(array)-1, array)
        return array
        
    # O(log(n)) time, O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            
            # check conditions to swap
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[currentIdx] > heap[idxToSwap]: # idxToSwap is the smaller one of the child node
                self.swap(currentIdx,idxToSwap,heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return 

    # O(log n) time, O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2 
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]: # < cux min heap, > in max heap
            # while not at the top of the heap
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx-1) // 2



    # O(1), O(1)
    def peek(self):
        # check the node value
        return self.heap[0]
        
    # O(log n) time, O(1) space
    def remove(self): 
        # swap it with the last index
        # pop off the last index\
        self.swap(0,len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop() # pop removes the last index
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valueToRemove
        
    
    # O(log n) time , O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap) # don
       
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j],heap[i]

   

