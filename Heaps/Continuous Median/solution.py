
class ContinuousMedianHandler:
    def __init__(self):
        
        self.lowers = Heap(MAX_HEAP_FUNC,[])
        self.greaters = Heap(MIN_HEAP_FUNC,[])
        self.median = None
# T = O(log n) insertion in heaps, S = O(n)
    def insert(self, number):
        # lower half is empty or the num is less than the largeset value of the lower half
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)

        self.rebalanceHeaps()
        self.updateMedian()

    # remove and insert (O(log N))
    def rebalanceHeaps(self):
        if self.lowers.length - self.greaters.length == 2:
            # insert num removed from lower half in greater half
            self.greaters.insert(self.lowers.remove())  
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    # O (1)
    def updateMedian(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek()+ self.greaters.peek())/2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median
    

class Heap:
    def __init__(self, comparisonFunc, array):
        self.comparisonFanc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array)-2) // 2
        for curIdx in reversed(range(firstParentIdx+1 )):
            self.siftDown(curIdx,len(array-1), array)
        return array
    
    def siftDown(self, curIdx, endIdx, heap):
        childOneIdx = curIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = curIdx * 2 + 2 if curIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFanc(heap[childTwoIdx],heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                 idxToSwap = childOneIdx

            if self.comparisonFanc(heap[idxToSwap],heap[curIdx]):
                self.swap(curIdx, idxToSwap, heap)
                curIdx = idxToSwap
                childOneIdx = curIdx * 2 + 1
            else:
                return 
            
    def siftUp(self, curIdx, heap):
        parentIdx = (curIdx - 1 )//2
        while curIdx > 0:
            if self.comparisonFanc(heap[curIdx], heap[parentIdx]):
                self.swap(curIdx, parentIdx, heap)
                curIdx = parentIdx
                parentIdx = (curIdx-1)//2
            else:
                return
            
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, self.length -1, self.heap)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length-1, self.heap)
        return valueToRemove
    
    def insert(self,value):
        self.heap.append(value)
        self.length += 1 
        self.siftUp(self.length-1, self.heap)

    def swap(self, i , j , array):
        array[i], array[j] = array[j], array[i]

def MAX_HEAP_FUNC(a,b):
    return a >b
def MIN_HEAP_FUNC(a,b):
    return a < b
