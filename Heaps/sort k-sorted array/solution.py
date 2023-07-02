# time = O(n log(k))
# space = O(k)

def sortKSortedArray(array,k):
    minHeapWithKElements = MinHeap(array[:min(k+1, len(array))])
    nextIdxToInsertElement = 0 
    for idx in range(k+1, len(array)):
        minElement = minHeapWithKElements.remove()
        array[nextIdxToInsertElement] = minElement
        nextIdxToInsertElement += 1

        curElement = array[idx]
        minHeapWithKElements.insert(curElement)

    while not minHeapWithKElements.isEmpty():
        minElement = minHeapWithKElements.remove()
        array[nextIdxToInsertElement] = minElement
        nextIdxToInsertElement += 1

    return array



class MinHeap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)
        

    def isEmpty(self): # check if the HEAP is empty
        return len(self.heap) == 0
            
        
    def buildHeap(self, array): 
        # return array not HEAP
        firstParentIdx = (len(array)-2)//2
        for curIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(curIdx,len(array)-1, array)
        return array
    def siftDown(self,curIdx, endIdx, heap):
        childOneIdx = (2 * curIdx) +1 
        while childOneIdx <= endIdx:
            # check if childTwo is possible
            childTwoIdx = (2 * curIdx) + 2 if ( (2 * curIdx) + 2 <= endIdx )else -1 

            # checking b/w two children
            # In MinHeap, heap[parentIdx] < heap[childOneIdx]  < heap[childTwoIdx]
            if childTwoIdx != -1 and heap[childOneIdx] > heap[childTwoIdx]:
                idxToSwap = childTwoIdx
            else: 
                idxToSwap = childOneIdx

            
            # curIdx is parentIdx
            if heap[curIdx] > heap[idxToSwap]:
                self.swap(curIdx,idxToSwap, heap)
                curIdx = idxToSwap
                childOneIdx = (2 * curIdx) + 1
            else: 
                return 


    def siftUp(self, curIdx, heap):
        parentIdx =(curIdx -1 ) //2 
        # curIdx > O   >>> to end while loop
        # heap[curIdx] MUST < heap[parentIdx] in MINHEAP
        while curIdx > 0 and heap[curIdx] < heap[parentIdx]:
            # value swap
            self.swap(curIdx,parentIdx,heap)
            curIdx = parentIdx
            parentIdx = (curIdx -1) // 2


    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    # ** does not pass value to remove but return value to remove
    # use pop function
    def remove(self): 
        self.swap(0, len(self.heap)-1,self.heap )
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1,self.heap)
        return valueToRemove
        


    # does not use array, use HEAP
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j],heap[i]

        
