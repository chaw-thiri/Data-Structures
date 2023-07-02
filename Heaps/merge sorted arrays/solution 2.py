# O(nlog (k)+k ) time
# O(n+k) space
def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIdx in range(len(arrays)):
        smallestItems.append({"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})
    minHeap = MinHeap(smallestItems)
    while not minHeap.isEmpty():
        smallestItem= minHeap.remove()
        arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"]
        sortedList.append(num)
        if elementIdx == len(arrays[arrayIdx])-1 :
            continue
        minHeap.insert({"arrayIdx": arrayIdx, "elementIdx": elementIdx+ 1, "num": arrays[arrayIdx][elementIdx+1]})
    return sortedList

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap)== 0
    
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
            if childTwoIdx != -1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[currentIdx]["num"] > heap[idxToSwap]["num"]: # idxToSwap is the smaller one of the child node
                self.swap(currentIdx,idxToSwap,heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return 

    # O(log n) time, O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2 
        while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]: # < cux min heap, > in max heap
            # while not at the top of the heap
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx-1) // 2



        
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

   

